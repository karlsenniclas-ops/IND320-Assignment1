import matplotlib.pyplot as plt
import streamlit as st
from data import load_data

st.title("Plot")

df = load_data()

# Units per column, used as y axis labels
UNITS = {
    "fill_level": "Share of capacity",
    "capacity_twh": "TWh",
    "stored_energy_twh": "TWh",
    "fill_level_prev_week": "Share of capacity",
    "fill_level_change": "Change in share of capacity",
}

# Share columns first, TWh columns last: keeps the legend colours in sync with the left axis when all columns are plotted together
PLOT_ORDER = ["fill_level", "fill_level_prev_week", "fill_level_change", "capacity_twh", "stored_energy_twh"]
TWH_COLUMNS = ["capacity_twh", "stored_energy_twh"]

column_choice = st.selectbox("Column", ["All columns"] + list(df.columns))

# Month options as "YYYY-MM" strings, default to just the first month
months = sorted(df.index.strftime("%Y-%m").unique())
start_month, end_month = st.select_slider(
    "Month range",
    options=months,
    value=(months[0], months[0]),
)

# Filter rows to the chosen month range
month_strings = df.index.strftime("%Y-%m")
mask = (month_strings >= start_month) & (month_strings <= end_month)
plot_df = df.loc[mask]

fig, ax = plt.subplots()

if column_choice == "All columns":
    ordered = plot_df[PLOT_ORDER]
    ordered.plot(ax=ax, secondary_y=TWH_COLUMNS)
    ax.set_ylabel("Share of capacity")
    ax.right_ax.set_ylabel("TWh")

    # Combine the legend from both axes and place it below the plot so it does not cover the lines
    lines = ax.get_lines() + ax.right_ax.get_lines()
    labels = [line.get_label() for line in lines]
    ax.get_legend().remove()
    ax.legend(lines, labels, loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=3)
else:
    plot_df[column_choice].plot(ax=ax)
    ax.set_ylabel(UNITS[column_choice])

ax.set_xlabel("Date")
ax.set_title(f"{column_choice}, Norway, {start_month} to {end_month}")

st.pyplot(fig)
