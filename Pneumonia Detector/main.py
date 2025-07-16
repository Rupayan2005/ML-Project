import streamlit as st
from PIL import Image
from keras.models import load_model
from keras.layers import DepthwiseConv2D
from utils import classify
import time


# Custom DepthwiseConv2D class that ignores the 'groups' parameter
# This is a compatibility fix for models saved with older TensorFlow versions
# that included a 'groups' parameter no longer supported in newer versions
class CustomDepthwiseConv2D(DepthwiseConv2D):
    def __init__(self, *args, **kwargs):
        # Remove 'groups' parameter if it exists to prevent deserialization errors
        kwargs.pop('groups', None)
        super().__init__(*args, **kwargs)


# Configure page
st.set_page_config(
    page_title="Pneumonia Detector",
    page_icon="🫁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }

    .upload-section {
        background: black;
        padding: 2rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }

    .result-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }

    .info-box {
        background: blue;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #2196f3;
        margin: 1rem 0;
    }

    .warning-box {
        background: black;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #ff9800;
        margin: 1rem 0;
    }

    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown("""
<div class="main-header">
    <h1>🫁 AI-Powered Pneumonia Detection</h1>
    <p>Upload a chest X-ray image for instant pneumonia screening</p>
</div>
""", unsafe_allow_html=True)

# Sidebar with information
with st.sidebar:
    st.markdown("### 📋 About This Tool")
    st.markdown("""
    This AI model analyzes chest X-ray images to detect signs of pneumonia. 

    **How to use:**
    1. Upload a chest X-ray image
    2. Wait for AI analysis
    3. Review the results
    """)

    st.markdown("### ⚠️ Important Notice")
    st.markdown("""
    <div class="warning-box">
        <strong>Medical Disclaimer:</strong> This tool is for educational purposes only. 
        Always consult healthcare professionals for medical diagnosis.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📊 Supported Formats")
    st.markdown("- PNG images")
    st.markdown("- JPG/JPEG images")
    st.markdown("- RGB color format")


# Load model with progress indicator
@st.cache_resource
def load_pneumonia_model():
    try:
        with st.spinner("🔄 Loading AI model..."):
            model = load_model('./model/pneumonia_classifier.h5',
                               custom_objects={'DepthwiseConv2D': CustomDepthwiseConv2D})
        return model
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        return None


# Load class names
@st.cache_data
def load_class_names():
    try:
        with open('./model/labels.txt', 'r') as f:
            class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
        return class_names
    except FileNotFoundError:
        st.error("❌ Labels file not found. Please check the path.")
        return None


# Initialize model and class names
model = load_pneumonia_model()
class_names = load_class_names()

if model is None or class_names is None:
    st.stop()

# Success message for model loading
st.success("✅ AI model loaded successfully!")

# Upload section
st.markdown("""
<div class="upload-section">
    <h3>📁 Upload Your Chest X-ray Image</h3>
    <p>Please select a clear chest X-ray image in PNG, JPG, or JPEG format.</p>
</div>
""", unsafe_allow_html=True)

# File uploader
file = st.file_uploader(
    "Choose an image file",
    type=['png', 'jpg', 'jpeg'],
    help="Upload a chest X-ray image for pneumonia detection"
)

# Main content area
col1, col2 = st.columns([1, 1])

if file is not None:
    with col1:
        st.markdown("### 🖼️ Uploaded Image")
        image = Image.open(file).convert('RGB')
        st.image(image, use_container_width=True, caption="Chest X-ray for analysis")

        # Image info
        st.markdown(f"""
        <div class="info-box">
            <strong>Image Details:</strong><br>
            📏 Size: {image.size[0]} × {image.size[1]} pixels<br>
            📂 Format: {image.format}<br>
            🎨 Mode: {image.mode}
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("### 🔍 AI Analysis")

        # Analysis with progress bar
        with st.spinner("🧠 Analyzing image..."):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)

            try:
                class_name, conf_score = classify(image, model, class_names)

                # Clear progress bar
                progress_bar.empty()

                # Display results
                confidence_percentage = int(conf_score * 1000) / 10

                # Color coding based on result
                if "normal" in class_name.lower():
                    result_color = "#4caf50"  # Green
                    icon = "✅"
                else:
                    result_color = "#f44336"  # Red
                    icon = "⚠️"

                st.markdown(f"""
                <div class="result-section">
                    <h2 style="text-align: center; margin-bottom: 1rem;">
                        {icon} Diagnosis Result
                    </h2>
                    <div style="text-align: center; font-size: 2rem; font-weight: bold; margin: 1rem 0;">
                        {class_name.title()}
                    </div>
                    <div style="text-align: center; font-size: 1.5rem; margin: 1rem 0;">
                        Confidence: {confidence_percentage}%
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # Confidence meter
                st.markdown("### 📊 Confidence Level")
                st.progress(conf_score)

                if confidence_percentage < 70:
                    st.warning(
                        "⚠️ Low confidence result. Consider retaking the X-ray or consulting a medical professional.")
                elif confidence_percentage >= 90:
                    st.success("✅ High confidence result.")
                else:
                    st.info("ℹ️ Moderate confidence result.")

            except Exception as e:
                st.error(f"❌ Error during classification: {e}")
                st.info("💡 Please try uploading a different image or check the image format.")

else:
    # Show sample images or instructions when no file is uploaded
    st.markdown("""
    <div class="info-box">
        <h3>🎯 How to get the best results:</h3>
        <ul>
            <li>Use clear, high-quality chest X-ray images</li>
            <li>Ensure the image is properly oriented</li>
            <li>Avoid blurry or low-resolution images</li>
            <li>Make sure the chest area is clearly visible</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #666;">
    <p>🔬 Powered by Deep Learning | 💻 Built with Streamlit</p>
    <p><small>For educational and research purposes only. Not intended for clinical use.</small></p>
</div>
""", unsafe_allow_html=True)