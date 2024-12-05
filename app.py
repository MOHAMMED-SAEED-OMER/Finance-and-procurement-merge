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
        requester_name = st.text_input("Your Name", max_chars=50)
        department = st.selectbox("Department", ["Finance", "Procurement", "HR", "Operations"])
        project = st.text_input("Project Name", max_chars=100)
        purpose = st.text_area("Purpose of Request", max_chars=500)
        amount_requested = st.number_input("Amount Requested (USD)", min_value=1.0, step=0.01)

        # Submit button
        submitted = st.form_submit_button("Submit Request")
        if submitted:
            if all([requester_name, department, project, purpose, amount_requested]):
                # Save to database
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO Requests (requester_name, department, project, purpose, amount_requested, status)
                    VALUES (?, ?, ?, ?, ?, 'Pending')
                """, (requester_name, department, project, purpose, amount_requested))
                conn.commit()
                st.success("Your request has been submitted successfully!")
            else:
                st.error("Please fill in all fields.")


# Manager Dashboard Page
elif selected_page == "Manager Dashboard":
    st.header("Manager Dashboard")

    # Fetch pending requests from the database
    cursor = conn.cursor()
    cursor.execute("SELECT id, requester_name, department, project, purpose, amount_requested FROM Requests WHERE status = 'Pending'")
    pending_requests = cursor.fetchall()

    if pending_requests:
        # Display pending requests in a table
        for request in pending_requests:
            st.subheader(f"Request ID: {request[0]}")
            st.write(f"**Requester Name:** {request[1]}")
            st.write(f"**Department:** {request[2]}")
            st.write(f"**Project Name:** {request[3]}")
            st.write(f"**Purpose:** {request[4]}")
            st.write(f"**Amount Requested:** ${request[5]:,.2f}")

            # Approval and Rejection buttons
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"Approve Request {request[0]}"):
                    cursor.execute("UPDATE Requests SET status = 'Approved' WHERE id = ?", (request[0],))
                    conn.commit()
                    st.success(f"Request ID {request[0]} has been approved!")

            with col2:
                if st.button(f"Reject Request {request[0]}"):
                    cursor.execute("UPDATE Requests SET status = 'Rejected' WHERE id = ?", (request[0],))
                    conn.commit()
                    st.error(f"Request ID {request[0]} has been rejected!")

            st.markdown("---")
    else:
        st.info("No pending requests at the moment.")


# Finance Dashboard Page
elif selected_page == "Finance Dashboard":
    st.header("Finance Dashboard")
    st.write("This is where finance officers will manage funds and liquidations. (Placeholder for now)")

