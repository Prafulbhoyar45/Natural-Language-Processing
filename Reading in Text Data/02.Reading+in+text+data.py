#!/usr/bin/env python
# coding: utf-8

# # NLP Basics: Reading in text data & why do we need to clean the text?

# ### Read in semi-structured text data

# In[1]:


# Read in the raw text
rawData = open("SMSSpamCollection.tsv").read()

# Print the raw data
rawData[0:500]


# In[2]:


parsedData = rawData.replace('\t', '\n').split('\n')


# In[3]:


parsedData[0:5]


# In[4]:


labelList = parsedData[0::2]
textList = parsedData[1::2]


# In[5]:


print(labelList[0:5])
print(textList[0:5])


# In[6]:


import pandas as pd

fullCorpus = pd.DataFrame({
    'label': labelList,
    'body_list': textList
})

fullCorpus.head()


# In[7]:


print(len(labelList))
print(len(textList))


# In[8]:


print(labelList[-5:])


# In[9]:


fullCorpus = pd.DataFrame({
    'label': labelList[:-1],
    'body_list': textList
})

fullCorpus.head()


# In[10]:


#alternative step
dataset = pd.read_csv("SMSSpamCollection.tsv", sep="\t", header=None)
dataset.head()


# In[ ]:




