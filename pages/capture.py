import streamlit as st

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import data_manager as dm


match_name = st.session_state['actual_match']
category = st.session_state['actual_category']
division = st.session_state['actual_division']
datetime = st.session_state['actual_datetime']

match_info_dict = {'name': match_name, 'category': category, 'division': division, 'datetime': datetime}

st.markdown("""
<style>
    div[data-testid="stElementContainer"]:has(.add_points) + div[data-testid="stElementContainer"] button {
        background-color: #28a745 !important;
        color: white !important;
        width: 45px !important;
        height: 45px !important;
        border-radius: 4px !important;
    }
    
    div[data-testid="stElementContainer"]:has(.sub_points) + div[data-testid="stElementContainer"] button {
        background-color: #dc3545 !important; 
        color: white !important;              
        width: 45px !important;               
        height: 45px !important;              
        border-radius: 4px !important;
    }
    
    div[data-testid="stElementContainer"]:has(.add_points) + div[data-testid="stElementContainer"] button:hover { 
        background-color: #218838 !important; 
    }
    div[data-testid="stElementContainer"]:has(.sub_points) + div[data-testid="stElementContainer"] button:hover { 
        background-color: #c82333 !important; 
    }
</style>
""", unsafe_allow_html=True)

def add_points(player_name):
    st.session_state[f"points_{player_name}"] += 1

def sub_points(player_name):
    if st.session_state[f"points_{player_name}"] > 0:
        st.session_state[f"points_{player_name}"] -= 1

def add_fouls(player_name):
    if st.session_state[f"fouls_{player_name}"] == 5:
        st.toast("El jugador ya tiene el máximo de faltas", icon="⚠️")
    else:
        st.session_state[f"fouls_{player_name}"] += 1

def sub_fouls(player_name):
    if st.session_state[f"fouls_{player_name}"] > 0:
        st.session_state[f"fouls_{player_name}"] -= 1

def create_list_of_dicts(players_stats):
    players_stats_list = []
    for lplayer in players_stats:
        lnum = lplayer["number"]
        lname = lplayer["name"]

        actual_player_dict = {
            'num': lnum,
            'name': lname,
            'points': st.session_state[f"points_{lname}"],
            'fouls': st.session_state[f"fouls_{lname}"]
        }
        players_stats_list.append(actual_player_dict)
    return players_stats_list



st.title(f"Captura de Partido - {match_name}")
st.write(f"{category} - {division} - {datetime}")
players = dm.players_recovery(category, division)

if st.button("Guardar estadísticas"):
    dm.stats_to_excel(create_list_of_dicts(players), match_info_dict)

if not players:
    st.write("⚠️ No se encontraron jugadores")
else:
    for player in players:
        num = player["number"]
        name = player["name"]

        if f"points_{name}" not in st.session_state:
            st.session_state[f"points_{name}"] = 0

        if f"fouls_{name}" not in st.session_state:
            st.session_state[f"fouls_{name}"] = 0

        with st.container():

            st.markdown(
                f"**#{num} - {name}** | Puntos: **{st.session_state[f'points_{name}']}** | Faltas: **{st.session_state[f'fouls_{name}']}**")

            col_pt_mas, col_pt_menos, col_fl_mas, col_fl_menos = st.columns(4)

            with col_pt_mas:
                st.caption("Puntos")
                st.markdown('<div class="add_points"></div>', unsafe_allow_html=True)
                st.button("+", key=f"add_pts_{num}", on_click=add_points, args=(name,))

            with col_pt_menos:
                st.markdown("&nbsp;", unsafe_allow_html=True)
                st.markdown('<div class="sub_points"></div>', unsafe_allow_html=True)
                st.button("-", key=f"sub_pts_{num}", on_click=sub_points, args=(name,))

            with col_fl_mas:
                st.caption("Faltas")
                st.markdown('<div class="add_points"></div>', unsafe_allow_html=True)
                st.button("+", key=f"add_fls_{num}", on_click=add_fouls, args=(name,))

            with col_fl_menos:
                st.markdown("&nbsp;", unsafe_allow_html=True)
                st.markdown('<div class="sub_points"></div>', unsafe_allow_html=True)
                st.button("-", key=f"sub_fls_{num}", on_click=sub_fouls, args=(name,))


            st.divider()


if st.button("Regresar al Inicio"):
    st.switch_page("app.py")

