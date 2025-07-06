import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder
import joblib

#Load the dataset
df=pd.read_csv("data/telco_churn.csv")

#Cleaning
df.dropna(inplace=True)
df['Churn']=df["Churn"].apply(lambda x:1 if x=="Yes" else 0)

#Separate the features and target
# x=df.drop("Churn",axis=1)
x= df.drop(["Churn", "customerID"], axis=1)
y=df['Churn']

#identify the column types
numerical_cols=x.select_dtypes(include=['int64','float64']).columns.tolist()
categorical_cols=x.select_dtypes(include=['object']).columns.tolist()

#Preprocessing
numeric_transformer=Pipeline(steps=[('Scaler',StandardScaler())])
categorical_transformer=Pipeline(steps=[('onehot',OneHotEncoder(handle_unknown='ignore'))])

preprocessor=ColumnTransformer(transformers=[
    ("num",numeric_transformer,numerical_cols),
    ("cat",categorical_transformer,categorical_cols)
])

#Combine preprocessing and classifier

clf=Pipeline(steps=[
    ("preprocessor",preprocessor),
    ("classifier",RandomForestClassifier(random_state=42))
])

#Train the model
x_train, _, y_train, _ = train_test_split(x, y, test_size=0.2, random_state=42)
clf.fit(x_train, y_train)

#Save the model
joblib.dump(clf,"model.pkl")

print("Done")