from main import get_followers, return_followers, GitProfile, make_followers_json


def test_get_followers():
    followers = get_followers("KyMann")
    if "mwburke" in followers and isinstance(followers, list):
        return True
    else:
        return False


def test_return_followers():
    # This test will break if KyMann gets any more followers and the test_profile is no longer the first returned. Need to alter it to make it more stable
    followers_zero_depth = return_followers("KyMann", 0)
    test_profile = GitProfile("lauramjohnson", depth=0)
    followers_one_depth = return_followers("KyMann", 1)
    if test_profile.followers == followers_one_depth[0].followers and len(followers_one_depth) == 4:
        return True
    else:
        return False


def test_make_followers_json():
    expected_json = "{}"
    output_json = make_followers_json("KyMann")
    if output_json == expected_json:
        return True
    else:
        return False


if __name__ == "__main__":
    print(test_get_followers() and test_return_followers() and test_make_followers_json())
