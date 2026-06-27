import streamlit as st

def save_into_session(match, cat, div, dt):
    st.session_state.update({
        'actual_match': match,
        'actual_category': cat,
        'actual_division': div,
        'actual_datetime': dt
    })

st.session_state.clear()

st.set_page_config(page_title="Club Cuervos", page_icon="🏀", layout="centered", initial_sidebar_state="collapsed")
st.title("Estadísticas - Club Cuervos")


col1, col2, col3 = st.columns(3)
with col1:
    match_name = st.text_input("Partido")
with col2:
    category = st.selectbox("Categoría", ["Seleccionar...", "Pañal", "Micro", "Infantil", "Pasarela", "Cadetes", "Juvenil Menor", "Juvenil Mayor"])
with col3:
    division = st.selectbox("Rama", ["Seleccionar...", "Mixto", "Varonil", "Femenil"])
datetime = st.datetime_input("Fecha y hora", "now")

if st.button("Capturar estadísticas"):
    if match_name and category != "Seleccionar..." and division != "Seleccionar...":
        save_into_session(match_name, category, division, datetime)
        st.switch_page("pages/capture.py")
    else:
        st.toast("¡LLene todos los campos!", icon="⚠️")