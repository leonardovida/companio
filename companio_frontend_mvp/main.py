import streamlit as st

from companio_frontend_mvp.components import (
    component_num_people,
    component_category_choices,
    component_search_bar,
    component_budget_choices,
    component_dates,
    component_submit_form
)
from companio_frontend_mvp.config import (
    apply_custom_submit_form,
    apply_custom_header_style
)

def main():
    """Main function for the companio frontend mvp."""
    apply_custom_submit_form()
    apply_custom_header_style()
    st.markdown(
        """
        <div class="header">
            <h1>companio</h1>
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.subheader("Copilot for travel")
    st.write("Create a travel plan to discover your next restaurant, bar, or cafe")
    
    with st.form("my_form"):
        search_row_1, search_row_2 = st.columns([2, 1])
        # Search bar
        with search_row_1:
            component_search_bar()
        with search_row_2:
            component_dates()
            
        choices_row_1, choices_row_2, choices_row_3 = st.columns([4,2,2])
        # Category choices
        with choices_row_1:
            component_category_choices()
        
        # Budget choices
        with choices_row_2:
            component_budget_choices()
        
        with choices_row_3:
            component_num_people()
        
        # Submit the form
        component_submit_form()
        

if __name__ == '__main__':
    main()
