# Pokémon Type Predictor

A machine learning app that predicts a Pokémon's primary type based on its stats using a Random Forest model.

![App Screenshot](screenshot.png)

## Features
- Predict Pokémon Type 1 using stats like HP, Attack, Defense, etc.
- Interactive user interface with Streamlit.
- Pre-trained Random Forest model for fast predictions.

## Tech Stack
- **Python**
- **Streamlit** (UI)
- **scikit-learn** (Model)
- **pandas** (Data Handling)
- **poetry** (Dependency Management)

## Data set
Download the pokedex.csv data set on Kaggle [here](https://www.kaggle.com/datasets/christofferms/pokemon-with-stats-and-image), then save it in the `data/` folder.

## Installation & Setup (Replit + Poetry)

1. **Clone the Project on Replit**
   - Import the repository directly into Replit: `https://github.com/your-username/pokemon-type-predictor.git`


2. **Install Dependencies**
```bash
poetry install
```

3. **Train the Model**
```bash
poetry run python scripts/train_model.py
```

4. **Run the App**
```bash
poetry run streamlit run app.py
```

## File Structure
```
├── app.py                    # Streamlit app
├── data/                     # Pokémon dataset
├── models/                   # Trained model
├── scripts/                  # Model training script
└── pyproject.toml            # Poetry dependencies
```