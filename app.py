import streamlit as st
from modules.llm import generate_text
from modules.image import generate_image
from modules.audio import generate_audio

from PIL import Image
import requests
from io import BytesIO

# =========================
# 🔹 CONFIG
# =========================
st.set_page_config(
    page_title="AI Creative Studio",
    page_icon="🤖",
    layout="centered"
)

if "history" not in st.session_state:
    st.session_state.history = []

# =========================
# 🔹 HEADER
# =========================
st.markdown(
    """
    <h1 style='text-align: center;'>🤖 AI Creative Studio</h1>
    <p style='text-align: center; color: gray;'>
    Generate Text • Image • Audio dalam satu klik
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# =========================
# 🔹 INPUT
# =========================
user_input = st.text_input("💡 Masukkan ide kamu:", placeholder="contoh: naga api di gunung")

col1, col2 = st.columns([1, 1])

generate = col1.button("🚀 Generate")
clear = col2.button("🗑️ Clear")

if clear:
    st.rerun()

# =========================
# 🔹 PROCESS
# =========================
if generate:
    if user_input.strip() == "":
        st.warning("⚠️ Masukkan teks terlebih dahulu!")
    else:
        with st.spinner("AI sedang bekerja... ⏳"):

            # 🔹 TEXT
            text_result = generate_text(user_input)

        st.divider()

        st.session_state.history.append({
    "user": user_input,
    "ai": text_result
})

        # =========================
        # 📄 TEXT OUTPUT
        # =========================
        st.markdown(
    f"""
    <div style='
        background: linear-gradient(135deg, #1e1e1e, #2c2c2c);
        padding:20px;
        border-radius:12px;
        color:#ffffff;
        line-height:1.7;
        font-size:16px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    '>
    {text_result}
    </div>
    """,
    unsafe_allow_html=True
)

        # =========================
        # 🖼️ IMAGE OUTPUT
        # =========================
        st.markdown("## 🖼️ Visualisasi AI")

        image_prompt = "cartoon illustration of " + user_input
        image_url = generate_image(image_prompt)

        try:
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            st.image(img, width="stretch")

            img_bytes = BytesIO()
            img.save(img_bytes, format="PNG")

            st.download_button(
                label="📥 Download Gambar",
                data=img_bytes.getvalue(),
                file_name="ai_image.png",
                mime="image/png"
            )

        except:
            st.error("Gagal memuat gambar")
            from io import BytesIO

        # =========================
        # 🔊 AUDIO OUTPUT
        # =========================
        st.markdown("## 🔊 Audio Narasi")

        try:
            audio_file = generate_audio(text_result)
            st.audio(audio_file)
        except:
            st.error("Gagal membuat audio")

        st.success("✅ Konten berhasil dibuat!")
        with open(audio_file, "rb") as f:
            st.download_button(
                label="📥 Download Audio",
            data=f, 
                file_name="ai_audio.mp3",
                mime="audio/mp3"
            )

st.divider()
st.markdown("## 💬 Riwayat Percakapan")

for chat in st.session_state.history[::-1]:

    # USER (KANAN)
    st.markdown(
        f"""
        <div style='text-align:right; margin-bottom:10px;'>
            <div style='
                display:inline-block;
                background:#4CAF50;
                color:white;
                padding:10px 15px;
                border-radius:15px 15px 0px 15px;
                max-width:70%;
            '>
                {chat['user']}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # AI (KIRI)
    st.markdown(
        f"""
        <div style='text-align:left; margin-bottom:20px;'>
            <div style='
                display:inline-block;
                background:#2c2c2c;
                color:white;
                padding:10px 15px;
                border-radius:15px 15px 15px 0px;
                max-width:70%;
            '>
                {chat['ai']}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )