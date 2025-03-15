# 🍄 Mushroom Classification using Random Forest Classifier

## 📌 Table of Contents  
- [Demo](#demo)  
- [Overview](#overview)  
- [Motivation](#motivation)  
- [Technical Aspect](#technical-aspect)  
- [Installation, Run & Deployment](#installation-run--deployment)  
- [Directory Structure](#directory-structure)  
- [To-Do & Bug / Feature Request](#to-do--bug--feature-request)  
- [Technologies Used](#technologies-used)  
- [Credits](#credits)  

---

## 🎥 Demo  
🔗 **Live Demo**: [Add your deployment link here]  
![Demo](https://your-demo-link.com/demo.gif)  

## 📖 Overview  
This project classifies **mushrooms as edible or poisonous** based on their **physical attributes** using machine learning techniques, specifically the **Random Forest Classifier**. The dataset includes mushroom characteristics such as **cap shape, color, odor, gill size, and habitat**.  

💡 **Models Used**: Logistic Regression, K-Nearest Neighbors (KNN), Support Vector Classifier (SVC), Decision Tree Classifier, Random Forest Classifier (**Best Performing Model**), and Gradient Boosting Classifier.  
📊 **Evaluation Metrics**: Accuracy Score.  

## 🎯 Motivation  
Eating **poisonous mushrooms** can be **fatal**. This project aims to build an accurate **mushroom classification model** to help **foragers, health organizations, and researchers** identify safe mushrooms.  

## ⚙️ Technical Aspect  
This project consists of **two main components**:  
1️⃣ **Model Training & Evaluation**:  
   - **Data Preprocessing**: Handling missing values, encoding categorical data, and transforming features.  
   - **Dimensionality Reduction**: **Principal Component Analysis (PCA)** is used to reduce the number of features.  
   - **Model Training**: Comparing multiple classification models.  
   - **Model Evaluation**: Using Accuracy Score for performance comparison.  
   - **Best Model Selection**: Random Forest Classifier is used for final predictions.  

2️⃣ **Model Deployment using Streamlit**:  
   - A **user-friendly UI** where users can input mushroom attributes.  
   - Predicts whether the mushroom is **edible or poisonous**.  

## ⚡ Installation, Run & Deployment  
```bash
# Install dependencies
pip install -r requirements.txt  

# Run the project
python mushroom_classification_by_random_forest_classifier.py  

# Install Streamlit for deployment
pip install streamlit  

# Run Streamlit app
streamlit run app.py  

📂 Directory Structure
📦 Mushroom Classification  
 ┣ 📂 data  
 ┃ ┣ 📄 mushrooms.csv  
 ┣ 📂 models  
 ┃ ┣ 📄 mushroom_prediction.pkl  
 ┣ 📂 scripts  
 ┃ ┣ 📄 mushroom_classification_by_random_forest_classifier.py  
 ┣ 📂 streamlit_app  
 ┃ ┣ 📄 app.py  
 ┣ 📄 requirements.txt  
 ┣ 📄 README.md  
 ┣ 📄 LICENSE

✅ To-Do & Bug / Feature Request
# To-Do  
✔ Deploy the model using Flask API  
✔ Enable real-time mushroom classification  

# Bug / Feature Request  
If you find a bug or want to request a new feature, open an issues
https://github.com/sowjanyabudhala/Mushroom_classification/edit/main/README.md


🛠 Technologies Used
# Libraries Used:  
✔ Scikit-Learn (Machine Learning)  
✔ Streamlit (Web App Framework)  
✔ Pandas (Data Analysis)  
✔ Matplotlib (Data Visualization)  

🙌 Credits
# Dataset:  
✔ Kaggle Mushroom Classification Dataset  

# Contributors:  
✔ B. Sowjanya  

---



