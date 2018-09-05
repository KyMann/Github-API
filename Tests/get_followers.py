from main import get_followers


def test_get_followers():
    followers = get_followers("KyMann")
    if "mwburke" in followers and isinstance(followers, list):
        return True
    else:
        return False


def test_return_followers():
    pass


if __name__ == "__main__":
    test_get_followers()
    