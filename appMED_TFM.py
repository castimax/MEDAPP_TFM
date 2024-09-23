import streamlit as st
import math

# Configuración de la página
st.set_page_config(
    page_title='Bot Médico',
    page_icon=':hospital:', # Ícono relacionado con el tema médico
)

# Título del bot médico
'''
# :hospital: Bot Médico Inteligente

Simulador de preguntas y respuestas médicas. Esta herramienta permite obtener respuestas a preguntas médicas ficticias con fines demostrativos.
'''

# Espacio extra para estéticamente separar el contenido
''
''

# Simulador de la selección de preguntas médicas
pregunta_tipo = st.selectbox(
    'Seleccione el tipo de pregunta que desea simular:',
    ['Preguntas simples (Wikipedia)', 'Preguntas complejas (Mayo Clinic)']
)

pregunta_simulada = st.selectbox(
    'Seleccione una pregunta para mostrar la respuesta simulada:',
    ['¿Qué es la gripe?', 
     '¿Cuáles son los síntomas del resfriado común?', 
     '¿Cómo prevenir la gripe?', 
     '¿Qué causa el dolor de cabeza?',
     '¿Qué es la diabetes tipo 2?', 
     '¿Cuáles son los síntomas de un ataque al corazón?', 
     '¿Qué tratamientos existen para la hipertensión?', 
     '¿Cuáles son los síntomas del cáncer de pulmón?']
)

# Espacio para mostrar la respuesta simulada según la pregunta seleccionada
if pregunta_simulada == '¿Qué es la gripe?':
    st.write("**Respuesta**: La gripe es una infección viral que afecta principalmente al sistema respiratorio. Se transmite a través del aire cuando una persona infectada tose o estornuda.")
elif pregunta_simulada == '¿Cuáles son los síntomas del resfriado común?':
    st.write("**
