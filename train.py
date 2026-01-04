
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor
import joblib

# Load the dataset
df = pd.read_csv('dataset/Clean_Dataset.csv')

# Define features and target
categorical_features = ['airline', 'source_city', 'destination_city', 'departure_time', 'arrival_time', 'stops', 'class']
numerical_features = ['duration', 'days_left']
target = 'price'

X = df[categorical_features + numerical_features]
y = df[target]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ],
    remainder='passthrough'
)

# Create the model pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', XGBRegressor(objective='reg:squarederror', n_estimators=100, random_state=42))
])

# Train the model
model.fit(X_train, y_train)

# Save the model and preprocessor
joblib.dump(model, 'flight_price_model.pkl')
joblib.dump(preprocessor, 'preprocessor.pkl')

print("Model training complete and artifacts saved.")
