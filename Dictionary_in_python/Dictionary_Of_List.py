import pandas as pd
Student_Info = {
    "Name": ["Alice", "David", "Bob", "Glory", "Francisca"],
    "Age" : [20, 21, 19, 22, 20],
    "School" : ["MIT", "Stanford", "Harvard", "Yale", "Princeton"],
    "Gender" : ["F", "M", "M", "F", "F"]
}   
print(Student_Info)
df = pd.DataFrame(Student_Info) 
print(df)    

