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
                                