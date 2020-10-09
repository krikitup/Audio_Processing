#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from sympy import *
from IPython.display import Audio


# In[46]:


yellow= 'yellow.wav'
rate, audio = wavfile.read(yellow)
audio = np.mean(audio, axis=1)
N = audio.shape[0]
L = N / rate
t = np.arange(N)/rate

print(f'Audio length: {L:.2f} seconds')

f, ax = plt.subplots()
ax.plot(t, audio)
ax.set_xlabel('Time [s]')
ax.set_ylabel('Amplitude [unknown]');
f.savefig('Audio.pdf')


# In[4]:


Audio(yellow)


# In[5]:


def der(f, n, a, dt):
    if(a<n):
        return (f[a+1] - f[a])/dt
    if(a==n):
        return (f[n] - f[n-1])/dt
    else:
        return 0
audio_no = audio
for i in range(len(audio)):
    if(audio_no[i] == 0):
        audio_no[i] = 0.5e-18
    else:
        audio_no[i] = audio_no[i]


# In[48]:


dt = t[1] - t[0]
audio_dt = [0.0001]*len(audio)
for i in range(len(audio)-1):
    audio_dt[i] = der(audio_no, len(audio), i, dt)
f2 = plt.figure()
plt.plot(t,audio_dt)
f2.savefig('differntiated_wave.pdf')


# In[49]:


sigma = 10
v = [1e-8]*len(audio)
for i in range(len(audio)):
    v[i] = audio_dt[i]/sigma + audio_no[i]


# In[ ]:





# In[50]:


f3 = plt.figure()
plt.plot(t,v)
f3.savefig('V.pdf')


# In[9]:


v_dt = [1e-8]*len(v)
for i in range(len(v)-1):
    v_dt[i] = der(v,len(v),i, dt)
plt.plot(t,v_dt)


# In[10]:


r = 28
w = [r/20]*len(audio)
for i in range(len(audio)):
    w[i] = w[i] - (v[i] +v_dt[i])/20*audio_no[i] + 1e-8


# In[51]:


f4 = plt.figure()
plt.plot(t,w)
f4.savefig('W.pdf')


# In[12]:


w_dt = [1e-8]*len(w)
for i in range(len(w)-1):
    w_dt[i] = der(w,len(w),i,dt)


# In[13]:


plt.plot(t,w_dt)


# In[17]:





# In[18]:





# In[30]:





# In[31]:





# In[45]:





# In[42]:





# In[36]:





# In[38]:





# In[ ]:




