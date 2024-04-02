import streamlit as st
import pandas as pd
from joblib import load

# Load the trained model
model = load('pipeline.joblib')  # Replace 'pipeline.joblib' with the path to your trained model file

# List of diseases
diseases = [
    'Breast carcinoma',
    'Colorectal carcinoma',
    'Lung (NSCLC)',
    'Head and Neck SCC',
    'Ovarian carcinoma',
    'Bladder carcinoma',
    'Esophageal SCC',
    'Hepatocellular carcinoma',
    'Pancreatic carcinoma',
    'B-Chronic lymphocytic leukemia',
    'Other',
    'Unknown'
]

# Function to predict pathogenicity
def predict_pathogenicity(mutant_codon, disease):
    # Perform any necessary preprocessing on the input features
    # For example, you might encode categorical variables and transform the input data
    
    # Make the prediction
    prediction = model.predict([[mutant_codon, disease]])
    return prediction

# Main function to run the Streamlit app
def main():
    # Set page title
    st.title('PathFinder: TP53 Variant Pathogenicity Predictor')
    
    # Add input fields for mutant codon and disease
    mutant_codon = st.text_input('Enter Mutant Codon:', 'AAA')
    disease = st.selectbox('Select Disease:', diseases, index=diseases.index('Breast carcinoma'))
    
    # Make prediction when the 'Predict' button is clicked
    if st.button('Predict'):
        prediction = predict_pathogenicity(mutant_codon, disease)
        st.write('Prediction:', prediction)

# Run the main function
if __name__ == '__main__':
    main()
