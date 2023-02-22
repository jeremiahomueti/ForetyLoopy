#!/usr/bin/env python

# coding: utf-8

# In[1]:

integers = [1,2,3,4,5]

# In[2]:


for number in integers:
    
    print(number)


# In[3]:


#notice above the forLoop is used as a counter.


# In[5]:


integers = [1,2,3,4,5]

for number in integers:
    
    print('Yep!')


# In[6]:


integers = [1,2,3,4,5]

for numbers in integers:
    
    print(numbers + numbers)


# In[23]:


ice_cream_dict = {'name': 'Alex Freberg', 'weekly intake': 5, 'favorite ice creams': ['MCC', 'Chocolate']}


print(ice_cream_dict)


# In[57]:


for cream in ice_cream_dict.values():
    print(cream)


# In[59]:


for cream in ice_cream_dict.items():
    
    
    print(cream)


# In[58]:


for cream, juicy in ice_cream_dict.items():
    
    print(cream, "-->", juicy)


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:





