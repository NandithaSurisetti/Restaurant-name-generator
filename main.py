import streamlit as st
from namegen import name_generation

st.title("Restaurant Name Generator")


cuisine=st.sidebar.selectbox('Pick a Cuisine' , ('Indian' , 'American' , 'Arabic', 'Italian' , 'Mexican' ,'Asian' ))



if cuisine :
    response=name_generation(cuisine) 
    st.header(response['restaurant_name'].strip())
    menu_items=response['menu_items'].strip().split(",")
    st.write("**Menu items**")
    for item in menu_items:
        st.write(item )
    
