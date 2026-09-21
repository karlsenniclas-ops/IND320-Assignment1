import pandas as pd
import streamlit as st

# Norwegian to English column names, same mapping as in the notebook
COLUMN_RENAME = {
    "dato_Id": "date",
    "omrType": "area_type",
    "omrnr": "area_number",
    "iso_aar": "iso_year",
    "iso_uke": "iso_week",
    "fyllingsgrad": "fill_level",
    "kapasitet_TWh": "capacity_twh",
    "fylling_TWh": "stored_energy_twh",
    "neste_Publiseringsdato": "next_publication_date",
    "fyllingsgrad_forrige_uke": "fill_level_prev_week",
    "endring_fyllingsgrad": "fill_level_change",
}

# The five columns we plot and show in the app
VALUE_COLUMNS = [
    "fill_level",
    "capacity_twh",
    "stored_energy_twh",
    "fill_level_prev_week",
    "fill_level_change",
]


@st.cache_data
def load_data():
    """Load weekly reservoir data for all of Norway, sorted by date.

    Cached with st.cache_data so the CSV is only read once per session
    instead of on every rerun. In part 2 this reads from MongoDB instead.
    """
    df = pd.read_csv("reservoirs.csv", parse_dates=["dato_Id"])
    df = df.rename(columns=COLUMN_RENAME)

    # Keep only the rows for all of Norway, the raw file also has price areas and watercourse areas
    df = df[df["area_type"] == "NO"]

    # The raw rows are not sorted by date, so sort and use date as index
    df = df.sort_values("date").set_index("date")

    return df[VALUE_COLUMNS]
