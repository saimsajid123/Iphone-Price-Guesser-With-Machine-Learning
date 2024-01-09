import tkinter as tk
from tkinter import ttk
import pandas as pd
from sklearn.linear_model import LinearRegression


class PriceGuesser:
    def __init__(self):
        self.root = tk.Tk()
        self.entry1 = tk.Entry(self.root)
        self.entry1.pack()
        self.button1 = tk.Button(self.root, text="Predict Price", command=self.predict_price)
        self.button1.pack()

        self.data = pd.read_csv("pricegusserofiphone.csv")

        self.model = LinearRegression()
        self.model.fit(self.data[["version"]], self.data["price"])

        self.label_result = tk.Label(self.root, text="")
        self.label_result.pack()

        self.root.mainloop()

    def predict_price(self):
        try:
            model_to_predict = float(self.entry1.get())
            predicted_price = self.model.predict([[model_to_predict]])
            predicted_price = predicted_price[0]

            result_text = f"Predicted price for iPhone {model_to_predict}: {predicted_price:.2f}"
        except ValueError:
            result_text = "Please enter a valid numeric value."

        self.label_result.config(text=result_text)


app = PriceGuesser()
