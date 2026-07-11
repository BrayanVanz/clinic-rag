# 🏥 ClinicRAG

> 🤖 Um sistema de RAG (Retrieval-Augmented Generation) para consulta inteligente de Protocolos Clínicos e Diretrizes Terapêuticas (PCDT) do Ministério da Saúde.

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
| 📥 Coleta de dados | `requests`, `pypdf`, `beautifulsoup4` |
| 🧠 Orquestração do RAG | `LangChain` + `LangGraph` |
| 🔍 Embeddings & LLM | `Ollama` (execução local, via `langchain-ollama`) |
| 🗂️ Base vetorial | `FAISS` (`faiss-cpu`) |
| 💻 Interface | `Streamlit` |
| 🛠️ Utilitários | `tqdm` |
| 🐳 Ambiente | Docker |

> 💡 O suporte a GPU via NVIDIA Container Toolkit é opcional, configurado por um `docker-compose.override.yml` separado — usado por Carlos Alberto.

## 🚀 Como executar

O projeto inteiro roda dentro de um container Docker, com Streamlit e Ollama já configurados.

```bash
cd docker/scripts
bash setup.sh
```

Isso vai construir a imagem, subir os containers em segundo plano, baixar os modelos necessários no Ollama, e deixar disponível:

- 📊 Streamlit → [`http://localhost:8501`](http://localhost:8501)

## 🗂️ Estrutura de pastas

```
clinic-rag/
├── academic/                          👉 projeto principal do desafio
│   ├── data/                          👉 dados em cada estágio do pipeline
│   │   ├── chunks/                    ✂️ texto já cortado para embeddings
│   │   ├── embeddings/                🔢 vetores gerados
│   │   ├── processed/                 📄 texto normalizado (JSONL por página)
│   │   └── raw/                       📄 PDFs brutos baixados
│   │       └── pdfs/PCDT/
│   ├── eval/                          🧪 avaliação do RAG (LLM as judge)
│   ├── src/                           💻 código-fonte do pipeline
│   │   ├── chunking/                  ✂️ divisão do texto em pedaços
│   │   │   ├── chunks/
│   │   │   ├── io/
│   │   │   ├── sections/
│   │   │   └── semantic/
│   │   ├── embedding/                 🔢 geração de embeddings
│   │   │   ├── processing_embeddings/
│   │   │   └── vector_db/
│   │   ├── ingestion/                 📥 coleta e ingestão dos PDFs
│   │   ├── interface/                 🖥️ aplicação Streamlit
│   │   │   └── .streamlit/
│   │   ├── logs/                      📝 logs de execução
│   │   ├── rag/                       🔗 orquestração, recuperação e geração
│   │   └── util/                      🧰 utilitários compartilhados
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

## Acervo Utilizado

O sistema utiliza como base de conhecimento os **Protocolos Clínicos e Diretrizes Terapêuticas (PCDT)** disponibilizados oficialmente pelo **Ministério da Saúde**. Os documentos foram obtidos a partir do portal público de PCDTs (https://www.gov.br/saude/pt-br/assuntos/pcdt), que reúne protocolos organizados por condição clínica e atualizados periodicamente conforme novas evidências científicas e normativas do SUS.

Os PCDTs são documentos normativos que estabelecem critérios para diagnóstico, tratamento, acompanhamento e monitoramento de doenças no âmbito do Sistema Único de Saúde (SUS). Eles definem, entre outros aspectos:

- critérios diagnósticos;
- critérios de inclusão e exclusão de pacientes;
- medicamentos recomendados;
- posologias;
- exames necessários;
- mecanismos de monitoramento clínico;
- critérios para avaliação dos resultados terapêuticos.

As recomendações presentes nesses documentos são fundamentadas em evidências científicas e consideram aspectos de eficácia, segurança, efetividade e custo-efetividade das tecnologias incorporadas ao SUS.

> **Importante:** os PCDTs **não substituem o julgamento clínico do profissional de saúde** e **não devem ser utilizados como ferramenta de diagnóstico clínico**. Seu propósito é padronizar a assistência prestada no SUS, definindo critérios técnicos e administrativos para diagnóstico, tratamento e acompanhamento dos pacientes.

### Tipos de perguntas suportadas

Considerando a natureza dos PCDTs, o sistema foi projetado para responder perguntas fundamentadas exclusivamente nas informações presentes nesses documentos. As principais categorias de consultas são:

#### 1. Elegibilidade e acesso (Quem?)

Perguntas destinadas a identificar quais pacientes têm direito ao tratamento pelo SUS, incluindo critérios de inclusão, critérios de exclusão, contraindicações e requisitos clínicos ou laboratoriais para acesso às terapias.

**Exemplos:**

- Quem pode receber determinado medicamento pelo SUS?
- Quais são os critérios de exclusão do protocolo?
- Em quais situações o tratamento é contraindicado?

#### 2. Conduta terapêutica e linha de cuidado (O que fazer?)

Perguntas relacionadas ao fluxo terapêutico recomendado pelo protocolo, incluindo primeira, segunda e terceira linhas de tratamento, posologias padronizadas, intervenções não farmacológicas e alternativas diante de falha terapêutica.

**Exemplos:**

- Qual é o tratamento de primeira linha?
- Qual medicamento deve ser utilizado após falha terapêutica?
- Qual a dose recomendada para adultos?

#### 3. Resolução diagnóstica (Como comprovar?)

Perguntas sobre os requisitos necessários para confirmação diagnóstica antes do início da terapia, incluindo exames laboratoriais, exames de imagem, critérios clínicos, escalas e códigos CID-10 previstos pelo protocolo.

**Exemplos:**

- Quais exames são necessários para confirmar o diagnóstico?
- Qual CID-10 é utilizado para esta condição?
- Quais critérios laboratoriais são exigidos?

#### 4. Monitoramento, segurança e desfechos (Até quando?)

Perguntas relacionadas ao acompanhamento longitudinal do paciente, monitoramento de efeitos adversos, exames periódicos, critérios de resposta terapêutica e condições que determinam a continuidade ou interrupção do tratamento.

**Exemplos:**

- Com que frequência o paciente deve ser reavaliado?
- Quais exames devem ser realizados durante o tratamento?
- Em quais situações o tratamento deve ser suspenso?

## Aplicação no Contexto da Saúde

Os PCDTs são documentos extensos e altamente estruturados, tornando a localização manual de informações um processo demorado. Um sistema **Retrieval-Augmented Generation (RAG)** permite consultar esse acervo em linguagem natural, recuperando apenas os trechos relevantes para responder às perguntas do usuário.

Essa abordagem pode auxiliar profissionais de saúde e gestores na consulta rápida aos protocolos oficiais do Ministério da Saúde, reduzindo o tempo gasto na busca por informações como critérios de elegibilidade, exames necessários, linhas terapêuticas, posologias e recomendações de monitoramento.

Como as respostas são fundamentadas exclusivamente no conteúdo dos PCDTs e acompanhadas da referência ao documento-fonte, o sistema oferece maior transparência e confiabilidade durante a consulta às diretrizes oficiais.

---

# 🏥 ClinicRAG

> 🤖 A Retrieval-Augmented Generation (RAG) system for intelligent querying of Clinical Protocols and Therapeutic Guidelines (PCDT) from Brazil's Ministry of Health.

---

## 📖 About the project

**ClinicRAG** is a project built as a challenge for the AI Agentic Builder internship program, in partnership with **Compass**. The goal is to apply, hands-on, the full lifecycle of building a RAG system — from raw data collection to a working query interface — using **LLMs running locally via Ollama**, with a strong focus on clean architecture, reproducibility, and documentation.

The system automatically collects PDF files of **Clinical Protocols and Therapeutic Guidelines (PCDT)** publicly published by the Brazilian government, processes that content, and allows a user to ask natural language questions about the protocols, receiving answers grounded directly in the official documents.

## 🎯 Objective

- 🛠️ Build a complete, working RAG pipeline from scratch, following solid engineering practices.
- 📚 Deepen the understanding of the full LLM/AI stack, from theoretical foundations to production.
- 🧩 Explore modular architecture, containerization, and reproducibility with Docker.
- 🎨 Contribute unique creative differentiators from each squad member (such as 3D modeling applied to interfaces).

## 🧪 Tech stack

| Layer | Technology |
|---|---|
| 🐍 Language | Python 3.10+ |
| 📥 Data collection | `requests`, `pypdf`, `beautifulsoup4` |
| 🧠 RAG orchestration | `LangChain` + `LangGraph` |
| 🔍 Embeddings & LLM | `Ollama` (local inference, via `langchain-ollama`) |
| 🗂️ Vector store | `FAISS` (`faiss-cpu`) |
| 💻 Interface | `Streamlit` |
| 🛠️ Utilities | `tqdm` |
| 🐳 Environment | Docker |

> 💡 GPU support via the NVIDIA Container Toolkit is optional, configured through a separate `docker-compose.override.yml` — used only by Carlos Alberto.

## 🚀 How to run

The entire project runs inside a Docker container, with Streamlit and Ollama already configured.

```bash
cd docker/scripts
bash setup.sh
```

This builds the image, starts the containers in the background, downloads the required models into Ollama, and makes available:

- 📊 Streamlit → [`http://localhost:8501`](http://localhost:8501)

## 🗂️ Project structure

```
clinic-rag/
├── academic/                          👉 main challenge project
│   ├── data/                          👉 data at each pipeline stage
│   │   ├── chunks/                    ✂️ text already split for embeddings
│   │   ├── embeddings/                🔢 generated vectors
│   │   ├── processed/                 📄 normalized text (JSONL per page)
│   │   └── raw/                       📄 raw downloaded PDFs
│   │       └── pdfs/PCDT/
│   ├── eval/                          🧪 RAG evaluation (LLM as judge)
│   ├── src/                           💻 pipeline source code
│   │   ├── chunking/                  ✂️ text splitting
│   │   │   ├── chunks/
│   │   │   ├── io/
│   │   │   ├── sections/
│   │   │   └── semantic/
│   │   ├── embedding/                 🔢 embedding generation
│   │   │   ├── processing_embeddings/
│   │   │   └── vector_db/
│   │   ├── ingestion/                 📥 PDF collection and ingestion
│   │   ├── interface/                 🖥️ Streamlit application
│   │   │   └── .streamlit/
│   │   ├── logs/                      📝 execution logs
│   │   ├── rag/                       🔗 orchestration, retrieval and generation
│   │   └── util/                      🧰 shared utilities
│   ├── .env.example                   🔐 environment variables template
│   ├── requirements.txt               📦 Python dependencies
│   └── README.md                      📘 project-specific documentation
├── docker/                            🐳 infrastructure and automation
│   └── scripts/                       ⚙️ setup.sh and entrypoint.sh
├── CONTRIBUICOES.md                   👥 who did what + squad reflection
└── README.md                          📘 this file
```

Click the links below to navigate directly:

- [`academic/`](./academic) — main challenge folder
- [`academic/data/`](./academic/data) — raw, processed, chunked and embedded data
- [`academic/eval/`](./academic/eval) — RAG tests and evaluation
- [`academic/src/`](./academic/src) — all pipeline source code
- [`academic/requirements.txt`](./academic/requirements.txt) — project dependencies
- [`docker/`](./docker) — Dockerfile, docker-compose and automation scripts
- [`CONTRIBUICOES.md`](./CONTRIBUICOES.md) — individual contribution from each member

## 👥 Team

| Member | Role |
|---|---|
| 🧭 **Carlos Alberto da Silva Neto** | Sprint Leader |
| 👨‍💻 Ismael Diógenys dos Santos Correia | Squad member |
| 👨‍💻 Brayan Vanz de Oliveira | Squad member |
| 👩‍💻 Maria Camila Gonçalves Guimarães | Squad member |
| 👨‍💻 Guilherme de Almeida Gama | Squad member |
| 👨‍💻 Thiago de Sousa Carvalho | Squad member |

📄 Individual contribution details are documented in [`CONTRIBUICOES.md`](./CONTRIBUICOES.md).

## Knowledge Base Used

The system uses as its knowledge base the **Clinical Protocols and Therapeutic Guidelines (PCDT)** officially published by Brazil's **Ministry of Health**. The documents were obtained from the public PCDT portal (https://www.gov.br/saude/pt-br/assuntos/pcdt), which gathers protocols organized by clinical condition and updated periodically according to new scientific evidence and SUS (Brazil's public health system) regulations.

PCDTs are normative documents that establish criteria for diagnosis, treatment, follow-up, and monitoring of diseases within SUS. Among other things, they define:

- diagnostic criteria;
- patient inclusion and exclusion criteria;
- recommended medications;
- dosages;
- required exams;
- clinical monitoring mechanisms;
- criteria for evaluating therapeutic outcomes.

The recommendations in these documents are grounded in scientific evidence and take into account the efficacy, safety, effectiveness, and cost-effectiveness of technologies incorporated into SUS.

> **Important:** PCDTs **do not replace the clinical judgment of a healthcare professional** and **must not be used as a clinical diagnostic tool**. Their purpose is to standardize care provided within SUS, defining technical and administrative criteria for diagnosis, treatment, and patient follow-up.

### Supported question types

Given the nature of PCDTs, the system was designed to answer questions grounded exclusively in the information present in these documents. The main query categories are:

#### 1. Eligibility and access (Who?)

Questions aimed at identifying which patients are entitled to treatment through SUS, including inclusion criteria, exclusion criteria, contraindications, and clinical or laboratory requirements for accessing therapies.

**Examples:**

- Who can receive a given medication through SUS?
- What are the protocol's exclusion criteria?
- In which situations is the treatment contraindicated?

#### 2. Therapeutic approach and care pathway (What to do?)

Questions related to the therapeutic flow recommended by the protocol, including first, second, and third lines of treatment, standardized dosages, non-pharmacological interventions, and alternatives in case of therapeutic failure.

**Examples:**

- What is the first-line treatment?
- Which medication should be used after therapeutic failure?
- What is the recommended dose for adults?

#### 3. Diagnostic confirmation (How to confirm?)

Questions about the requirements needed to confirm a diagnosis before starting therapy, including lab tests, imaging exams, clinical criteria, scales, and ICD-10 codes foreseen by the protocol.

**Examples:**

- Which exams are needed to confirm the diagnosis?
- Which ICD-10 code is used for this condition?
- Which laboratory criteria are required?

#### 4. Monitoring, safety and outcomes (Until when?)

Questions related to longitudinal patient follow-up, adverse effect monitoring, periodic exams, therapeutic response criteria, and conditions that determine whether treatment should continue or be discontinued.

**Examples:**

- How often should the patient be reassessed?
- Which exams should be performed during treatment?
- In which situations should treatment be suspended?

## Application in the Healthcare Context

PCDTs are lengthy, highly structured documents, making manual information lookup a time-consuming process. A **Retrieval-Augmented Generation (RAG)** system allows this collection to be queried in natural language, retrieving only the relevant excerpts to answer the user's questions.

This approach can help healthcare professionals and managers quickly consult official Ministry of Health protocols, reducing the time spent searching for information such as eligibility criteria, required exams, therapeutic lines, dosages, and monitoring recommendations.

Since answers are grounded exclusively in the content of the PCDTs and accompanied by a reference to the source document, the system offers greater transparency and reliability when consulting official guidelines.