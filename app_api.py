import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"


headers = {"Accept": "application/vnd.github.v4+json"}
r = requests.get(url, headers=headers)
print(f"status code: {r.status_code}")

# store api response in a variable
response_dict = r.json()


# process results
print(response_dict.keys())

print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories.
repo_dicts = response_dict["items"]
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
