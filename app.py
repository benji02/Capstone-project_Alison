{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0cc3b04d",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-04-01 15:25:09.053 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\aliva\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "from joblib import load\n",
    "\n",
    "# Load the trained model\n",
    "model = load('pipeline.joblib')  # Replace 'your_model.joblib' with the path to your trained model file\n",
    "diseases = [\n",
    "    'Other',\n",
    "    'Breast carcinoma',\n",
    "    'Colorectal carcinoma',\n",
    "    'Lung (NSCLC)',\n",
    "    'Head and Neck SCC',\n",
    "    'Ovarian carcinoma',\n",
    "    'Bladder carcinoma',\n",
    "    'Esophageal SCC',\n",
    "    'Hepatocellular carcinoma',\n",
    "    'Pancreatic carcinoma',\n",
    "    'B-Chronic lymphocytic leukemia',\n",
    "    'Unknown'\n",
    "]\n",
    "\n",
    "# Function to predict pathogenicity\n",
    "def predict_pathogenicity(mutant_codon, disease):\n",
    "    # Perform any necessary preprocessing on the input features\n",
    "    # For example, you might encode categorical variables and transform the input data\n",
    "\n",
    "    # Make the prediction\n",
    "    prediction = model.predict([[mutant_codon, disease]])  \n",
    "    return prediction\n",
    "\n",
    "# Main function to run the Streamlit app\n",
    "def main():\n",
    "    # Set page title\n",
    "    st.title('Mutation Pathogenicity Predictor')\n",
    "\n",
    "    # Add input fields for mutant codon and disease\n",
    "    mutant_codon = st.text_input('Enter Mutant Codon:', 'AAA')\n",
    "    disease = st.selectbox('Select Disease:', diseases, index=diseases.index('Breast carcinoma'))\n",
    "\n",
    "    # Make prediction when the 'Predict' button is clicked\n",
    "    if st.button('Predict'):\n",
    "        prediction = predict_pathogenicity(mutant_codon, disease)\n",
    "        st.write('Prediction:', prediction)\n",
    "\n",
    "# Run the main function\n",
    "if __name__ == '__main__':\n",
    "    main()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
