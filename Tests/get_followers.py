from main import get_followers

if __name__ == "__main__":
    followers = get_followers("KyMann")
    print(followers.contains("mwburke"))
