import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Virtual Try-On",
    layout="centered",
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
.step {
    display: inline-block;
    padding: 8px 14px;
    border-radius: 50%;
    background: #e5e7eb;
    color: #374151;
    font-weight: 600;
    margin-right: 8px;
}
.step.active {
    background: #ec4899;
    color: white;
}
.notice {
    background-color: #ffe4e6;
    padding: 12px;
    border-radius: 8px;
    color: #be123c;
    font-size: 14px;
    margin-bottom: 25px;
}
.upload-box {
    border: 2px dashed #d1d5db;
    padding: 30px;
    border-radius: 10px;
    text-align: center;
    color: #6b7280;
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown("<h1 style='text-align:center;'>Virtual Try-On Experience</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color:#6b7280;'>"
    "Upload your photo, enter your measurements, and see how any garment looks on you before you buy. "
    "Precision fitting powered by AI.</p>",
    unsafe_allow_html=True
)

# ---------- Privacy Notice ----------
st.markdown(
    "<div class='notice'>🔒 Your photos and measurements are used only for this session and are not stored permanently.</div>",
    unsafe_allow_html=True
)

# ---------- Steps ----------
st.markdown("""
<div style="text-align:center; margin-bottom:30px;">
    <span class="step active">1</span> Your Photo
    <span class="step">2</span> Measurements
    <span class="step">3</span> Clothing
    <span class="step">4</span> Preview
</div>
""", unsafe_allow_html=True)

# ---------- Upload Section ----------
st.markdown("### Upload Clothing Image")
st.markdown(
    "Upload a clear image of the garment you want to try on. "
    "Flat-lay or mannequin photos work best."
)

uploaded_file = st.file_uploader(
    "",
    type=["jpg", "jpeg", "png"],
    label_visibility="collapsed"
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Clothing Image", use_container_width=True)

# ---------- Buttons ----------
col1, col2 = st.columns([1, 1])

with col1:
    st.button("⬅ Back")

with col2:
    if st.button("Start Try-On"):
        if uploaded_file is None:
            st.warning("Please upload a clothing image first.")
        else:
            st.success("Starting virtual try-on...")
            # 👉 Call your ML / CV model here
