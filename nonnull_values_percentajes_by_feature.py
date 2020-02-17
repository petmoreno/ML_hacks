##This line is a interpretation of the info() altough it give us the percentaje of non-null values per feaure in a dataframe df_source
(df_source.count()/len(df_source))*100

#The following line counts how many null values has the data set per feature
df_source.isnull().sum()
