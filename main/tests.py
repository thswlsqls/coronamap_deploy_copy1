from django.test import TestCase
from django.shortcuts import render, HttpResponse
from bs4 import BeautifulSoup
import requests
import json

# Create your tests here.

url = "https://www.seoul.go.kr/coronaV/coronaStatus.do"
url2 = "http://news.seoul.go.kr/welfare/archives/513105"
#headers = {
#  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
#}

req = requests.get(url)
req2 = requests.get(url)
r = req.text
r2 = req2.text

soup = BeautifulSoup(r, "html.parser")
soup2 = BeautifulSoup(r2, "html.parser")

# table = soup.find(id="patients")
table = soup.find("table", {"class":"tstyle05 tstyleP status-datatable datatable-multi-row"})
table2 = soup2.find("table", {"class":"route-datatable datatable-multi-row"})

#print(table);
#print(table2);

columns = [column.text for column in table.select("thead th")]
columns2 = [column.text for column in table2.select("thead th")]

# patients_rows = list(table.select("tbody tr"))[::-1]
patients_rows = list(table.select("tbody tr"))[::-1]
patients_rows2 = list(table2.select("tbody tr"))[::-1]

#print(patients_rows)
#print(patients_rows2)

# total_patients = int(len(patients_rows) / 2)
total_patients = int(len(patients_rows))
total_patients2 = int(len(patients_rows2))

# # print(total_patients)
#print(total_patients2)

patients = {}
patients2 = {}

patient_num = 0

for num, rows in enumerate(patients_rows):
    informations = [info.text for info in rows.select('td')]
    #print(informations)
    patients[patient_num] = {}
    patients[patient_num]['ID'] = informations[0]
    patients[patient_num]['Gender'] = '정보 없음'
    patients[patient_num]['Age'] = '정보 없음'
    patients[patient_num]['Region'] = informations[2]
    patients[patient_num]['Confirmed Date'] = informations[1]
    patients[patient_num]['Current Status'] = informations[5]
    patient_num += 1
#print(patients)

patient_num2 = 0
for num, rows in enumerate(patients_rows2):
    informations2 = [info.text for info in rows.select('td')]
    #print(informations2)
    #print(informations2[0].replace('\t','').replace('\n','').replace('\r','').replace('<tr>','').replace('<td class="tdl" colspan="5">','').replace('<p>','').replace('</p>','').replace('</td>','').replace('</tr>','').replace('<b>','/').replace('<span>','  ').replace('</b>','').replace('</span>','').replace('<span class=\'alignR\'>',''))
    pathinfo = informations2[0].replace('\t','').replace('\n','').replace('\r','').replace('<tr>','').replace('<td class="tdl" colspan="5">','').replace('<p>','').replace('</p>','').replace('</td>','').replace('</tr>','').replace('<b>',' / ').replace('<span>','  ').replace('</b>','').replace('</span>','').replace('<span class=\'alignR\'>','')
    patients2[patient_num2] = {}
    patients2[patient_num2]["ID"] = informations2[1]
    patients2[patient_num2]["Gender"] = '정보없음'
    patients2[patient_num2]["Age"] = '정보없음'
    patients2[patient_num2]["Region"] = informations2[4]
    patients2[patient_num2]["Confirmed Date"] = informations2[3]
    patients2[patient_num2]["Current Status"] = informations2[5]
    patients2[patient_num2]["paths"] = informations2[0]
    patient_num2 += 1
print(patients2)

values = []
infected = soup.select_one('#move-cont1 > div.status-confirm.chart-wrap.display-block > div > p > span').get_text()
cured = soup.select_one('#container > div.layout-inner.layout-sub > div > div.status > div.status-seoul > div.cell-group.first-cell > div.cell.cell5 > div.num.num8 > p.counter').get_text()

values.append(infected)
values.append(cured)
#print(values)

test = soup.select('#DataTables_Table_0 > tbody')
#print(table2)

#patient > td.name
#patient > td.
#patient > td:nth-child(3)
#DataTables_Table_0

