import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout,style_background_home
from src.components.footer import footer_home

def home_screen():
   # st.header("Home Screen")


    header_home()
    style_background_home()
    style_base_layout()
    

    col1, col2 =st.columns(2,gap="large")
    with col1:
     

      st.header("I'm a student")
      st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=80)
      if st.button(" Student portal",type="primary",icon=":material/arrow_outward:",icon_position="right"):
            st.session_state["login_type"] = "student"
            st.rerun()
     
        

    with  col2:
     


     st.header("I'm a teacher")
     st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=115)
     if st .button(" Teacher portal",type="primary",icon=":material/arrow_outward:",icon_position="right"):
        st.session_state["login_type"] = "teacher"  
        st.rerun()
    footer_home()     