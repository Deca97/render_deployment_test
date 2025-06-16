import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.datasets import load_iris
import joblib


#1. Caricamento dataset
iris = load_iris()
X, y = iris.data, iris.target

# 2. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Addestramento modello
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. Valutazione
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# 5. Salvataggio
joblib.dump(model, "model.pkl")
print("✅ Modello salvato come model.pkl")
