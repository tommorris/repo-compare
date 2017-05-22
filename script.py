import requests
import iso8601

repos = [
    "Nexmo/nexmo-python",
    "Nexmo/nexmo-java",
    "Nexmo/nexmo-ruby",
    "Nexmo/nexmo-cli",
    "Nexmo/nexmo-php",
    "Nexmo/nexmo-node",
    "Nexmo/nexmo-dotnet"
]

for repo in repos:
    last_commit = requests.get("https://api.github.com/repos/" + repo +
                               "/commits?per_page=1")
    last_commit_date = last_commit.json()[0]['commit']['author']['date']
    last_commit_dt = iso8601.parse_date(last_commit_date)

    last_tag = requests.get("https://api.github.com/repos/" + repo +
                            "/tags?per_page=1")
    last_tag_commit = last_tag.json()[0]['commit']['url']

    last_tag_commit_data = requests.get(last_tag_commit)
    last_tag_commit_date = last_tag_commit_data.json()['commit']['author'][
        'date']
    last_tag_commit_dt = iso8601.parse_date(last_tag_commit_date)

    days_diff = (last_commit_dt - last_tag_commit_dt).days

    if days_diff > 14:
        print repo + " -- " + str(
            days_diff) + " days between master and last release"
