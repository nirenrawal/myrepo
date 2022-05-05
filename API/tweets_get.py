import json
from bottle import get, response, view
import g


@get("/tweets-get")
@view("logged-user")
def _():
    try:
        tweets = []
        if g.TWEETS == {}:
            response.status = 204
            return {"Info":"No tweets"}
        

        for key in reversed(list(g.TWEETS.keys())):
            tweets.append(g.TWEETS[key])

        response.status = 200
        response.content_type = 'application/json; charset=UTF-8'
        return json.dumps(dict(tweets=tweets))

    except Exception as ex:
        print(ex)
        response.status = 500
        return {"Info": "Somthing's not good"}