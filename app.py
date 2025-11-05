import streamlit as st

st.title("Acta Digital")
st.write("¡Bienvenido a tu primera app con Streamlit!")

import streamlit as st
import hashlib
import time
import json

st.title("Acta Digital — Prompt 2")
st.write("Librerías básicas importadas correctamente.")

import streamlit as st
import hashlib
import time
import json

# Título principal
st.title("Acta Digital — Comprobación de librerías")

# Mostrar la hora actual
current_time = time.strftime("%Y-%m-%d %H:%M:%S")
st.write("🕒 Hora actual:", current_time)

# Crear un texto de prueba
texto = "Prueba de hash"
st.write("📄 Texto original:", texto)

# Calcular su hash
hash_result = hashlib.sha256(texto.encode()).hexdigest()
st.write("🔒 Hash SHA-256:", hash_result)

# Crear un registro en formato JSON
registro = {
    "texto": texto,
    "hash": hash_result,
    "hora": current_time
}
st.write("🧾 Registro JSON:", json.dumps(registro, indent=2))
