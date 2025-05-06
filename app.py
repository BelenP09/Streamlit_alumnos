#importamos la libreria a usar streamlit
import streamlit as st
import pandas as pd #Importamos pandas para usar dataframes

#-------------------------------------------------------------------------------------------------------------------
#SETUP DE LA APP
# De layaut usar wide or centered
st.set_page_config (page_title="Mi primera app", page_icon=":tada", layout="centered")

#-------------------------------------------------------------------------------------------------------------------

# Textos
#st.title("Mi primera app") #Título principal

#Encabezado
#st.header("Encabezado 1") #Encabezado 1
#st.subheader("Encabezado 2") #Encabezado 2

#texto normal
#st.text("Hola mundo") #Texto normal

#markdown
#st.markdown("Hola mundo en **negrita** y _cursiva_") #Texto markdown


#latex
#st.latex(r'''a^2 + b^2 = c^2''') #Texto latex

#code
#st.code('print("Hola mundo")', language='python') #Texto en código

#Información, advertencia y error   
#st.info("Esto es una información") #Texto de información
#st.warning("Esto es una advertencia") #Texto de advertencia
#st.error("Esto es un error") #Texto de error
#st.exception("Esto es una excepción") #Texto de excepción

#-------------------------------------------------------------------------------------------------------------------

#Medios y recursos  
#Imagenes (la ruta puede ser local o una url)
#st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit", use_column_width=True) #Imagen

#Audios
#st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format= "audio/mp3") #Audio

#Videos
#st.video("https://www.youtube.com/watch?v=2Vv-BfVoq4g") #Video

#--------------------------------------------------------------------------------------------------------------------

#sidebar
#st.sidebar.title("Sidebar") #Título de la sidebar
#st.sidebar.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit", use_column_width=True) #Imagen en la sidebar

#--------------------------------------------------------------------------------------------------------------------

#Pestañas
tab1, tab2, tab3 = st.tabs(["Textos", "medios y recursos", "Dataframe"]) #Creamos las pestañas
with tab1: #Pestaña 1
     #Textos
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

with tab2: #Pestaña 2
    #Medios y recursos  
    #Imagenes (la ruta puede ser local o una url)
    st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit", use_column_width=True) #Imagen

    #Audios
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format= "audio/mp3") #Audio

    #Videos
    st.video("https://www.youtube.com/watch?v=2Vv-BfVoq4g") #Video

with tab3: #Pestaña 3
 #dataframe ejemplo     
 df = pd.DataFrame({
     'col1': [1, 2, 3, 4],
     'col2': [5, 6, 7, 8],
     'col3': [9, 10, 11, 12]
 }) #Creamos un dataframe de ejemplo

 st.dataframe(df) #Mostramos el dataframe

#--------------------------------------------------------------------------------------------------------------------

#columnas   
col1, col2, col3 = st.columns(3) #Creamos las columnas

with col1: #Columna 1
     #Imagenes (la ruta puede ser local o una url)
    st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit", use_column_width=True) #Imagen

with col2: #Columna 2
     #Imagenes (la ruta puede ser local o una url)
    st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit", use_column_width=True) #Imagen

with col3: #Columna 3
     #Imagenes (la ruta puede ser local o una url)
    st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit", use_column_width=True) #Imagen

    #--------------------------------------------------------------------------------------------------------------------

    #Sesions states son variables que se mantienen en la sesion
    # se pueden usar para guardar datos entre sesiones

#crear cotador en estado de sesion
    if 'contador' not in st.session_state: #Si no existe la variable contador
        st.session_state.contador = 0

# funciones auxiliares para incrementar, decrementar y reiniciar el contador
    def incrementar_contador(): #Funcion para incrementar el contador
        st.session_state.contador += 1  

    def decrementar_contador(): #Funcion para decrementar el contador
        st.session_state.contador -= 1  
    def reiniciar_contador(): #Funcion para reiniciar el contador
        st.session_state.contador = 0

#interfaz
st.title("Contador") #Título del contador
st.write("Contador:", st.session_state.contador) #Mostramos el contador 

#botones para incrementar, decrementar y reiniciar el contador
col1, col2, col3 = st.columns(3) #Creamos las columnas para los botones

with col1: #Columna 1
    if st.button("Incrementar"): #Botón para incrementar el contador
        incrementar_contador() #Llamamos a la funcion para incrementar el contador

with col2: #Columna 2
    if st.button("Decrementar"): #Botón para decrementar el contador
        decrementar_contador() #Llamamos a la funcion para decrementar el contador

with col3: #Columna 3
    if st.button("Reiniciar"): #Botón para reiniciar el contador
        reiniciar_contador() #Llamamos a la funcion para reiniciar el contador

