import pages
import streamlit as st
from db import run_query
from time import time
from data import *
from finalpage import *

#Function to display necessary information in the query page
def page(page_number):
    
    col1,col2,col3,col4,col5,col6,col7=st.columns(7)
    with col1:
        title="Question:"+str(page_number)
        st.title(title) #To display Title of each question
    with col7:
        container_score=st.empty()
        score="Score:"+str(getscore())
        container_score.write(score) #Container to Display Score
    container_schema=st.empty()
    schema_of_tables=''
    for i in range(len(schema[page_number-1])):
        schema_of_tables+=schema[page_number-1][i]
    container_schema.write(schema_of_tables) #Container to Display Schema
    st.write("What is the query and on what column/columns should Peter create an index, if any, to optimise the following retrieval.")
    container_question = st.empty() #Container to Display Questions
    container_question.write(Question_Queries[page_number-1])

    placeholder = st.empty() #Placeholder to get the user input
    query=placeholder.text_input("Input your query here",key="clear_query")
    

    col1,col2,col3,col4,col5,col6,col7=st.columns(7)
    with col7:
        execute=st.button("Execute")
    with col1:
        show_hint=st.button("Hint")
    container_hint=st.empty()

    st.subheader("OUTPUT")
    container_output=st.empty() #Container to Display Output
    container_number_of_rows=st.empty() #Container to Display the number of rows
    container_time_taken=st.empty() #Container to Display the time taken

    st.subheader("OPTIMISED OUTPUT")
    show_output=st.button("Show Output")
    container_optimised=st.empty() #Container to Display the correct output

    #To display finish button in last page
    if page_number==30:
        col1,col2,col3,col4,col5,col6,col7=st.columns(7)
        finish=st.button("Finish")
        if finish:
            finalpage()

    #Logic when execute button is pressed
    if execute:
        Attempted[page_number-1]=1
        optimal_output=run_query(Output_queries[page_number-1])

        total_time=0
        tic = time()
        user_output=run_query(query)
        toc = time()
        total_time=toc-tic

        number_of_rows="Number of rows returned:"+str(len(user_output))

        #If the user output and the optimal output are same and when no indexes are required
        if user_output==optimal_output and len(index_columns[page_number-1])==0:

            if Already_solved[page_number-1]==0:
                update_score(page_number)
                Already_solved[page_number-1]=1

            container_output.write("Correct Query!")
            container_number_of_rows.write(number_of_rows)
            time_taken="Time taken: "+str(round(total_time,3))+" sec"
            container_time_taken.write(time_taken)
            score="Score: "+str(getscore())
            container_score.write(score)

        #If the user output and the optimal output are same and the user has created proper indexes
        elif user_output==optimal_output and checkindex(page_number):

            if Already_solved[page_number-1]==0:
                update_score(page_number)
                Already_solved[page_number-1]=1

            container_output.write("Correct Query!")
            container_number_of_rows.write(number_of_rows)
            time_taken="Time taken: "+str(round(total_time,3))+" sec"
            container_time_taken.write(time_taken)
            score="Score: "+str(getscore())
            container_score.write(score)

        #If the user output and the optimal output are same and the user hasn't created proper indexes
        elif user_output==optimal_output:
            container_output.write("Correct Query! But try to optmise the query by adding indexes. ")
            container_number_of_rows.write(number_of_rows)
            time_taken="Time taken: "+str(round(total_time,3))+" sec"
            container_time_taken.write(time_taken)

        #To handle queries which contains create and alter
        elif 'create' in query or 'alter' in query:
            container_output.write("Query Successfully Executed!")
            time_taken="Time taken: "+str(round(total_time,3))+" sec"
            container_time_taken.write(time_taken)

        #To handle queries which contains show, index and explain
        elif 'show' in query or 'index' in query or 'explain' in query:
            container_output.write("Query Successfully Executed!")
            container_number_of_rows.write("Try this query in Terminal for Output")
            time_taken="Time taken: "+str(round(total_time,3))+" sec"
            container_time_taken.write(time_taken)
        
        #To handle incorrect queries
        elif user_output!=optimal_output:
            container_output.write("Incorrect Query!")
            
        
    #Logic when show output button is pressed           
    if show_output:
        container_optimised.write(Output_answers[page_number-1])
        Attempted[page_number-1]=1
        Opened_hints[page_number-1]=2

    #Logic when show hint button is pressed
    if show_hint:
        container_hint.write(Hints[page_number-1])
        Attempted[page_number-1]=1
        Opened_hints[page_number-1]=1

    

#Function to check whether the user has created correct indexes or not  
def checkindex(page_number):
    count=0
    #To handle the FULLTEXT query
    if page_number==30:
        index_output=run_query(index_queries[page_number-1][0])
        for rows in index_output:
            if rows[10]=='FULLTEXT' and (rows[4]=='fname' or rows[4]=='lname'):
                count+=1
        if count==2:
            return True
        else:
            return False

    #To check if the indexes are created with proper naming conventions
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


    