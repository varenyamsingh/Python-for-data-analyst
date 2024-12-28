import pandas as pd
'''data = {"Name":["Tony", "Peter", "Hulk"],
        "Age":[23, 25, 34],
        "Salary":[3000, 45000, 34000]}

df = pd.DataFrame(data)
print(df)
df["Bonus"] = (df["Salary"]/100)*20 # Here this will add a new column of bonus of 20% of their dalary will be shon
print(df)'''

# Groupby function 
'''gp = data.groupby("Department").agg({"EId":"Count"})
print(gp)'''




# For reading excel file or any other data file we will write:
# data = pd.read_csv("File name/path") #this will generate the same type of data as above we are getting
# data = pd.read_excel("file path/file name")




