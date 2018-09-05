from main import get_followers, return_followers


def test_get_followers():
    followers = get_followers("KyMann")
    if "mwburke" in followers and isinstance(followers, list):
        return True
    else:
        return False


def test_return_followers():
    followers_zero_depth = return_followers("KyMann", 0)
    followers_one_depth = return_followers("KyMann", 1)
    print(followers_one_depth)


if __name__ == "__main__":
    #test_get_followers()
    test_return_followers()