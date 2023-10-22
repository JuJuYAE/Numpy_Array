#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 


# In[2]:


arr = np.arange(0,11)


# In[3]:


arr


# In[6]:


arr[1:5]


# In[8]:


arr[0:10:2]


# In[9]:


arr[5:]


# In[10]:


arr[0:5] = 100


# In[11]:


arr


# In[12]:


arr = np.arange(0,11)


# In[13]:


arr


# In[14]:


slice_off_arr = arr[:6]


# In[16]:


arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])


# In[17]:


arr_2d


# In[22]:


arr_2d[2,1]


# In[40]:


arr_2d_copy = arr_2d[:2,1:].copy()


# In[41]:


arr_2d_copy


# In[42]:


arr_2d_copy[:] = 1


# In[43]:


arr_2d_copy


# In[44]:


arr_2d[1:]


# In[45]:


arr


# In[47]:


arr > 5


# In[48]:


bool_arr = arr > 5


# In[49]:


bool_arr


# In[50]:


arr[bool_arr]


# In[53]:


arr_2d = np.arange(50).reshape(5,10)


# 

# In[54]:


arr_2d


# In[56]:


arr_2d[1:3,3:5]


# In[57]:


arr = np.arange(0,11)


# In[58]:


arr


# In[59]:


arr + arr 


# In[60]:


arr * arr 


# In[61]:


3 * arr 


# In[62]:


arr/arr


# In[63]:


1/arr


# In[64]:


arr 

