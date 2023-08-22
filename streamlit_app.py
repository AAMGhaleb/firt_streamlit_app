import streamlit  

streamlit.title('My Mom\'s  New Healthy Diner') 

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie') 
streamlit.text('🐔 Hard-Boiled Free-Range Egg')  
streamlit.text('🥑 🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
  
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show) 

#New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','apple')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# take the json version pf the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as a table 
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector


import streamlit as st

# Access Snowflake connection info from secrets
snowflake_secrets = st.secrets["snowflake"]

account_name = snowflake_secrets["account_name"]
warehouse = snowflake_secrets["warehouse"]
database = snowflake_secrets["database"]
schema = snowflake_secrets["schema"]
username = snowflake_secrets["username"]
password = snowflake_secrets["password"]

# Use the connection information to interact with Snowflake
# Example: Connect to Snowflake using your preferred library (e.g., snowflake-connector-python) 

