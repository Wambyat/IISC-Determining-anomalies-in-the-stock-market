import streamlit as st
import time
def model_page():
    st.write("This is the model page")
    if st.button("Run Model"):
        with st.spinner("Model 1 is running"):
            time.sleep(2)
            st.success("LESSGOOO")
        st.session_state["model_run"] = "Done"