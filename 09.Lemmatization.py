#!/usr/bin/env python
# coding: utf-8

# # Supplemental Data Cleaning: Using a Lemmatizer

# ### Test out WordNet lemmatizer (read more about WordNet [here](https://wordnet.princeton.edu/))

# In[1]:


import nltk

wn = nltk.WordNetLemmatizer()
ps = nltk.PorterStemmer()


# In[2]:


dir(wn)


# In[3]:


print(ps.stem('meanness'))
print(ps.stem('meaning'))


# In[4]:


print(wn.lemmatize('meanness'))
print(wn.lemmatize('meaning'))


# In[5]:


print(ps.stem('goose'))
print(ps.stem('geese'))


# In[6]:


print(wn.lemmatize('goose'))
print(wn.lemmatize('geese'))


# ### Read in raw text

# In[7]:


import pandas as pd
import re
import string
pd.set_option('display.max_colwidth', 100)

stopwords = nltk.corpus.stopwords.words('english')

data = pd.read_csv("SMSSpamCollection.tsv", sep='\t')
data.columns = ['label', 'body_text']

data.head()


# ### Clean up text

# In[8]:


def clean_text(text):
    text = "".join([word for word in text if word not in string.punctuation])
    tokens = re.split('\W+', text)
    text = [word for word in tokens if word not in stopwords]
    return text

data['body_text_nostop'] = data['body_text'].apply(lambda x: clean_text(x.lower()))

data.head()


# ### Lemmatize text

# In[9]:


def lemmatizing(tokenized_text):
    text = [wn.lemmatize(word) for word in tokenized_text]
    return text

data['body_text_lemmatized'] = data['body_text_nostop'].apply(lambda x: lemmatizing(x))

data.head(10)


# In[ ]:




