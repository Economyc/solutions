import streamlit as st




st.set_page_config(
    page_title="SB SOLUTIONS",
    page_icon="⚙️"
)


from streamlit_option_menu import option_menu
import MODULOS.TallerDelSol as TallerDelSol
  
class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, function): 
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        # Añadir imagen


        with st.sidebar:
            app = option_menu(
                menu_title="Panel de Operaciones",
                options=["Taller Del Sol"],
                icons=['brightness-alt-high-fill'],
                menu_icon='chat-text-fill',
                default_index=0,  # Establecer el índice por defecto a "Home"
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"}, 
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"}
                }
            )

        for app_info in self.apps:
            if app == app_info["title"]:
                app_info["function"]()

multi_app = MultiApp()
multi_app.add_app("Taller Del Sol", TallerDelSol.app)



print("Aplicaciones agregadas:", [app_info["title"] for app_info in multi_app.apps])

multi_app.run()