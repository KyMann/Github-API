# Github-API
Python package to retrieve json info from github

Currently Non-functional as I could not figure out Auth. Will continue tonight (9/4). 

The entry point for the requirements is the function make_followers_json, and in the future make_repos_and_stargazers_json. Both will take in a github id and return the desired json.
They work by creating classes that have recursive functions, such as return_followers, that generate more of the same object down to a desired depth. These recursive functions in turn use the api wrappers, such as get_followers, that do the work of reaching out to github and retrieving the json.

TODOs:
-Get https://api.github authentication to work - blocker for testing
-Write repos and stargazers recursive functions
-Package for Pip

Blockers:
Authentication https://developer.github.com/v3/#authentication
-Authentication attempted using private token
-Authentication attempted using oauth token in url
-Authentication attempted using client id and secret key in url
-Why the heck won't any of these Auth things work

-Reached out to STLTech and LCC Slack channels for help. Hopefully that's alright, though nothing's come back.



