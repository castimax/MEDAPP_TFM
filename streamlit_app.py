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
    st.write("**Respuesta**: Los síntomas del resfriado común incluyen congestión nasal, dolor de garganta, estornudos, tos y dolor de cabeza.")
elif pregunta_simulada == '¿Cómo prevenir la gripe?':
    st.write("**Respuesta**: Para prevenir la gripe, se recomienda la vacunación anual, lavarse las manos con frecuencia y evitar el contacto cercano con personas infectadas.")
elif pregunta_simulada == '¿Qué causa el dolor de cabeza?':
    st.write("**Respuesta**: El dolor de cabeza puede ser causado por estrés, deshidratación, tensión muscular o factores ambientales como la falta de sueño.")
elif pregunta_simulada == '¿Qué es la diabetes tipo 2?':
    st.write("**Respuesta**: La diabetes tipo 2 es una afección en la que el cuerpo no usa la insulina adecuadamente, lo que causa niveles altos de glucosa en sangre. Es común en adultos y se puede controlar con dieta, ejercicio y medicamentos.")
elif pregunta_simulada == '¿Cuáles son los síntomas de un ataque al corazón?':
    st.write("**Respuesta**: Los síntomas de un ataque al corazón incluyen dolor en el pecho, dificultad para respirar, sudoración excesiva y malestar en el brazo izquierdo o la mandíbula.")
elif pregunta_simulada == '¿Qué tratamientos existen para la hipertensión?':
    st.write("**Respuesta**: Los tratamientos comunes para la hipertensión incluyen cambios en la dieta, ejercicio regular, reducción del estrés y medicamentos antihipertensivos.")
elif pregunta_simulada == '¿Cuáles son los síntomas del cáncer de pulmón?':
    st.write("**Respuesta**: Los síntomas del cáncer de pulmón pueden incluir tos persistente, dolor en el pecho, pérdida de peso inexplicada, y dificultad para respirar.")

# Espacio para métricas adicionales
st.write("---")
st.header('Simulación de preguntas complejas en Mayo Clinic', divider='gray')

# Simulación de crecimiento de consultas médicas
cols = st.columns(4)

preguntas_complejas = ['Diabetes tipo 2', 'Ataque al corazón', 'Hipertensión', 'Cáncer de pulmón']
crecimientos = [1.3, 1.8, 2.2, 1.9]

for i, pregunta in enumerate(preguntas_complejas):
    col = cols[i % len(cols)]
    with col:
        st.metric(
            label=f'{pregunta}',
            value=f'{crecimientos[i]:.2f}x más consultas',
            delta=f'{crecimientos[i]:.2f}x',
            delta_color='normal'
        )
        
# Pie de página
''
st.write("**Nota**: Este bot médico es solo un simulador y no debe ser utilizado como sustituto de un consejo médico profesional.")
