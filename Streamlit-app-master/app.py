import streamlit as st
import pandas as pd
import matplotlib as plt
import numpy

st.title('Need help with data Science?')

file_ = open('Most Popular Websites 1996 - 2019.mp4', 'rb').read()
st.text('This is what data can do.')
st.video(file_)

name_list = {}
status = st.radio('What is your status?', ('Active', 'Inactive'))
if status == 'Active':
    st.success('That\'s great! These are the tools'
               ' we use or you can call it a '
               'data scientist\'s tech stack. There you go...')
    st.help(st)
    st.help(pd)
    st.help(plt)
    st.help(numpy)

elif status == 'Inactive':

    # dict
    number_months = st.number_input('Years inactive')
    name = st.text_input('Name')
    occupation = st.text_input('Current occupation')
    one = name.capitalize()
    two = occupation.capitalize()
    # dict over

    if name != '':
        st.success(f'Hi {name.capitalize()}! Here we will make sure you'
                   f' get what you\'re looking for.'
                   ' But just to be clear, we are strictly talking about data science. In other as'
                   'pects you can help yourself. Wink wink!')
        desired_occ = st.selectbox('What would you want to be?',
                                   ['Data Scientist', 'Data Analyst', 'Data collector', 'Business analyst'])
        location = st.selectbox('Choose locations:', ['Pune', 'Mumbai', 'Delhi', 'Chennai'])

        #dict update with new inputs
        name_list.update(
            {'Name': one, 'Current occupation': two, 'Wants to be': desired_occ, 'Desired location': location})
        print(name_list)

        st.write('You selected ', len(location), ' locations.')
        slide = st.slider('Level', 1, 5)

        if slide > 2:
            st.success('Amazing, there you go...')
            st.help(st)
            st.help(pd)
            st.help(plt)
        else:
            st.warning('You need to improve your skills, i mean, c\'mon...')

    elif name == '':
        st.warning('Enter your name or we won\'t be able to help you.')
