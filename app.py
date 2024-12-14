# app.py
import streamlit as st
from db import initialize_database

# Initialize the database
initialize_database()

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Welcome", "Submit Request", "Manager View", "Finance View", "All Requests"])

if page == "Welcome":
    import pages.welcome as welcome
    welcome.show_page()
elif page == "Submit Request":
    import pages.request as request_page
    request_page.show_page()
elif page == "Manager View":
    import pages.manager_view as manager_view
    manager_view.show_page()
elif page == "Finance View":
    import pages.finance_view as finance_view
    finance_view.show_page()
elif page == "All Requests":
    import pages.all_requests as all_requests
    all_requests.show_page()
