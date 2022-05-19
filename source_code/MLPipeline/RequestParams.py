

import requests

from .References import References

class RequestParams(References):


    def reply_to_tweet(self, tweetId, complain, complain_type, entities, user):
        """ Reply to Tweet"""
        # defining a params dict for the parameters to be sent to the API
        PARAMS = {'tweetId': tweetId.strip(), "complain": complain, "complain_type": complain_type, "entities": entities,
                  "user": user.strip()}
        print(PARAMS)
        # sending get request and saving the response as response object
        r = requests.post(url=self.URL, data=PARAMS)

        # extracting data in json format
        data = r.json()
        print("reply to tweeeeeeeeeeeeeet", data)
        if data['replied']:
            return str(data["ticketId"])
        else:
            return ""


# a = RequestParams()
# a.reply_to_tweet("1415389426465656832","1231", "sdafs", "aefas", "    _nihit_")