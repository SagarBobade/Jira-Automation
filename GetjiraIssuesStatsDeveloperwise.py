#python countOfBugsOfParticularDeveloper.py 2020-06-01 2021-12-02

from array import *
import requests
from requests.auth import HTTPBasicAuth
import json
import sys


startDate = str(sys.argv[1])
endDate = str(sys.argv[2])


thisdict = {
  "User1": "57058:31a58364-e9ad-459b-a583-74e02137b84d",
  "User2": "62f0d9a6a4c09006aa0bde0",
  "User3": "6112d7ed047850068545813",
  "User4": "55058:37a9d058-ad75-4ef5-aae9-a7c2c23fd7f7",
  "User5": "6112d7f332636006a37f850",
  "User6": "6113a6d062f4c00694f451a",
  "User7": "7021:58502ba5-003a-4cc2-ae39-b83a3752fb6d",
  "User8": "6012d8020445000695b9e12",
  "User9": "5f843a31c682d0029085f92",
  "User10": "6dd4e747536500070b50c6f",
  "User11": "56110597bc26f6fb6255616",
  "User12": "6112d7ea41ea5006a545037"
}

for y,z in thisdict.items():
  print("----------")
  print(y)

  totalOpen=0
  totalForRetesting=0
  totalClosed=0

  arr=[["High","Assigned"],["High","Re-test"],["High","Closed"],["High","Feedback"],["Medium","Assigned"],["Medium","Re-test"],["Medium","Closed"],["Medium","Feedback"],["Low","Assigned"],["Low","Re-test"],["Low","Closed"],["Low","Feedback"]]

  for x in arr:

    url = "https://phynart.atlassian.net/rest/api/3/search"
    auth = HTTPBasicAuth("sagaxxxxx@.com", "tg9z4Zx8Hj5MDacJB8MaB490")
    headers = {
       "Accept": "application/json"
    }

    query = {
    "jql": "project = BUGS AND issuetype = Bug AND status = "+str(x[1])+" AND priority = "+str(x[0])+" AND created >= "+startDate+" AND created <= "+endDate+" AND assignee in ("+z+") ORDER BY created DESC"
    }

    response = requests.request(
       "GET",
       url,
       headers=headers,
       params=query,
       auth=auth
    )
#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

    data=response.json()
    print(str(x)+":- "+str(data['total']))

    if str(x[1])=="Assigned":
      totalOpen+=data['total']
    if str(x[1])=="Re-test":
      totalForRetesting+=data['total']
    if str(x[1])=="Closed":
      totalClosed+=data['total']

  print("")
  print("Total Open:- "+ str(totalOpen))
  print("Total for re-testing:- "+ str(totalForRetesting))
  print("Total Closed:- "+ str(totalClosed))
