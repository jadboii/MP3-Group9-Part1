import tkinter as tk
from tkinter import messagebox
import datetime
import numpy as np


# Function to calculate the Lagrange interpolation
def lagrange_interpolation(x, y, target):
    """
    x: List of dates in ordinal (numeric) format
    y: List of corresponding USD to PHP exchange rates
    target: The target date in ordinal (numeric) format
    """
    # Number of points
    n = len(x)
    # Initialize the result
    result = 0
    # Loop over all points
    for i in range(n):
        # Calculate the Lagrange basis polynomial
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (target - x[j]) / (x[i] - x[j])
        # Add the term to the result
        result += term
    return result


# Main GUI class
class CurrencyConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("USD to PHP Conversion Calculator")
        self.geometry("400x400")

        # Data storage
        self.data = []

        # Input for date and exchange rate
        self.date_label = tk.Label(self, text="Date (YYYY-MM-DD):")
        self.date_label.grid(row=0, column=0, padx=10, pady=10)
        self.date_entry = tk.Entry(self)
        self.date_entry.grid(row=0, column=1, padx=10, pady=10)

        self.rate_label = tk.Label(self, text="USD to PHP rate:")
        self.rate_label.grid(row=1, column=0, padx=10, pady=10)
        self.rate_entry = tk.Entry(self)
        self.rate_entry.grid(row=1, column=1, padx=10, pady=10)

        # Button to add data point
        self.add_button = tk.Button(self, text="Add Data Point", command=self.add_data_point)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Listbox to display data points
        self.data_listbox = tk.Listbox(self)
        self.data_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Input for target date
        self.target_label = tk.Label(self, text="Target Date (YYYY-MM-DD):")
        self.target_label.grid(row=4, column=0, padx=10, pady=10)
        self.target_entry = tk.Entry(self)
        self.target_entry.grid(row=4, column=1, padx=10, pady=10)

        # Button to calculate interpolation
        self.calculate_button = tk.Button(self, text="Calculate Conversion Rate",
                                          command=self.calculate_conversion_rate)
        self.calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Result display
        self.result_label = tk.Label(self, text="Estimated Conversion Rate:")
        self.result_label.grid(row=6, column=0, padx=10, pady=10)
        self.result_value = tk.Label(self, text="")
        self.result_value.grid(row=6, column=1, padx=10, pady=10)

    def add_data_point(self):
        try:
            # Get date and rate from input
            date_str = self.date_entry.get()
            rate = float(self.rate_entry.get())
            # Convert the date string to a date object and then to ordinal format
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            date_ordinal = date.toordinal()

            # Append the data point to the list
            self.data.append((date_ordinal, rate))
            # Add to the listbox for display
            self.data_listbox.insert(tk.END, f"{date_str}: {rate}")

            # Clear the input fields
            self.date_entry.delete(0, tk.END)
            self.rate_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid date and rate.")

    def calculate_conversion_rate(self):
        if len(self.data) < 2:
            messagebox.showerror("Insufficient Data", "Please enter at least two data points to perform interpolation.")
            return

        try:
            # Get the target date from input
            target_date_str = self.target_entry.get()
            target_date = datetime.datetime.strptime(target_date_str, "%Y-%m-%d")
            target_ordinal = target_date.toordinal()

            # Separate the data into x (dates) and y (exchange rates)
            x = [point[0] for point in self.data]
            y = [point[1] for point in self.data]

            # Calculate the estimated rate using Lagrange interpolation
            estimated_rate = lagrange_interpolation(x, y, target_ordinal)

            # Display the result
            self.result_value.config(text=f"{estimated_rate:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter a valid target date.")


# Create and run the application
app = CurrencyConverterApp()
app.mainloop()