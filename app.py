import streamlit as st

# st.navigation shows these pages as a sidebar menu and lets the page files stay in the project's root folder instead of a pages subfolder
pg = st.navigation([
    st.Page("home.py", title="Home", default=True),
    st.Page("table.py", title="Table"),
    st.Page("plot.py", title="Plot"),
    st.Page("page4.py", title="Page 4"),
])
pg.run()
