# streamlit_app.py

import streamlit as st
import mysql.connector

import db

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Perform query.
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()



