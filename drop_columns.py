#Line to delete columns by its position number
df_source=df_source.drop(df_source.columns[i],axis=1)

#Line to delete columns by its name
df_source=df_source.drop('column_name',axis=1)
