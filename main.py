import json
import requests

import secret_token

# TODO: setup API?


def get_followers(Github_id, max=5):
    """returns a list of followers from an id, max is max number returned"""
    url = "https://api.github.com/{0}/followers?client_id={1}&client_secret={2}".format(Github_id, secret_token.Client_ID, secret_token.Client_Secret)
    page = requests.get(url)
    page_content = page.text
    followers_json = json.loads(page_content)
    # assumes json from git is a dictionary type format on surface
    followers = followers_json["followers"]
    if len(followers) > max:
        followers = followers[0:max]
    return followers


def get_repositories(Github_id, max=3):
    """returns a list of repositories from an id, max is max number returned"""
    url = "https://api.github.com/{0}/repositories?client_id={1}&client_secret={2}".format(Github_id, secret_token.Client_ID, secret_token.Client_Secret)
    page = requests.get(url)
    page_content = page.text
    page_dict = json.loads(page_content)
    repos = page_dict["repositories"]
    if len(repos) > max:
        repos = repos[0:max]
    return repos


def get_stargazers(Github_id, repository, max=3):
    """returns a list of stargazers from a given github repository, max is max number returned"""
    url = "https://api.github.com/{0}/{1}/stargazers?client_id={2}&client_secret={3}".format(Github_id, repository, secret_token.Client_ID, secret_token.Client_Secret)
    page = requests.get(url)
    page_content = page.text
    page_dict = json.loads(page_content)
    stargazers = page_dict["stargazers"]
    if len(stargazers) > max:
        stargazers = stargazers[0:max]
    return stargazers


class Git_profile():
    def __init__(self, Github_id, followers):
        self.Github_id = Github_id
        self.followers = followers

    def make_json(self):
        json_dict = {"Github_id":self.Github_id}
        follower_list = []
        for follower in self.followers:
            try:
                follower_list = follower.make_json
            except AttributeError:
                follower_list = follower
        json_dict["followers"] = follower_list

class Git_repo():
    def __init__(self, Github_id, repo, stargazers):
        self.owner = Github_id
        self.name = repo
        self.stargazers = stargazers


def return_followers(Github_id, depth=3):
    """recursive function stacks git profile objects on followers"""
    if depth == 0:  # escape case
        followers = Git_profile(Github_id, get_followers(Github_id))
        return followers
    else:
        this_followers_followers = get_followers(Github_id)  # this namespace is confusing
        for index, follower_id in this_followers_followers:  # for each follower
            this_followers_followers[index] = return_followers(follower_id, depth-1)  # we run the function again, but not as deep
        followers = Git_profile(Github_id, this_followers_followers)  # that way we create the pyramid of followers from the bottom up
        return followers

    # Top_profile = Git_profile(Github_id, get_followers(Github_id))
    # adding_profile = Top_profile # we can't loose our reference to the top of the pyramid, so we'll have two
    # while index < depth:
    #     for index, follower in enumerate(Top_profile.followers):
    #         Top_profile.followers[index] = get_followers(follower)
    #     index += 1
    # return followers_json


def make_followers_json(Github_id):
    

def return_repos_and_stargazers(Github_id, depth=3):
    """returns json of a github users repos and the stargazers watching, 3 levels deep"""
    repos_and_stargazers = {}
    top_repos = get_repositories(Github_id)
    for repo in top_repos:
        top_stargazers = get_stargazers(Github_id, repo)
        for stargazer in top_stargazers:
            second_repos = get_repositories(stargazer)
        # TODO: reach the bottom level of the nested list and call the correct function on it

    repos_and_stargazers_json = make_json()
    return repos_and_stargazers_json


# TODO: make pip package
