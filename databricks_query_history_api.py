import requests

db_token = ""
db_workspace = ""
table_name_to_find = ""
headers = {"Authorization": f"Bearer {db_token}", "Content-Type": "application/json"}
data = """{
        "max_results": 1000, 
        "filter_by": {
            "query_start_time_range": 
            {
                "end_time_ms": 1665853775000,
                "start_time_ms": 1595357086200
            }       
        }
}"""
url = f"https://{db_workspace}/api/2.0/sql/history/queries"
request = requests.get(url, headers=headers,data=data)
users = []

while request:
    for e in request.json()["res"]:
        if e["query_text"].find(table_name_to_find)>0:
            users.append(e["user_name"])
    if request.json()["has_next_page"]:
        ntoken = request.json()["next_page_token"]
        request = request.get(url+"?next_page_token="+ntoken, headers=headers,data=data)
    else:
        request = None

for u in list(dict.fromkeys(users)):
    print(u)