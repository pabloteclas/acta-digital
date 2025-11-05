# Prompt 2 — Importar librerías básicas
import streamlit as st
import hashlib, time, json

# Prompt 3 — Crear función de hash
def get_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

# Interfaz básica
st.title("Acta Digital — Generador de Hash")

st.write("🧩 Escribe un texto y genera su hash SHA-256 automáticamente:")

# Campo de texto
texto_usuario = st.text_input("Introduce el texto:")

# Si el usuario escribe algo, se calcula el hash
if texto_usuario:
    hash_resultado = get_hash(texto_usuario)
    st.write("🔢 **Hash generado:**")
    st.code(hash_resultado)

# Información adicional opcional
st.write("---")
st.write("⏱️ Tiempo actual:", time.time())
st.write("📦 Ejemplo JSON:", json.dumps({"texto": texto_usuario, "hash": get_hash(texto_usuario) if texto_usuario else None}))

st.write("Timestamp:", time.time())
st.write("Ejemplo JSON:", json.dumps({"ok": True, "msg": "listo"}))

