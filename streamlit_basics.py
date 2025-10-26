from cProfile import label

import streamlit as st
import pandas as pd
import time as t
# st.code('''
# for i in range(1,11):
#     print(i*i)
# '''
# )
# # latex
# st.latex("""
# ax^3+by^2+cz+d
#
# """)
# # displaying data frame
# df = pd.DataFrame({
#     'name':['Alice','Bob','Carl'],
#     'marks':[10,20,30],
#     'branch':['Cse','IT','Cse']
# })
# # displaying json data
# json_obj = {'name':['Alice','Bob','Carl']}
# st.json(json_obj)
#
# st.dataframe(df)
# # using metric to create flash cards
# st.metric('2024_sales','11 Lahks','-17%')
# st.metric('2025_sales','34 Lahks','29%')
#
# # sidebar
# st.sidebar.title('Drop Down Menu')
# st.sidebar.title('menu2')
# st.sidebar.header('menu3')
#
#
# st.sidebar.code('''
# for i in range(1,11):
#     print(i*i)
# '''
# )
#
#
# # columns
# col1,col2,col3 = st.columns(3)
#
# with col1:
#     st.write('This is Col1 Area')
#     st.metric('2024_sales', '11 Lahks', '-17%')
# with col2:
#     st.write('This is Col2 Area')
#     st.metric('2025_sales', '34 Lahks', '29%')
# with col3:
#     st.write('This is Col3 Area')
#     st.metric('2026_sales', '49 Lahks', '89%')
#
# st.info('Hello to Proceed Pls Login')
# st.warning('Passwrod Cannot be empty')
# st.success('Login Successful')
# st.error('Login Failed, Pls Retry Password!!')
# # st.balloons()
# # st.snow()
#
# # progress bar
# bar = st.progress(0)
# for percent in range(101):
#     t.sleep(0.05)
#     bar.progress(percent,text = "Your File is Uploading Pls Wait few seconds.")
# st.success("✅ File Uploaded!")
#
# tab1,tab2 = st.tabs(['Pandas_Videos','Numpy_Videos'])
# with tab1:
#     st.header("Welcome to Pandas Section")
#     st.metric('2024_sales', '11 Lahks', '-17%')
# with tab2:
#     st.metric('2024_sales', '11 Lahks', '-17%')
#
#
# with st.spinner('Wait for it...'):
#     t.sleep(5)
# st.success('Done!')
#
# st.date_input()

# input functions
# email = st.text_input('Enter Email Id: ')
# password = st.number_input('Enter you Password: ')
#
# btn = st.button('Click Login')
# if btn is not None:
#     if email == 'dino123@gmail.com' and password == 1234:
#         st.success('Login Successful')
#         st.balloons()
#     else:
#         st.error('Login Failed!!!')

#
# file = st.file_uploader("Choose a CSV File")
# if file is not None:
#     df = pd.read_csv(file)
#     st.dataframe(df.describe())

files = st.file_uploader("Choose a CSV File",accept_multiple_files=True)
for file in files:
    if file is not None:
        df = pd.read_csv(file)
        st.dataframe(df.describe())
        
feedback = st.text_area('Enter Your Feedback')
st.write(feedback)

st.link_button('You Can Visit My linkedin Profile By Clicking Link -->','https://www.linkedin.com/in/adnan/')

option = st.selectbox('Select Your Fav Python Lib' , ['pandas','matplotlib','numpy'],index = None,placeholder = 'select any one')
st.write(f'You have selected {option}')

rating = st.radio('Rate us',['1','2','3','4','5'],index = None)
st.write(f'Your rating is {rating}')

multi_options = st.multiselect('Select Your Fav Tech',['C','C++','py','java'])
st.write(multi_options)
st.write(multi_options[2])

st.date_input('Enter Date')
st.time_input('Enter Time')


aws = st.checkbox('Do You Have knowledge about AWS?')
if aws:
    st.write('Glad u Know AWS')
else:
    st.write('rejected')

dark_mode = st.toggle("Dark Mode")
st.write("Dark Mode is ON" if dark_mode else "Light Mode is ON")

price = st.slider("Select price range", 0, 10000, (0, 5000))
st.write("Selected range:", price)
st.write(price[1])
