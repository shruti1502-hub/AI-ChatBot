#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install nltk 


# In[2]:


pip install newspaper3k


# # Newspaper
# Newspaper is a Python module used for extracting and parsing newspaper articles. Newspaper use advance algorithms with web scrapping to extract all the useful text from a website. It works amazingly well on online newspapers websites. 

# # Count Vectorizer
# The CountVectorizer provides a simple way to both tokenize a collection of text documents and build a vocabulary of known words, but also to encode new documents using that vocabulary.
# Tokenization of text means- Tokenization is essentially splitting a phrase, sentence, paragraph, or an entire text document into smaller units, such as individual words or terms. Each of these smaller units are called tokens

# In[3]:


#import the libraries
from newspaper import Article 
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# # Punkt Package-
# Punkt Sentence Tokenizer. This tokenizer divides a text into a list of sentences, by using an unsupervised algorithm to build a model for abbreviation words, collocations, and words that start sentences. It must be trained on a large collection of plaintext in the target language before it can be used.

# In[4]:


#Download the punkt package
nltk.download('punkt',quiet=True)


# In[5]:


#Get the article
article = Article('https://www.mayoclinic.org/diseases-conditions/chronic-kidney-disease/symptoms-causes/syc-20354521')
article.download()
article.parse()
article.nlp() #apply nlp on the article
corpus = article.text


# In[6]:


#print the articles text
print(corpus)


# In[7]:


#tokenization
text = corpus
sentence_list = nltk.sent_tokenize(text) #list of sentences
#sent_tokenize is used to divide a paragraph into sentences i.e. to tokenize a given paragraph


# In[8]:


#print the list of sentences
print(sentence_list)


# In[9]:


#A function to return a random greeting response to a user's greeting
def greeting_response(text):
    text = text.lower()
    
    #Bots greeting response
    bot_greetings = ['howdy','hi', 'hey','hello', 'hola']
    
    #User's greeting response
    user_greetings = ['hi','hey','hello','hola','greetings','wassup']
    
    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)


# In[10]:


def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))
    
    x=list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                #swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
                
    return list_index          


# In[11]:


#Create the bots response
def bot_response(user_input):
    user_input = user_input.lower() #returns lowercased string from given string
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0
    
    
    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response+' '+sentence_list[index[i]]
            response_flag = 1
            j = j+1
        if j > 2:
            break
            
    if response_flag == 0:
        bot_response = bot_response+' '+"I apologize,I don't understand."
        
    sentence_list.remove(user_input)
    
    return bot_response
    
    
    
    


# In[ ]:


#Start the chat
print('Doc Bot: I am Doctor Bot or Doc Bot for short. I will answer your queries about Chronic Kidney Disease. If you want to exit, type bye.')

exit_list=['exit','see you later','bye','quit','break']

while(True):
    user_input = input()
    if user_input.lower() in exit_list:
        print('Doc Bot: Chat with you later !')
        break
    else:
        if greeting_response(user_input) != None:
            print('Doc Bot: '+greeting_response(user_input))
        else:
            print('Doc Bot: '+bot_response(user_input))
        


# In[ ]:




