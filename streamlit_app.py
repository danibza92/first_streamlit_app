# Importamos streamlit que es un paquete de python
import streamlit

## Comandos de texto de streamlit
streamlit.title ('My Parents New Healthy Diner')
streamlit.header ('Breakfat Favorite')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Importamos la libreria pandas de python
import pandas

# Leemos el fichero de frutas de la nuve de S3
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#Seteamos como indice el campo de frutas
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include: al señalar dos frutas lo que haces
# es que por defecto haya dos seleccionadas
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])

##Con este comando lo que haces , es que te devuelva unicamente las filas del dataset my fruit list que han sido selccionadas en
##en la variable furists selected (el streamlit.multiselect
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page. Pero mostramos la tabla filrada de fruits to show y no el dataframe completo de my_fruit_list
streamlit.dataframe(fruits_to_show)

# read from a api
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# Se normaliza en formato tabla el archivo de JSON que viene de la llamada a la api de fruityvice
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# se pintq el df obtenido
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
import pyarrow

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows= my_cur.fetchall()
streamlit.header("The list contains:")
streamlit.dataframe(my_data_rows)

fruits_selected = streamlit.multiselect("Add some fruits:", list(select * from fruit_load_list))







