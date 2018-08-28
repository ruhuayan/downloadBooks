
'''
import csv
from datetime import date
import time
from random import randint
list = [i for i in range(1, 105)]

with open('names.csv', 'w') as csvfile:
    fieldnames = ["id",'name', 'salary', "Date", "age"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in list:
        writer.writerow({"id": i, 'name': 'name -%d'%i, 'salary': randint(100, 1000), "Date": date.today()})


with open('outfile.csv', 'w') as outfile:
    writer = csv.DictWriter(outfile, ['name', 'salary', "time"])
    writer.writeheader()
    with open('names.csv') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            print(row['name'], row['salary'])
            writer.writerow({'name':row['name'], 'salary': int(row['salary'])*3, "time": time.time()})
            
'''   
import csv
from datetime import date
import urllib2
from bs4 import BeautifulSoup
list = [i for i in range(1, 10)]
product = raw_input("what are you looking for: ")
page = urllib2.urlopen("https://www.amazon.ca/s/field-keywords="+product)
soup = BeautifulSoup(page, "lxml")
print(soup.prettify())

#items = soup.find_all("div", {"class": "s-item-container"})
specs = soup.find_all("h2", {"class": "s-access-title"})
prices = soup.find_all("span", {"class": "a-color-price"})

if len(specs)==0:
	exit()
	
with open(product+'.csv', 'w') as csvfile:
    fieldnames = ["id",'spec', 'price', "date"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for spec in specs:
		i = specs.index(spec)
		writer.writerow({"id": i, 'spec': spec.get_text(), 'price': prices[i].get_text() , "date": date.today() })				