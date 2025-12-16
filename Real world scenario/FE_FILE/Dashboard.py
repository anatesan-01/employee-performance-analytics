#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import streamlit as st
import warnings
warnings.filterwarnings("ignore")
import logging
logging.getLogger("streamlit").setLevel(logging.ERROR)



# In[23]:


emp_data=pd.read_csv("df_fe.csv")
emp_data.drop(columns='Unnamed: 0',inplace=True)
emp_data


# In[24]:


avg_increment = emp_data['increment_percentage'].mean()
avg_salary = emp_data['salary'].mean()
retention_rate = emp_data['termination_flag'].value_counts(normalize = True)['No']*100


# In[25]:


# Streamlit Dashboard Title
st.title("Employee KPI Dashboard")


# In[26]:


col1 , col2 , col3 = st.columns(3)
col1.metric("Average Salary", f"{avg_salary: ,.0f}")
col2.metric("Average Increment" , f"{avg_increment : .1f}%")
col3.metric("Retention Rate" , f"{retention_rate : .1f}%")


# In[28]:


#Filters
st.sidebar.header("Filters")
exp_range = st.sidebar.slider("Experience Years" , 
                              min_value = 0,
                              max_value = int(emp_data['experience_years'].max()) +1 ,
                              value = (0, int(emp_data['experience_years'].max())))
termination_filter = st.sidebar.selectbox('Termination Status' , ['All','Active','Terminated'])



# In[29]:


#Apply filter
filter_map = {'Active' :'No',
              'Terminated' : 'Yes',
              'All' : 'All'}

flag_value = filter_map[termination_filter]
mask = emp_data['experience_years'].between(exp_range[0],
                                      exp_range[1]) & np.where(flag_value == 'All' ,True, emp_data['termination_flag'] == flag_value)

filtered_df = emp_data[mask]


# In[30]:


# Scatterplot

fig = px.scatter(
    filtered_df,
    x = 'experience_years',
    y = 'salary',
    color = 'promotion_hr_based',
    title = 'Salary Vs Experience By Promotion Status',
    labels = {'experience_years' : 'Experience (in Years)',
              'salary' : 'Salary',
              'promotion_hr_based' : 'Promotion Status'},
    color_discrete_map={'Promotion Pipeline' : '#1f77b4', 
                        'Not In Promotion Pipeline' : '#1ec94c'})


st.plotly_chart(fig , use_container_width= True)



# In[ ]:




