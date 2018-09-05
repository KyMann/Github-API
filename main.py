import json
import requests

import secret_token

# TODO: setup API?


def get_followers(Github_id, max=5):
    """returns a list of followers from an id, max is max number returned"""
    # TODO: test after Auth, check dictionary names and flow
    url = "https://api.github.com/users/{0}/followers".format(Github_id)
    page = requests.get(url, auth=(secret_token.TOKEN, "x-oauth-basic"))
    page_content = page.text # returns an array of dictionary type objects
    followers_array = json.loads(page_content)
    followers = []
    for follower_dict in followers_array:
        followers.append(follower_dict["login"])
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


class GitProfile():
    def __init__(self, Github_id, depth=3):
        self.Github_id = Github_id
        self.followers = return_followers(Github_id, depth)

    def __repr__(self):
        return self.Github_id + " followed by:" + ", ".join(self.followers)

    def make_json(self):
        """makes the object, and it's follwer objects into dictionaries, then json.dumps them"""
        # TODO: make_json is insufficient or broken, needs thorough testing
        json_dict = {"Github_id":self.Github_id}
        follower_list = []
        for follower in self.followers:
            try:
                follower_list = follower.make_json
            except AttributeError:
                follower_list = follower
        json_dict["followers"] = follower_list
        return json.dumps(json_dict)

class GitRepo():
    def __init__(self, Github_id, repo, stargazers):
        self.owner = Github_id
        self.name = repo
        self.stargazers = stargazers


class GitStargazers():
    def __init__(self, Github_id, repos):
        self.Github_id = Github_id
        self.repos = repos


def return_followers(Github_id, depth):
    """helper function for GitProfile init, recursive function stacks git profile objects on followers"""
    if depth == 0:  # escape case
        followers = get_followers(Github_id)
        return followers
    else:
        # TODO: this could be sped up by saving searches and reusing them, but that's a lot of work
        this_followers_followers = get_followers(Github_id)  # this namespace is confusing
        followers = []
        for follower_id in this_followers_followers:  # for each follower
            followers.append(GitProfile(follower_id, depth-1))  # we repeat the profile creation (and implicitly repeat the return followers with one less depth)
        return followers


def make_followers_json(Github_id):
    """wraps all the logic and classes, takes id and returns specific json"""
    profile = GitProfile(Github_id, 3)
    return profile.make_json()


def return_repos_and_stargazers(Github_id, depth=3):
    """returns json of a github users repos and the stargazers watching, 3 levels deep"""
    # TODO: Also make repos and stargazers recursive using objects
    # TODO: maybe break into 2 functions that will call each other? Starting with top user as a stargazer object
    # TODO: null case will be stargazers at a certain level
    repos_and_stargazers = {}
    top_repos = get_repositories(Github_id)
    for repo in top_repos:
        top_stargazers = get_stargazers(Github_id, repo)
        for stargazer in top_stargazers:
            second_repos = get_repositories(stargazer)

    repos_and_stargazers_json = make_json()
    return repos_and_stargazers_json


# TODO: make pip package
