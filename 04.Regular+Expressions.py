#!/usr/bin/env python
# coding: utf-8

# # NLP Basics: Learning how to use regular expressions

# ### Using regular expressions in Python
# 
# Python's `re` package is the most commonly used regex resource. More details can be found [here](https://docs.python.org/3/library/re.html).

# In[1]:


import re

re_test = 'This is a made up string to test 2 different regex methods'
re_test_messy = 'This      is a made up     string to test 2    different regex methods'
re_test_messy1 = 'This-is-a-made/up.string*to>>>>test----2""""""different~regex-methods'


# ### Splitting a sentence into a list of words

# In[2]:


re.split('\s', re_test)


# In[3]:


re.split('\s', re_test_messy)


# In[4]:


re.split('\s+', re_test_messy)


# In[5]:


re.split('\s+', re_test_messy1)


# In[6]:


re.split('\W+', re_test_messy1)


# In[7]:


re.findall('\S+', re_test)


# In[8]:


re.findall('\S+', re_test_messy)


# In[9]:


re.findall('\S+', re_test_messy1)


# In[10]:


re.findall('\w+', re_test_messy1)


# ### Replacing a specific string

# In[11]:


pep8_test = 'I try to follow PEEP8 guidelines'


# In[12]:


import re

re.findall('[a-z]+', pep8_test)


# In[13]:


re.findall('[A-Z]+', pep8_test)


# In[15]:


re.findall('[A-Z]+[0-9]+', pep8_test)


# In[16]:


re.sub('[A-Z]+[0-9]+', 'PEP8 Python Styleguide', pep8_test)


# In[ ]:




