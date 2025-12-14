import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="Virtual Try-On",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🧥 Virtual Try-On Demo")
st.markdown("This is a professional prototype. Upload a person and a clothing image, adjust measurements, and preview the result.")

# ----------------------------
# SIDEBAR CONTROLS
# ----------------------------
with st.sidebar:
    st.header("Measurements & Controls")
    height = st.slider("Height (cm)", 140, 210, 170)
    chest = st.slider("Chest (cm)", 70, 120, 90)
    waist = st.slider("Waist (cm)", 60, 110, 80)
    hips = st.slider("Hips (cm)", 70, 120, 90)
    tightness = st.slider("Tightness", 0.0, 1.0, 0.5)
    st.markdown("---")
    apply_button = st.button("Apply Clothing")
    reset_button = st.button("Reset Inputs")

# ----------------------------
# IMAGE UPLOADS
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Person Image")
    person_file = st.file_uploader("Upload Person Photo", type=["png", "jpg", "jpeg"], key="person")

with col2:
    st.subheader("Clothing Image")
    clothing_file = st.file_uploader("Upload Clothing Photo", type=["png", "jpg", "jpeg"], key="clothing")

# ----------------------------
# RESET FUNCTIONALITY
# ----------------------------
if reset_button:
    st.session_state.person = None
    st.session_state.clothing = None
    st.experimental_rerun()

# ----------------------------
# LOAD IMAGES
# ----------------------------
person_img = None
clothing_img = None

if person_file:
    person_img = Image.open(person_file).convert("RGBA")
if clothing_file:
    clothing_img = Image.open(clothing_file).convert("RGBA")

# ----------------------------
# APPLY CLOTHING (PLACEHOLDER)
# ----------------------------
def apply_clothing_demo(person, clothing, tightness=0.5):
    """
    Dummy function to simulate clothing application.
    Scales clothing based on tightness and overlays on person.
    """
    if person is None or clothing is None:
        return None

    # Resize clothing proportionally to person
    p_w, p_h = person.size
    scale_factor = 0.6 + tightness * 0.4  # tight clothes = bigger overlay
    new_w = int(p_w * scale_factor)
    new_h = int(clothing.height * (new_w / clothing.width))
    clothing_resized = clothing.resize((new_w, new_h), Image.ANTIALIAS)

    # Overlay clothing in center
    result = person.copy()
    pos_x = (p_w - new_w) // 2
    pos_y = int(p_h * 0.3)  # position around torso
    result.paste(clothing_resized, (pos_x, pos_y), clothing_resized)
    return result

# ----------------------------
# DISPLAY PREVIEW
# ----------------------------
st.subheader("Preview")
if apply_button:
    if person_img and clothing_img:
        output = apply_clothing_demo(person_img, clothing_img, tightness)
        st.image(output, use_column_width=True)
    else:
        st.warning("Please upload both person and clothing images to preview.")
elif person_img:
    st.image(person_img, caption="Person Image", use_column_width=True)
elif clothing_img:
    st.image(clothing_img, caption="Clothing Image", use_column_width=True)
else:
    st.info("Upload images to see a preview.")

# ----------------------------
# OPTIONAL: INFO / NOTES
# ----------------------------
st.markdown("---")
st.markdown("""
**Notes:**  
- This is a demo prototype.  
- Measurements are illustrative; model integration will produce realistic fit.  
- Tightness slider simulates how tight or loose clothing appears.  
""")
