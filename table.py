import pandas as pd
import streamlit as st
from data import load_data

st.title("Table")

df = load_data()

# First month present in the data, e.g. Jan 1995
first_month = df.index.strftime("%Y-%m")[0]
first_month_df = df[df.index.strftime("%Y-%m") == first_month]

# One row per column, with the whole first month as a list of weekly values so it can draw a small chart
table_data = pd.DataFrame({
    "column": first_month_df.columns,
    "first_month": [first_month_df[col].tolist() for col in first_month_df.columns],
})

st.dataframe(
    table_data,
    hide_index=True,
    column_config={
        "first_month": st.column_config.LineChartColumn("First month"),
    },
)
