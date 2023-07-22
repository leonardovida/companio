import time
from datetime import datetime, timedelta
import requests
import streamlit as st

def component_search_bar():
    """
    Component for selecting category choices
    """
    # Large search bar
    search_value = st.text_input("Search Bar", value="", placeholder="Where are you going?", max_chars=None, key=None, type="default")
    st.session_state.search_value = search_value


def component_budget_choices():
    """
    Component for selecting category choices
    """
    choices = ["$", "$$", "$$$"]
    selected_budgets = st.multiselect(
        "Choose a budget:",
        choices,
        default=["$", "$$"],
        help="Select your budget range"
    )
    st.session_state.selected_budgets = selected_budgets

    
def component_category_choices():
    """
    Component for selecting category choices
    """
    choices = ["Restaurant", "Bar/Cafe", "Brunch", "Drinks"]
    selected_categories = st.multiselect(
        "Choose a category:",
        choices,
        default="Restaurant",
        help="Select one or more categories to search for."
    )
    st.session_state.selected_categories = selected_categories


def component_dates():
    """
    Component for selecting dates
    """
    col1, col2 = st.columns(2)
    #Date input for check-in and check-out
    today = datetime.today().date()
    tomorrow = today + timedelta(days=1)
    
    with col1:
        check_in_date = st.date_input('Arrival date', today)
    with col2:
        check_out_date = st.date_input('Leaving date', tomorrow)

    # Ensure check-out is after check-in
    if check_out_date <= check_in_date:
        st.error("Leaving date must be after check-in date.")
        
    st.session_state.check_in_date = check_in_date
    st.session_state.check_out_date = check_out_date


def component_num_people():
    """
    Component for selecting number of people
    """
    # List of numbers from 0 to 10
    numbers = list(range(11))
    
    col1, col2 = st.columns([1, 1])

    numbers = list(range(11))
    
    adult_count = st.session_state.get("adult_count", 0)
    child_count = st.session_state.get("child_count", 0)

    with col1:
        st.session_state.adult_count = st.selectbox("Adults", options=numbers, index=adult_count, key='adult_selectbox')
    with col2:
        st.session_state.child_count = st.selectbox("Child", options=numbers, index=child_count, key='child_selectbox')


def component_submit_form():
    """
    Component for submit button
    """
    if st.form_submit_button('Search', help="Click to search for the list of places to your next destination!"):
        with st.spinner('Creating your personalized list...'):
            time.sleep(5)
        
        # Replace with your API endpoint
        api_endpoint = "https://your-api-endpoint.com/data"
        
        # Data payload
        payload = {
            "search_value": st.session_state.search_value,
            "selected_budgets": st.session_state.selected_budgets,
            "selected_categories": st.session_state.selected_categories,
            "check_in_date": st.session_state.check_in_date,
            "check_out_date": st.session_state.check_out_date,
            "adult_count": st.session_state.adult_count,
            "child_count": st.session_state.child_count
        }

        # Send data to API
        response = requests.post(api_endpoint, json=payload, timeout=10)
        
        # Handle API response
        if response.status_code == 200:
            st.success("Data sent successfully!")
        else:
            st.error(f"Error sending data. Status code: {response.status_code}")

        st.success('Ready!')