import pickle
import streamlit as st 
import pandas as pd 
import numpy as np  

from llm_handler import * 

@st.cache(allow_output_mutation=True)
def get_data(): 
    return pd.read_csv('handbook_df.csv'), pickle.load(open('handbook_embeddings.pkl', 'rb')) 

data, embeddings = get_data()

st.subheader("DotBot")  

with st.form(key='f'): 
    
    query = st.text_input("Ask me anything about the employee handbook")  
    password = st.text_input("Password")
    go = st.form_submit_button("go") 
    

if go:  
    
    if password == st.secrets['password']: 
    
        with st.spinner("Contacting DotBot 🤖"): 
            res = answer_query_with_context(query, 
                                            data, 
                                            embeddings, 
                                            show_prompt=False)  

        st.write(res) 
        
    else: 
        st.error("Incorrect password")
 
