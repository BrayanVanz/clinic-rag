# app/ — Interface Streamlit do RAG 

Este módulo implementa a interface de usuário do assistente RAG sobre os Protocolos Clínicos e Diretrizes Terapêuticas (PCDT) do Ministério da Saúde, construída com **Streamlit**.

Ele não implementa nenhuma etapa do pipeline de RAG (decomposição, recuperação, geração ou reflexão): toda essa lógica pertence ao pacote `rag`, mantido separadamente. A interface consome o pacote `rag` através de uma camada fina de integração (`rag_pipeline.py`), responsável apenas por expor um ponto de entrada único (`get_answer`) e reaproveitar os componentes já inicializados do pipeline (LLM + retriever) entre uma pergunta e outra.

## Visão geral do fluxo

```
pergunta do usuário (st.chat_input)
    -> exibida imediatamente no histórico do chat
    -> get_answer(question)                          (rag_pipeline.py)
       -> _get_components() [cache em módulo]
       -> rag.answer_question(question, components)   (pacote rag)
    -> resposta + sub-perguntas + fontes + low_confidence
    -> renderização:
         resposta (st.markdown)
         aviso de baixa confiança, se houver           (render_extras)
         sub-perguntas usadas na busca, se houver       (render_extras)
         cards com documentos-fonte                     (render_sources)
    -> turno completo salvo em st.session_state.history
```

Esse fluxo é puramente de apresentação: a interface não decide nada sobre qualidade da resposta, apenas exibe os metadados de transparência que o pipeline já calcula (sub-perguntas, fontes, sinalização de baixa confiança).

## Estrutura do módulo

| Arquivo | Responsabilidade |
| --- | --- |
| `app.py` | Interface Streamlit propriamente dita: layout, estado de sessão, renderização do chat, sidebar. |
| `rag_pipeline.py` | Camada de integração entre `app.py` e o pacote `rag`; expõe `get_answer`. |
| `.streamlit/config.toml` | Tema visual (cores, fonte) aplicado globalmente pela interface. |

A seguir, cada arquivo é detalhado.

## `app.py`

### Configuração da página
`st.set_page_config` define título da aba (`RAG Clínico — Assistente de Acervo`), ícone (🩺) e `layout="wide"`, para aproveitar toda a largura da tela — importante porque os cards de fonte e o histórico de chat podem ficar extensos.

### Estilo customizado
Um bloco CSS é injetado via `st.markdown(..., unsafe_allow_html=True)` para estilizar os cards de documentos-fonte (`.source-card`, `.source-name`, `.section-text`), com borda azul clara e cantos arredondados, consistente com a paleta definida em `config.toml`.

### `render_extras(sub_questions, low_confidence)`
Renderiza dois elementos condicionais, ambos vindos diretamente do resultado do pipeline:
- **Aviso de baixa confiança**: `st.caption` exibido quando `low_confidence=True`, alertando que o modelo não teve certeza mesmo após tentar novas buscas.
- **Sub-perguntas usadas na busca**: se existirem, aparecem em um `st.expander` recolhível, expondo ao usuário a etapa de decomposição feita pelo pipeline sem sobrecarregar a resposta principal.

### `render_sources(sources)`
Renderiza os documentos-fonte recuperados como cards HTML dentro de um `st.expander`. Cada card mostra apenas nome do arquivo de origem e caminho da seção — o pipeline não retorna trecho de texto nem pontuação de similaridade, então a interface se limita a exibir o que de fato está disponível no contrato de dados de `answer_question`.

### Estado de sessão
`st.session_state.history` guarda a conversa completa (pergunta, resposta, fontes, sub-perguntas, `low_confidence`) como lista de dicionários. Como o Streamlit reexecuta o script inteiro a cada interação, é esse estado que permite reconstruir visualmente todo o histórico a cada rerun, iterando com `st.chat_message`.

### Sidebar
Título, legenda e um bloco "Sobre" explicando o propósito do assistente. Inclui o botão **"🗑️ Limpar conversa"**, que zera `st.session_state.history` e força `st.rerun()`.

### Novo turno de pergunta
Ao receber uma pergunta via `st.chat_input`:
1. A pergunta é exibida imediatamente.
2. Um `st.spinner` cobre a chamada a `get_answer(question)`, com mensagem descrevendo as etapas internas do pipeline ("Decompondo a pergunta, buscando no acervo e refletindo sobre a resposta...").
3. Resposta, extras e fontes são renderizados assim que o resultado retorna.
4. O turno completo é acrescentado ao histórico da sessão.

Não há streaming de tokens — a resposta é exibida de uma vez, após o retorno completo de `answer_question`. Essa foi uma decisão consciente da interface diante das limitações arquiteturais do pacote `rag` para expor streaming incremental sem alterações no core do pipeline.

## `rag_pipeline.py`

Camada de integração que isola `app.py` do pacote `rag`, expondo um único ponto de entrada:

- **`_get_components()`**: constrói os componentes do pipeline (`rag.build_pipeline()`) e os mantém em uma variável global de módulo (`_components`), evitando recarregar o índice FAISS e o LLM a cada pergunta — o mesmo padrão de reaproveitamento recomendado pela própria documentação do pacote `rag` para uso em loop.
- **`get_answer(question)`**: função consumida por `app.py`. Obtém os componentes cacheados e delega para `rag.answer_question(question, components=components)`, repassando o dicionário de retorno (`answer`, `sources`, `sub_questions`, `low_confidence`, etc.) sem nenhuma transformação — a interface confia inteiramente no contrato de dados exposto pelo pipeline.
- O ajuste de `sys.path` no topo do arquivo garante que o pacote `rag` seja importável independentemente de onde o Streamlit for executado.

## `.streamlit/config.toml`

Define o tema visual global da interface:

| Parâmetro | Valor | Descrição |
| --- | --- | --- |
| `base` | `light` | Tema claro. |
| `primaryColor` | `#0369A1` | Azul usado em botões, links e destaques. |
| `backgroundColor` | `#EFF6FC` | Fundo geral da aplicação. |
| `secondaryBackgroundColor` | `#DCEAF7` | Fundo da sidebar e elementos secundários. |
| `textColor` | `#1E293B` | Cor do texto principal. |
| `font` | `sans serif` | Fonte padrão. |

A paleta reforça visualmente o caráter clínico da aplicação e é consistente com as cores usadas nos cards de fonte definidos em `app.py`.

## Divisão de responsabilidades

- **Interface (`app.py`, `rag_pipeline.py`, `config.toml`)**: sob minha responsabilidade — experiência do usuário, estado de sessão, renderização de respostas/fontes/sub-perguntas, tema visual e tratamento de casos como baixa confiança.

## Avaliação com juiz LLM (antes da otimização dos chunks)

Foi conduzida uma rodada de avaliação com um LLM como juiz, usando um conjunto de **12 perguntas** sobre os PCDT. Para cada pergunta, o juiz avaliou a resposta e o contexto recuperado com base em dois critérios — **fidelidade** (a resposta está de fato ancorada no contexto recuperado, sem alucinação) e **relevância** (o contexto recuperado é pertinente à pergunta feita) — atribuindo também uma nota geral de 1 a 5.

