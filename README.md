# 💰 Budget Tracker with Predictions

A simple **budget tracking app** built with **Streamlit** and **Prophet** for expense prediction. Track your expenses by category, visualize trends, and get **future expense predictions** for the next 5 days.

## ✨ Features

* **Add and track expenses** by **category** and **date**.

* View **expense history** in a table.

* **Bar chart** showing total spending per category.

* **Line chart** showing expense trends over time.

* Predict **future expenses** using **Prophet**.

* Supports **multiple categories** and custom category names.

## 🛠️ Tech Stack

* **Python 3.x**

* **Streamlit** – interactive web app

* **Pandas** – data manipulation

* **Prophet** – time-series predictions

* **SQLite** – storing expense data

* **scikit-learn** – optional (linear regression fallback)

## 🚀 Setup Instructions

1. **Clone the repository**:

git clone https://github.com/Voix-22/budget_tracker.git
cd budget_tracker


2. **Create a virtual environment**:

python -m venv .venv


3. **Activate the virtual environment**:

* **Windows**:

  ```
  .venv\Scripts\activate
  
  ```

* **Mac/Linux**:

  ```
  source .venv/bin/activate
  
  ```

4. **Install dependencies**:

pip install -r requirements.txt


## 🏃‍♀️ Run the App

streamlit run streamlit_app.py


Open the URL shown in your terminal (usually `http://localhost:8501`).

Add expenses, view charts, and check future predictions
