
# Gmail → Google Image URL API


------------------------------------------------------------------------------
1. Objective
------------------------------------------------------------------------------

This project builds a small HTTP API where:

- You pass a Gmail ID in the URL
- The API returns a mapped Google image URL (or any image URL you configure)
- 
Example:

http://127.0.0.1:5000/get-photo?email=shivanshi@gmail.com

Output:

https://lh3.googleusercontent.com/a/demo_shivanshi_photo

The browser will display ONLY the URL as plain text.

------------------------------------------------------------------------------
2. What This API DOES and DOES NOT Do
------------------------------------------------------------------------------

✅ DOES:
- Exposes GET endpoint /get-photo
- Accepts email as query parameter
- Returns mapped image URL in plain text
- Handles missing email and unknown users gracefully

❌ DOES NOT:
- Call real Google APIs
- Fetch real Gmail user photos automatically
- Bypass privacy or security

 This uses a DEMO mapping:

  EMAIL_TO_IMAGE = { "email": "image_url" }

 In production, you can replace this with:
 - Google People API (OAuth)
 - Database mapping
 - Identity Provider

 ------------------------------------------------------------------------------
 3. Tech Stack
 ------------------------------------------------------------------------------

 Language   : Python 3
 Framework  : Flask
 Environment: Local Machine
 Client     : Browser / curl / Postman

 ------------------------------------------------------------------------------
 4. High Level Design
 ------------------------------------------------------------------------------

 Browser ----> Flask API ----> Dictionary Lookup ----> Image URL Returned

 Input:
   /get-photo?email=someone@gmail.com

 Output:
   Only the image URL (plain text)

 ------------------------------------------------------------------------------
 5. Step-by-Step Setup (From Zero)
 ------------------------------------------------------------------------------

 5.1 Check Python

python3 --version

 Expected output:
 Python 3.x.x

 ------------------------------------------------------------------------------
 5.2 Create Project Folder

mkdir gmail_photo_api
cd gmail_photo_api

 ------------------------------------------------------------------------------
 5.3 Create Virtual Environment (Recommended)

python3 -m venv venv

 Activate (Mac/Linux):
source venv/bin/activate

 Activate (Windows):
 venv\Scripts\activate

 ------------------------------------------------------------------------------
 5.4 Install Flask

pip install flask

 ------------------------------------------------------------------------------
 5.5 Create app.py (Paste Code Below)
 ------------------------------------------------------------------------------

cat > app.py << 'EOF'
from flask import Flask, request

app = Flask(__name__)

# Demo mapping: Gmail ID -> Image URL
EMAIL_TO_IMAGE = {
    "shivanshi@gmail.com": "https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png",
    "mentor@gmail.com": "https://upload.wikimedia.org/wikipedia/commons/7/72/Default-welcomer.png",
    "testuser@gmail.com": "https://upload.wikimedia.org/wikipedia/commons/3/34/PICA.jpg"
}

@app.route("/")
def home():
    return "Email -> Google Image URL API is running"

@app.route("/get-photo", methods=["GET"])
def get_photo():
    email = request.args.get("email")

    if not email:
        return (
            "Please provide email as query parameter, e.g. /get-photo?email=someone@gmail.com",
            400,
        )

    image_url = EMAIL_TO_IMAGE.get(email)
    if not image_url:
        return "No image found for this email", 404

    return image_url, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
EOF

 ------------------------------------------------------------------------------
 6. Run the API Server
 ------------------------------------------------------------------------------

python3 app.py

 Expected Output:
 Running on http://127.0.0.1:5000
 
<img width="767" height="378" alt="Screenshot 2025-12-03 at 1 23 03 PM" src="https://github.com/user-attachments/assets/3e7917df-21bd-452a-b6eb-e84a050a0d03" />

 ------------------------------------------------------------------------------
 7. Testing the API
 ------------------------------------------------------------------------------

 7.1 Health Check

curl http://127.0.0.1:5000/

 Output:
 Email -> Google Image URL API is running

<img width="566" height="103" alt="Screenshot 2025-12-03 at 1 38 01 PM" src="https://github.com/user-attachments/assets/ea7ee034-229c-4301-b368-df0573408d88" />

 ------------------------------------------------------------------------------
 7.2 Get Photo by Gmail (Main API)

curl "http://127.0.0.1:5000/get-photo?email=shivanshi@gmail.com"

 Output:
 https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png
 
<img width="689" height="101" alt="Screenshot 2025-12-03 at 1 23 33 PM" src="https://github.com/user-attachments/assets/05c8b9c6-417e-434a-a528-629708dd7883" />

curl "http://127.0.0.1:5000/get-photo?email=mentor@gmail.com"

 ------------------------------------------------------------------------------
 8. Use Real Google Profile Images (Optional)
 ------------------------------------------------------------------------------

 Steps:
 1. Open Gmail
 2. Click profile image (top-right)
 3. Open image in new tab
 4. Copy image URL
 5. Paste into EMAIL_TO_IMAGE dictionary

 Restart server:
 CTRL + C
 python3 app.py

------------------------------------------------------------------------------
9. Error Handling
------------------------------------------------------------------------------

 9.1 No email provided

curl "http://127.0.0.1:5000/get-photo"

 Output:
 Please provide email as query parameter...
 HTTP 400

------------------------------------------------------------------------------
9.2 Email Not Found

curl "http://127.0.0.1:5000/get-photo?email=random@gmail.com"

 Output:
 No image found for this email
 HTTP 404

------------------------------------------------------------------------------

