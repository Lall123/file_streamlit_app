import streamlit

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

streamlit.title('Dexter and Max favorite menu')
streamlit.text('🥣 🥗 🐔 🥑 all of them ')
streamlit.text('🥣 🥗 🐔 🍞 all of them ')
streamlit.text('🥣 🥗 🍞 all of them ')
streamlit.text('🥣 🥗  all of them ')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
