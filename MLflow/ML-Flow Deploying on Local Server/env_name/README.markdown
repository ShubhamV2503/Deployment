# Iris Classifier with MLflow Serving (macOS & Windows Setup)

This project demonstrates how to train, log, and serve a machine learning model (Iris Classifier) using **MLflow** on **macOS** and **Windows**.

## 🧠 Model Info

- **Dataset**: Iris (from `sklearn.datasets`)
- **Model Type**: Classification (Logistic Regression)
- **Framework**: Scikit-learn
- **Serving**: MLflow's `pyfunc` server

## 📦 Requirements (macOS & Windows)

- **Operating System**: macOS (Ventura/Sonoma) or Windows (10/11)
- **Python**: 3.8 or higher
- **Package Manager**: `pip` or `conda`
- **Dependencies**:
  - MLflow >= 2.0
  - Scikit-learn
  - Uvicorn (installed automatically by MLflow)

### Install Dependencies

Create a virtual environment and install dependencies using the provided `requirements.txt`.

#### On macOS
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

#### On Windows
```bash
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

If using **Homebrew Python** (macOS):
```bash
brew install python
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

If using **Conda** (macOS or Windows):
```bash
conda create -n env python=3.8
conda activate env
pip install -r requirements.txt
```

## 🚀 Train & Log the Model

Run the training script to train the model and log it to the local MLflow tracking URI:

```bash
python train_and_log.py
```

This will:
- Train a Logistic Regression model on the Iris dataset
- Log the model to MLflow
- Output the **run ID** (save this for serving the model)

## 🌐 Serve the Model Locally

Use the **run ID** from the training step to serve the model. Replace `<run_id>` with the actual ID:

```bash
mlflow models serve -m runs:/<run_id>/iris_model -p 5000 --no-conda
```

You should see output like:
```
Uvicorn running on http://127.0.0.1:5000
```

**Note**: Ensure no other process is using port 5000. If needed, change the port by modifying the `-p` flag (e.g., `-p 5001`).

## 🔍 Test the REST API

Open a new terminal (or command prompt on Windows) and test the model’s REST API.

### Method 1: Using `instances`
Send a prediction request with raw feature values:

#### On macOS
```bash
curl http://127.0.0.1:5000/invocations \
  -H "Content-Type: application/json" \
  -d '{
        "instances": [[6.0, 2.2, 4.0, 1.0]]
      }'
```

#### On Windows (Command Prompt)
```bash
curl http://127.0.0.1:5000/invocations -H "Content-Type: application/json" -d "{\"instances\": [[6.0, 2.2, 4.0, 1.0]]}"
```

### Method 2: Using `dataframe_records` (Recommended)
Use this method if the model expects named features (e.g., `"sepal length (cm)"`).

#### On macOS
```bash
curl http://127.0.0.1:5000/invocations \
  -H "Content-Type: application/json" \
  -d '{
        "dataframe_records": [
          {
            "sepal length (cm)": 6.0,
            "sepal width (cm)": 2.2,
            "petal length (cm)": 4.0,
            "petal width (cm)": 1.0
          }
        ]
      }'
```

#### On Windows (Command Prompt)
```bash
curl http://127.0.0.1:5000/invocations -H "Content-Type: application/json" -d "{\"dataframe_records\": [{\"sepal length (cm)\": 6.0, \"sepal width (cm)\": 2.2, \"petal length (cm)\": 4.0, \"petal width (cm)\": 1.0}]}"
```

**Expected Response**:
```json
{"predictions": [1]}
```

## 📝 Notes

- Ensure the MLflow server is running before sending prediction requests.
- Use `dataframe_records` for models trained with named columns (recommended for clarity and compatibility).
- On Windows, use double quotes (`"`) for JSON data in `curl` commands and escape them properly.
- If you encounter issues, verify that:
  - The virtual environment is activated.
  - All dependencies are installed correctly.
  - The MLflow tracking URI is accessible (default: `http://127.0.0.1:5000`).

## 📁 Project Structure

```
.
├── train_and_log.py
├── requirements.txt
└── README.md
```

## 🛠 Optional: Create a Virtual Environment

If not already done, create a virtual environment to isolate dependencies.

#### On macOS
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

#### On Windows
```bash
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

## 🛠 Troubleshooting

- **Port Conflict**: If port 5000 is in use, try a different port (e.g., `-p 5001`).
- **Python Version**: Ensure Python 3.8+ is installed (`python --version` or `python3 --version`).
- **Windows `curl` Issues**: If `curl` is not available, install it via `winget install curl` or use PowerShell’s `Invoke-RestMethod`.
- **MLflow Errors**: Check the MLflow tracking URI and ensure the `runs:/<run_id>/iris_model` path is correct.

## 📬 Contact

Feel free to open an issue or submit a pull request if you have improvements or encounter issues!