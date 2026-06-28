import streamlit as st

# to run-- streamlit run app.py

# Title of the page 
st.title("Hello Streamlit!!")

# display a simple text
st.write("Welcome to streamlit")

# display a dataframe --df = pd.Dataframe({...}) -> st.write(df)

# Create a line chart -- st.line_chart(df)

# input 
name = st.text_input("Ener your name")
if name:
    st.write(f"Hello, {name}")

# Slider 
age = st.slider("writeAge:",0,100,25)
st.write(f"your age: {age}")

# Select Box
languages = ['python', 'java', 'cpp']
choice = st.selectbox("Enter language:",languages)
st.write(f"you selected {choice}")

# st.info,warning,write,success,error

# upload button
file = st.file_uploader("choose a csv file")
if file is not None:
    st.write("File uploaded")