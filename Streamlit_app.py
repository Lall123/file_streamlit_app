import streamlit

streamlit.title('dexter and Max are playing')
streamlit.text('emojis not found  🥣 🥗 🐔 🥑🍞')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
