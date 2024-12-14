import streamlit as st
from db import initialize_database

# Initialize the database
initialize_database()

# Sidebar for navigation
st.sidebar.title("Navigation")
pages = {
    "Welcome": "welcome",
    "Submit Request": "request",
    "Manager View": "manager_view",
    "Finance View": "finance_view",
    "All Requests": "all_requests"
}

# Navigation
page_name = st.sidebar.radio("Go to", list(pages.keys()))
page_module = pages[page_name]

# Dynamic import and page rendering
try:
    # Import page dynamically
    page = __import__(f"pages.{page_module}", fromlist=["show_page"])
    page.show_page()
except Exception as e:
    st.error(f"Error loading page '{page_name}': {e}")
