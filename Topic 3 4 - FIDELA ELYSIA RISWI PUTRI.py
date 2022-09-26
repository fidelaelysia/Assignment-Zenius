#!/usr/bin/env python
# coding: utf-8

# ##Topic 3 - Python Structure & Data Type Assignment
# 

# # Data Type Declaration

# 1. > Create an empty variable (Points : 5)

# In[1]:


variabel_kosong=""
print(variabel_kosong)


# 2. > Create a variable containing your name (Points : 5)

# In[2]:


Nama_saya="Fidela Elysia Riswi Putri"
print(Nama_saya)


# 3. > Create a list of 5 items you can find in the classroom (Points : 5)

# In[4]:


item_kelas=['meja','kursi','papan tulis','mading','jam']
print(item_kelas)


# 4. > Create a dictionary containing 2 keys and value (Points : 5)

# In[8]:


dictionary={
    "makanan":["lunpia","gudeg"],
    "kota":["Semarang","Jogja"]
}
print(dictionary)


# # Basic Data Operation

# You sold 20 pieces of electronics at the price of 12000. The customer gets a total discount of 10%.
# 
# Below are those variables:
# 
# 1.   price=12000
# 2.   quantity_sold=20
# 3.   discount=10%
# 
# 
# Using Python code, write the code the find the total money that the customer to pay. (Points : 15)

# In[16]:


price=12000
quantity_sold=20
discount=10/100

Total=(price*quantity_sold)*(1-discount)
print('Jumlah uang yang harus dibayar customer adalah '+str(Total)+ ' rupiah')


# # List Data Operation

# 5. > Follow the instructions in the code blocks
# 
# 
# 
# 

# In[17]:


# Create list of countries in the world (total 7 countries) (Points : 5)

countries=['Indonesia','Malaysia','India','Vietnam','Jepang','Thailand','Singapura']
print(countries)


# In[18]:


# Get 4 countries from the first index of the list (Points : 5)

print(countries[:4])


# In[19]:


# Append new country to the list (Points : 5)

new_country='Laos'

countries.append(new_country)
print(countries)


# In[20]:


# Drop one country from the list (Points : 5)

countries.remove('India')
print(countries)


# In[21]:


# Get country in the last index (Points : 5)

print(countries[-1])


# # Dictionary Data Operation

# 6. >  Follow the instructions below
# 
# 
# 
# 

# In[60]:


# Given the dictionary below

customer={
    "name":['Dio','Eka','Wayu','Riki'],
    "age":[20,19,24,39],
    "gender":[1,0,0,1],
    "membership":['Platinum','Gold','Silver','Silver']
}


# In[61]:


# Print all keys in customer (Points : 5)

customer.keys()


# In[62]:


# Print all customer names (Points : 5)

customer["name"]


# In[63]:


# Print the first customer name (Points : 5)

customer["name"][0]


# In[64]:


# Drop "age" key from the dictionary (Points : 5)

del customer["age"]
#"age" key sudah terhapus

print(customer)


# In[66]:


# Replace customer gender list value (Points : 20)
# gender 1 => Male
# gender 0 => Female 


customer["gender"]=["Male","Female","Female","Male"]
                     
print(customer)


# In[ ]:




