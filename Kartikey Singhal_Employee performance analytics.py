#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as  plt
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns


# In[26]:


df=pd.read_csv('Test_data.csv')


# In[5]:


df.head()


# In[6]:


df


# In[7]:


df.dtypes


# In[8]:


df.isnull().sum()


# In[9]:


df.shape


# In[10]:


num_cols=df.dtypes[df.dtypes!="object"].index
num_cols


# In[11]:


df.info()


# In[12]:


df['education'].value_counts()


# In[13]:


df.columns


# In[14]:


df.describe()


# In[15]:


plt.figure(figsize=(10,4.5))
sns.barplot(df['department'],df['avg_training_score'])


# In[16]:


plt.figure(figsize = (8,5))
sns.countplot(y= df.department,hue = df.avg_training_score)


# In[17]:


df.groupby(by='gender')['avg_training_score'].mean()


# In[18]:


df.groupby(by='gender')['avg_training_score'].value_counts()


# In[19]:


plt.figure(figsize=(10,4.5))
sns.barplot(df['gender'],df['avg_training_score'])


# In[20]:


plt.figure(figsize = (8,5))
sns.countplot(y= df.gender,hue = df.avg_training_score)


# In[21]:


df.groupby(by='department')['avg_training_score'].mean()


# In[22]:


df.groupby(by='department')['avg_training_score'].value_counts()


# In[23]:


Technology = df[df.department == 'Technology '] 
Technology.shape


# In[24]:


df = df.rename(columns={'KPIs_met >80%': 'KPIs_met', 'awards_won?': 'awards_won'})
df.head()


# In[35]:


df.groupby(by='previous_year_rating')['avg_training_score'].mean()


# In[36]:


df.groupby(by='previous_year_rating')['avg_training_score'].value_counts()


# In[37]:


plt.figure(figsize=(10,4.5))
sns.barplot(df['previous_year_rating'],df['avg_training_score'])


# In[38]:


plt.figure(figsize = (8,5))
sns.countplot(y= df.previous_year_rating,hue = df.avg_training_score)


# In[39]:


df.groupby(by='length_of_service')['avg_training_score'].mean()


# In[40]:


df.groupby(by='length_of_service')['avg_training_score'].value_counts()


# In[42]:


plt.figure(figsize=(10,4.5))
sns.barplot(df['length_of_service'],df['avg_training_score'])


# In[43]:


plt.figure(figsize = (8,5))
sns.countplot(y= df.length_of_service,hue = df.avg_training_score)

