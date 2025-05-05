import streamlit as st
import streamlit_authenticator as stauth
from dotenv import load_dotenv
from yaml.loader import SafeLoader
import yaml
import os

from utility import hide_github

load_dotenv()


def str_to_bool(str_input):
    if not isinstance(str_input, str):
        return False
    return str_input.lower() == "true"

authentication_required = str_to_bool(os.environ.get("AUTHENTICATION_REQUIRED", False))

# Carrega a configuração
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)
# Chama o login sem desempacotar o retorno
authenticator.login(location="main", key="LoginForm")
# Recupera os dados de autenticação do session_state
name = st.session_state.get("name")
authentication_status = st.session_state.get("authentication_status")
username = st.session_state.get("username")
#### Terminei o login


def main():
    # Inicializa a variável de página, se ainda não existir
    if "page" not in st.session_state:
        st.session_state.page = "home"

    # Criação do menu lateral (sidebar)
    st.sidebar.title("Plataforma CliviaWeb")
    
    if st.sidebar.button("Home"):
        st.session_state.page = "home"
    if st.sidebar.button("Ajuda Humana"):
        st.session_state.page = "ajuda_humana"
    
    st.sidebar.markdown("---")
    st.sidebar.title("Controles Clivia")
    if st.sidebar.button("Pausar Clivia"):
        st.session_state.page = "pausar_clivia"
    
    
    st.sidebar.markdown("---")
    st.sidebar.title("Terceira opção")
    if st.sidebar.button("Terceira opcao"):
        st.session_state.page = "terceira_opcao"
   
    # Carrega a página selecionada
    load_page(st.session_state.page)
def load_page(page):
    """
    Função que carrega a página de acordo com o valor armazenado em st.session_state.page.
    """
    if page == "home":
        printaHome()
    elif page == "ajuda_humana":
        # Executa o script do revisor – considere refatorar para uma função, se possível.
        app.main()
    elif page == "pausar_clivia":
        exec(open("02_Pausar_Clivia.py").read())
    # Adicione outras páginas conforme necessário
    else:
        st.error("Página não encontrada.")    
def printaHome():
    st.title("Bem vindo ao site do Clivia! :female-doctor: :stethoscope:")
    st.write('Aqui você poderá interagir para controlar ações da Clivia')
    
   
    st.write('Em caso de dúvidas, me contacte via [Whatsapp](https://api.whatsapp.com/send?phone=5562982169350&text=Ol%C3%A1,%20estou%20com%20d%C3%BAvidas%20ao%20usar%20o%20sistema%20da%20Clivia.).')
    hide_github()

if authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.write(f"Bem vindo, *{name}*!")
    main()
    
elif authentication_status is False:
    st.error("Usuário ou senha inválida.")
elif authentication_status is None:
    st.warning("Por favor, insira seu usuário e senha.")
    
if __name__ == "__main__":
    st.write(" ")        
# def mostrar_tela_de_login():
#     """Exibe a tela de login."""
#     st.title("Tela de Login")
#     username = st.text_input("Utilizador")
#     password = st.text_input("Senha", type="password")
#     login_button = st.button("Entrar")

#     if login_button:
#         USUARIOS_VALIDOS = {"admin": "123"} 
#         if username.lower() in USUARIOS_VALIDOS and USUARIOS_VALIDOS[username.lower()] == password:
#             st.success("Login realizado com sucesso!")
#             st.session_state.logged_in = True
#             st.session_state.username = username.lower()
#             st.rerun()
#         else:
#             st.error("Utilizador ou senha incorretos.")

# def mostrar_pagina_principal(container):
#     """Exibe a página principal após o login."""
#     container.markdown(
#         """
#         <style>
#         .stApp {
#             max-width: 90%; /* Aumenta a largura máxima para 90% da tela */
#             margin: auto; /* Centraliza o conteúdo na página */
#             padding: 20px; /* Adiciona algum preenchimento ao redor do conteúdo */
#         }
#         div.block-container {
#             max-width: 90%;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

#     container.write(f"Bem-vindo, {st.session_state.username}!")
#     container.markdown(
#         """
#     ## Próxima Etapa: Login por Clínica

#     A próxima etapa no desenvolvimento é a implementação do **Login por Clínica**. Esta tela terá o formato de uma tabela, onde cada linha representará uma ocorrência/interação com um cliente.

#     **Estrutura da Tabela:**

#     A tabela será composta por 4 colunas:

#     1.  **Número do Cliente:** Exibirá o ID ou número de identificação do cliente.

#     2.  **Duas Últimas Mensagens:** Mostrará as duas últimas mensagens trocadas entre a clínica e o cliente.

#     3.  **Causa:** Apresentará a causa da interação/ocorrência. A causa deve ser claramente explicada para fácil entendimento.

#     4.  **Ação Clivia:** Esta coluna conterá um botão que permitirá ativar ou desativar a Clivia para o contato específico.

#     **Detalhes Adicionais:**

#     * **Responsividade:** A tabela deve ser responsiva, adaptando-se a diferentes tamanhos de tela (desktop, tablet, mobile).

#     * **Ordenação:** Deve ser possível ordenar as linhas da tabela por qualquer uma das colunas (Número do Cliente, Mensagens, Causa, Ação Clivia).

#     * **Filtro:** Deve ser possível filtrar as linhas da tabela por qualquer uma das colunas.

#     * **Estilização:** A tabela deve ter uma estilização clara e organizada, facilitando a leitura e a identificação das informações.

#     * **Botão Ativar/Desativar:** O botão na coluna "Ação Clivia" deve indicar claramente o estado atual da Clivia para o contato (Ativada ou Desativada) e permitir a alteração desse estado com um clique. A alteração do estado deve ser persistida e refletida na interface.

#     * **Mensagens:** As "Duas Últimas Mensagens" devem ser exibidas de forma concisa, evitando quebras de linha excessivas. Se as mensagens forem muito longas, considere usar um resumo ou truncamento com a opção de ver a mensagem completa ao passar o mouse.
#     """,
#         unsafe_allow_html=True,
#     )


# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False
# col1, col2, col3 = st.columns([1, 2, 1]) 
# with col2:
#     if not st.session_state.logged_in:
#         mostrar_tela_de_login()
#     else:
#         mostrar_pagina_principal(st)
       
