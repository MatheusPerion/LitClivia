import streamlit as st
from unidecode import unidecode

import warnings
warnings.filterwarnings('ignore')

import sys
sys.path.append("../code")
from utility import hide_github


def main():
    hide_github()
    st.title("Pausar Clivia")
    st.write('Página dedicada onde você pode controlar a quem a Clivia continua respondendo')

    st.divider()
    st.write('Teste')

if __name__ == "__main__":
    main()