import json
jsonfile=open('C:\cowin.json','r')
jsondata=jsonfile.read()
obj=json.loads(jsondata)
list=obj['centers']
print(len(list))
count=0
count_1=0
count_2=0
for i in range(len(list)):
    print(list[i]['name'])
    count=count+1
print(count)
lis=obj['centers']
for j in range(len(lis)):
    sessiner=lis[j]['sessions']
    for x in range(len(sessiner)):
        if(sessiner[x]['min_age_limit']>=45):
            count_1=count_1+1
        if(sessiner[x]['min_age_limit']>=18):
            count_2=count_2+1
print(count_1)
print(count_2)

