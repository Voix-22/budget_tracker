import streamlit as st
import pandas as pd
import datetime
from data_handler import initialize_db, load_expenses, save_expense
from prediction import predict_future, predict_future_all

# Initialize DB
initialize_db()

st.title("💰 Budget Tracker with Predictions")

# Load existing data
data = load_expenses()

# ----------------- Add new expense -----------------
st.subheader("Add a New Expense")
category = st.text_input("Category", value="Other")  # allows custom category
amount = st.number_input("Amount", min_value=1, step=1)
date = st.date_input("Date", value=datetime.date.today())

if st.button("Add Expense"):
    save_expense(category, amount, date)
    st.success(f"Added {amount} in {category} on {date}!")
    data = load_expenses()  # reload data after saving

# ----------------- Show expense history -----------------
st.subheader("Expense History")
st.dataframe(data)

# ----------------- Category-wise expense chart -----------------
if not data.empty:
    st.subheader("Expense Chart by Category")
    chart_data = data.groupby("category")["amount"].sum().reset_index()
    st.bar_chart(chart_data.set_index("category"))

# ----------------- Expense trend over time -----------------
if not data.empty:
    st.subheader("Expense Trend Over Time")
    data_sorted = data.sort_values("date")
    st.line_chart(data_sorted.set_index("date")["amount"])

# ----------------- Future expense prediction -----------------
if not data.empty:
    st.subheader("Future Expense Prediction (Prophet)")
    
    # Select category
    selected_category = st.selectbox("Select Category for Prediction", ["All"] + list(data["category"].unique()))
    
    if selected_category == "All":
        all_preds = predict_future_all(data)
        st.write("📈 Predicted average expense for next 5 days (all categories):")
        st.table(all_preds)  # show dictionary as table
    else:
        cat_pred = predict_future(data, category=selected_category)
        st.write(f"📈 Predicted average expense for next 5 days in **{selected_category}**: {cat_pred:.2f}")
        
        # Optional: visualize next 5 days
        future_df = pd.DataFrame({
            "Date": pd.date_range(start=pd.to_datetime("today"), periods=5),
            "Predicted Amount": [cat_pred]*5
        })
        future_df = future_df.set_index("Date")
        st.line_chart(future_df)
