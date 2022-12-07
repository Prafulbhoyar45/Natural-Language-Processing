#!/usr/bin/env python
# coding: utf-8

# # NLP Basics: What is Natural Language Processing & the Natural Language Toolkit?

# ### How to install NLTK on your local machine
# 
# Both sets of instructions below assume you already have Python installed. These instructions are taken directly from [http://www.nltk.org/install.html](http://www.nltk.org/install.html).
# 
# **Mac/Unix/Windows**
# 
# From the terminal:
# 1. Install NLTK: run `pip install -U nltk`
# 2. Test installation: run `python` then type `import nltk`
# 
# 

# ### Download NLTK data

# In[1]:


import nltk
nltk.download()


# In[2]:


dir(nltk)


# ### What can you do with NLTK?

# In[3]:


from nltk.corpus import stopwords

stopwords.words('english')[0:100:10]


# In[ ]:




