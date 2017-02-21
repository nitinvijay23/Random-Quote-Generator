
# coding: utf-8

# # Random Quote Generator
# 
# Just Enter any Cateogry and get any random quote of that category
# 
# Category can be: movies or famous
# 
# Note: Only two categories are allowed.

# In[6]:

#These code snippets use an open-source library. http://unirest.io/python
import requests
url = "https://andruxnet-random-famous-quotes.p.mashape.com/"
print("Enter the category movies or famous")
cat = input()
data = {'cat': cat}
headers={
   "X-Mashape-Key": "your API Key",
   "Content-Type": "application/x-www-form-urlencoded",
   "Accept": "application/json"
 }
r = requests.post(url, data=data, headers = headers)
results = r.json()
print("Quote: {}".format(results["quote"]))
print("Author: {}".format(results["author"]))


# In[5]:

get_ipython().system('jupyter nbconvert --to script Random_Quote_Generator.ipynb')


# In[ ]:



