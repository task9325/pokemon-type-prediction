import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
data_path = os.path.join('data', 'pokedex.csv')
data = pd.read_csv(data_path)

# Data preprocessing
# Drop columns that are not useful for the model
data = data.drop(columns=['Image', 'Index', 'Name', 'Type 2'])

# Drop any rows with missing values
data = data.dropna()

# Separate features and target variable
X = data[['HP', 'Attack', 'Defense', 'SP. Atk.', 'SP. Def', 'Speed']]
y = data['Type 1']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42)

# Initialize the model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model accuracy: {accuracy:.2f}')

# Save the model to the models/ folder
model_path = os.path.join('models', 'pokemon_type_model.pkl')
joblib.dump(model, model_path)

print(f'Model saved to {model_path}')
