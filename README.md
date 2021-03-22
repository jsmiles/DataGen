# DataGen
Data Scientists sometimes need to generate random data. I thought it might be useful for someone to see how I generated a random data set. I needed one for a novel Machine Learning project. The [Faker](https://faker.readthedocs.io/en/master/index.html) module is very useful for this kind of work. A large number of the most interesting analytical problems are on the individual level but because of data privacy and commercial sensitivity this information is only infrequently available. 

# Componenets
There are three sections to my data generator: a setup bit at the top that imports the rependencies we require, the definition of some functions and finally the building of the dataframe that contains our new fake data. This file generates 100 records but if you change the *size* variable on line 79 of *datagen.py* you can create as many records as you like.  
