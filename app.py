import streamlit as st
import joblib
import pandas as pd
import os

# Custom CSS for gradient background and stylish table cards
st.markdown("""
    <style>
        body {
            background: linear-gradient(120deg, #89f7fe 0%, #66a6ff 100%);
        }
        .stApp {
            background: linear-gradient(120deg, #89f7fe 0%, #66a6ff 100%);
            font-family: 'Poppins', sans-serif;
        }
        .section {
            background-color: rgba(255,255,255,0.92);
            padding: 2em 2em 1.5em 2em;
            margin-bottom: 2em;
            border-radius: 15px;
            box-shadow: 1px 2px 24px #c9ddff;
        }
        .data-card {
            background-color: rgba(230,245,255,0.85);
            border-radius: 14px;
            box-shadow: 1px 2px 12px #e6ddff;
            padding: 0.5em 0.5em 0.2em 0.5em;
            margin-bottom: 2em;
        }
        .dataframe thead tr th {
            background: linear-gradient(90deg,#43cea2 10%,#185a9d 90%);
            color: #fff;
        }
    </style>
""", unsafe_allow_html=True)

model = joblib.load(r"best_fit_model.pkl")

st.sidebar.markdown("<h2 style='color:#1abc9c; font-family:Space Mono;'>📌 Navigation</h2>", unsafe_allow_html=True)
page = st.sidebar.radio("Go to", ["🏠 Home", "ℹ️ Overview", "📊 Prediction"])

st.markdown("""<hr style="height:2px;border:none;color:#e6e6e6;background-color:#ededed;" /> """, unsafe_allow_html=True)

def load_data():
    try:
        # The file is named "Input.csv" and attached. If running locally, make sure it's in your working directory.
        df = pd.read_csv(r"C:\Users\DELL\Desktop\new\Data\Ecommerce_Final (1).csv")
        return df
    except Exception as e:
        return None

# HOME PAGE
if page == "🏠 Home":
    st.markdown(
        """
        <h1 style='
            background: linear-gradient(90deg, #43cea2 0%, #185a9d 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 3.2rem;
            font-family: "Poppins", sans-serif;
            text-align: center;
        '>📱 Products Discount Data Analysis & Estimation</h1>
        """, unsafe_allow_html=True
    )
    st.markdown("""
        <div class='section'>
            <div style='font-size:1.2rem; text-align:center;'>
                <b>Welcome to the Smartphone Discount Prediction</b><br>
                This app helps you <span style="color:#26a69a;"><b>predict the discount price</b></span> of smartphones<br>
                based on their brand, RAM, storage, display size, battery, and camera details.
            </div>
            <ul style="font-size: 1.05rem; color: #555;">
                <li>📊 Helps <span style="color:#00b894;">e-commerce sellers</span> plan competitive discounts.</li>
                <li>🛒 Assists <span style="color:#ff7675;">buyers</span> in estimating the best deal.</li>
                <li>📈 Useful for <span style="color:#6c5ce7;">market analysis</span> and price trends.</li>
                <li>🧠 Supports <span style="color:#00cec9;">data-driven</span> decisions.</li>
                <li>⏳ Predict prices <span style="color:#0984e3;">instantly</span>—no manual calculation.</li>
                <li>🎯 Target <span style="color:#d35400;">specific segments</span> with personalized discounts.</li>
                <li>📦 Plan <span style="color:#2d3436;">inventory clearance</span> with optimal rates.</li>
                <li>🔍 Get <span style="color:#6ab04c;">brand-wise pricing</span> insights.</li>
            </ul>
            <div style="text-align:center; font-size:1rem; margin-top:1em;">
                Navigate to the <b>Prediction</b> tab from the sidebar to try it yourself!
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Data Preview
    st.markdown(
        "<h3 style='color:#185a9d; font-family:Poppins;'>📊 Latest Smartphone Discount Data</h3>",
        unsafe_allow_html=True
    )
    df = load_data()
    if df is not None:
        st.markdown("<div class='data-card'>", unsafe_allow_html=True)
        with st.expander("Click to view smartphone data table ⬇", expanded=True):
            st.dataframe(df.head(20), use_container_width=True, height=420)
            if df.shape[0]>20:
                st.info(f"Showing 20 of {df.shape[0]:,} rows. Download the file for full data!")

        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("Data file not found or format error. Please check file location. (Input.csv)")

# OVERVIEW PAGE
elif page == "ℹ️ Overview":
    st.markdown("""
        <style>
            /* Fade-in animation for overview content */
            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translate3d(0, 20px, 0);
                }
                to {
                    opacity: 1;
                    transform: translate3d(0, 0, 0);
                }
            }
            .animated-section {
                animation: fadeInUp 1s ease forwards;
                opacity: 0;
                color: #18304b !important;  /* Dark text for readability */
            }
            .section {
                background-color: rgba(255,255,255,0.95) !important;
                padding: 2em 2em 1.5em 2em !important;
                border-radius: 15px !important;
                box-shadow: 1px 2px 24px #c9ddff !important;
            }
            ul, ol {
                margin-left: 24px;
            }
        </style>

        <h2 style='color:#0984e3; font-size:2.4rem; font-family:Poppins;'>📖 Project Overview</h2>
        <div class='section animated-section'>
            <div style='font-size:1.2rem; margin-bottom:1.5em;'>
                <b>Objective:</b> Predict the <span style='color:#26a69a;font-weight:bold;'>Discount Price</span> of smartphones using machine learning.
            </div>
            <div style='margin-bottom:1em;'>
                <b>Dataset:</b><br>
                Model trained on data scraped from:
                <ul>
                    <li>Amazon 📦</li>
                    <li>Flipkart 🛒</li>
                </ul>
            </div>
            <hr>
            <div style='margin-bottom:1em;'>
                <b>Features Used:</b>
                <ul>
                    <li>Brand 🏷️</li>
                    <li>RAM 💾</li>
                    <li>ROM 📂</li>
                    <li>Display Size 📱</li>
                    <li>Battery 🔋</li>
                    <li>Front Camera 🤳</li>
                    <li>Back Camera 📷</li>
                </ul>
            </div>
            <div style='margin-bottom:1em;'>
                <b>How It Works:</b>
                <ol>
                    <li>Enter smartphone specifications</li>
                    <li>The app processes your input</li>
                    <li>Prediction = <span style='color:#27ae60;font-weight:bold;'>discount price</span> instantly!</li>
                </ol>
            </div>
            <div>
                <b>Use Cases:</b>
                <ul>
                    <li>Price strategy for sellers</li>
                    <li>Buyer budget estimation</li>
                    <li>Competitive market analysis</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)



# PREDICTION PAGE
elif page == "📊 Prediction":
    st.markdown("""
        <h2 style='
            color: #6a89cc;
            font-family: "Poppins",sans-serif;
            font-size: 2.6rem;
            letter-spacing: 1px;
            text-shadow: 1px 2px 7px #e1e6eb;
        '>📊 Predict Smartphone Discount Price</h2>
        <div class='section'>
    """, unsafe_allow_html=True)

    df = load_data()
    if df is None:
        st.error("Data file not found or format error. Please check file location. (Input.csv)")
    else:
        # Get distinct brands
        brands = sorted(df['Brand'].dropna().unique())
        selected_brand = st.selectbox("Select Brand", brands)

        # Filter models for selected brand
        filtered_models = df[df['Brand'] == selected_brand]['Brand_Model'].dropna().unique()
        selected_model = st.selectbox("Select Model", filtered_models)

        # Get details of selected model from dataset
        model_details = df[(df['Brand'] == selected_brand) & (df['Brand_Model'] == selected_model)].iloc[0]

        # Show and allow user to adjust the specs or take these as defaults
        ram = st.number_input("RAM (GB)", min_value=0, value=int(model_details['RAM']), step=1)
        rom = st.number_input("ROM (GB)", min_value=0, value=int(model_details['ROM']), step=1)
        display_size = st.number_input("Display Size (inches)", min_value=0.0, value=float(model_details['Display_Size']), step=0.1, format="%.2f")
        battery = st.number_input("Battery Capacity (mAh)", min_value=0, value=int(model_details['Battery']), step=100)
        front_cam = st.number_input("Front Camera (MP)", min_value=0, value=int(model_details['Front_Cam(MP)']), step=1)
        back_cam = st.number_input("Back Camera (MP)", min_value=0, value=int(model_details['Back_Cam(MP)']), step=1)

        # Prepare input features for prediction
        input_features = {
            'Brand': selected_brand,
            'RAM': ram,
            'ROM': rom,
            'Display_Size': display_size,
            'Battery': battery,
            'Front_Cam(MP)': front_cam,
            'Back_Cam(MP)': back_cam
        }

        if st.button("🚀 Predict Discount Price"):
            input_df = pd.DataFrame([input_features])
            prediction = model.predict(input_df)[0]
            st.success(f"💰 Predicted Discount Price: ₹{prediction:,.2f}", icon="✅")
            st.markdown(
                f"<span style='font-size:1.6rem;color:#27ae60;'>💰 Predicted Discount Price: ₹{prediction:,.2f}</span>",
                unsafe_allow_html=True
            )
            st.balloons()
            st.markdown("<div style='text-align:center;font-size:1.1rem;'>🎉 Great deals await! Use data to win the smartphone game. 📱</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
