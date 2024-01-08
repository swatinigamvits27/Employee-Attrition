#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#Load dataset
df = pd.read_csv("C:/Users/Swati Nigam/Desktop/Employee Attrition Dataset.csv")


# In[3]:


#show top 5 rows
df.head()


# In[4]:


#show last 5 rows
df.tail()


# In[5]:


#Get the no of rows and colum
df.shape


# In[6]:


#display information about the DataFrame's structure and characteristics.
df.info()


# In[7]:


#get the data type of column
df.dtypes


# In[8]:


#check for missing or null values 
df.isnull()


# In[9]:


#Get a count of empty value for each column
df.isnull().sum()


# In[11]:


#if any non null value drop.na()
#view some statistics
df.describe()


# In[12]:


df['Attrition'].value_counts()


# In[13]:


#attrition rate
185/1473


# In[14]:


#to check how many duplicate records we have
df[df.duplicated()]


# In[18]:


#to remove duplicate df = df.drop_duplicates(keep = 'First')
#It will keep the 1st value and remove duplicate and data will be stored in df
# use this function to find corelation between different colum with same data type df.corr()


# In[24]:


ftr = ['Age', 'Department', 'DistanceFromHome', 'HourlyRate', 'JobRole', 'YearsAtCompany']


# In[25]:


ftr


# In[26]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[31]:


import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'df' is your DataFrame and 'ftr' contains column names
fig, axes = plt.subplots(4, 2, figsize=(10, 15))  # Create a figure with 4 rows and 2 columns of subplots

# Flatten the axes array to loop through subplots
axes = axes.flatten()

# Loop through the features and create countplots on each subplot
for idx, feature in enumerate(ftr):
    sns.countplot(x=feature, data=df, hue='Attrition', ax=axes[idx])

plt.tight_layout()  # Adjust layout to prevent overlapping
plt.show()


# In[ ]:


#Attrition rate = No of employees left/no of total employees

