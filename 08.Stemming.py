#!/usr/bin/env python
# coding: utf-8

# # Supplemental Data Cleaning: Using Stemming

# ### Test out Porter stemmer

# In[1]:


import nltk

ps = nltk.PorterStemmer()


# In[2]:


dir(ps)


# In[3]:


print(ps.stem('grows'))
print(ps.stem('growing'))
print(ps.stem('grow'))


# In[4]:


print(ps.stem('run'))
print(ps.stem('running'))
print(ps.stem('runner'))


# ### Read in raw text

# In[5]:


import pandas as pd
import re
import string
pd.set_option('display.max_colwidth', 100)

stopwords = nltk.corpus.stopwords.words('english')

data = pd.read_csv("SMSSpamCollection.tsv", sep='\t')
data.columns = ['label', 'body_text']

data.head()


# ### Clean up text

# In[6]:


def clean_text(text):
    text = "".join([word for word in text if word not in string.punctuation])
    tokens = re.split('\W+', text)
    text = [word for word in tokens if word not in stopwords]
    return text

data['body_text_nostop'] = data['body_text'].apply(lambda x: clean_text(x.lower()))

data.head()


# ### Stem text

# In[7]:


def stemming(tokenized_text):
    text = [ps.stem(word) for word in tokenized_text]
    return text

data['body_text_stemmed'] = data['body_text_nostop'].apply(lambda x: stemming(x))

data.head()


# In[ ]:




