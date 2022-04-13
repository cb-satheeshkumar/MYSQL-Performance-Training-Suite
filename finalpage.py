import streamlit as st 
import data
import finalpage

#Function to display the final results
def finalpage():
    total_1 =0 #Number of Attempted questions 
    total_2 =0 #Number of Solved questions
    for ele in range(0, 30):
        total_1 = total_1 + data.Attempted[ele]
        total_2 = total_2 + data.Already_solved[ele]
    st.title('Hooray, you finished the game!!')
    score="Score: "+str(data.getscore())
    st.write(score)
    total_attempted="Number of questions Attempted: "+str(total_1)
    total_solved="Number of questions Solved: "+str(total_2)
    st.write(total_attempted)
    st.write(total_solved)
