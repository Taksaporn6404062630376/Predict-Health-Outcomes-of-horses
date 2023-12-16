import streamlit as st
import pickle
import pandas as pd
import joblib

model_path = "C:\\Users\\USER\\mlweb\\randomforest.pkl"
classifier = joblib.load(model_path)

# Assuming df is your DataFrame
df = pd.read_csv("C:\\Users\\USER\\mlweb\\test.csv")  # Replace with the actual path to your data


def get_data_for_id(selected_id):
    # Function to retrieve data for the selected ID
    selected_data = df[df['id'] == selected_id]
    selected_data = selected_data.drop('hospital_number', axis=1)
    selected_data = selected_data.drop('lesion_1', axis=1)
    selected_data = selected_data.drop('lesion_2', axis=1)
    selected_data = selected_data.drop('lesion_3', axis=1)
    return selected_data

# Display part
labels = ['died', 'euthanized' , 'lived']

st.write("# Predict Health Outcomes of Horses")

# Allow the user to input an ID
selected_id = st.text_input("Enter ID for prediction:", 0)

# If the user inputs a valid ID, retrieve and display the corresponding data
if selected_id.isdigit():
    selected_id = int(selected_id)
    user_input_data = get_data_for_id(selected_id)

    # Display the retrieved data
    st.subheader(f"User Input Parameters for ID {selected_id}")
    st.write(user_input_data)
    
    # Ensure that 'user_input_data' and 'classifier' have aligned columns
    user_input_data, _ = user_input_data.align(classifier, axis=1, fill_value=0)

   # Predict health outcomes
    prediction = classifier.predict(user_input_data)
    prediction_label = labels[prediction[0]]

    prediction_probabilities = classifier.predict_proba(user_input_data)

    st.subheader('Prediction')
    st.write(prediction_label)

    st.subheader('Prediction Probability')
    st.write(prediction_probabilities)

    st.write(prediction_probabilities)
else:
    st.warning("Please enter a valid numeric ID.")
