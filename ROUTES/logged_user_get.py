from tokenize import tabsize
from bottle import get, redirect, request, response, view
import g
import jwt


@get("/logged-user/<user_id>")
@view("logged-user")
def _(user_id):
    try:
        response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")
        session_user = request.get_cookie("jwt_user")
        if session_user not in g.SESSIONS:
            return redirect("/login")

        for session in g.SESSIONS:
            if session == session_user:
                jwt_user = jwt.decode(session, g.USER_SECRET, algorithms=["HS256"])

        user_first_name = g.USERS[user_id]["user_first_name"]
        user_last_name = g.USERS[user_id]["user_last_name"]
        user_name = g.USERS[user_id]["user_name"]
        user_image = g.USERS[user_id]["user_image"]

        

        logged_user_tweet = []
        if g.TWEETS == {}:
            return {"Info": "There are no tweets available"}

        for key in reversed(list(g.TWEETS.keys())):
            if user_id in g.TWEETS[key]["user_id"]:
                logged_user_tweet.append(g.TWEETS[key])

       
        return dict(
            user_id=user_id,
            user_first_name=user_first_name,
            user_last_name=user_last_name,
            user_name=user_name,
            user_image=user_image,
            logged_user_tweet=logged_user_tweet,
            jwt_user=jwt_user,
            tabs=g.TABS,
            trends=g.TRENDS,
            items=g.ITEMS,
            tweets=g.TWEETS


        )

    except Exception as ex:
        print(ex)
        response.status = 500
        return {"Info": "Something went wrong!!"}
   