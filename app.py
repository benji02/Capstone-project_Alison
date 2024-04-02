import streamlit as st
import pandas as pd
from joblib import load
import numpy as np

# Load the trained model
model = load('c:\\Users\\aliva\\Downloads\\Capstone\\Sprint 3\\pipeline.joblib')  # Replace 'pipeline.joblib' with the path to your trained model file

# List of mutant codons
mutant_codons = ['AAA', 'AAC', 'AAG', 'AAT', 'ACA', 'ACC', 'ACG', 'ACT', 'AGA', 'AGC', 'AGG', 'AGT', 'ATA', 'ATC', 'ATG', 
                 'ATT', 'CAA', 'CAC', 'CAG', 'CAT', 'CCA', 'CCC', 'CCG', 'CCT', 'CGA', 'CGC', 'CGG', 'CGT', 'CTA', 
                 'CTC', 'CTG', 'CTT', 'GAA', 'GAC', 'GAG', 'GAT', 'GCA', 'GCC', 'GCG', 'GCT', 'GGA', 'GGC', 'GGG', 
                 'GGT', 'GTA', 'GTC', 'GTG', 'GTT', 'TAG', 'TAT', 'TCA', 'TCC', 'TCG', 'TCT', 'TGA', 'TGC', 'TGG', 
                 'TGT', 'TTA', 'TTC', 'TTG', 'TTT']

# List of diseases
diseases = ['B-Chronic lymphocytic leukemia', 'Bladder carcinoma', 'Breast carcinoma', 'Colorectal carcinoma', 
            'Esophageal SCC', 'Head and Neck SCC', 'Hepatocellular carcinoma', 'Lung (NSCLC)', 'Ovarian carcinoma', 
            'Pancreatic carcinoma']

# List of Variant Types
variant_types = ['DEL', 'INS']

# Function to predict pathogenicity
def predict_pathogenicity(HG38_Start, mutant_codon, disease, variant_type):
    # Prepare input data with the user-selected values
    input_data = pd.DataFrame(columns=['HG38_Start'] + mutant_codons + diseases + variant_types)
    
    # Check columns of the DataFrame
    print("Columns of input_data:", input_data.columns)
    
    # Set the selected features
    input_row = [HG38_Start] + \
                [1 if codon == 'Mutant_Codon_' + mutant_codon else 0 for codon in mutant_codons] + \
                [1 if d == 'Disease_' + disease else 0 for d in diseases] + \
                [1 if v == 'Variant_Type_' + variant_type else 0 for v in variant_types] 

    print("Input row:", input_row)  # Add this line to print out the input_row
    input_data.loc[0] = input_row
    
    # Make the prediction
    prediction = model.predict(input_data)
    return prediction


# Main function to run the Streamlit app
def main():
    # Set page title
    st.title('PathFinder: TP53 Variant Pathogenicity Predictor')
    
    # Add input fields for mutant codon, disease, variant type, HG38_Start, somatic_stat, and tumor_rep
    HG38_Start = st.text_input("Enter HG38 Start site:")
    mutant_codon = st.selectbox('Select Mutant Codon:', mutant_codons)
    disease = st.selectbox('Select Disease:', diseases, index=diseases.index('Breast carcinoma'))
    variant_type = st.selectbox('Select Variant Type:', variant_types)
    
    # Make prediction when the 'Predict' button is clicked
    if st.button('Predict'):
        prediction = predict_pathogenicity(HG38_Start, mutant_codon, disease, variant_type)
        st.write('Prediction:', prediction)

# Run the main function
if __name__ == '__main__':
    main()
