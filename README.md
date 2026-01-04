# ✈️ Flight Price Predictor 🔮

A sleek and simple web application to predict flight prices using a machine learning model. Built with Streamlit and Scikit-learn, this tool provides a user-friendly interface for estimating flight costs.

<img src="https://i.hizliresim.com/a87zfj3.png" alt="Project Banner" width="70%">

---

## ✨ Features

- **Intuitive UI:** Simple and clean interface built with Streamlit.
- **Dynamic Predictions:** Select your flight details and get an instant price estimate.
- **ML Powered:** Uses an XGBoost Regressor model trained on thousands of flight records.
- **Easy to Run:** Get the application running locally in just a few commands.

---

## 🚀 Getting Started

Follow these steps to run the Flight Price Predictor on your local machine.

### Prerequisites

- Python 3.9 or later
- `pip` package manager

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/alihaktan35/Flight-Price-Prediction.git
    cd Flight-Price-Prediction
    ```

2.  **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3.  **Train the model (if needed):**
    The pre-trained model is already included. However, you can re-train it by running:
    ```sh
    python train.py
    ```

4.  **Run the Streamlit app:**
    ```sh
    streamlit run app.py
    ```
    Open your browser and navigate to the local URL provided (usually `http://localhost:8501`).

---

## 🛠️ Built With

*   [**Python**](https://www.python.org/) - The core programming language.
*   [**Scikit-learn**](https://scikit-learn.org/) - For the machine learning pipeline and model.
*   [**XGBoost**](https://xgboost.ai/) - The gradient boosting library used for the regression model.
*   [**Pandas**](https://pandas.pydata.org/) - For data manipulation and analysis.
*   [**Streamlit**](https://streamlit.io/) - To create the interactive web UI.
*   [**Joblib**](https://joblib.readthedocs.io/) - For saving and loading the trained model.

---
Made by alihaktan35