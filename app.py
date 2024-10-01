import streamlit as st
import random

# Função para sortear os grupos
def sortear_grupos(nomes, max_alunos_por_grupo, max_grupos):
    random.shuffle(nomes)
    grupos = []
    for i in range(max_grupos):
        grupo = nomes[i * max_alunos_por_grupo: (i + 1) * max_alunos_por_grupo]
        if grupo:
            grupos.append(grupo)
    return grupos

# Interface do Streamlit
st.title('Sorteador de Grupos')

# Input para o número de grupos e número de pessoas por grupo
max_grupos = st.number_input('Quantos grupos?', min_value=1, max_value=10, value=5)
max_alunos_por_grupo = st.number_input('Número máximo de pessoas por grupo', min_value=1, max_value=10, value=6)

# Campo para adicionar uma pessoa
pessoa = st.text_input('Adicionar pessoa à lista')

# Lista de pessoas que serão sorteadas
if 'nomes' not in st.session_state:
    st.session_state.nomes = []

# Adicionar pessoa à lista
if st.button('Adicionar pessoa'):
    if pessoa:
        st.session_state.nomes.append(pessoa)
        st.success(f'{pessoa} foi adicionada à lista.')
    else:
        st.error('Digite um nome para adicionar.')

# Exibir lista de pessoas
st.subheader('Lista de pessoas:')
if st.session_state.nomes:
    st.write(st.session_state.nomes)
else:
    st.write('Nenhuma pessoa adicionada.')

# Botão para confirmação de sorteio
if st.button('Você tem certeza que quer sortear?'):
    if len(st.session_state.nomes) > 0:
        st.session_state.confirmar_sorteio = True
    else:
        st.error('Adicione pelo menos uma pessoa antes de sortear os grupos.')

# Se o sorteio for confirmado, mostra os grupos
if 'confirmar_sorteio' in st.session_state and st.session_state.confirmar_sorteio:
    grupos_sortados = sortear_grupos(st.session_state.nomes, max_alunos_por_grupo, max_grupos)
    
    # Exibir os grupos sorteados
    st.subheader('Grupos Sorteados:')
    for i, grupo in enumerate(grupos_sortados, start=1):
        st.write(f"**Grupo {i}:**")
        st.write(', '.join(grupo))
    
    # Resetar a confirmação após exibir os grupos
    if st.button('Resetar sorteio'):
        st.session_state.confirmar_sorteio = False
