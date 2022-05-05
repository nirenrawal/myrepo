from bottle import get, redirect, request, response, view
import g

@get("/admin")
@view("admin")
def _():
    try:
        jwt_admin = request.get_cookie("jwt_admin")
        if jwt_admin not in g.SESSIONS:
            return redirect("/login")
        
        tweets = []
        if g.TWEETS == {}:
            return "There's no tweet"

        for key in reversed(list(g.TWEETS.keys())):
            tweets.append(g.TWEETS[key])
        
        return dict (tweets=tweets)

    except Exception as ex:
        print(ex)
        response.status = 500
        return {"Info": "There's and error"}