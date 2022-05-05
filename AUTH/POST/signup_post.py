
from bottle import post, redirect, request, response
import re
import g
import uuid
import os
import json
import imghdr


@post("/signup")
def _():

    # VALIDATION
    if not request.forms.get("user_first_name"):
        return redirect("/signup?error=user_first_name")
    
    if not request.forms.get("user_last_name"):
        return redirect("/signup?error=user_last_name")
    
    if not re.match(g.REGEX_EMAIL, request.forms.get("user_email")):
        response.status = 400
        return "Please insert a valid email"
        # return redirect("/signup?error=user_email")
    
    if not re.match(g.REGEX_PASSWORD, request.forms.get("user_password")):
        # return redirect("/signup?error=user_password")
        response.status = 400
        return "Password must contain minimum eight characters, at least one letter and one number"
    
    user_id = str(uuid.uuid4())
    user_first_name = request.forms.get("user_first_name")
    user_last_name = request.forms.get("user_last_name")
    user_email = request.forms.get("user_email")
    user_password = request.forms.get("user_password")


    # CHECK IF EMAIL ALREADY EXISTS?
    for id in g.USERS:
        if g.USERS[id]["user_email"] == request.forms.get("user_email"):
            return redirect(f"/signup?error=user_email_exists&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}")
    
    # SIGNUP WITHOUT IMAGE
    image = request.files.get("user_image")
    if not image:
        g.USERS[user_id] = {
            "user_id": user_id,
            "user_first_name": user_first_name,
            "user_last_name": user_last_name,
            "user_email": user_email,
            "user_name": f"{user_first_name}{user_last_name}",
            "user_password": user_password,
            "user_image": "",
            "user_created_at": g.USER_CREATED_DATE
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

    # SIGNUP WITH IMAGE
        g.USERS[user_id] = {
            "user_id": user_id,
            "user_first_name": user_first_name,
            "user_last_name": user_last_name,
            "user_email": user_email,
            "user_name": f"{user_first_name}{user_last_name}",
            "user_password": user_password,
            "user_image": image_name,
            "user_created_at": g.USER_CREATED_DATE
        }
    
    response.status = 200
    return redirect("/login")
