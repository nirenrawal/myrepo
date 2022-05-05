import re
from bottle import put, request, response
import g
import json
import os
import imghdr
import uuid

@put("/tweets/<tweet_id>")
def _(tweet_id):
    try:
        if not re.match(g.UUID4, tweet_id):
            response.status = 204
            return
        if tweet_id not in g.TWEETS:
            response.status = 204
            return

        if not request.forms.get("tweet_text"):
            response.status = 400
            return {"Info": "No tweet found"}

        tweet_text = request.forms.get("tweet_text").strip()

        if len(tweet_text) < 1:
            response.status = 400
            return {"Info": "Minimum tweet length is 1 character."}
        if len(tweet_text) > 100:
            response.status = 400
            return {"Info": "Maximum tweet lenght is 100 charactrs"}

        image = request.files.get("tweet_image")

        if not image:
            g.TWEETS[tweet_id]["tweet_text"] = tweet_text

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
            
            g.TWEETS[tweet_id]["tweet_text"] = tweet_text
            g.TWEETS[tweet_id]["tweet_image"] = image_name

    except Exception as ex:
        print(ex)
        response.status = 500
        return {"Info": "Somethins is fishy"}

    return json.dumps(dict(tweet=g.TWEETS[tweet_id], tweet_text=g.TWEETS[tweet_id]["tweet_text"]))