import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import matplotlib.pyplot as plt

class ForexData:
    """
    A class to represent the Forex data and related operations.
    """
    def __init__(self, dates, exchange_rates):
        """
        Initialize the ForexData with dates and exchange rates.
        """
        self.dates = dates
        self.exchange_rates = exchange_rates
        self.date_values = [self.date_to_num(date) for date in self.dates]

    def lagrange_interpolation(self, x, x_data, y_data):
        """
        Calculates the Lagrange polynomial for a given x value.
        """
        n = len(x_data)
        result = 0
        for i in range(n):
            numerator = 1
            denominator = 1
            for j in range(n):
                if i != j:
                    numerator *= (x - x_data[j])
                    denominator *= (x_data[i] - x_data[j])
            result += y_data[i] * numerator / denominator
            print(f"f({result}) = {y_data[i]} * {numerator} / {denominator}")
        return result

    def date_to_num(self, date_str):
        """
        Convert a date string to numerical value.
        """
        ref_date = datetime(2002, 1, 1)
        target_date = datetime.strptime(date_str, "%Y-%m-%d")
        return (target_date - ref_date).days

    def interpolate_exchange_rate(self, target_date_str):
        """
        Interpolate the exchange rate for a given date.
        """
        try:
            target_value = self.lagrange_interpolation(self.date_to_num(target_date_str), self.date_values, self.exchange_rates)
            return f"Interpolated exchange rate for {target_date_str}: {target_value:.4f}"
        except ValueError:
            return "Invalid date format. Please enter a date in YYYY-MM-DD format."

    def plot_exchange_rates(self):
        """
        Plot the exchange rates data.
        """
        plt.plot(self.dates, self.exchange_rates, marker='o')
        plt.xlabel('Date')
        plt.ylabel('Exchange Rate')
        plt.title('U$ to PHP Forex Exchange Rate Interpolation Forex Exchange Rates')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

class ForexGUI:
    """
    A class to represent the Forex GUI using tkinter.
    """
    def __init__(self, root):
        """
        Initialize the GUI elements.
        """
        self.root = root
        self.root.title("AU$ to PHP Forex Exchange Rate Interpolation")

        self.label = tk.Label(root, text="Enter a date (YYYY-MM-DD):")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Calculate", command=self.calculate_rate)
        self.button.pack()

        self.plot_button = tk.Button(root, text="Plot Data", command=forex_data.plot_exchange_rates)
        self.plot_button.pack()

    def calculate_rate(self):
        """
        Calculate the interpolated exchange rate.
        """
        target_date_str = self.entry.get()
        result = forex_data.interpolate_exchange_rate(target_date_str)
        messagebox.showinfo("Result", result)

# Sample data (replace with actual forex data)
dates = ["2002-01-01", "2002-02-01", "2002-03-01", "2002-04-01", "2002-05-01", "2002-06-01", "2002-07-01", "2002-08-01", "2002-09-01", "2002-10-01", "2002-11-01", "2002-12-01", "2003-01-01", "2003-02-01", "2003-03-01", "2003-04-01", "2003-05-01", "2003-06-01", "2003-07-01", "2003-08-01", "2003-09-01", "2003-10-01", "2003-11-01", "2003-12-01"]
exchange_rates = [26.5850, 26.2703, 26.7617, 27.2878, 27.3863, 28.6447, 28.0576, 28.0241, 28.5094, 29.0770, 29.9216, 30.1003, 31.1729, 32.1087, 32.8384, 32.1492, 34.0153, 35.4584, 35.5996, 35.8302, 36.3606, 38.1060, 39.6118, 40.8515]

forex_data = ForexData(dates, exchange_rates)

root = tk.Tk()
app = ForexGUI(root)
root.mainloop()
