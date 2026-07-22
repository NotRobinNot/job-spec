import json
from keywords import keywords

with open("reed_all_jobs.json", "r") as jsonfile:
    job_list = json.load(jsonfile)

key = "jobDescription"
description = job_list[0][key]
keyterm = keywords["BigQuery"]

for term in keyterm:
    if term.lower() in description.lower():
        print(f"Found: {term}")
    else:
        print(f"Not found: {term}")

print(f"---> \n {description}")
