import streamlit as st
import hashlib, time, json

# Función para generar hash
def get_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

st.title("Acta Digital — Generador y Verificador de Hash")

# --- Paso 1: Generar un hash ---
st.header("Paso 1️⃣ — Generar un nuevo hash")

texto = st.text_input("Introduce el texto para generar su hash:")
if texto:
    hash_generado = get_hash(texto)
    st.code(hash_generado)
    st.session_state["ultimo_hash"] = hash_generado  # Guarda el hash en memoria temporal
    st.success("✅ Hash generado y guardado para verificación.")
else:
    st.info("Escribe un texto arriba para generar su hash.")

# --- Paso 2: Verificar un hash existente ---
st.header("Paso 2️⃣ — Verificar un hash anterior")

texto_verif = st.text_input("Introduce el texto que quieres verificar:")

# Recupera el hash anterior si existe en sesión
hash_prev = st.text_input(
    "Introduce el hash anterior para comparar:",
    st.session_state.get("ultimo_hash", "")
)

if texto_verif and hash_prev:
    hash_nuevo = get_hash(texto_verif)

    # Normalizamos para evitar errores por espacios
    if hash_nuevo.strip() == hash_prev.strip():
        st.success("✅ Coinciden: el texto genera el mismo hash.")
    else:
        st.error("❌ No coinciden: el texto no corresponde al hash indicado.")

    st.write("Hash calculado ahora:")
    st.code(hash_nuevo)

# --- Información adicional ---
st.write("---")
st.write("⏱️ Tiempo actual:", time.time())
st.write("📦 Ejemplo JSON:", json.dumps({
    "texto": texto,
    "hash": get_hash(texto) if texto else None
}))
