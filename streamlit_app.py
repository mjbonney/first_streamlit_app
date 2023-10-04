import streamlit
import pandas
import requests

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title('My Parents\' New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice!')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

# write your own comment -what does the next line do? This line normalises the json response
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do? This line creates a dataframe table from the json values
streamlit.dataframe(fruityvice_normalized)
