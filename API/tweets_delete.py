from bottle import delete, response
import re
import g


@delete("/tweets/<tweet_id>")
def _(tweet_id):
    try:
        if not re.match(g.UUID4, tweet_id):
            response.status = 204
            return

        if tweet_id not in g.TWEETS:
            response.status = 204
            return

        g.TWEETS.pop(tweet_id)
        response.status = 200
        return "Tweet Deleted"

    except Exception as ex:
        print(ex)
        response.status = 500
        return "Something went wrong"