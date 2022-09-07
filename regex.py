import re

with open("names.txt") as text: #names.txt should be in your project folder for your homework
    data = text.readlines()
    
for item in data:
    items = re.compile('([\w]+)@([a-z]+)(.com|.org|.gov|.uk|.co)')
    item = items.findall(data[0])

for i in range(11):
    item = items.findall(data[i])
    print(item[0][0]+ '@' +item[0][1]+ item[0][2])

job_finder = re.compile('([\w]+)([A-Z][a-z]+)|([A-Z][A-Z]+)')

job_finder2 = re.compile('([A-Z][a-z]+) ([A-Z][a-z]+) ([A-Z][a-z]+) ([A-Z][a-z]+)')

jobs = job_finder.findall(str(data))

jobs2 = job_finder2.findall(str(data))

for job in jobs:
    print(job[1]+job[2])
    
for job2 in jobs2:
    print(job2[0]+ " " +job2[1]+ " " +job2[2]+ " " +job2[3])
# Generate the desired output. Hint: use an asterisk * in your re.compile()

