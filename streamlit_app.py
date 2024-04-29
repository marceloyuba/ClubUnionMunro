import streamlit as st



st.set_page_config(page_title="Club Union Munro", page_icon="scr/fondo.jpg", layout="wide")
           
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")
with st.container():
    st.markdown('<style>h4{color: black;}, font=</style>', unsafe_allow_html=True)    
    st.markdown('<style>h3 {color: black;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h2 {color: black;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h1 {color: black;}, font=</style>', unsafe_allow_html=True)
    st.title("")
with st.container():
    
   
    st.title("")
    st.title("Analisis estadistico Handball 2024 - Club Union Munro")
  

def main():
    st.title("Dashboard del PI2 en forma de muestra")
    st.markdown(
        """
        <div style="display: flex; justify-content: center;">
       <iframe title="DatasetMockup" width="1240" height="1000" src="https://app.powerbi.com/view?r=eyJrIjoiZjRmOWFiOWUtZmE4Yy00MDcwLTllNjktNjE5NTcwZDY3OTJlIiwidCI6ImUyYjc5Nzc5LTBhODgtNDMzMS05YjQyLTM4NGNkNzFjODVkNyIsImMiOjR9&pageName=ReportSection10f0c58045468d53ab10" frameborder="0" allowFullScreen="true"></iframe></div>
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