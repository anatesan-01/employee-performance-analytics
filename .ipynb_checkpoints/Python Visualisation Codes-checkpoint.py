


# # Visualisation For Python 

# In[37]:


# 


# In[120]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# In[ ]:


# Sample data
np.random.seed(42)
data = np.random.randn(100)  # Random data for histogram
categories = ['A', 'B', 'C', 'D']
values = [4, 3, 2, 1]
df_v1 = pd.DataFrame({
    'x': np.random.rand(50),
    'y': np.random.rand(50),
    'category': np.random.choice(['Group1', 'Group2'], 50)
})


# In[ ]:


df_v1


# # 1 . Histogram with matplotlib

# In[ ]:


plt.figure(figsize = (8,6))
plt.hist(data , bins = 20 , color = 'skyblue' , edgecolor = 'black' , alpha = 0.7)
plt.title('Histogram Of Random Data' , fontsize = 14, pad = 10)
plt.xlabel('Values' , fontsize = 12)
plt.ylabel('Frequency' , fontsize = 12)
plt.grid(True , alpha = 0.3)
plt.show()


# # 2. Barplot

# In[ ]:


plt.figure(figsize = (8,6))
sns.barplot(x = categories , y = values , palette = 'Blues')
plt.title('Bar Plot For Categories' , fontsize = 14 , pad = 10)
plt.xlabel('Category' , fontsize = 12)
plt.ylabel('Values' , fontsize = 12)
plt.show()


# # 3. Scatterplot with hue

# In[ ]:


plt.figure(figsize = (8,6))
sns.scatterplot(x = 'x' , y = 'y' , hue = 'category' , palette = 'deep' , data = df_v1 , s = 100)
plt.title('Scatterplot With Categories' , fontsize = 14 , pad = 10)
plt.xlabel('Category' , fontsize = 12)
plt.ylabel('Values' , fontsize = 12)
plt.legend(title = 'Category')
plt.show()


# # 4. Saving Your Figure

# In[ ]:


plt.figure(figsize = (8,6))
sns.histplot(data , bins = 20 , color = 'coral' , edgecolor = 'black' , alpha = 0.7)
plt.title('Histogram (for saving purpose)' , fontsize = 14 , pad = 10)
plt.xlabel('X Axis' , fontsize = 12)
plt.ylabel('Y Axis' , fontsize = 12)
plt.savefig('histogram_youtube_v1' ,dpi = 300 , bbox_inches = 'tight')
plt.show()


# # 1. Kernel Density Estimate (KDE) in Histplot

# ## sample data 

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# In[ ]:


# Sample salary data (real-world HR context)
np.random.seed(42)
data = pd.DataFrame({
    'salary': np.random.normal(60000, 15000, 100),  # Salaries in $
    'experience': np.random.uniform(1, 20, 100),    # Years of experience
    'increment_pct': np.random.uniform(2, 15, 100), # Increment percentages
    'department': np.random.choice(['HR', 'IT', 'Sales', 'Marketing'], 100),
    'gender': np.random.choice(['Male', 'Female'], 100)
})

# Wide-format salary data for melting
salary_data_wide = pd.DataFrame({
    'HR': np.random.normal(55000, 10000, 50),
    'IT': np.random.normal(70000, 12000, 50),
    'Sales': np.random.normal(65000, 11000, 50),
    'Marketing': np.random.normal(60000, 9000, 50),
    'gender': np.random.choice(['Male', 'Female'], 50)
})


# In[ ]:


data


# In[ ]:


salary_data_wide


# In[ ]:


# KDE In Histplot


# In[ ]:


plt.figure(figsize = (8,6))
sns.histplot(data['salary'] , bins = 30 , kde = True , color = 'teal' , stat = 'density')
plt.title('Salary Distribution With KDE' , fontsize = 14)
plt.xlabel('Salary' , fontsize = 12)
plt.ylabel('Density' , fontsize = 12)
plt.show()


# # 2. Boxplot With sns.boxplot()

# In[ ]:


plt.figure(figsize = (8,6))
sns.boxplot(x = 'department' , y = 'increment_pct' , data = data , palette = 'Pastel1')
plt.title('Increment % by Department (Boxplot)', fontsize = 14)
plt.xlabel('Department' , fontsize = 12)
plt.ylabel('Increment %' , fontsize = 12)
plt.show()


# # 3. pd.melt() and Grouped Bar Chart

# In[ ]:


melted_data = pd.melt(salary_data_wide , id_vars = ['gender'] , value_vars = ['HR', 'IT', 'Sales', 'Marketing'],
                      var_name = 'Department' , value_name = 'Salary')
plt.figure(figsize = (8,6))
sns.barplot(x = 'Department' , y = 'Salary' , hue = 'gender' , data = melted_data , palette = 'Set2')
plt.title('Grouped Salary By Gender and Department' , fontsize = 14)
plt.xlabel('Department' , fontsize = 12)
plt.ylabel('Salary' , fontsize = 12)
plt.legend(title = 'Gender')
plt.show()


# # 4. Advanced Scatterplot With Styling And Custom Legend

# In[ ]:


#scatterplot advanced


# In[ ]:


plt.figure(figsize = (8,6))
sns.scatterplot(x = 'experience' , y = 'salary', hue = 'department' , size = 'increment_pct',
                style = 'gender' , data = data , palette = 'deep' , sizes = (50 , 200))
plt.title('Salary vs Experience' , fontsize = 14)
plt.xlabel('Years of experience' , fontsize = 12)
plt.ylabel('Salary' , fontsize = 12)
plt.legend(bbox_to_anchor = (1.05 , 1) , loc = 'upper left')
plt.tight_layout()
plt.show()


# In[ ]:





# # 3. Correlation With ScatterPlot (Advanced Series)

# ## Correlation With Scatterplot

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Dana', 'Eve', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['Sales', 'Marketing', 'Sales', 'HR', 'Marketing', 'Sales', 'HR', 'Marketing', 'Sales', 'HR'],
    'Sales': [15000, 12000, 18000, 8000, 14000, 16000, 9000, 13000, 17000, 10000],
    'Productivity': [85, 78, 92, 65, 88, 90, 70, 82, 95, 75]
}
df = pd.DataFrame(data)
print(ds(df.head(10)))


# In[ ]:


plt.figure(figsize = (8,6))
sns.scatterplot(x = 'Productivity' , y = 'Sales', data = df , hue = 'Department' , palette = 'viridis' , s = 100)
plt.title('Sales vs Productivity by Department' , fontsize = 14)
plt.xlabel('Productivity Score' , fontsize = 12)
plt.ylabel('Sales Scores' , fontsize = 12)
plt.show()


# # 3b. Grouping Data With Groupby

# In[ ]:


grouped = df.groupby('Department').mean(numeric_only  = True)
print(ds(grouped))

sns.scatterplot(x = 'Sales' , y = 'Productivity' , hue = 'Department' , data = grouped , s=100)
plt.show()


# # 3c. Top Performer Using Barchart and use of ax.bar_label

# In[ ]:


top_performers = df.sort_values(by = 'Sales' , ascending = False).head(5)
print(ds(top_performers))

# barplot

plt.figure(figsize = (8,6))
ax = sns.barplot(x = 'Name' , y = 'Sales' , data = top_performers , palette = 'coolwarm')
plt.title('Top 5 Sales Performer' , fontsize = 14)
plt.xlabel('Emp Name' , fontsize = 12)
plt.ylabel('Sales Amount' , fontsize = 12)
ax.bar_label(ax.containers[0] , fmt = '$%d' , padding = 3)
plt.show()


# # 3c. Customisation With Color Map and Labels

# In[ ]:


plt.figure(figsize = (8,6))
ax = sns.barplot(x = 'Name' , y = 'Sales' , data = top_performers , palette = 'coolwarm')
plt.title('Top 5 Sales Performer' , fontsize = 14)
plt.xlabel('Emp Name' , fontsize = 12)
plt.ylabel('Sales Amount' , fontsize = 12)
ax.bar_label(ax.containers[0] , fmt = '$%d' , padding = 3)
plt.xticks(rotation = 45)
plt.show()


# # 4. Lineplot

# ## sample data and marker addition

# In[ ]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
np.random.seed(42)
data = pd.DataFrame({
    'Experience': np.random.normal(10, 3, 100),  # Years of experience
    'Promotion_Hours': np.random.normal(50, 15, 100)
    })  # Hours spent on promotions


# In[ ]:


data


# In[ ]:


data['Experience_Rounded'] = data['Experience'].round(0)
line_data = data.groupby('Experience_Rounded')['Promotion_Hours'].mean().reset_index()


# In[ ]:


line_data


# # LinePlot
# 

# In[ ]:


plt.figure(figsize =(8,6))
sns.lineplot(x = 'Experience_Rounded' ,
             y = 'Promotion_Hours',
             data = line_data,
             color = 'teal',
             marker = 'o')
plt.title('Promotion_Hours vs Experience_Rounded' , fontsize = 14)
plt.xlabel('Years_Of_Experience' , fontsize = 12)
plt.ylabel('Average_Promotion_Hours' ,fontsize = 12)
plt.grid(True, alpha = 0.3)
plt.show()


# # 4. Pie Plot And Uncut

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Sample employee dataset
data = {
    'EmployeeID': range(1, 101),
    'Department': np.random.choice(['HR', 'IT', 'Sales'], 100),
    'TerminationStatus': np.random.choice(['Active', 'Terminated'], 100, p=[0.65, 0.35]),
    'Year': np.random.choice([2020, 2021, 2022, 2023], 100)
}
df = pd.DataFrame(data)


# In[ ]:


df


# In[ ]:


status_counts


# In[ ]:


plt.figure(figsize = (8,6))
status_counts = df['TerminationStatus'].value_counts()
plt.pie(status_counts,
        labels = status_counts.index,
        autopct = '%1.1f%%',
        colors = sns.color_palette('Set2'),
        startangle = 90)
plt.title('Terminated Status')
plt.axis('equal')
plt.show


# # 4b . Unstack()

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Sample employee dataset
data = {
    'EmployeeID': range(1, 101),
    'Department': np.random.choice(['HR', 'IT', 'Sales'], 100),
    'TerminationStatus': np.random.choice(['Active', 'Terminated'], 100, p=[0.65, 0.35]),
    'Year': np.random.choice([2020, 2021, 2022, 2023], 100)
}
df = pd.DataFrame(data)


# In[ ]:


df


# In[ ]:


dept_year = df.groupby(['Year','Department']).size().unstack(fill_value = 0)
plt.figure(figsize = (8,6))
dept_year.plot(kind = 'bar',
               stacked  = True,
               color = sns.color_palette('Pastel1'))
plt.title('Employee Counts Per Dept and Year' , fontsize =14)
plt.xlabel('Years' , fontsize = 12 )
plt.ylabel('Number Of Employees' , fontsize = 12)
plt.legend(title = 'Department')
plt.xticks(rotation = 0)
plt.show()


# In[ ]:


import streamlit as st


# In[ ]:


import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Set page configuration
st.set_page_config(page_title="Employee Dashboard", layout="wide")

# Sample dataset
np.random.seed(42)
data = pd.DataFrame({
    'employee_id': range(1, 101),
    'experience_years': np.random.randint(1, 15, 100),
    'salary': np.random.randint(30000, 120000, 100),
    'department': np.random.choice(['HR', 'IT', 'Sales', 'Marketing'], 100)
})

# Title
st.title("Employee Analytics Dashboard")

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total Employees", len(data))
col2.metric("Average Experience (Years)", round(data['experience_years'].mean(), 1))
col3.metric("Average Salary ($)", round(data['salary'].mean(), 0))

# Plotly Charts
st.subheader("Salary vs Experience by Department")
fig1 = px.scatter(data, 
                  x="experience_years", 
                  y="salary", 
                  color="department", 
                  title="Salary vs Experience",
                  labels={"experience_years": "Years of Experience", 
                          "salary": "Salary ($)"},
                  hover_data=["employee_id"])
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Department Distribution")
fig2 = px.histogram(data, 
                    x="department", 
                    title="Employee Count by Department",
                    color="department")
st.plotly_chart(fig2, use_container_width=True)

# Display data
st.subheader("Employee Data")
st.dataframe(data)


# In[ ]:





# In[ ]:





# # Python Visualisation Project
1.Salary distribution analysis
2.Salary comparison based on promotion status
3.Increment percentage evaluation
4.Relationship between experience and salary growth
# In[122]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import plotly.express as px


# ## Salary distribution analysis

# In[123]:


df


# In[124]:


plt.figure(figsize = (10,6))
sns.histplot(df['salary'],
             bins = 20 ,
             kde = True,
             color = 'Teal',
             edgecolor = 'black')
plt.title('Salary Distribution Across Employee' , fontsize = 14)
plt.xlabel('Salary' , fontsize = 12)
plt.ylabel('Count' , fontsize = 12)
plt.grid(True , alpha = 0.3)
plt.show()



# ## Salary comparison based on promotion status

# In[125]:


df


# In[126]:


employee_melted_data = pd.melt(df,
        id_vars = ['promotion_hr_based'],
        value_vars = ['salary','final_incremented_salary'],
        var_name = 'Salary_Type',
        value_name = 'Salary')
plt.figure(figsize = (10,6))
sns.barplot(x = 'promotion_hr_based',
            y = 'Salary',
            hue = 'Salary_Type',
            palette = 'Set2',
            data = employee_melted_data)
plt.title('Salary Comparison By Promotion Status', fontsize = 14)
plt.xlabel('Promotion HR Data' , fontsize = 12)
plt.ylabel('Salary' , fontsize = 12)
plt.legend(title = 'Salary Type')
plt.show()


# ## Increment percentage evaluation

# In[127]:


df


# In[128]:


plt.figure(figsize = (10,6))
sns.boxplot(x = 'promotion_hr_based',
            y = 'increment_percentage',
            hue = 'promotion_hr_based',
            palette = 'Pastel1',
            data = df)
plt.title('Increment Percentage', fontsize = 14)
plt.xlabel('Promotion HR Based', fontsize = 12)
plt.ylabel('Increment Percentage (%)' , fontsize = 12)
plt.legend(title = 'Promotion Status')
plt.show()


# ## Relationship between experience and salary growth

# In[129]:


df


# In[130]:


plt.figure(figsize = (10,6))
sns.scatterplot(x = 'experience_years',
                y = 'salary',
                hue = 'promotion_hr_based',
                size = 'increment_percentage',
                style = 'promotion_hr_based',
                palette = 'deep',
                data = df,
                sizes = (50,200))
plt.title('Experience Vs Salary (By Promotion Cycle)', fontsize = 14)
plt.xlabel('Year Of Experience' , fontsize = 12),
plt.ylabel('Salary' ,fontsize = 12)
plt.legend(title = 'Promotion Status')
plt.show()


5. Sales vs Productivity
6. Average sales and productivity by experience 
7. Top performers 
8. Experience distribution
9. Promotion hours vs experience 
10.Bubble chart (experience vs sales)
# In[131]:


df


# # Sales vs Productivity

# In[132]:


plt.figure(figsize = (10,6))
sns.scatterplot(x = 'time_productive',
                y = 'sales',
                hue = 'experience_years',
                palette = 'viridis',
                size = 'experience_years',
                data = df)
plt.title('Sales VS Productivity' , fontsize = 14)
plt.xlabel('Productivity Time' ,fontsize = 12)
plt.ylabel('Sales' , fontsize = 12)
plt.show()


# # Average sales and productivity by experience 

# In[133]:


grouped_data = df.groupby('experience_years')[['sales','time_productive']].mean().reset_index()
print(ds('Grouped Data(Average Sales and Productivity):' , grouped_data))


# # Top 5 Performers

# In[134]:


top_performers = df[['first_name' , 'sales']].sort_values(by = 'sales' , ascending = False).head(5)
plt.figure(figsize = (10,6))
sns.barplot(x = 'first_name',
            y = 'sales',
            data = top_performers,
            palette = 'Blues')
plt.title('Top 5 Performers', fontsize = 14)
plt.xlabel('Employee Name' , fontsize = 12)
plt.ylabel('Sales' , fontsize = 12)
plt.xticks(rotation = 45)
plt.show()


# In[135]:


top_performers


# # Experience distribution

# In[136]:


plt.figure(figsize = (8,6))
sns.histplot(df['experience_years'],
             bins = 20,
             color = 'Teal',
             kde = True)
plt.title('Distribution In Employee Experience' , fontsize = 14)
plt.xlabel('Experience Years' , fontsize = 12)
plt.ylabel('Counts' , fontsize = 12)
plt.show()


# # Promotion Hours And Experience

# In[137]:


promotion_data = df.groupby('experience_years')['time_productive'].mean().reset_index()
plt.figure(figsize = (8,6))
sns.lineplot(x = 'experience_years',
             y = 'time_productive',
             data = promotion_data,
             palette = 'Set2',
             marker = 'o')
plt.title('Promotion Hours Vs Experience' , fontsize = 14)
plt.xlabel('Experience Years' , fontsize = 12)
plt.ylabel('Promotion (Productive Hours)' , fontsize = 12)
plt.show()


# # Bubble chart (experience vs sales)

# In[138]:


bubble_chart = px.scatter(df,
           x = 'experience_years',
           y = 'sales',
           color = 'time_productive',
           hover_data = ['first_name'],
           title = 'Sales Vs Experience (Bubble Chart)')
bubble_chart.update_layout(xaxis_title = 'Experience (Years)',
                           yaxis_title = 'Sales',
                           coloraxis_colorbar_title = 'Productivity Time (Hours)')
bubble_chart.show()

1. avg_increment
2. avg_salary
3. retention_rate
# In[143]:


avg_increment = df['increment_percentage'].mean()
avg_salary = df['salary'].mean()
retention_rate = df['termination_flag'].value_counts(normalize = True)['No']*100


# In[160]:


print(f"Average Increment Percentage : {avg_increment :.1f}%")
print(f"Average Salary : {avg_salary : ,.0f}")
print(f"Retention Rate : {retention_rate : .1f}%")


# # Streamlit 

# In[39]:


df.to_csv("df_fe.csv", index = True)





