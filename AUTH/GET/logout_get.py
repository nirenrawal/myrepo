from bottle import get, redirect, request
import g

@get("/logout")
def _():
    jwt_user = request.get_cookie("jwt_user")
    g.SESSIONS.remove(jwt_user)
    return redirect("/login")