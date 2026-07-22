import json
from keywords import keywords

with open("reed_all_jobs.json", "r") as jsonfile:
    job_list = json.load(jsonfile)

key = "jobDescription"
description = job_list[0][key]
keywords = "SQL"

if keywords.lower() in description.lower():
    print(f"Found: {keywords}")
