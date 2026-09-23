import csv

APP="Instagram"

minutes=[]

with open("digital_behaviour.csv","r",encoding="utf-8") as f:
    reader=csv.DictReader(f)
    for row in reader:
        minutes.append(int(row["Instagram_Minutes"]))
minutes=minutes[0:7]
#total=sum(int(i) for i in minutes)
total=sum(minutes)
average=total/len(minutes)
highest=max(minutes)
lowest=min(minutes)
c=0
for i in minutes:
    if(i>average):
       c=c+1

print(f"App Name : {APP} \nTotal minutes : {total}\nAverage minutes :{average}\nHighest day :{highest}\nLowest day :{lowest}\nDays Above Average :{c}")