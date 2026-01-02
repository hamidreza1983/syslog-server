import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib
from config import CSV_FILE

df = pd.read_csv(CSV_FILE)
df = df.groupby('state').filter(lambda x: len(x) >= 2)

X = df[['cpu', 'mem', 'disk']]
y = df['state']

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42,
)


model = RandomForestClassifier(
    n_estimators=200,
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))
print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

joblib.dump(model, "rf_model.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")

print("\nModel and LabelEncoder saved successfully.")
