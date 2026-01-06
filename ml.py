#Importing Libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# Load dataset
df = pd.read_csv('StudentPerformance (1).csv')
# Map Extracurricular Activities to 0/1
df['Extracurricular Activities'] = df['Extracurricular Activities'].map({
    "Yes": 1,
    "No": 0
})
# Features and target
X = df.drop('Performance Index', axis=1)
y = df['Performance Index']
# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)
# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)
# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)
# Evaluate model
y_pred = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))
# User input for prediction
def predict_performance(hours, prev, extra, sleep, sample):
    new_student = pd.DataFrame(
        [[hours, prev, extra, sleep, sample]],
        columns=X.columns
    )
    new_student_scaled = scaler.transform(new_student)
    new_student_scaled = pd.DataFrame(new_student_scaled, columns=X.columns)
    prediction = model.predict(new_student_scaled)[0]
    return max(0, prediction)   # no negative

