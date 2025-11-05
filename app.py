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

st.title("Acta Digital — Import Test")

st.write("✅ Librerías importadas:")
st.code("streamlit, hashlib, time, json")



st.write("Timestamp:", time.time())
st.write("Ejemplo JSON:", json.dumps({"ok": True, "msg": "listo"}))

# Prompt 3 — Crear función de hash
def get_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

st.title("Acta Digital — Hash Generator")

text = st.text_input("Escribe algo para calcular su hash:")

if text:
    st.write("🔢 Hash SHA-256:")
    st.code(get_hash(text))
