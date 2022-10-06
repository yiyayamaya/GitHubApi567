import requests
import json


def get(user_id):
    url = "https://api.github.com/users/" + user_id + "/repos"
    # handle network issue
    try:
        response = requests.get(url)
    except requests.ConnectionError:
        return "network not working"
    x = response.text
    repos = json.loads(x)
    # handle userId not existing
    if type(repos) is dict:
        return "can not find user"
    res=""
    for repo in repos:
        #res+="Repo: "+ repo["name"]+" Number of commits: "
        print("Repo: "+ repo["name"]+" Number of commits: ",end="")
        repo_url = "https://api.github.com/repos/" + user_id + "/" + repo["name"] + "/commits"
        x = json.loads(requests.get(repo_url).text)
        #res+=str(len(x))+"\n"
        print(str(len(x))+"\n")
    return res


if __name__ == '__main__':
    print(get("lujinghan"))
    print(get("yiyayamaya"))
    print(get("yiyayamaya123123"))
