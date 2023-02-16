import json



# Opening JSON file
f = open('Client_ID.json')

# returns JSON object as
# a dictionary
data = json.load(f)

key = "Client_Details"


for i,details in enumerate(data[key]):
    print (details["Name"])
    print (details["Api_Key"])
    print (details["Api_Secret"])
    	