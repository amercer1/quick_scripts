from twython import TwythonStreamer

import secrets

tweets = []

class MyStreamer(TwythonStreamer):
    
    def on_success(sef, data):
        if data["lang"] == "en":
            tweets.append(data)
            print("received tweet #", len(tweets))

        # stop when we've collected enough
        if len(tweets) >= 1000: self.disconnect()
    
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()


stream = MyStreamer(secrets.cKey, secrets.cSecret, 
                    secrets.aKey, secrets.aSecret)
# starts consuming public statuses that contain the keyword 'data'
stream.statuses.filter(track='data')
