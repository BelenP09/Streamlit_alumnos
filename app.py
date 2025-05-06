#importamos la libreria a usar streamlit
import streamlit as st

#-------------------------------------------------------------------------------------------------------------------
#SETUP DE LA APP
# De layaut usar wide or centered
st.set_page_config (page_title="Mi primera app", page_icon=":tada", layout="centered")

#-------------------------------------------------------------------------------------------------------------------

# Textos
st.title("Mi primera app") #Título principal

#Encabezado
st.header("Encabezado 1") #Encabezado 1
st.subheader("Encabezado 2") #Encabezado 2

#texto normal
st.text("Hola mundo") #Texto normal

#markdown
st.markdown("Hola mundo en **negrita** y _cursiva_") #Texto markdown


#latex
st.latex(r'''a^2 + b^2 = c^2''') #Texto latex

#code
st.code('print("Hola mundo")', language='python') #Texto en código

#Información, advertencia y error   
st.info("Esto es una información") #Texto de información
st.warning("Esto es una advertencia") #Texto de advertencia
st.error("Esto es un error") #Texto de error
st.exception("Esto es una excepción") #Texto de excepción

#-------------------------------------------------------------------------------------------------------------------

#Medios y recursos  
#Imagenes (la ruta puede ser local o una url)
st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit", use_column_width=True) #Imagen

#Audios
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format= "audio/mp3") #Audio

#Videos
st.video("https://www.youtube.com/watch?v=2Vv-BfVoq4g") #Video

#--------------------------------------------------------------------------------------------------------------------

st.sidebar("Sidebar") #Sidebar
st.sidebar.title("Sidebar") #Título de la sidebar
