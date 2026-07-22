import requests
import json
import time


# api call for job desc

# url = "https://jsonplaceholder.typicode.com/posts/1"

# response = requests.get(url)

# print("Status code:", response.status_code)
# print("Content-type:", response.headers.get("Content-type"))

# data = response.json()  # Parse JSON to dict

# print("Post title:", data["title"])

KEY = "5649c6dc-3a29-4d60-997f-87fea0e4d66e"

JOB_URL = "https://www.reed.co.uk/api/1.0/search"
DETAIL_URL = "https://www.reed.co.uk/api/1.0/jobs/{}"


def get_jobs(keywords, results=20):
    """First part, get the job IDs from the job search api"""

    # param list - https://www.reed.co.uk/developers/Jobseeker
    payload = {"keywords": keywords, "resultsToTake": results}

    # api takes the key as username and blank password
    response = requests.get(JOB_URL, params=payload, auth=(KEY, ""))

    # checks request is successful or not
    response.raise_for_status()
    # can also use response.status_code to check if needs be

    return response.json().get("results", [])


def get_detail(job_id):
    """part two, take the job_id from part one and get detail"""

    url = DETAIL_URL.format(job_id)
    response = requests.get(url, auth=(KEY, ""))
    response.raise_for_status()

    return response.json()


def main():
    """Put the parts together to pull the detail and tie it to the job"""
    start_time = time.time()

    keywords = input("Enter job keywords e.g. 'Data engineer'")
    print(f"Searching for '{keywords}'...")

    job_results = get_jobs(keywords, results=100)
    print(f"Found {len(job_results)} job records...")

    # Now with the jobs create a list and fetch the detail for Searching
    all_jobs = []

    # 1-jobA, 2-jobB, 3-JobC etc...
    for i, job in enumerate(job_results):
        # for this loop set job id equal to the key(jobId) value for that job..
        # job comes back as json to dict so can use key values searching..
        job_id = job["jobId"]

        try:
            detail = get_detail(job_id)
            all_jobs.append(detail)
        except requests.exceptions.HTTPError as e:
            print(f"Failed to fetch {job_id}: {e}")

        # can be best practice to implement delay.. but didnt see any info in the docs
        time.sleep(0.2)

    with open("reed_all_jobs.json", "w") as f:
        json.dump(all_jobs, f, indent=2)

    print("Saved all job records to file...")
    print("took --- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
