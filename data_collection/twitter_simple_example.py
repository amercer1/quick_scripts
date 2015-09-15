from twython import Twython

import secrets

twitter = Twython(secrets.cKey,secrets.cSecret)
for status in twitter.search(q='"data science"')["statuses"]:
    user = status["user"]["screen_name"].encode("utf-8")
    text = status["text"].encode("utf-8")
    print(user, ":", text)
    print()
