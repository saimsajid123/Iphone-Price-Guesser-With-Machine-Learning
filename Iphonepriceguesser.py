import pandas as pd

from sklearn.linear_model import LinearRegression

data = pd.read_csv("priceguesserofiphone.csv")

model = LinearRegression()

model.fit(data[["version"]], data[["price"]])

latest_version = data["version"].max()

model_to_predict = int(input("Enter the number of the model you want to predict: "))

predicted_price = model.predict([[model_to_predict]])

print(f"Predicted price for iPhone {model_to_predict}: {predicted_price}")
