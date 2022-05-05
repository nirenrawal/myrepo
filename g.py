from datetime import datetime



NOW = datetime.now()
USER_CREATED_DATE = NOW.strftime("%B %Y")
TWEET_CREATED_AT = NOW.strftime("%b %d. %H:%M")


USERS = {}
##############################################################

TWEETS = {
    "c1892b77-bc64-489f-990d-784dae7bdcb0 ":{
        "tweet_id": "c1892b77-bc64-489f-990d-784dae7bdcb0 ", 
        "user_id": "8aeab5f2-2272-40c8-99ef-c8ad38500f01",
        "user_first_name": "Lionel", 
        "user_last_name": "Messi", 
        "user_name": "LionelMessi",
        "user_image": "messi.jpeg",
        "tweet_text": "Second burn of the Merlin Vacuum engine complete; <15 minutes until Starlink satellites deploy", 
        "tweet_image": "fcb.jpeg",
        "tweet_created_at": "May 6. 14.13", 
        },
   
}
##############################################################

UUID4 = '^[0-9a-f]{8}-[0-9a-f]{4}-[4][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'

##############################################################

SESSIONS = []
##############################################################


USER_SECRET = "Dinamaraca"
ADMIN_SECRET = "Español"
##############################################################

REGEX_ID = "^[0-9a-f]{8}-[0-9a-f]{4}-[4][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
##############################################################

REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
##############################################################

REGEX_PASSWORD = '^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
##############################################################

ADMIN = {
    "admin_id": "52084008-4a9f-473c-8953-72845c3e18cb",
    "admin_name": "admin",
    "admin_email": "admin@admin.com",
    "admin_password": "admin123"
}

TABS = [
    {"icon": "fas fa-home fa-fw", "title": "Home", "id": "home",  "href": "/home"},
    {"icon": "fas fa-hashtag fa-fw", "title": "Explore", "id": "explore",  "href": "/explore"},
    {"icon": "far fa-bell fa-fw", "title": "Notifications", "id": "notifications",  "href": "/notifications"},
    {"icon": "far fa-envelope fa-fw", "title": "Messages", "id": "messages",  "href": "/messages"},
    {"icon": "far fa-bookmark fa-fw", "title": "Bookmarks", "id": "bookmarks", "href": "/bookmarks"},
    {"icon": "fas fa-clipboard-list fa-fw", "title": "Lists", "id": "lists",  "href": "/lists"},
    {"icon": "far fa-user fa-fw", "title": "Profile", "id": "profile", "href": "/profile"},
    {"icon": "fa-solid fa-arrow-right-from-bracket", "title": "Logout", "id": "logout", "href": "/logout"},
    {"icon": "fas fa-ellipsis-h fa-fw", "title": "More", "id": "more",  "href": "/logout"}

]


TRENDS = [
    {"category": "Trending in Denmark", "title": "NFTs", "tweets_counter": "985K"},
    {"category": "Politics", "title": "Russia", "tweets_counter": "40k"},
    {"category": "Ukraine", "title": "Ukraine", "tweets_counter": "50k"},
    {"category": "Music", "title": "Rock", "tweets_counter": "60k"},
    {"category": "News", "title": "Afganistan", "tweets_counter": "844k"},
]

ITEMS = [
    {"img": "barca.png", "title": "FC barcelona", "user_name": "FCBarcelona"},
    {"img": "bbc.png", "title": "BBC News world", "user_name": "BBCnewswrold"},
    {"img": "madrid.jpeg", "title": "RealMadrid", "user_name": "FCRealMadrid"},
]