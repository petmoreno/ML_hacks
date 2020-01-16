## Function that apply the value_counts() to every features of the dataset
def df_values(df):
    for i in range(0, len(df.columns)):
        print("*****start of feature ", df.columns[i], "*************************")
        print (df.iloc[:,i].value_counts())
        print ("*****end of feature ", df.columns[i], "************************** \n")
