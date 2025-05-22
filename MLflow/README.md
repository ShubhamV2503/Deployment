
# MLflow Tutorial for Binary Classification

This repository demonstrates the use of **MLflow** for tracking, managing, and deploying machine learning models on an imbalanced binary classification problem.

## 📌 Project Overview

This project showcases a complete ML workflow:
- Generating an imbalanced binary classification dataset (90% class 0, 10% class 1).
- Training models: **Logistic Regression**, **Random Forest**, and **XGBoost**.
- Handling imbalance with **SMOTETomek**.
- Using **MLflow** to log parameters, metrics, and models.
- Registering and transitioning models to production.

## 🚀 Features

- ✅ Generate synthetic imbalanced binary classification data
- ✅ Train and evaluate multiple ML models
- ✅ Handle class imbalance using `SMOTETomek`
- ✅ Track experiments with MLflow (params, metrics, artifacts)
- ✅ Register and manage models using MLflow Model Registry
- ✅ Load and use models for inference

## ⚙️ Getting Started

### Prerequisites

- Python 3.10.11
- Jupyter Notebook
- MLflow tracking server running locally (`http://localhost:5000`)
- Python libraries:
  ```
  numpy
  scikit-learn
  xgboost
  imbalanced-learn
  mlflow
  ```

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/mlflow-binary-classification-demo.git
cd mlflow-binary-classification-demo

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start MLflow server
mlflow server --host 127.0.0.1 --port 5000

# Launch Jupyter
jupyter notebook
```

## 📓 Notebooks

| Notebook | Description |
|----------|-------------|
| `first_experiment.ipynb` | Basic MLflow experiment with Logistic Regression |
| `ml_flow_binary_classification.ipynb` | Full pipeline with multiple models and logging |
| `ml_flow_model_management.ipynb` | Imbalance handling, model registry, and deployment steps |

## 📊 Usage

1. Open any notebook in Jupyter.
2. Follow the cell-by-cell instructions.
3. Track experiments at [http://localhost:5000](http://localhost:5000).
4. Use the model management notebook for registration and deployment.

## 📄 License

Licensed under the **Apache License 2.0**. See the `LICENSE` file for more details.

## 🙏 Acknowledgements

- [MLflow](https://mlflow.org/) for lifecycle management
- [Codebasics](https://www.youtube.com/c/codebasics) for course inspiration
- Libraries: `scikit-learn`, `xgboost`, `imbalanced-learn`, `numpy`
