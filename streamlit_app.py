import pandas as pd
import streamlit as st

try:
    df=pd.read_csv("transactions.csv")
except FileNotFoundError:
    df=pd.DataFrame(columns=["date","category","type","amount"])

print("Your Transaction DataFrame:")
print(df.head())