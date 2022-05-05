
from bottle import error, get, run, static_file, view

from AUTH.GET import(
    signup_get,
    login_get,
    logout_get
)

from AUTH.POST import (
    signup_post,
    login_post
)
import ROUTES.logged_user_get
import ROUTES.admin

from API import (
    tweets_create,
    tweets_delete,
    tweets_get,
    tweets_update
)



####################

@get("/")
@view("index")
def _():
    return

####################

@get("/app.css")
def _():
    return static_file("app.css", root=".")
#####################

@get("/images/<file_name:path>")
def _(file_name):
    return static_file(file_name, root="./images")


#####################
@get("/app.js")
def _():
    return static_file("app.js", root=".")

#####################
@get("/validator.js")
def _():
    return static_file("validator.js", root=".")

#####################

@error(404)
@view("404")
def _(error):
    print(error)
    return
#####################


run(host="127.0.0.1", port=3300, debug=True, reloader=True, server="paste")