import streamlit as st
import pandas as pd

def inserting(df, a):
    a['Firstname'] = st.text_input("Frist Name")
    a['LastName'] = st.text_input("Last Name")
    a['Gender'] = st.text_input("Gender")
    a['Contact Details'] = st.text_input("Contact details")
    df1 = df.append(a, ignore_index=True)
    st.table(df1)

if __name__=="__main__":
    df=pd.read_csv('I:\C driver\Ingrity\demo.csv')
    a=dict()
    st.button("Add row", on_click=inserting(df,a))







