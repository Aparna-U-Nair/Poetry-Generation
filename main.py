import streamlit as st
import pickle 
from poem_generator import gen_poem
# import tensorflow 


st.title("Poetry Generation!")
st.markdown("""_ Let's write a poem on the topic of your interest _""")
subj = st.text_input("Please enter the subject to generate a poem")    
if subj:
    lines = st.text_input("Number of lines required")
    if lines:
        st.markdown(f"""**{subj.upper()}**""")
        poem = gen_poem(subj,int(lines))
        for lines in poem:
            st.write(lines.capitalize())
        # st.write(r"**-------------------------**")