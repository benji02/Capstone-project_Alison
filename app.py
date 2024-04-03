import streamlit as st
import pandas as pd
from joblib import load
import numpy as np

# Load the trained model
model = load('pipeline.joblib')  # Replace 'pipeline.joblib' with the path to your trained model file

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
    input_data = pd.DataFrame(columns=['HG38_Start'] + ['Mutant_Codon_' + mutant_codon for mutant_codon in mutant_codons] + 
                              ['Disease_' + disease for disease in diseases] + 
                              ['Variant_Type_' + variant_type for variant_type in variant_types])
    
    
    # Check columns of the DataFrame
    print("Columns of input_data:", input_data.columns)
    
    # Set the selected features
    input_row = [HG38_Start] + \
                [1 if mc == mutant_codon else 0 for mc in mutant_codons] + \
                [1 if d == disease else 0 for d in diseases] + \
                [1 if vt == variant_type else 0 for vt in variant_types] 

    print("Input row:", input_row)  # Add this line to print out the input_row
    input_data.loc[0] = input_row

    st.dataframe(input_data)
    st.write("Shape of input_data:", input_data.shape)  # Print the shape of input_data
    st.write("Data type of input_data:", input_data.dtypes)  # Print the data type of input_data
    
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
    st.write(mutant_codon)
    
    # Make prediction when the 'Predict' button is clicked
    if st.button('Predict'):
        # Convert inputs to integers
        HG38_Start_int = int(HG38_Start)
        prediction = predict_pathogenicity(HG38_Start_int, mutant_codon, disease, variant_type)

      
        st.write(type(prediction))
        st.write(type(input_data))
        

              
        st.write('Prediction:', prediction)
        if prediction == 1:
            st.write("This mutant codon is Pathogenic")
        elif prediction == 2:
            st.write("This mutant codon is likely to be Pathogenic")
        elif prediction == 3:
            st.write("This mutant codon has uncertain significance")
        elif prediction == 4:
            st.write("This mutant codon is Benign")
        else:
            st.write("Unknown")
    else:
        st.write('Please fill out the required fields to predict the pathogenicity')

# Run the main function
if __name__ == '__main__':
    main()
