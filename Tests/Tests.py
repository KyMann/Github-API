from main import get_followers, return_followers, GitProfile, make_followers_json


def test_get_followers():
    followers = get_followers("KyMann")
    if "mwburke" in followers and isinstance(followers, list):
        return True
    else:
        return False


def test_return_followers():
    # This test will break if KyMann gets any more followers and the test_profile is no longer the first returned.
    # Need to alter it to make it more stable
    followers_zero_depth = return_followers("KyMann", 0)
    test_profile = GitProfile("lauramjohnson", depth=0)
    followers_one_depth = return_followers("KyMann", 1)
    if test_profile.followers == followers_one_depth[0].followers and len(followers_one_depth) == 4:
        return True
    else:
        return False


def test_make_followers_json():
    expected_json = {"Github_id": "KyMann", "followers": [{"Github_id": "lauramjohnson", "followers": [{"Github_id": "KyMann", "followers": [{"Github_id": "lauramjohnson", "followers": ["KyMann"]}, {"Github_id": "janglehorse", "followers": ["KyMann", "julite", "henrywlau", "zachurich"]}, {"Github_id": "mwburke", "followers": ["KyMann"]}, {"Github_id": "dmwelch", "followers": ["healthonrails", "langstraat", "hobu", "shafik-wassef", "Slothpoo"]}]}]}, {"Github_id": "janglehorse", "followers": [{"Github_id": "KyMann", "followers": [{"Github_id": "lauramjohnson", "followers": ["KyMann"]}, {"Github_id": "janglehorse", "followers": ["KyMann", "julite", "henrywlau", "zachurich"]}, {"Github_id": "mwburke", "followers": ["KyMann"]}, {"Github_id": "dmwelch", "followers": ["healthonrails", "langstraat", "hobu", "shafik-wassef", "Slothpoo"]}]}, {"Github_id": "julite", "followers": []}, {"Github_id": "henrywlau", "followers": [{"Github_id": "janglehorse", "followers": ["KyMann", "julite", "henrywlau", "zachurich"]}]}, {"Github_id": "zachurich", "followers": [{"Github_id": "Olysalas", "followers": ["riyasmohamedmr", "FMCalisto", "ganipa93", "ceduardo2901", "AbuYami"]}]}]}, {"Github_id": "mwburke", "followers": [{"Github_id": "KyMann", "followers": [{"Github_id": "lauramjohnson", "followers": ["KyMann"]}, {"Github_id": "janglehorse", "followers": ["KyMann", "julite", "henrywlau", "zachurich"]}, {"Github_id": "mwburke", "followers": ["KyMann"]}, {"Github_id": "dmwelch", "followers": ["healthonrails", "langstraat", "hobu", "shafik-wassef", "Slothpoo"]}]}]}, {"Github_id": "dmwelch", "followers": [{"Github_id": "healthonrails", "followers": [{"Github_id": "dmwelch", "followers": ["healthonrails", "langstraat", "hobu", "shafik-wassef", "Slothpoo"]}, {"Github_id": "Bmetz", "followers": ["otobrglez", "mbunge", "fakestarbaby", "fabianishere", "hbokmann"]}, {"Github_id": "explura", "followers": ["mbunge", "tumayun", "yanguanglan", "danielmunro", "Lujaw"]}, {"Github_id": "hendychua", "followers": ["david-cys", "jsyeo", "chuajiesheng", "noobxinyu", "rctay"]}, {"Github_id": "jimmytravel", "followers": ["abhishekbhalani", "zhouguangming", "csjaba", "dennissenner", "irtefa"]}]}, {"Github_id": "langstraat", "followers": [{"Github_id": "shafik-wassef", "followers": ["MichalPaszkiewicz"]}, {"Github_id": "jessicaforbes", "followers": ["dmwelch", "healthonrails", "langstraat", "bmswgnp", "iancmason"]}, {"Github_id": "FMCalisto", "followers": ["sathishxcode", "rzlourenco", "annaizabell", "lidiamcfreitas", "cusspvz"]}]}, {"Github_id": "hobu", "followers": [{"Github_id": "sabman", "followers": ["mlandauer", "hughevans", "timriley", "kashif", "geoffevason"]}, {"Github_id": "springmeyer", "followers": ["eknuth", "ansis", "sabman", "michael", "llimllib"]}, {"Github_id": "iwillig", "followers": ["markherringer", "juliamae", "springmeyer", "whitmo", "mejymejy"]}, {"Github_id": "mweisman", "followers": ["springmeyer", "sgillies", "iwillig", "wonderchook", "adaburrows"]}, {"Github_id": "gadomski", "followers": ["hobu", "dantasse", "jplewicke", "chambbj", "susqurugger"]}]}, {"Github_id": "shafik-wassef", "followers": [{"Github_id": "MichalPaszkiewicz", "followers": ["CraigyHK", "drahmel", "AbubakerB", "pjmagee", "liamjmc"]}]}, {"Github_id": "Slothpoo", "followers": []}]}]}
    output_json = make_followers_json("KyMann")
    if output_json == expected_json:
        return True
    else:
        print(output_json)
        return False


if __name__ == "__main__":
    print(test_get_followers() and test_return_followers() and test_make_followers_json())
