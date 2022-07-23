Import Streamlit

Streamlit.title('dexter and Max are playing')
Streamlit.text('emojis not found  🍠')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
Streamlit.dataframe(my_fruit_list)
