import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Title of the Web App
st.title("🍄 Mushroom Classification App")

# Load and Preprocess Dataset
@st.cache_data
def load_data():
    df = pd.read_csv("mushrooms.csv")

    # Encoding categorical variables
    le = LabelEncoder()
    for column in df.columns:
        df[column] = le.fit_transform(df[column])

    # Feature-target split
    X = df.drop('class', axis=1)
    y = df['class']

    # PCA for dimensionality reduction
    pca = PCA(n_components=7)
    X_pca = pca.fit_transform(X)

    return X_pca, y, pca

X, y, pca = load_data()

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)

# Sidebar for User Input
st.sidebar.header("Enter Mushroom Features")

cap_shape = st.sidebar.slider("Cap Shape (0-5)", 0, 5, 2)
cap_surface = st.sidebar.slider("Cap Surface (0-3)", 0, 3, 2)
cap_color = st.sidebar.slider("Cap Color (0-9)", 0, 9, 4)
bruises = st.sidebar.radio("Bruises (0: No, 1: Yes)", [0, 1])
odor = st.sidebar.slider("Odor (0-8)", 0, 8, 2)
gill_attachment = st.sidebar.slider("Gill Attachment (0-1)", 0, 1, 0)
gill_spacing = st.sidebar.slider("Gill Spacing (0-1)", 0, 1, 1)
gill_size = st.sidebar.slider("Gill Size (0-1)", 0, 1, 1)
gill_color = st.sidebar.slider("Gill Color (0-11)", 0, 11, 5)
stalk_shape = st.sidebar.slider("Stalk Shape (0-1)", 0, 1, 1)
stalk_root = st.sidebar.slider("Stalk Root (0-4)", 0, 4, 2)
stalk_surface_above_ring = st.sidebar.slider("Stalk Surface Above Ring (0-3)", 0, 3, 2)
stalk_surface_below_ring = st.sidebar.slider("Stalk Surface Below Ring (0-3)", 0, 3, 2)
stalk_color_above_ring = st.sidebar.slider("Stalk Color Above Ring (0-8)", 0, 8, 3)
stalk_color_below_ring = st.sidebar.slider("Stalk Color Below Ring (0-8)", 0, 8, 3)
veil_type = st.sidebar.slider("Veil Type (0-1)", 0, 1, 0)
veil_color = st.sidebar.slider("Veil Color (0-3)", 0, 3, 2)
ring_number = st.sidebar.slider("Ring Number (0-2)", 0, 2, 1)
ring_type = st.sidebar.slider("Ring Type (0-5)", 0, 5, 2)
spore_print_color = st.sidebar.slider("Spore Print Color (0-8)", 0, 8, 4)
population = st.sidebar.slider("Population (0-5)", 0, 5, 2)
habitat = st.sidebar.slider("Habitat (0-6)", 0, 6, 2)

# Prediction Button
if st.sidebar.button("Predict Edibility"):
    user_input = np.array([[cap_shape, cap_surface, cap_color, bruises, odor, gill_attachment, gill_spacing, gill_size, 
                            gill_color, stalk_shape, stalk_root, stalk_surface_above_ring, stalk_surface_below_ring,
                            stalk_color_above_ring, stalk_color_below_ring, veil_type, veil_color, ring_number,
                            ring_type, spore_print_color, population, habitat]])
    
    user_input_pca = pca.transform(user_input)
    prediction = rf_model.predict(user_input_pca)

    if prediction[0] == 1:
        st.sidebar.error("⚠️ The mushroom is **Poisonous**! DO NOT EAT! ⚠️")
    else:
        st.sidebar.success("✅ The mushroom is **Edible**! Safe to eat.")

