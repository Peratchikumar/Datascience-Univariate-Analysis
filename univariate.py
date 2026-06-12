class univariate():
    def QualitativeQuantitative(dataset): #Function - is a procedure
        Qualitative=[]
        Quantitative=[]
        
        for columnName in dataset.columns: #Print the column name in the dataset - For Loop
            print(columnName)
            if(dataset[columnName].dtype=='object'):
                print("Qualitative")
                Qualitative.append(columnName)
            else:
                print("Quantitative")
                Quantitative.append(columnName)
        return Qualitative, Quantitative   


    def freqTable(ColumnName,dataset):
        freqTable=pd.DataFrame(columns=["Unique_Values","Frequency","Relative Frequency", "cumsum"])
        freqTable["Unique_Values"]=dataset[ColumnName].value_counts().index 
        freqTable["Frequency"]=dataset[ColumnName].value_counts().values
        freqTable["Relative Frequency"]=(freqTable["Frequency"]/103)
        freqTable["cumsum"]=freqTable["Relative Frequency"].cumsum()
        return freqTable


   def Univariate(dataset,Quantitative):
    descriptive=pd.DataFrame(index=["Mean", "Median", "Mode", "Q1:25%", "Q2:50%", "Q3:75%", "99%", "Q4:100%", "IQR", "1.5rule", "Lesser", "Greater", "Min", "Max", "kurtosis", "skew", "var", "std"],columns=Quantitative) #Index
        for ColumnName in Quantitative:
            descriptive[ColumnName]["Mean"]=dataset[ColumnName].mean()
            descriptive[ColumnName]["Median"]=dataset[ColumnName].median()
            descriptive[ColumnName]["Mode"]=dataset[ColumnName].mode()[0]
            descriptive[ColumnName]["Q1:25%"]=dataset.describe()[ColumnName]["25%"]
            descriptive[ColumnName]["Q2:50%"]=dataset.describe()[ColumnName]["50%"]
            descriptive[ColumnName]["Q3:75%"]=dataset.describe()[ColumnName]["75%"]
            descriptive[ColumnName]["99%"]=np.percentile(dataset[ColumnName],99)
            descriptive[ColumnName]["Q4:100%"]=dataset.describe()[ColumnName]["max"]
            descriptive[ColumnName]["IQR"]=descriptive[ColumnName]["Q3:75%"]-descriptive[ColumnName]["Q1:25%"]
            descriptive[ColumnName]["1.5rule"]=1.5*descriptive[ColumnName]["IQR"]
            descriptive[ColumnName]["Lesser"]=descriptive[ColumnName]["Q1:25%"]-descriptive[ColumnName]["1.5rule"]
            descriptive[ColumnName]["Greater"]=descriptive[ColumnName]["Q3:75%"]+descriptive[ColumnName]["1.5rule"]
            descriptive[ColumnName]["Min"]=dataset[ColumnName].min()
            descriptive[ColumnName]["Max"]=dataset[ColumnName].max()
            descriptive[ColumnName]["kurtosis"]=dataset[ColumnName].kurtosis()
            descriptive[ColumnName]["skew"]=dataset[ColumnName].skew()
            descriptive[ColumnName]["var"]=dataset[ColumnName].var()
            descriptive[ColumnName]["std"]=dataset[ColumnName].std()
            
        return descriptive  