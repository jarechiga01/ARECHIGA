
import streamlit as st

st.set_page_config(page_title="Cuestionario Interactivo - ABP y Funciones Trigonométricas")

st.title("🧠 Cuestionario Interactivo")
st.subheader("Estrategias de Enseñanza y Aprendizaje en Ciencias Matemáticas y Físicas")

st.markdown("Este cuestionario evalúa tu comprensión sobre estrategias didácticas y el uso del Aprendizaje Basado en Problemas (ABP), con énfasis en funciones trigonométricas.")

# Pregunta 1
st.markdown("### 1. ¿Cuál de las siguientes estrategias promueve la colaboración y el pensamiento crítico mediante la resolución de problemas complejos y reales?")
respuesta1 = st.radio("Selecciona una opción:", 
                     ["Aprendizaje Basado en Proyectos", "Aprendizaje Basado en Problemas (ABP)", "Evaluación Formativa", "Uso de Contextos Reales"])

if respuesta1 == "Aprendizaje Basado en Problemas (ABP)":
    st.success("¡Correcto! El ABP se centra en problemas reales que promueven la colaboración y el análisis.")
else:
    st.error("Respuesta incorrecta. La respuesta correcta es 'Aprendizaje Basado en Problemas (ABP)'.")

# Pregunta 2
st.markdown("### 2. ¿Qué representa la amplitud en la función trigonométrica \( y(t) = A \\sin(\\omega t + \\phi) \)?")
respuesta2 = st.selectbox("Elige la mejor definición:",
                          ["La frecuencia de oscilación", 
                           "La posición de equilibrio", 
                           "El desplazamiento inicial", 
                           "El desplazamiento máximo desde el equilibrio"])

if respuesta2 == "El desplazamiento máximo desde el equilibrio":
    st.success("¡Correcto! La amplitud es la distancia máxima desde el punto de equilibrio.")
else:
    st.error("Incorrecto. La amplitud representa el desplazamiento máximo.")

# Pregunta 3
st.markdown("### 3. En el ABP, ¿cuál es el propósito de permitir que los estudiantes investiguen por su cuenta?")
respuesta3 = st.checkbox("Fomentar el aprendizaje autónomo")
respuesta4 = st.checkbox("Evitar que el profesor intervenga")
respuesta5 = st.checkbox("Desarrollar habilidades de investigación")
respuesta6 = st.checkbox("Limitar el contenido teórico")

if respuesta3 and respuesta5 and not respuesta4 and not respuesta6:
    st.success("¡Bien hecho! La investigación independiente fomenta el aprendizaje autónomo y habilidades de investigación.")
elif st.button("Revisar Respuesta"):
    st.error("Revisa tus selecciones. Solo la 1 y la 3 son correctas.")

# Pregunta 4
st.markdown("### 4. ¿Cuál de las siguientes funciones describe un sistema amortiguado?")
respuesta7 = st.text_input("Ingresa la forma general de la función (usa 'A', 'e', 't', 'omega', 'phi'):")

if "Ae" in respuesta7 or "A*e" in respuesta7 or "A·e" in respuesta7:
    st.success("Correcto. Una forma común es: A·e^(-αt)·sin(ωt + φ)")
elif respuesta7:
    st.warning("Parece que falta el término de amortiguación exponencial. Inténtalo de nuevo.")

# Reflexión
st.markdown("### 📝 Reflexión Final")
reflexion = st.text_area("¿Cómo podrías aplicar estas estrategias en tu próxima clase de matemáticas o física?")
if st.button("Enviar Reflexión"):
    st.success("¡Gracias por tu reflexión! Aplicar estas ideas marca la diferencia en la enseñanza.")

st.markdown("---")
st.caption("Desarrollado como apoyo didáctico para docentes en ciencias exactas.")
