import streamlit as st

def apply_custom_submit_form():
    st.markdown(
        """
        <style>
            .stButton>button {
                background-color: #007BFF;
                color: white;
                padding: 0.25rem 1rem;
                border: none;
                border-radius: 0.25rem;
            }
        </style>
        """, 
        unsafe_allow_html=True
    )
    
def apply_custom_header_style():
    st.markdown(
        """
        <style>
            .header {
                background-color: #f1f1f1;  /* light gray background */
                padding: 10px 16px;
                margin: -20px -20px 20px -20px;  /* expand header to edges */
            }
            .header h1 {
                color: #333;  /* dark text color */
                font-size: 24px;
            }
        </style>
        """, 
        unsafe_allow_html=True
    )