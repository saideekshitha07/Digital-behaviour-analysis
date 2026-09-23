import csv
import numpy as np
insta_minutes=[]
study_minutes=[]
with open (
    "./digital_behaviour.csv",
    "r",
    encoding="utf-8"
) as f:
    reader=csv.DictReader(f)
    for row in reader:
        insta_minutes.append(int(row["Instagram_Minutes"]))
        study_minutes.append(int(row["Study_Minutes"]))
insta_minutes=insta_minutes[:7]
study_minutes=study_minutes[:7]
instagram=np.array(insta_minutes)
study=np.array(study_minutes)
print(instagram,study)
#help(np)
#total=np.sum(instagram) - standard operation
#inplace operation : 
total=instagram.sum()
average=instagram.mean()
maximum=instagram.max()
minimum=instagram.min()
days=len(instagram)
print(f"Total Insta {total}, Average Insta {average}, Maximum Insta {maximum},Minimum Insta {minimum},Days Insta {days}")
print(instagram[::2])
insta_hours=instagram/60
insta_hours=insta_hours.round(2)
#insta_hours=np.round(insta_hours,2)
print(insta_hours)
# ----- --------------------- for study 
total1=study.sum()
average1=study.mean()
maximum1=study.max()
minimum1=study.min()
days1=len(study)
print(f"Total Study {total1}, Average Study {average1}, Maximum Study {maximum1},Minimum Study {minimum1},Days Study {days1}")
print(study[::2])
study_hours=study/60
study_hours=study_hours.round(2)
print(study_hours)

differnce=study - instagram
"""
for val in difference :
    if val>100 :
        greater.append(val)
List comprehension Technique
"""
# greater = [val for val in difference if val>100]
#using numpy fast calculation greater contains boolean values 

boolean_i=instagram>100

#greater = [bool_ for bool_ in boolean if bool_]
#greater= filter(lambda bool_ : bool_,boolean_i)

greater_i=instagram[instagram>100] #[] is iterator if true it takes the value else it forgets 
#[] remembers the index . hence we use instagram[] so that we get elements 

"""count= (instagram>100)
   count=count.sum()"""
count=(instagram>100).sum()

greater_avg_i=instagram[instagram>average]
#boolean indexing method - one of the dunder methods
