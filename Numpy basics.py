#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
list1 = [0,1,2,3,4]
arr1d = np.array(list1)
print (type(arr1d))
arr1d


# In[2]:


arr1d + 2


# In[4]:


list2 = [[0,1,2],[3,4,5],[6,7,8]]
arr2d = np.array(list2)
print(arr2d)


# #arr2d_f = np.array(list2,dtype = 'float')

# In[6]:


arr2d_f = np.array(list2,dtype = 'float')
arr2d_f


# In[7]:


arr2d_f.astype('int')


# In[9]:


arr2d_f


# In[10]:


arr2d_f.astype('int').astype('str')


# In[15]:


arr2d_b = np.array([1,0,10],dtype='bool')
arr2d_b


# In[16]:


arr1d_obj = np.array([1,'a'],dtype = 'object')
arr1d_obj


# In[17]:


arr1d_obj.tolist()


# In[18]:


arr1d_obj = np.array([1,'a'])
arr1d_obj


# In[19]:


list2 = [[1,2,3,4],[3,4,5,6],[5,6,7,8]]
arr2 = np.array(list2,dtype = 'float')
arr2


# In[20]:


print('Shape:',arr2.shape)
print('Datatype:',arr2.dtype)
print('Size:',arr2.size)
print('Num Dimensions:',arr2.ndim)


# In[21]:


arr2


# In[22]:


arr2[:2,:2]


# In[23]:


b = arr2>4
b


# In[30]:


arr2[b]


# In[25]:



arr2[::-1,::-1]


# In[26]:


arr2[::-1,]


# In[31]:


arr2[0:2,]


# In[32]:


arr2[1,1] = np.nan
arr2[1,2] = np.inf
arr2


# In[35]:


missing_bool = np.isnan(arr2) | np.isinf(arr2)
arr2[missing_bool] = -1
arr2


# In[36]:


print('Mean value is:',np.mean(arr2))


# In[37]:


print('Mean value is:',arr2.mean())
print('Max value is:',arr2.max())
print('Min value is:',arr2.min())


# In[41]:


print('Column wise min:',np.amin(arr2,axis=0))
print('Row wise max:',np.amax(arr2,axis=1))


# In[44]:


np.cumsum(arr2)


# In[45]:


arr2a = arr2[:2,:2]
arr2a[:1,:1] = 100
arr2


# In[47]:


arr2b = arr2[:2,:2].copy()
arr2b[:1,:1] = 101
arr2


# In[48]:


arr2.reshape(4,3)


# In[49]:


arr2 


# In[60]:


arr2.flatten()


# In[51]:


arr2


# In[61]:


b1 = arr2.flatten()
b1[0] = 201
arr2


# In[53]:


b2 = arr2.ravel()
b2[0] = 101
arr2


# In[65]:


print(np.arange(5))
print(np.arange(0,10))
print(np.arange(0,10,2))
print(np.arange(10,0,-1))


# In[74]:


np.linspace(start=0,stop=50,num=15,dtype = int)


# In[88]:


np.logspace(start=1,stop=50,num=10,base=10,dtype = float)


# In[93]:


np.zeros([3,3])


# In[95]:


np.ones([2,2])


# In[99]:


a  = [1,2,3]
np.tile(a,3)


# In[98]:


np.repeat(a,3)


# In[ ]:




