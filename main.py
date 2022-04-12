import streamlit as st
from desc import description
from pages import *
from data import *

next = st.button("Next")
if next:
    current_page=Headings.index(st.session_state["radio_option"])
    if current_page==len(Headings)-1:
        st.session_state.radio_option =Headings[0]
    else:
        st.session_state.radio_option =Headings[current_page+1]
    st.session_state["clear_query"]=""

option = st.sidebar.radio("OUTLINE", Headings , key="radio_option")

if option =='DESCRIPTION':
    description()
else:
    page_number=Headings.index(option)
    page(page_number)

