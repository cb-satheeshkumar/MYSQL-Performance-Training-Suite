import pages
import streamlit as st
from db import run_query
from time import time
from data import *


def page(page_number):
    
    col1,col2,col3,col4,col5,col6,col7=st.columns(7)
    with col1:
        st.title(Headings[page_number])
    with col7:
        container_score=st.empty()
        score="Score: "+str(getscore())
        container_score.write(score)

    container_question = st.empty()
    container_question.write(Question_Queries[page_number-1])

    placeholder = st.empty()
    query=placeholder.text_input("Input your query here",key="clear_query")
    

    col1,col2,col3,col4,col5,col6,col7=st.columns(7)
    with col7:
        execute=st.button("Execute")
    with col1:
        show_hint=st.button("Hint")
    container_hint=st.empty()

    st.subheader("OUTPUT")
    container_output=st.empty()
    container_number_of_rows=st.empty()
    container_time_taken=st.empty()

    st.subheader("OPTIMISED OUTPUT")
    show_output=st.button("Show Output")
    container_optimised=st.empty()

    if execute:

        optimal_output=run_query(Output_queries[page_number-1])

        total_time=0
        tic = time()
        user_output=run_query(query)
        toc = time()
        total_time=toc-tic

        number_of_rows="Number of rows returned:"+str(len(user_output))


        
        if user_output==optimal_output and len(index_columns[page_number-1])==0:
            if Already_solved[page_number-1]==0:
                update_score()
                Already_solved[page_number-1]=1

            container_output.write("Correct Query!")
            container_number_of_rows.write(number_of_rows)
            time_taken="Time taken: "+str(round(total_time,3))+" sec"
            container_time_taken.write(time_taken)
            score="Score: "+str(getscore())
            container_score.write(score)

        elif user_output==optimal_output and checkindex(page_number):

            if Already_solved[page_number-1]==0:
                update_score()
                Already_solved[page_number-1]=1

            container_output.write("Correct Query!")
            container_number_of_rows.write(number_of_rows)
            time_taken="Time taken: "+str(round(total_time,3))+" sec"
            container_time_taken.write(time_taken)
            score="Score: "+str(getscore())
            container_score.write(score)

        elif user_output==optimal_output:
            container_output.write("Correct Query! But try to optmise the query by adding indexes. ")
            container_number_of_rows.write(number_of_rows)
            time_taken="Time taken: "+str(round(total_time,3))+" sec"
            container_time_taken.write(time_taken)

        elif "create" or "alter" in query:
            container_output.write("Query Successfully Executed")
            time_taken="Time taken: "+str(round(total_time,3))+" sec"
            container_time_taken.write(time_taken)

        elif user_output!=optimal_output:
            container_output.write("Incorrect Query!")
            
        
                
    if show_output:
        container_optimised.write(Output_answers[page_number-1])

    if show_hint:
        container_hint.write(Hints[page_number-1])
    
def checkindex(page_number):
    count=0
    for i in range(0,len(index_columns[page_number-1])):
        index_output=run_query(index_queries[page_number-1][i])
        for rows in index_output:
            if rows[2]==index_columns[page_number-1][i]:
                count=count+1
                break
    if count==len(index_columns[page_number-1]):
        return True
    else:
        return False


    