# pages/5_All_Requests.py
import streamlit as st
from db import get_connection

def show_page():
    st.title("All Requests")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Requests")
    all_requests = cur.fetchall()

    for req in all_requests:
        st.write(f"Request ID: {req[0]}, Name: {req[1]}, Status: {req[6]}")
    conn.close()