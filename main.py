import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pymongo

# Load dataset
data = pd.read_csv("dataset.csv")

# Encode categorical features
data = pd.get_dummies(data, columns=["SoilType", "Fertilizer"])

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["cropdb"]
collection = db["cropdata"]
collection.insert_many(data.to_dict("records"))

# Split into features and target
X = data.drop("Yield", axis=1)
y = data["Yield"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("Sample prediction:", predictions[:5])

