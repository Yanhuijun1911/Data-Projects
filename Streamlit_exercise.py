import streamlit as st
import pandas as pd
import numpy as np
import io

st.title('Check the nulls of a file')

st.header('1. Upload data file')
my_csv = st.file_uploader('Select a CSV file',
                          type = 'csv',
                          accept_multiple_files = False)

if my_csv is not None:
    my_df = pd.read_csv(my_csv) # dataframe
    st.header('2. Show the dataframe')
    st.write(my_df) # print the dataframe

    #information of the dataset
    st.header('3. Show the information of the dataframe') #create the header
    st.subheader('  Descriptive statistics') # create the subheader
    st.write(my_df.describe()) # show the descriptive statistics
    st.subheader('  Total rows and columns') # create the subheader
    st.write(my_df.shape) # show the total number of rows and columns

    st.subheader('  Information of the dataframe') # create the subheader
    buffer = io.StringIO() #use StringIO method to pass string to the constructor
    my_df.info(buf=buffer) # pass info as string to the buffer
    information = buffer.getvalue() #return the string containing the whole contents of the buffer
    st.text(information) #show the information of the dataframe. It can see the numbers of null values of each column, which gives a general picture to the users before they choose a column

    # print columns

    col = my_df.columns.values.tolist() # put columns to a list col
    st.header('4. Show column names') # create the header for this session
    st.write(col) # print the columns


    # select a column
    st.header('5. Select a column') # create the header for this session
    selected_col =st.selectbox('select',col) #create a selectbox with column names

    st.text('show the values of the column') #create a text message
    st.write(my_df[selected_col]) #print the values of the column

    #count the value of the column
    count = my_df[selected_col].value_counts() # assign the number of each values of the selected column to a variable count
    st.text('show the count of each value in this column') #create a text message
    st.write(count) # print the count values

    # dealing with null

    st.header('6. Deal with Null value') # create the header for this session
    ## choose the filling method
    dealed_null = st.selectbox('choose a method to deal with null value',['drop_null','fill_0','fill_median','fill_mean']) #create a selectbox with four methods to deal with the null.

    st.text('show the column after feature engineering') # create a text message

    ## create outputs for the four methods
    if dealed_null == 'drop_null':
        drop_null = my_df[selected_col].dropna(axis = 0, inplace = False) # drop the null value of this column
        st.write(drop_null) # show the current column
    elif dealed_null == 'fill_0':
        fill_0 = my_df[selected_col].fillna(0) # fill null value with 0
        st.write(fill_0) # show the current column
    elif dealed_null == 'fill_mean':
        fill_mean = my_df[selected_col].fillna(my_df[selected_col].mean()) # fill null value with the mean of the selected column
        st.write(fill_mean) # show the current column
    else:
        fill_median = my_df[selected_col].fillna(my_df[selected_col].median()) # fill null value with the median of the selected column
        st.write(fill_median) # show the current column


