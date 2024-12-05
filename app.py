import streamlit as st
import sqlite3
from db import create_connection, create_tables

# Initialize database
db_file = "requests.db"
conn = create_connection(db_file)
if conn:
    create_tables(conn)

# App title
st.title("Request Management System")
st.sidebar.title("Navigation")

# Sidebar navigation
pages = ["Home", "Submit Request", "Manager Dashboard", "Finance Dashboard"]
selected_page = st.sidebar.radio("Go to:", pages)

# Home Page
if selected_page == "Home":
    st.header("Welcome to the Request Management System")
    st.write("""
        This system helps manage item and fund requests efficiently.
        Navigate through the sections to submit requests, approve them, or manage finances.
    """)

# Submit Request Page
elif selected_page == "Submit Request":
    st.header("Submit a Request")

    # Form for submitting a request
    with st.form("request_form"):
        requester_name = st.text_input("Your Name")
        department = st.text_input("Department")
        project = st.text_input("Project Name")
        purpose = st.text_area("Purpose of Request")
        amount_requested = st.number_input("Amount Requested", min_value=0.0, step=100.0)

        # Submit button
        submitted = st.form_submit_button("Submit Request")
        if submitted:
            # Simulate saving to database
            if conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO Requests (requester_name, department, project, purpose, amount_requested)
                    VALUES (?, ?, ?, ?, ?)
                """, (requester_name, department, project, purpose, amount_requested))
                conn.commit()
                st.success("Your request has been submitted successfully!")

# Manager Dashboard Page
elif selected_page == "Manager Dashboard":
    st.header("Manager Dashboard")
    st.write("This is where managers will see and approve requests. (Placeholder for now)")

# Finance Dashboard Page
elif selected_page == "Finance Dashboard":
    st.header("Finance Dashboard")
    st.write("This is where finance officers will manage funds and liquidations. (Placeholder for now)")

