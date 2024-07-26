#In this program, we are simply trying to fetch the list of all finalist participants of Techgig Code Gladiators from https://www.techgig.com/codegladiators

import requests
from bs4 import BeautifulSoup
import csv


"https://www.techgig.com/codegladiators/event-result?round=semifinal&type=coding&page=1"
final_list=[]
for i in range(1,16):
    # Fetch the HTML content
    url = "https://www.techgig.com/codegladiators/event-result?round=semifinal&type=coding&page="+str(i)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")

    # Extract information based on a class name
    specific_info = soup.find_all(class_="table2 code-candidate-list")
    print(specific_info,type(specific_info),len(specific_info))
    for info in specific_info:
        tmp=[]
        for line in info.text.splitlines():
            if line.strip()!='' and line.strip()!='No record found':
                tmp.append(line.strip())
            else:
                if len(tmp)!=0:
                    if len(tmp)==2:
                        tmp.append('')
                    final_list.append(tmp)
                    print(tmp)
                tmp=[]
print("---------------------------------------------------------")
print(final_list)
csv_file = 'output.csv'
with open(csv_file, 'w',encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    
    # Write the data
    writer.writerows(final_list)
print("---------------------------------------------------------")
    