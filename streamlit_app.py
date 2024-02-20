# Importamos streamlit que es un paquete de python
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
import pyarrow


## Comandos de texto de streamlit
streamlit.title ('My Parents New Healthy Diner')
streamlit.header ('Breakfat Favorite')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Importamos la libreria pandas de python


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
def get_fruityvice_data(this_fruit_choice):
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
      #Se normaliza en formato tabla el archivo de JSON que viene de la llamada a la api de fruityvice
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      return fruityvice_normalized

#new section
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else: 
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
    
except URLError as e:
  streamlit.error()



streamlit.header("The list contains:")
#snowflake related functions;
def get_fruit_load_list():
      with my_cnx.cursor() as my_cur:
           my_cur.execute("select * from fruit_load_list")
           return my_cur.fetchall()

#add a button to load the fruit;
if streamlit.button('Get Fruit Load List'):
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      my_data_rows= get_fruit_load_list()
      streamlit.dataframe(my_data_rows)

#allow the end user add fruit

def insert_row_snoflake(ne_fruit):
      with my_cnx.cursor as my_cur:
            my_cur.execute ("insert into fruit_load_list values ('from streamlit')")
            return "Thanks fo adding" + new_fruit
add_my_fruit = streamlit.text_input('What fruit would you like to add')
if streamlit.button('Add a Fruit to the List'):
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      back_from_function= insert_row_snowflake(add_my_fruit)
      streamlit.text(back_from_function)








