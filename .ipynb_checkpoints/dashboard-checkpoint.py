#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import plotly.express as px


# In[2]:


df_fe = pd.read_csv("/Users/shubhamsarkar/Python Freelance Workshop  DA/df_fe.csv")

df_fe = df_fe.drop('Unnamed: 0' , axis =1)
# In[3]:


df_fe


# In[4]:


avg_increment = df_fe['increment_percentage'].mean()
avg_salary = df_fe['salary'].mean()
retention_rate = df_fe['termination_flag'].value_counts(normalize = True)['No']*100


# In[6]:


# Streamlit Dashboard Title
st.title("Employee KPI Dashboard")

# Display KPI
col1 , col2 , col3 = st.columns(3)
col1.metric("Average Salary", f"{avg_salary: ,.0f}")
col2.metric("Average Increment" , f"{avg_increment : .1f}%")
col3.metric("Retention Rate" , f"{retention_rate : .1f}%")

#Filters
st.sidebar.header("Filters")
exp_range = st.sidebar.slider("Experience Years" , 
                              min_value = 0,
                              max_value = int(df_fe['experience_years'].max()) +1 ,
                              value = (0, int(df_fe['experience_years'].max())))
termination_filter = st.sidebar.selectbox('Termination Status' , ['All','Active','Terminated'])


#Apply filter
filter_map = {'Active' :'No',
              'Terminated' : 'Yes',
              'All' : 'All'}

flag_value = filter_map[termination_filter]
mask = df_fe['experience_years'].between(exp_range[0],
                                      exp_range[1]) & np.where(flag_value == 'All' ,True, df_fe['termination_flag'] == flag_value)

filtered_df = df_fe[mask]

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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




