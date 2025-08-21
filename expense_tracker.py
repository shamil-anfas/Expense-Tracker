import datetime
import pandas as pd
import matplotlib.pyplot as plt

class Expensetracker:
    def __init__(self, expense, category, note):
        self.expense = expense
        self.category = category.lower()
        self.note = note
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def save_to_file(self):
        with open("expenses.txt", "a") as file:
            file.write(f"{self.expense},{self.category},{self.note},{self.date}\n")

def show_bar_pie():
    try:
        df = pd.read_csv("expenses.txt", names=["Expense", "Category", "Note", "Date"])
        df["Expense"] = pd.to_numeric(df["Expense"], errors="coerce")

        if df.empty:
            print("No data to show graph.")
            return

        summary = df.groupby("Category")["Expense"].sum()

        fig, axes = plt.subplots(1, 2, figsize=(12, 6))

        # # Bar chart
        # summary.plot(kind="bar", color="skyblue", ax=axes[0])
        # axes[0].set_title("Expenses by Category (Bar Chart)")
        # axes[0].set_xlabel("Category")
        # axes[0].set_ylabel("Total Expense (₹)")

        # # Pie chart
        # summary.plot(kind="pie", autopct="%1.1f%%", ax=axes[1], startangle=90, colormap="tab20")
        # axes[1].set_ylabel("")
        # axes[1].set_title("Expenses by Category (Pie Chart)")

        # plt.tight_layout()
        # plt.show()

    except FileNotFoundError:
        print("No expenses to show graph.")

def show_table():
    try:
        df = pd.read_csv("expenses.txt", names=["Expense", "Category", "Note", "Date"])
        df["Expense"] = pd.to_numeric(df["Expense"], errors="coerce")

        if df.empty:
            print("No expenses found.")
            return

        fig, ax = plt.subplots(figsize=(10, 4))
        ax.axis("tight")
        ax.axis("off")
        table = ax.table(cellText=df.values, colLabels=df.columns, loc="center", cellLoc="center")
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1.2, 1.2)
        plt.title("All Expenses Table", fontsize=14)
        plt.show()

    except FileNotFoundError:
        print("No expenses found.")

def show_total_pie():
    try:
        df = pd.read_csv("expenses.txt", names=["Expense", "Category", "Note", "Date"])
        df["Expense"] = pd.to_numeric(df["Expense"], errors="coerce")

        if df.empty:
            print("No expenses found.")
            return

        summary = df.groupby("Category")["Expense"].sum()

        plt.figure(figsize=(6,6))
        summary.plot(kind="pie", autopct="%1.1f%%", startangle=90, colormap="Set3")
        plt.ylabel("")
        plt.title("Total Expenses by Category")
        plt.show()

    except FileNotFoundError:
        print("No expenses found.")

while True:
    print("Expense Tracker")
    print("1. Add Expense ")
    print("2. View All Expenses ")
    print("3. Show Total Expenses ")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        exp = int(input("Enter the amount: "))
        cate = input("Enter the Category: ")
        note = input("Enter a Note: ")

        obj = Expensetracker(exp, cate, note)
        obj.save_to_file()
        show_bar_pie()

    elif choice == "2":
        show_table()

    elif choice == "3":
        show_total_pie()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")