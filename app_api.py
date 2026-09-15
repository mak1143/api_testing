import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"


headers = {"Accept": "application/vnd.github.v4+json"}
r = requests.get(url, headers=headers)
print(f"status code: {r.status_code}")

# store api response in a variable
response_dict = r.json()


# process results
print(response_dict.keys())
