import os
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tqdm import tqdm

"""Rode este script para baixar os PDFs dos protocolos clínicos do site do Ministério da Saúde e salvá-los em academic/data/raw/pdfs/PCDT/.
Para cada protocolo, o script cria um arquivo PDF com o nome do protocolo. Se o arquivo já existir, ele não será baixado novamente.
Esses PFDs podem então ser processados pelo script ingest.py para gerar um arquivo JSONL de saída em academic/data/processed"""

#URL base do site do Ministério da Saúde para os protocolos clínicos e caminho para salvar os PDFs baixados. 
# O script cria o diretório se ele não existir.
BASE_URL = "https://www.gov.br/saude/pt-br/assuntos/pcdt"
DOWNLOAD_FOLDER = "../data/raw/pdfs/PCDT"

os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# Reutiliza a conexão HTTP
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0"
})

# Coleta as letras disponíveis no site do Ministério da Saúde, que contêm os links para os protocolos clínicos.
print("Obtendo lista de letras...")

response = session.get(BASE_URL, timeout=30)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Armazena os links das letras encontradas no site do Ministério da Saúde.
letter_urls = []

# Coleta todas as letras disponíveis no site do Ministério da Saúde, que contêm os links para os protocolos clínicos.
for a in soup.select("a.govbr-card-content"):
    href = a.get("href")

    if href:
        letter_urls.append(urljoin(BASE_URL, href))

print(f"{len(letter_urls)} letras encontradas.\n")

# Coleta todas as doenças e seus respectivos links para os protocolos clínicos, que serão usados para baixar os PDFs.
diseases = []

# Coleta os links para os protocolos clínicos de cada doença, que serão usados para baixar os PDFs.
for letter_url in tqdm(letter_urls, desc="Letras"):

    try:
        response = session.get(letter_url, timeout=30)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        for a in soup.select("a.summary.url"):

            diseases.append({
                "name": a.get_text(strip=True),
                "url": urljoin(letter_url, a["href"])
            })

    except Exception as e:
        print(f"Erro na letra {letter_url}")
        print(e)

print(f"\n{len(diseases)} protocolos encontrados.\n")

# Download dos PDFs
for disease in tqdm(diseases, desc="Baixando PDFs"):

    try:

        response = session.get(disease["url"], timeout=30)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        pdf_url = None
        filename = None

        # Procura o link para o PDF do protocolo clínico na página da doença.
        for a in soup.find_all("a", href=True):

            href = a["href"]

            if "@@download/file" in href:

                pdf_url = urljoin(disease["url"], href)
                filename = a.get_text(strip=True)

                if not filename.lower().endswith(".pdf"):
                    filename += ".pdf"

                break
        
        # Se não encontrar o link para o PDF, imprime uma mensagem de erro e continua para a próxima doença.
        if pdf_url is None:
            print(f"PDF não encontrado: {disease['name']}")
            continue

        file_path = os.path.join(DOWNLOAD_FOLDER, filename)

        # Não baixa novamente o PDF se ele já existir no diretório de download.
        if os.path.exists(file_path):
            continue

        sucesso = False

        # Tenta baixar o PDF até 3 vezes em caso de falha na conexão.
        for tentativa in range(3):

            try:

                pdf = session.get(
                    pdf_url,
                    stream=True,
                    timeout=60
                )

                pdf.raise_for_status()

                with open(file_path, "wb") as f:

                    for chunk in pdf.iter_content(chunk_size=8192):

                        if chunk:
                            f.write(chunk)

                sucesso = True
                break

            except requests.RequestException:

                print(
                    f"Tentativa {tentativa+1}/3 falhou para {filename}"
                )

                time.sleep(2)

        if not sucesso:
            print(f"Não foi possível baixar {filename}")

        time.sleep(1)

    except Exception as e:

        print(f"Erro em {disease['name']}")
        print(e)

print("\nTodos os downloads foram processados.")
