import streamlit as st
import joblib
import os
import numpy as np

# Load the trained model
model_path = os.path.join('models', 'pokemon_type_model.pkl')
model = joblib.load(model_path)

st.title('Pokédex Type Predictor')

# Description of the streamlit app
st.write('''
This application predicts the primary Pokémon type based on its stats. 
Simply input the stats of a Pokémon, and the model will estimate 
what type the Pokémon most likely belongs to based on the trained model.
The type prediction is a result of a machine learning model trained 
using a Random Forest Classifier on historical Pokémon data.
''')

# Input fields for Pokémon stats
hp = st.number_input('HP', min_value=1, max_value=255, value=50)
attack = st.number_input('Attack', min_value=1, max_value=255, value=50)
defense = st.number_input('Defense', min_value=1, max_value=255, value=50)
sp_atk = st.number_input('SP. Atk.', min_value=1, max_value=255, value=50)
sp_def = st.number_input('SP. Def', min_value=1, max_value=255, value=50)
speed = st.number_input('Speed', min_value=1, max_value=255, value=50)

# When the user clicks the button, make a prediction
if st.button('Predict Pokémon Type'):
    # Create a feature vector from the inputs
    features = np.array([[hp, attack, defense, sp_atk, sp_def, speed]])

    # Make a prediction
    predicted_type = model.predict(features)[0]

    st.write(f'The predicted Pokémon type is: {predicted_type}')
