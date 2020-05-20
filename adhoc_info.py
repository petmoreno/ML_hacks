d=(df.count()/len(df))*100
df_info=pd.DataFrame(data=d, columns=['% non-null values'])
df_info['non-null values']=df.count()
df_info['dtype']=df.dtypes
df_info
