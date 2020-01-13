#!/usr/bin/env python
# coding: utf-8

# In[317]:


import xml.etree.ElementTree as elemTree
import xml.dom.minidom
import re
import math
import numpy as np

doc = elemTree.parse("EyeofSoul_200_last.xml")
root = doc.getroot()
xmlStr =elemTree.tostring(root, encoding='utf8', method='xml')


# In[318]:


add_song=[]#list of songs
add_song_index=[]
feature=""
song = re.split(r'(?<=>)(.+?)(?=<)', str(xmlStr))
for i in range(len(song)):
  if song[i].find("<data_set_id>") !=-1:
    song[i+1]=song[i+1].replace("C:\\Users\\q\\Desktop\\music_set_wav\\", "").replace(".wav", "")
    add_song.append(song[i+1])
    add_song_index.append(i+1)
add_song_index.append(len(song))
#print(add_song)


# In[319]:


song_value={}
#dictionary for each song in xml file

for i in range(len(add_song)):
  feature = []
  for j in range (add_song_index[i]+1, add_song_index[i+1]-1):
    feature.append(song[j])
  song_value[add_song[i]]= feature
#print((song_value['035-CHANGMO-01-BAND']))




# In[230]:



def dictionaryForSong(array):
  name_value = {}
  del_name = []
  add_name = []
  add_value =[]
  for i in range(len(array)):
    if array[i].find('<name>') != -1:
      value=[]
      if(i<len(array)-1):
          i+=1
      name=array[i]
      if(i<len(array)-1):
          i+=1
      while (array[i].find('<v>') !=-1 and i < len(array)-2) :
        value.append((float)(''.join(array[i+1])))
        i+=2
      name_value[name]=value

  for i in name_value.keys():
    if True:
      del_name.append(i)
      for j in range(len(name_value[i])):
        add_name.append(i+ " "+ str(j))
        add_value.append(((name_value[i][j])/math.sqrt(len(name_value[i]))))
  for i in range(len(add_name)):
    name_value[add_name[i]] = add_value[i]
  for i in del_name:
    del name_value[i]
  return name_value
row=len(dictionaryForSong(song_value[add_song[0]]).keys())
#print((dictionaryForSong(song_value['C:\\Users\\q\\Desktop\\music_set_wav\\035-CHANGMO-01-BAND.wav'])))
characters=dictionaryForSong(song_value[add_song[0]]).keys()#characters..

#song_value.keys().index(000):


# In[320]:


#normalize mat
num=0
num_song={}
mat=np.zeros(( len(song_value.keys()), row)) #200*77
for z in add_song:
    for y in dictionaryForSong(song_value[z]).keys():
        mat[add_song.index(z)][characters.index(y)]=dictionaryForSong(song_value[z])[y]

for j in range(mat.shape[1]):
    mean = 0
    dev = 0
    for i in range(mat.shape[0]):
        mean+=mat[i,j]/mat.shape[0]
    for i in range(mat.shape[0]):
        dev+=((mat[i,j]-mean)*(mat[i,j]-mean))/mat.shape[0]
    dev=math.sqrt(dev)
    for i in range(mat.shape[0]):
        mat[i,j]=(mat[i,j]-mean)/dev
        if math.isnan(mat[i, j]):
            mat[i, j]=0
    dev=0
    mean=0
    for i in range(mat.shape[0]):
        dev+=((mat[i,j])*(mat[i,j]))/mat.shape[0]
        mean+=mat[i,j]/mat.shape[0]


# In[321]:


def distance(a, b):
    tot=0
    song_1=add_song.index(a)
    song_2=add_song.index(b)
    for i in range(mat.shape[1]):
        tmp=mat[song_1, i]-mat[song_2, i]
        tot+=tmp*tmp
    return tot


# In[322]:



x=len(add_song)
a=np.zeros((x, x))
for i in range(x):
  for j in range(x):
    a[i][j]= distance(add_song[i], add_song[j])


# In[323]:


import sys
history=[add_song[0]]

def min(a):
  global history
  minimum = float(sys.float_info.max)
  mini=minimum
  ret = a
  if len(history) == len(add_song):
    return None
  for i in add_song:
    tmp = distance(a, i)
    if ( a != i and  not(i in history) and float(tmp)< mini):
      mini = tmp
      ret = i
  history.append(ret)
  if(ret != a):
    return min(ret)
  else: 
    return None


(min(add_song[0]))


# In[ ]:


np.savetext('Euclidean.txt', a, fmt='%.15f')#Euclidean.txt
np.savetext('songList.txt', add_song, fmt='%s')#songList.txt

