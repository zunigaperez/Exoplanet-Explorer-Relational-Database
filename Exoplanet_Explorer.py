#!/usr/bin/env python
# coding: utf-8

# # **Stage 1: Cleaning and Preprocessing Planet Data**

# In[1]:


# This code was created by me using lecture videos from the Data Science course
#and Database and Advanced Data Techniques and previous projects in Data Science listed under references
## my code starts here

#load libraries
import pandas as pd
import numpy as np


# ## **Planet Column Data**

# In[2]:


#load full column data file
column_data=pd.read_csv(r"C:\Users\maybe\OneDrive\Desktop\Databases and Advanced Techniques\planets_column_data.csv")

#check first rows to verify it loaded correctly
print(column_data.head(1))


# In[3]:


#### Find critical columns in column data
critical_column_data=['pl_name', 'hostname', 'pl_letter', 'sy_snum', 'sy_pnum', 
                         'sy_mnum','discoverymethod', 'disc_year', 'disc_facility', 
                         'pl_orbper','pl_orbsmax', 'pl_angsep' , 'pl_rade', 'pl_bmasse', 
                        'pl_dens', 'pl_orbeccen', 'pl_insol', 'pl_eqt', 'pl_orbincl', 'pl_tranmid', 
                        'pl_trandep', 'pl_trandur', 'pl_rvamp', 'st_spectype', 'st_rad', 'st_mass', 
                        'st_met', 'st_lum', 'st_logg', 'st_age', 'st_dens', 'st_vsin', 'st_rotp', 
                        'st_radv', 'ra', 'dec', 'sy_dist']

new_column_data = column_data[column_data['abbrev_name'].isin(critical_column_data)]

#new_column_data = column_data[critical_column_data]
print(new_column_data)


# In[4]:


#redoing the internal index column, 0 to 37
new_column_data=new_column_data.reset_index(drop=True)
print(new_column_data)


# In[5]:


#redoing the planet's column id, 1 to length of column, 1 to 38
new_column_data['column_id']=range(1, len(new_column_data) + 1)
print(new_column_data)


# In[6]:


#data types and null values for column data
new_column_data.info()


# In[7]:


#check for missing values or Na in each column, 
#True for missing, false for NOT missing
row_missing = new_column_data.isna()

#adds the number of rows in each column with missing values
row_total=row_missing.sum()
print(row_total)


# In[8]:


#store cleaned data in new CSV file
cleaned_column_data = new_column_data.copy()
cleaned_column_data.to_csv('cleaned_column_data.csv', index=False)
print(cleaned_column_data)


# ## **Planet Data**

# In[9]:


#load full planet data file
planet_data=pd.read_csv(r"C:\Users\maybe\OneDrive\Desktop\Databases and Advanced Techniques\full_planets_data.csv")


#correct discovery year to an integer, otherwise it will turn to float numbers
planet_data['disc_year']=planet_data['disc_year'].astype('Int64')

#check first rows to verify it loaded correctly
print(planet_data.head(1))


# In[10]:


### data types and null values for planet data
planet_data.info()


# In[11]:


#### Find critical columns
critical_planet_columns=['pl_name', 'hostname', 'pl_letter', 'sy_snum', 'sy_pnum', 
                         'sy_mnum','discoverymethod', 'disc_year', 'disc_facility', 
                         'pl_orbper','pl_orbsmax', 'pl_angsep' , 'pl_rade', 'pl_bmasse', 
                        'pl_dens', 'pl_orbeccen', 'pl_insol', 'pl_eqt', 'pl_orbincl', 'pl_tranmid', 
                        'pl_trandep', 'pl_trandur', 'pl_rvamp', 'st_spectype', 'st_rad', 'st_mass', 
                        'st_met', 'st_lum', 'st_logg', 'st_age', 'st_dens', 'st_vsin', 'st_rotp', 
                        'st_radv', 'ra', 'dec', 'sy_dist']

new_planet_data = planet_data[critical_planet_columns]
print(new_planet_data)


# In[12]:


#check for missing values or Na in each column, 
#True for missing, false for NOT missing
planet_missing = new_planet_data.isna()

#adds the number of rows in each column with missing values
row_total=planet_missing.sum()
print(row_total)


# In[13]:


#we need to drop all planets with missing values under a column, starting with pl_orbper
required_columns = ['disc_year','pl_orbper','pl_orbsmax', 'pl_angsep' , 'pl_rade', 'pl_bmasse', 
                        'pl_dens', 'pl_orbeccen', 'pl_insol', 'pl_eqt', 'pl_orbincl', 'pl_tranmid', 
                        'pl_trandep', 'pl_trandur', 'pl_rvamp', 'st_spectype', 'st_rad', 'st_mass', 
                        'st_met', 'st_lum', 'st_logg', 'st_age', 'st_dens', 'st_vsin', 'st_rotp', 
                        'st_radv', 'ra', 'dec', 'sy_dist']

new_planet_data.dropna(subset= required_columns, inplace=True)

#calculating columns with missing values again after dropping planets missing data
#all are zeros
missing_row_data=new_planet_data.isna()
total_rows=missing_row_data.sum()
print(total_rows)


# In[14]:


#calculating rows with missing values again after dropping planets missing data
#all are zeros
missing_column_data = new_planet_data.isna()
total_columns = missing_column_data.sum(axis=1)
#left with 162 entries, or 162 planets that have data in all the required columns
print(total_columns)


# In[15]:


#check to see if rows are full
print(new_planet_data)


# In[16]:


#redoing the internal index column, 0 to 70
new_planet_data=new_planet_data.reset_index(drop=True)
print(new_planet_data)


# In[17]:


#renaming the planet's id with new table, 1 to length of column, 1 to 71
#new_planet_data['planet_id']=range(1, len(new_planet_data) + 1)
print(new_planet_data)


# # **Stage 2. Model your data**

# In[18]:


## instead of having two datasets, make the columns names into their full names for more straight forward data handling

#rename columns here
new_planet_data = new_planet_data.rename(columns={'pl_name': 'Planet Name', 
                                                  'hostname': 'Host Name', 'pl_letter': 'Planet Letter', 
                                                  'sy_snum':'Number of Stars', 'sy_pnum':'Number of Planets',
                                                  'sy_mnum':'Number of Moons','discoverymethod':'Discovery Method', 
                                                  'disc_year':'Discovery Year','disc_facility': 'Discovery Facility', 
                                                  'pl_orbper':'Orbital Period [days]','pl_orbsmax':'Orbit Semi-Major Axis [au]',
                                                  'pl_angsep':'Angular Separation [mas]', 'pl_rade':'Planet Radius [Earth Radius]', 
                                                  'pl_bmasse':'Planet Mass or Mass*sin(i) [Earth Mass]','pl_dens':'Planet Density [g/cm**3]',
                                                  'pl_orbeccen': 'Eccentricity', 'pl_insol':'Insolation Flux [Earth Flux]',
                                                  'pl_eqt': 'Equilibrium Temperature [K]', 'pl_orbincl':'Inclination [deg]', 
                                                  'pl_tranmid':'Transit Midpoint [days]', 'pl_trandep':'Transit Depth [%]', 
                                                  'pl_trandur':'Transit Duration [hours]', 'pl_rvamp':'Radial Velocity Amplitude [m/s]', 
                                                  'st_spectype':'Spectral Type', 'st_rad':'Stellar Radius [Solar Radius]', 
                                                  'st_mass':'Stellar Mass [Solar mass]','st_met':'Stellar Metallicity [dex]', 
                                                  'st_lum':'Stellar Luminosity [log(Solar)]', 'st_logg':'Stellar Surface Gravity [log10(cm/s**2)]', 
                                                  'st_age':'Stellar Age [Gyr]', 'st_dens':'Stellar Density [g/cm**3]', 
                                                  'st_vsin':'Stellar Rotational Velocity [km/s]', 'st_rotp':'Stellar Rotational Period [days]',
                                                  'st_radv':'Systemic Radial Velocity [km/s]', 'ra':'RA [deg]', 'dec':'Dec [deg]', 
                                                  'sy_dist':'Distance [pc]'})
print(new_planet_data)


# In[19]:


## ************** foreign keys columns do not have 1 to n in sequential order ***********************

##add new columns to dataset, Star ID, Discovery ID, Solar System ID

#variables for number of columns and rows or current data

#number_columns = len(new_planet_data.columns)
#number_rows = len(new_planet_data)

## add new columns using data.insert(location, column name, rows) at the end of the data

#new_planet_data.insert(number_columns, 'Star ID', range(1,  number_rows + 1))

#new_planet_data.insert(number_columns + 1, 'System ID', range(1, number_rows + 1))

#new_planet_data.insert(number_columns + 2, 'Discovery ID', range(1, number_rows + 1))


print(new_planet_data)



# In[20]:


## Create a new dataset for Stars, Solar System, and Discoveries

#stars_data = new_planet_data['Star ID']
#print(stars_data)


#system_data =  new_planet_data['System ID']
#print(system_data)

#discoveries_data =  new_planet_data['Discovery ID']
#print(discoveries_data)


# In[21]:


## Add data to new data sets
#i need to find the columns, then i need add the columns to the new dataset

#Stars
#Spectral Type, Stellar Radius [Solar Radius], 
#Stellar Mass [Solar mass], Stellar Metallicity [dex], 
#Stellar Luminosity [log(Solar)], Stellar Surface Gravity [log10(cm/s**2)], 
#Stellar Age [Gyr], Stellar Density [g/cm**3], Stellar Rotational Velocity [km/s]
#Stellar Rotational Period [days], Systemic Radial Velocity [km/s],

#find columns and assign to variable
stars_columns=['Host Name','Spectral Type', 'Stellar Radius [Solar Radius]', 
'Stellar Mass [Solar mass]', 'Stellar Metallicity [dex]', 
'Stellar Luminosity [log(Solar)]', 'Stellar Surface Gravity [log10(cm/s**2)]', 
'Stellar Age [Gyr]', 'Stellar Density [g/cm**3]', 'Stellar Rotational Velocity [km/s]',
'Stellar Rotational Period [days]', 'Systemic Radial Velocity [km/s]']

#redefine stars_data using new varable with column names
stars_data = new_planet_data[stars_columns]

#set variable number of rows in dataset
#number_rows = len(stars_data)

## add new columns using data.insert(location, column name, rows) at the end of the data
#stars_data.insert(0, 'Star ID', range(1,  number_rows + 1))


print(stars_data)



# In[22]:


## there is a foreign key in stars data that links it to solar system 
# we need to add system_id at the end of the dataset like we need for exoplanets above in cell 19


number_rows = len(stars_data)

## add new columns using data.insert(location, column name, rows)
stars_data.insert(1, 'System ID', range(1, number_rows + 1))

print(stars_data)


# In[23]:


#System
#System ID, Host Name, Number of Stars, Number of Planets, RA [deg], 
#Dec [deg], Distance [pc]

system_columns=[ 'Host Name', 'Number of Stars', 'Number of Planets', 'RA [deg]', 
'Dec [deg]', 'Distance [pc]']

system_data = new_planet_data[system_columns]

#set variable number of rows in dataset
#number_rows = len(system_data)

## add new columns using data.insert(location, column name, rows) at the end of the data
#system_data.insert(0, 'System ID', range(1,  number_rows + 1))

print(system_data)


# In[24]:


#Discoveries
#Discovery ID, Discovery Method, Discovery Year, Discovery Facility

discovery_columns=['Host Name','Discovery Facility','Discovery Year','Discovery Method' ]

discoveries_data = new_planet_data[discovery_columns]

#set variable number of rows in dataset
#number_rows = len(discoveries_data)

## add new columns using data.insert(location, column name, rows) at the end of the data
#discoveries_data.insert(0, 'Discovery ID', range(1,  number_rows + 1))

print(discoveries_data)


# In[25]:


#Planet ID, Planet Name, Planet Letter, Number of Moons, Orbital Period [days], Orbit Semi-Major Axis [au], 
#Angular Separation [mas], Planet Radius [Earth Radius], Planet Mass or Mass*sin(i) [Earth Mass], Planet Density [g/cm**3]
#Eccentricity, Insolation Flux [Earth Flux], Equilibrium Temperature [K], Inclination [deg], Transit Midpoint [days]
#Transit Depth [%], Transit Duration [hours], Radial Velocity Amplitude [m/s], Star ID, System ID, Discovery ID  

planet_columns=['Host Name','Planet Name', 'Planet Letter', 'Number of Moons', 'Orbital Period [days]', 'Orbit Semi-Major Axis [au]', 
'Angular Separation [mas]', 'Planet Radius [Earth Radius]', 'Planet Mass or Mass*sin(i) [Earth Mass]', 'Planet Density [g/cm**3]',
'Eccentricity', 'Insolation Flux [Earth Flux]', 'Equilibrium Temperature [K]', 'Inclination [deg]', 'Transit Midpoint [days]',
'Transit Depth [%]', 'Transit Duration [hours]', 'Radial Velocity Amplitude [m/s]']

new_planet_data = new_planet_data[planet_columns]
print(new_planet_data)


# In[26]:


#check for missing values or Na in each column, 
#True for missing, false for NOT missing

missing_values = new_planet_data.isna()

#adds the number of rows in each column with missing values
row_total=missing_values.sum()
print(row_total)
print('________________________Exoplanets________________________')

missing_values = stars_data.isna()

#adds the number of rows in each column with missing values
row_total=missing_values.sum()
print(row_total)
print('________________________Stars_____________________________')


missing_values = system_data.isna()

row_total=missing_values.sum()
print(row_total)
print('______________________Solar System________________________')


missing_values = discoveries_data.isna()

row_total=missing_values.sum()
print(row_total)
print('______________________Discoveries_________________________')


# In[27]:


#count of entries before drop_duplicates
star_entries_before = len(stars_data)
print( 'stars before: ', star_entries_before)

stars_data.drop_duplicates(subset=['Spectral Type', 'Stellar Radius [Solar Radius]', 
'Stellar Mass [Solar mass]', 'Stellar Metallicity [dex]', 
'Stellar Luminosity [log(Solar)]', 'Stellar Surface Gravity [log10(cm/s**2)]', 
'Stellar Age [Gyr]', 'Stellar Density [g/cm**3]', 'Stellar Rotational Velocity [km/s]',
'Stellar Rotational Period [days]', 'Systemic Radial Velocity [km/s]'], inplace=True)

#after drops
star_entries_after = len(stars_data)
print( 'stars after:', star_entries_after)

#difference
star_entries_dropped = star_entries_before - star_entries_after
print("Duplicates Removed:", star_entries_dropped)





# In[28]:


#set variable number of rows in dataset
number_rows = len(stars_data)

## add new columns using data.insert(location, column name, rows) at the end of the data
stars_data.insert(0, 'Star ID', range(1,  number_rows + 1))

print(stars_data)


# In[29]:


#count of entries before drop_duplicates
system_entries_before = len(system_data)
print('system before: ', system_entries_before)

system_data.drop_duplicates(subset=['Host Name'], inplace=True)

#after
system_entries_after = len(system_data)
print( 'system after:', system_entries_after)

#difference
system_entries_dropped = system_entries_before - system_entries_after

print("Duplicates Removed:", system_entries_dropped)


# In[30]:


#set variable number of rows in dataset
number_rows = len(system_data)

## add new columns using data.insert(location, column name, rows) at the end of the data
system_data.insert(0, 'System ID', range(1,  number_rows + 1))

print(system_data)


# In[31]:


#count of entries before drop_duplicates
discovery_entries_before = len(discoveries_data)
print('discoveries before: ', discovery_entries_before)

discoveries_data.drop_duplicates(subset=[ 'Discovery Facility','Discovery Year','Discovery Method'], inplace=True)

#after
discovery_entries_after = len(discoveries_data)
print( 'discoveries after:', discovery_entries_after)

#difference
discovery_entries_dropped = discovery_entries_before - discovery_entries_after

print("Duplicates Removed:", discovery_entries_dropped)


# In[32]:


#set variable number of rows in dataset
number_rows = len(discoveries_data)

## add new columns using data.insert(location, column name, rows) at the end of the data
discoveries_data.insert(0, 'Discovery ID', range(1,  number_rows + 1))

print(discoveries_data)


# In[33]:


#count of entries before drop_duplicates
planet_entries_before = len(new_planet_data)
print('planets before: ', planet_entries_before)

new_planet_data.drop_duplicates(subset=['Planet Name'], inplace=True)

#after
planet_entries_after = len(new_planet_data)
print( 'planet after:', planet_entries_after)

#difference
planet_entries_dropped = planet_entries_before - planet_entries_after

print("Duplicates Removed:", planet_entries_dropped)


# In[34]:


#set variable number of rows in dataset
number_rows = len(new_planet_data)

new_planet_data.insert(0,'Planet ID', range(1, number_rows+1))

print(new_planet_data)


# In[35]:


#check for missing values or Na in each column, 
#True for missing, false for NOT missing

missing_values = new_planet_data.isna()

#adds the number of rows in each column with missing values
row_total=missing_values.sum()
print(row_total)
print('________________________Exoplanets________________________')

missing_values = stars_data.isna()

#adds the number of rows in each column with missing values
row_total=missing_values.sum()
print(row_total)
print('________________________Stars_____________________________')


missing_values = system_data.isna()

row_total=missing_values.sum()
print(row_total)
print('______________________Solar System________________________')


missing_values = discoveries_data.isna()

row_total=missing_values.sum()
print(row_total)
print('______________________Discoveries_________________________')


# In[36]:


print(new_planet_data)


# In[37]:


#merging or linking tables Stars with Systems before MySQL Lab, one to Many
# we can use map() and dict() because system_data is already normalized 
#and each row has a unique system or host name

#AUTOMATICALLY build the mapping dictionary from your stars DataFrame

#This pairs every star name with its MySQL-ready ID, no matter how many hundreds there are.

system_id_lookup = dict(zip(system_data['Host Name'], system_data['System ID']))

#Use .map() to fill the entire 'star_id' column at once

stars_data['System ID'] = stars_data['Host Name'].map(system_id_lookup)

#Clean up: Drop the text star_name column so MySQL stays perfectly relational

print(stars_data)


# In[38]:


#merging or linking tables Stars and Exoplanets before MySQL Lab
# creating junction data sets for junction data tables, Many to Many

junction = pd.merge(
    new_planet_data,
    stars_data,
    on = 'Host Name', 
    how= 'inner'
)

Star_Exoplanet_Orbits = junction[['Star ID','Planet ID']]

print(Star_Exoplanet_Orbits)


# In[39]:


#merging or linking tables Exoplanet and Discoveries before MySQL Lab
# creating junction data sets for junction data tables, Many to Many

junction = pd.merge(
    new_planet_data,
    discoveries_data,
    on = 'Host Name', 
    how= 'inner'
)

Exoplanet_Discoveries = junction[['Discovery ID','Planet ID']]


print(Exoplanet_Discoveries)


# In[40]:


#removing Host Name from all datasets where it's not needed for normalization

stars_data = stars_data.drop(columns=['Host Name'])
new_planet_data = new_planet_data.drop(columns=['Host Name'])
discoveries_data = discoveries_data.drop(columns=['Host Name'])


# In[41]:


#store cleaned datasets in new CSV files

#save stars data
cleaned_stars_data = stars_data.copy()
cleaned_stars_data.to_csv('cleaned_stars_data.csv', index=False)
print(cleaned_stars_data)

#save solar system data
cleaned_system_data = system_data.copy()
cleaned_system_data.to_csv('cleaned_system_data.csv', index=False)
print(cleaned_system_data)

#save discovery data
cleaned_discoveries_data = discoveries_data.copy()
cleaned_discoveries_data.to_csv('cleaned_discoveries_data.csv', index=False)
print(cleaned_discoveries_data)

#store cleaned exoplanet data
cleaned_planet_data = new_planet_data.copy()
cleaned_planet_data.to_csv('cleaned_planet_data.csv', index=False)
print(cleaned_planet_data)

#junction table Star_Exoplanet_Orbits
Star_Exoplanet_Orbits_cleaned = Star_Exoplanet_Orbits.copy()
Star_Exoplanet_Orbits_cleaned.to_csv('Star_Exoplanet_Orbits_cleaned.csv', index=False)
print(Star_Exoplanet_Orbits_cleaned)

#junction table Exoplanet Discoveries
Exoplanet_Discoveries_cleaned = Exoplanet_Discoveries.copy()
Exoplanet_Discoveries_cleaned.to_csv('Exoplanet_Discoveries_cleaned.csv', index=False)
print(Exoplanet_Discoveries_cleaned)



# In[ ]:


# my code ends here


# In[ ]:




