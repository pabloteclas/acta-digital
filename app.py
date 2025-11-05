# Prompt 2 — Importar librerías básicas
import streamlit as st
import hashlib, time, json, os

# Prompt 3 — Crear función de hash
def get_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

# ---- INTERFAZ PRINCIPAL ----
st.title("Acta Digital — Registro de Documentos y Verificación de Hashes")

menu = st.sidebar.radio("Navegación", ["Generar / Verificar Hash", "Registrar Documento", "Ver Registros"])

# --- SECCIÓN 1: Generar y verificar hash ---
if menu == "Generar / Verificar Hash":
    st.header("🧩 Paso 1 — Generar un hash")
    texto = st.text_input("Introduce el texto para generar su hash:")
    if texto:
        hash_generado = get_hash(texto)
        st.code(hash_generado)
        st.session_state["ultimo_hash"] = hash_generado
        st.success("✅ Hash generado y guardado para verificación.")
    else:
        st.info("Escribe un texto arriba para generar su hash.")

    st.header("🧩 Paso 2 — Verificar un hash anterior")
    texto_verif = st.text_input("Introduce el texto que quieres verificar:")
    hash_prev = st.text_input(
        "Introduce el hash anterior para comparar:",
        st.session_state.get("ultimo_hash", "")
    )

    if texto_verif and hash_prev:
        hash_nuevo = get_hash(texto_verif)
        if hash_nuevo.strip() == hash_prev.strip():
            st.success("✅ Coinciden: el texto genera el mismo hash.")
        else:
            st.error("❌ No coinciden: el texto no corresponde al hash indicado.")
        st.write("Hash calculado ahora:")
        st.code(hash_nuevo)

    st.write("---")
    st.write("⏱️ Tiempo actual:", time.time())
    st.write("📦 Ejemplo JSON:", json.dumps({
        "texto": texto,
        "hash": get_hash(texto) if texto else None
    }))

# --- SECCIÓN 2: Registro de documentos ---
elif menu == "Registrar Documento":
    st.header("🧾 Prompt 4 — Registro de Documentos Digitales")

    owner = st.text_input("👤 Propietario del documento")
    content = st.text_area("📄 Contenido del documento")

    if st.button("Registrar"):
        if owner and content:
            record = {"owner": owner, "hash": get_hash(content), "time": time.time()}

            # Guardar registro en archivo blockchain.json (simulación local)
            with open("blockchain.json", "a", encoding="utf-8") as f:
                f.write(json.dumps(record) + "\n")

            st.success("Documento registrado con éxito ✅")
            st.json(record)
        else:
            st.warning("⚠️ Debes introducir propietario y contenido antes de registrar.")

# --- SECCIÓN 3: Ver registros existentes ---
elif menu == "Ver Registros":
    st.header("📜 Registros guardados (simulación de cadena local)")
    if os.path.exists("blockchain.json"):
        with open("blockchain.json", "r", encoding="utf-8") as f:
            lines = f.readlines()
            if lines:
                for i, line in enumerate(lines, 1):
                    record = json.loads(line)
                    st.write(f"### Bloque #{i}")
                    st.json(record)
            else:
                st.info("No hay registros aún.")
    else:
        st.info("Aún no existe el archivo blockchain.json.")
