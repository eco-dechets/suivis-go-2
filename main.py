from repositories.auth_repository import AuthRepository
from repositories.database import DatabaseRepository
from views import home, statistics, admin


import streamlit as st
import streamlit_authenticator as stauth

from database2 import Database2


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    st.set_page_config(page_title='Gestion des carburants', page_icon=':fuelpump:', layout='wide')

    users = AuthRepository().get_users()

    usernames = [user[2] for user in users]
    names = [user[3] for user in users]
    passwords = [user[1] for user in users]


    users_dict = {}
    for i in range(len(users)):
        users_dict[usernames[i]] = {'email': usernames[i], 'name': names[i], 'password': passwords[i]}

    users_dict = {'usernames': users_dict}

    authenticator = stauth.Authenticate(
        users_dict,
        "eco-dechets",
        "HYZg6Z7X627dhb2ey0khe",
    )
    name, authentication_status, username = authenticator.login('Login', 'main')
    print(name, authentication_status, username)

    if authentication_status == False:
        st.error('Authentication failed')
    if authentication_status == None:
        st.info('Authentication required')

    if authentication_status:
        tab1, tab2, tab3 = st.tabs(["Accueil", "Statistique", "Admin"])
        with tab1:
            st.header('Accueil')
            home.main()

        with tab2:
            st.header('Statistique')
            statistics.main()

        #with tab3:
            #admin.main()



