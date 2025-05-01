import streamlit as st

def mostrar_tela_de_login():
    """Exibe a tela de login."""
    st.title("Tela de Login")
    username = st.text_input("Utilizador")
    password = st.text_input("Senha", type="password")
    login_button = st.button("Entrar")

    if login_button:
        USUARIOS_VALIDOS = {"admin": "123"}  # Credenciais de login válidas
        if username.lower() in USUARIOS_VALIDOS and USUARIOS_VALIDOS[username.lower()] == password:
            # Login bem-sucedido: define o estado de login como True
            st.success("Login realizado com sucesso!")
            st.session_state.logged_in = True
            st.session_state.username = username.lower()
            st.rerun()  # Força a atualização da página
        else:
            st.error("Utilizador ou senha incorretos.")

def mostrar_pagina_principal(container):
    """Exibe a página principal após o login."""
    # Define a largura máxima do container para ocupar mais espaço na tela
    container.markdown(
        """
        <style>
        .stApp {
            max-width: 90%; /* Aumenta a largura máxima para 90% da tela */
            margin: auto; /* Centraliza o conteúdo na página */
            padding: 20px; /* Adiciona algum preenchimento ao redor do conteúdo */
        }
        div.block-container {
            max-width: 90%;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    container.write(f"Bem-vindo, {st.session_state.username}!")
    container.markdown(
        """
    ## Próxima Etapa: Login por Clínica

    A próxima etapa no desenvolvimento é a implementação do **Login por Clínica**. Esta tela terá o formato de uma tabela, onde cada linha representará uma ocorrência/interação com um cliente.

    **Estrutura da Tabela:**

    A tabela será composta por 4 colunas:

    1.  **Número do Cliente:** Exibirá o ID ou número de identificação do cliente.

    2.  **Duas Últimas Mensagens:** Mostrará as duas últimas mensagens trocadas entre a clínica e o cliente.

    3.  **Causa:** Apresentará a causa da interação/ocorrência. A causa deve ser claramente explicada para fácil entendimento.

    4.  **Ação Clivia:** Esta coluna conterá um botão que permitirá ativar ou desativar a Clivia para o contato específico.

    **Detalhes Adicionais:**

    * **Responsividade:** A tabela deve ser responsiva, adaptando-se a diferentes tamanhos de tela (desktop, tablet, mobile).

    * **Ordenação:** Deve ser possível ordenar as linhas da tabela por qualquer uma das colunas (Número do Cliente, Mensagens, Causa, Ação Clivia).

    * **Filtro:** Deve ser possível filtrar as linhas da tabela por qualquer uma das colunas.

    * **Estilização:** A tabela deve ter uma estilização clara e organizada, facilitando a leitura e a identificação das informações.

    * **Botão Ativar/Desativar:** O botão na coluna "Ação Clivia" deve indicar claramente o estado atual da Clivia para o contato (Ativada ou Desativada) e permitir a alteração desse estado com um clique. A alteração do estado deve ser persistida e refletida na interface.

    * **Mensagens:** As "Duas Últimas Mensagens" devem ser exibidas de forma concisa, evitando quebras de linha excessivas. Se as mensagens forem muito longas, considere usar um resumo ou truncamento com a opção de ver a mensagem completa ao passar o mouse.
    """,
        unsafe_allow_html=True,
    )

# Inicializa o estado de login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Lógica principal para exibir a tela de login
col1, col2, col3 = st.columns([1, 2, 1])  # Divide a página em 3 colunas
with col2:  # Centraliza o conteúdo na coluna do meio
    if not st.session_state.logged_in:
        mostrar_tela_de_login()
    else:
        mostrar_pagina_principal(st)
