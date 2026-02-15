import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
df = pd.read_csv("svm.csv")
X = df.drop("Target", axis=1).copy()
y = df["Target"]
print(df.isnull().sum())
le = LabelEncoder()
X['Gender'] = le.fit_transform(X['Gender'])
X['City'] = le.fit_transform(X['City'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
sc = StandardScaler()
x_train_sc=sc.fit_transform(X_train)
x_test_sc=sc.transform(X_test)
model = SVC(kernel='linear', random_state=42)
model.fit(x_train_sc, y_train)
y_pred = model.predict(x_test_sc)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
