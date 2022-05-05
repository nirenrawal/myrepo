import os
import re
import uuid
import g
import json
import imghdr
from bottle import post, request, response


@post("/tweets-create/<user_id>")
def _(user_id):
    
    try: 
        tweet_id = str(uuid.uuid4())
        if not re.match(g.UUID4, tweet_id):
            response.status = 204
            return

        if not request.forms.get("tweet_text"):
            response.status = 400
            return
        
        tweet_text = request.forms.get("tweet_text").strip()

        if len(tweet_text) < 1:
            response.status = 400
            return {"Info": "Minimum tweet length is 1 character."}
        if len(tweet_text) > 100:
            response.status = 400
            return {"Info": "Maximum tweet lenght is 100 charactrs"}

        image = request.files.get("tweet_image")

        # %Image
        if not image:
            g.TWEETS[tweet_id] = {
                "tweet_id": tweet_id,
                "user_id": user_id,
                "user_first_name": g.USERS[user_id]["user_first_name"],
                "user_last_name": g.USERS[user_id]["user_last_name"],
                "user_name": g.USERS[user_id]["user_name"],
                "user_image": g.USERS[user_id]["user_image"],
                "tweet_text": tweet_text,
                "tweet_created_at": g.TWEET_CREATED_AT
            }

        else:
            file_name, file_extension = os.path.splitext(image.filename)
            print(file_name)
            print(file_extension)

            if file_extension not in (".png", ".jpg", ".jpeg"):
                return {"Info":"Invalid Image"}

            if file_extension == ".jpg": file_extension = ".jpeg"
            
            # NEW IMAGE
            image_id = str(uuid.uuid4())
            image_name = f"{image_id}{file_extension}"

            # SAVE IMAGE
            image_path = f"./images/{image_name}"
            image.save(image_path)

            # IMAGE TO JSON
            json.dumps(str(image_name))

            imghdr_extension = imghdr.what(image_path)
            if file_extension != f".{imghdr_extension}":
                os.remove(image_path)
                response.status = 400
                return {"Info": "The image you uploaded is invalid"}

            #+IMAGE
            if user_id in g.USERS:
                g.TWEETS[tweet_id] = {
                        "tweet_id": tweet_id,
                        "user_id": user_id,
                        "user_first_name": g.USERS[user_id]["user_first_name"],
                        "user_last_name": g.USERS[user_id]["user_last_name"],
                        "user_name": g.USERS[user_id]["user_name"],
                        "user_image": g.USERS[user_id]["user_image"],
                        "tweet_text": tweet_text,
                        "tweet_image": image_name,
                        "tweet_created_at": g.TWEET_CREATED_AT
                }

                response.status = 201
            
            else:
                return "Something is wrong"
        
    except Exception as ex:
        print(ex)
        response.status = 500
        return {"Info":"Something went wrong"}
    
    return json.dumps(dict(tweet=g.TWEETS[tweet_id])) ##YO LINE TALA BATA MATHI SAREKO HO...