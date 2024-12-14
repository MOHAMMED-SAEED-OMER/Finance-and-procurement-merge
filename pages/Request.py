import streamlit as st
from db import create_connection

def show_page():
    st.title("Submit a Request")
    requester_name = st.text_input("Your Name")
    department = st.text_input("Department")
    project = st.text_input("Project")
    purpose = st.text_area("Purpose")
    amount_requested = st.number_input("Amount Requested", min_value=0.0)

    if st.button("Submit Request"):
        conn = create_connection()
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO Requests (requester_name, department, project, purpose, amount_requested)
        VALUES (?, ?, ?, ?, ?)
        """, (requester_name, department, project, purpose, amount_requested))
        conn.commit()
        conn.close()
        st.success("Request submitted successfully!")
