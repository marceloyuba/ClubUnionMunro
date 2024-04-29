import streamlit as st



st.set_page_config(page_title="Club Union Munro", page_icon="scr/logo-union.jpg", layout="wide")
           
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")


titulo_css = """
    <style>
        .titulo-container {
            padding-top: 0px; /* Ajusta este valor según sea necesario */
        }
    </style>
"""

# Título alineado al centro y con margen superior
st.markdown(titulo_css, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Análisis estadístico Handball 2024 - Club Unión Munro</h1>", unsafe_allow_html=True)
st.title("")  

def main():
    st.markdown("<h1 style='text-align: center;'>Tablero de estadisticas</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="display: flex; justify-content: center;">
       <iframe title="DatasetMockup" width="1240" height="1000" src="https://app.powerbi.com/view?r=eyJrIjoiNzdiNGI2OTgtM2FlNy00NWFiLTg1ODYtN2IyYjcwZGFiMjNmIiwidCI6ImUyYjc5Nzc5LTBhODgtNDMzMS05YjQyLTM4NGNkNzFjODVkNyIsImMiOjR9&pageName=ReportSectionbf43e1f801cf877ccb9b" frameborder="0" allowFullScreen="true"></iframe></div>
        """,
        unsafe_allow_html=True
    )
    

if __name__ == "__main__":
    main()
st.title("")

    
page_bg_img = f"""
<style>

[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://github.com/marceloyuba/ClubUnionMunro/blob/main/scr/fondoTaxi.png?raw=true");
background-position: top left;
background-repeat: no-repeat;
background-attachment: fixed;
background-size: cover;
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown('<style>h4{color: black;}, font=</style>', unsafe_allow_html=True)    
st.markdown('<style>h3 {color: black;}, font=</style>', unsafe_allow_html=True)
st.markdown('<style>h2 {color: black;}, font=</style>', unsafe_allow_html=True)
st.markdown('<style>h1 {color: black;}, font=</style>', unsafe_allow_html=True)