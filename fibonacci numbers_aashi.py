#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fib(n):
    a, b = 0, 1
    while a < n:
        print (a, end=' ')
        a, b = b, a+b
        print ()
fib(1000)


# In[ ]:




