import streamlit as st
from streamlit_option_menu import option_menu

from con1_HOME import run_home
from con2_INTRO import run_intro
from con3_SKIN import run_skin
from con4_EYE import run_eye
from con5_DATE import run_date
from con6_CS import run_cs
from con7_ETC import run_etc


def main():

    #사이드바 메뉴
    with st.sidebar:
        option_menu_list = ['HOME', 'INTRODUCTION', 'SKIN CHECK', 'EYE CHECK', 'DATE' ,'C/S', 'ETC']
        choose = option_menu("Welcome!", option_menu_list,
                            icons=['bi bi-house-heart', 'bi bi-info-circle-fill', 'bi bi-bandaid-fill', 'bi bi-eye-fill', 'bi bi-calendar-check-fill', 'bi bi-wechat', 'bi bi-three-dots-vertical'],
                            menu_icon="bi bi-suit-heart", default_index=0,
                            styles={
            "container": {"padding": "5!important", "background-color": "#ffffff"},
            "icon": {"color": "#FFDBDB", "font-size": "18px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#FEA443"},
        }
        )



    #각 메뉴별 페이지
    if choose == option_menu_list[0]:
        run_home()

    elif choose == option_menu_list[1]:
        run_intro()

    elif choose == option_menu_list[2]:
        run_skin()

    elif choose == option_menu_list[3]:
        run_eye()

    elif choose == option_menu_list[4]:
        run_date()

    elif choose == option_menu_list[5]:
        run_cs()

    elif choose == option_menu_list[6]:
        run_etc()

    else :
        pass







if __name__ == '__main__':
    main()




