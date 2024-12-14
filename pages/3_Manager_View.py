# pages/3_Manager_View.py
import streamlit as st
from db import get_connection

def show_page():
    st.title("Manager View")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Requests WHERE status = 'Pending'")
    pending_requests = cur.fetchall()

    for req in pending_requests:
        st.write(f"Request ID: {req[0]}, Name: {req[1]}, Amount: {req[5]}")
        if st.button(f"Approve {req[0]}"):
            cur.execute("UPDATE Requests SET status = 'Approved' WHERE id = %s", (req[0],))
            conn.commit()
            st.success(f"Request {req[0]} approved!")
        if st.button(f"Decline {req[0]}"):
            cur.execute("UPDATE Requests SET status = 'Declined' WHERE id = %s", (req[0],))
            conn.commit()
            st.error(f"Request {req[0]} declined!")

    conn.close()
