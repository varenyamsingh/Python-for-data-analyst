import pandas as pd
data = {"Name":["Tony", "Peter", "Hulk"],
        "Age":[23, 25, 34],
        "Salary":[3000, 45000, 34000]}

df = pd.DataFrame(data)
print(df)

# For reading excel file or any other data file we will write:
# data = pd.read_csv("File name/path") #this will generate the same type of data as above we are getting
# data = pd.read_excel("file path/file name")


