# Github-API
Python package to retrieve json info from github

Requires an authentication key from a github profile to activate.
Current format is 

secret_token.py
---------
```TOKEN = :YourSecureToken```    
---------

The entry point for the requirements is the function **make_followers_json**, and in the future make_repos_and_stargazers_json. Both will take in a github id and return the desired json.

They work by creating classes that have recursive functions, such as return_followers, that generate more of the same object down to a desired depth. 

These recursive functions in turn use the api wrappers, such as get_followers, that do the work of reaching out to github and retrieving the information.
The get functions are all 

TODOs:
- Test flow through of followers retrieval
- Write repos and stargazers recursive functions
- Package for Pip




