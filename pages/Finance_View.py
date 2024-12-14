# pages/4_Finance_View.py
import streamlit as st
from db import get_connection

def show_page():
    st.title("Finance View")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Requests WHERE status = 'Approved'")
    approved_requests = cur.fetchall()

    for req in approved_requests:
        st.write(f"Request ID: {req[0]}, Name: {req[1]}, Amount: {req[5]}")
        if st.button(f"Issue Funds {req[0]}"):
            cur.execute("UPDATE Requests SET status = 'Issued', funds_issued = %s WHERE id = %s", (req[5], req[0]))
            conn.commit()
            st.success(f"Funds issued for Request {req[0]}!")

    conn.close()
