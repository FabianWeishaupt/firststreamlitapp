import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError



#Generate a dataframe from the fruits csv and set the index to readable names
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title('My Parents new burger place')

streamlit.header(' Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard boiled Eggs')
streamlit.text('🥑🍞 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

def get_fruitvice_data(this_fruit_choice):
    fruityvice_response = requests.get(f'https://fruityvice.com/api/fruit/{this_fruit_choice}')
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    getfromfrunction = get_fruitvice_data(fruit_choice)
    streamlit.dataframe(getfromfrunction)

except URLError as e:
  streamlit.error()

#streamlit.stop()

streamlit.header("The Fruit_Load_list contains:")
def get_fruit_load_list:
    with my_cnx.cursor as my_cur:
        my_cur.execute("SELECT * FROM Fruit_Load_list")
        return my_cur.fetchall()

if streamlit.button ("Get Fruit Load List"):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)

streamlit.stop()

add_my_fruit = streamlit.text_input('What fruit would you like information about?','jackfruit')
streamlit.write('Please add ', add_my_fruit)

my_cur.execute("insert into Fruit_Load_list values ('from streamlit')")
