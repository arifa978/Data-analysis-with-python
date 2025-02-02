import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,LabelEncoder
data = pd.read_csv('tourist_record.csv')
print(data)
x = data.iloc[:,[1,4]].values
y = data.iloc[:,2].values
print(x)
print(y)
lb = LabelEncoder()
x[:,0] = lb.fit_transform(x[:,0])
print(x)
lb2 = LabelEncoder()
y = lb2.fit_transform(y)
print("\n The respected dependent variable are =", y)
x_train, x_test, y_train, y_test = (train_test_split(x, y, test_size=0.3, random_state=0))
print(x_train)
print(x_test)

scale = MinMaxScaler()
x_train = scale.fit_transform(x_train)
x_test = scale.fit_transform(x_test)
print(x_train)
print(x_test)

model = SVC(kernel='linear' , random_state=0)
model.fit(x_train, y_train)
y_predict = model.predict(x_test)

cm = confusion_matrix(y_test, y_predict)
print(cm)
acc = accuracy_score(y_test, y_predict)
print(acc)

# Feature scaling
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Train model using Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(x_train, y_train)
y_pred_rf = rf_model.predict(x_test)

# Train model using SVM
svm_model = SVC()
svm_model.fit(x_train, y_train)
y_pred_svm = svm_model.predict(x_test)

# Evaluate models
print("Random Forest Accuracy:", accuracy_score(y_test, y_pred_rf))

print("SVM Accuracy:", accuracy_score(y_test, y_pred_svm))