#!/usr/bin/python3
"""Uses the GitHub API with Basic Authentication to display the user ID."""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(
        "https://api.github.com/user",
        auth=(sys.argv[1], sys.argv[2])
    )
    print(r.json().get("id"))
