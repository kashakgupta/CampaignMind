# CampaignMind
### Marketing Campaign Effectiveness Prediction Using Machine Learning and Deep Learning

CampaignMind is a machine learning and deep learning based application
that analyzes bank marketing campaign data and predicts whether a customer
is likely to subscribe to a term deposit.

## Project Overview

The project uses the UCI Bank Marketing dataset to explore customer
behavior, analyze campaign effectiveness, and compare predictive models.

## Technologies Used

- Python
- Streamlit
- Pandas and NumPy
- Scikit-learn
- TensorFlow / Keras
- Matplotlib and Seaborn
- Jupyter Notebook

## Machine Learning Models

- Random Forest Classifier
- Artificial Neural Network (ANN)

Random Forest is selected as the final prediction model based on its
overall balance of evaluation metrics.

## Features

- Interactive Streamlit dashboard
- Customer subscription prediction
- Exploratory Data Analysis (EDA)
- Random Forest model evaluation
- ANN model evaluation
- Model performance comparison
- Confusion matrices and ROC curves
- Feature importance visualization

## Project Structure

```text
CampaignMind/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── notebooks/
│   ├── 01_EDA_Preprocessing.ipynb
│   ├── 02_ML_RandomForest.ipynb
│   └── 03_DL_ANN.ipynb
│
├── dataset/
│   └── bank-full.csv
│
├── models/
│   ├── random_forest_model.pkl
│   ├── preprocessor.pkl
│   ├── ann_best.keras
│   └── ann_model.keras
│
└── results/
    ├── ann_results.json
    ├── random_forest_results.json
    ├── model_comparison.json
    └── graphs/
```

## Installation and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/kashakgupta/CampaignMind.git
   ```

2. Navigate to the project folder:

   ```bash
   cd CampaignMind
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

## Dataset

The project uses the Bank Marketing dataset from the UCI Machine
Learning Repository.

Dataset: https://archive.ics.uci.edu/dataset/222/bank+marketing

## Evaluation

The models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

## Project Repository

GitHub: https://github.com/kashakgupta/CampaignMind

---

**Project Title:** Marketing Campaign Effectiveness Prediction Using
Machine Learning and Deep Learning

**Project Name:** CampaignMind
