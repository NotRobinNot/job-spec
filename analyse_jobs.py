import json
from keywords import keywords

with open("reed_all_jobs.json", "r") as jsonfile:
    job_list = json.load(jsonfile)

key = "jobDescription"

i = 0
count = 0

for job in job_list:
    description = job[key]
    keyterm = keywords["Looker"]

    for term in keyterm:
        if term.lower() in description.lower():
            count += 1

    i += 1

print(
    f"Out of {len(job_list)} jobs, {count} of them contained reference to '{keyterm}'"
)
