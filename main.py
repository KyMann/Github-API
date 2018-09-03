import json

# TODO: setup API?

def get_followers(Github_id, max=5):
    """returns a list of followers from an id, max is max number returned"""
    # TODO: Get followers as list
    return []

def get_repositories(Github_id, max=3):
    """returns a list of repositories from an id, max is max number returned"""
    # TODO: get repositores as list
    return []

def get_stargazers(repository, max=3):
    """returns a list of stargazers from a given github repository, max is max number returned"""
    # TODO: get stargazers as list
    return []

def depth_repeat(depth, function, initial_input):
    """repeats a function on the results of that function"""
    # TODO: make an auto recursion function? Out of scope?
    return []

def make_json(nested_lists):
    """takes a list of lists and strings and turns it into json"""
    the_json = json.dumps(nested_lists)
    # TODO: test is json.dumps is sufficient
    return the_json

def return_followers(Github_id):
    """returns json of a github users followers and their followers 3 levels deep"""
    # TODO: if not using depth_repeat, 
    followers_list = depth_repeat(3, get_followers, Github_id)
    followers_json = make_json(followers_list)
    return followers_json

def return_repos_and_stargazers(Github_id, depth=3):
    """returns json of a github users repos and the stargazers watching, 3 levels deep"""
    for index in range(depth):
        # TODO: reach the bottom level of the nested list and call the correct function on it
    repos_and_stargazers_json = make_json()
    return repos_and_stargazers_json