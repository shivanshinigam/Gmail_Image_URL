
from flask import Flask, request

app = Flask(__name__)

# Demo mapping: Gmail ID -> Google image URL
EMAIL_TO_IMAGE = {

    "shivanshi@gmail.com": "https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png",

    #"shivanshi@gmail.com": "https://lh3.googleusercontent.com/a/demo_shivanshi_photo",
    "mentor@gmail.com": "https://lh3.googleusercontent.com/a/demo_mentor_photo",
    "testuser@gmail.com": "https://lh3.googleusercontent.com/a/demo_testuser_photo"
}

@app.route("/")
def home():
    return "Email -> Google Image URL API is running"

@app.route("/get-photo", methods=["GET"])
def get_photo():
    # Read email from query parameter: ?email=...
    email = request.args.get("email")

    if not email:
        # No email passed
        return "Please provide email as query parameter, e.g. /get-photo?email=someone@gmail.com", 400

    image_url = EMAIL_TO_IMAGE.get(email)

    if not image_url:
        # Email not found in our mapping
        return "No image found for this email", 404

    # Return just the URL as plain text (exactly what mentor wants)
    return image_url, 200

if __name__ == "__main__":
    # debug=True for development
    app.run(host="0.0.0.0", port=5001, debug=True)

