import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

# Load Iris dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Start MLflow run and log the model
with mlflow.start_run() as run:
    mlflow.sklearn.log_model(model, artifact_path="iris_model", registered_model_name="IrisClassifier")
    print("Model saved to MLflow!")
    print("Run ID:", run.info.run_id)
