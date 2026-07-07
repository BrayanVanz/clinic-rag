# 🏥 ClinicRAG

> 🤖 Um sistema de RAG (Retrieval-Augmented Generation) para consulta inteligente de Protocolos Clínicos e Diretrizes Terapêuticas (PCDT) do Ministério da Saúde.

🌐 *Read this in [English](./README.md)*

---

## 📖 Sobre o projeto

O **ClinicRAG** é um projeto desenvolvido como desafio do programa de internship em construção de agentes de IA (AI Agentic Builder), em parceria com a **Compass**. O objetivo é aplicar, na prática, todo o ciclo de construção de um sistema de RAG — desde a coleta de dados brutos até uma interface funcional de consulta — utilizando **LLMs rodando localmente via Ollama**, com foco em arquitetura limpa, reprodutibilidade e documentação.

O sistema coleta automaticamente os PDFs de **Protocolos Clínicos e Diretrizes Terapêuticas (PCDT)** disponibilizados publicamente pelo governo brasileiro, processa esse conteúdo, e permite que um usuário faça perguntas em linguagem natural sobre os protocolos, recebendo respostas fundamentadas diretamente nos documentos oficiais.

## 🎯 Objetivo

- 🛠️ Construir um pipeline de RAG completo e funcional, do zero, com boas práticas de engenharia.
- 📚 Aprofundar o entendimento de toda a stack de LLM/IA, da fundamentação teórica até a produção.
- 🧩 Explorar arquitetura modular, containerização e reprodutibilidade via Docker.
- 🎨 Contribuir com diferenciais criativos únicos de cada membro da squad (como modelagem 3D aplicada a interfaces).

## 🧪 Tecnologias utilizadas

| Camada | Tecnologia |
|---|---|
| 🐍 Linguagem | Python 3.10+ |
| 📥 Coleta de dados | `requests`, `BeautifulSoup4`, `pypdf` |
| 🧠 Orquestração do RAG | `LangChain` |
| 🔍 Embeddings & LLM | `Ollama` (execução local) |
| 🗂️ Base vetorial | `ChromaDB` |
| 💻 Interface | `Streamlit` |
| 🐳 Ambiente | Docker + NVIDIA Container Toolkit (GPU) |

## 🚀 Como executar

O projeto inteiro roda dentro de um container Docker, com Jupyter Lab e Streamlit já configurados.

```bash
cd docker/scripts
bash setup.sh
```

Isso vai construir a imagem, subir o container em segundo plano, e deixar disponíveis:

- 📓 Jupyter Lab → [`http://localhost:8888`](http://localhost:8888)
- 📊 Streamlit → [`http://localhost:8501`](http://localhost:8501)

## 🗂️ Estrutura de pastas

```
clinic-rag/
├── academic/                          👉 projeto principal do desafio
│   ├── data/                          👉 dados em cada estágio do pipeline
│   │   ├── raw/                       📄 PDFs brutos baixados
│   │   ├── processed/                 📄 texto normalizado (JSONL por página)
│   │   ├── chunks/                    ✂️ texto já cortado para embeddings
│   │   └── embeddings/                🔢 vetores gerados
│   ├── eval/                          🧪 avaliação do RAG (LLM as judge)
│   ├── src/                           💻 código-fonte do pipeline
│   │   ├── ingestion/                 📥 coleta e ingestão dos PDFs
│   │   ├── chunking/                  ✂️ divisão do texto em pedaços
│   │   └── embedding/                 🔢 geração de embeddings
│   ├── .env.example                   🔐 modelo de variáveis de ambiente
│   ├── requirements.txt               📦 dependências Python
│   └── README.md                      📘 documentação específica do projeto
├── docker/                            🐳 infraestrutura e automação
│   └── scripts/                       ⚙️ setup.sh e entrypoint.sh
├── CONTRIBUICOES.md                   👥 quem fez o quê + reflexão da squad
└── README.md                          📘 este arquivo
```

Clique nos links abaixo para navegar direto:

- [`academic/`](./academic) — pasta principal do desafio
- [`academic/data/`](./academic/data) — dados brutos, processados, chunks e embeddings
- [`academic/eval/`](./academic/eval) — testes e avaliação do RAG
- [`academic/src/`](./academic/src) — todo o código-fonte do pipeline
- [`academic/requirements.txt`](./academic/requirements.txt) — dependências do projeto
- [`docker/`](./docker) — Dockerfile, docker-compose e scripts de automação
- [`CONTRIBUICOES.md`](./CONTRIBUICOES.md) — contribuição individual de cada membro

## 👥 Equipe

| Membro | Papel |
|---|---|
| 🧭 **Carlos Alberto da Silva Neto** | Líder da Sprint |
| 👨‍💻 Ismael Diógenys dos Santos Correia | Membro da squad |
| 👨‍💻 Brayan Vanz de Oliveira | Membro da squad |
| 👩‍💻 Maria Camila Gonçalves Guimarães | Membro da squad |
| 👨‍💻 Guilherme de Almeida Gama | Membro da squad |
| 👨‍💻 Thiago de Sousa Carvalho | Membro da squad |

📄 Detalhes de contribuição individual estão documentados em [`CONTRIBUICOES.md`](./CONTRIBUICOES.md).

## 📜 Licença

Este projeto foi desenvolvido para fins acadêmicos, como parte do desafio Compass. Os documentos PCDT utilizados são de domínio público, disponibilizados pelo Ministério da Saúde do Brasil.