import requests

# start a sssion
session = requests.Session()

# Create the  payload
payload = {
            "email":"your email",
            "password":"your password"
}

url = "https://www.walmart.com/account/login?vid=oaoh"
# posting the payload  to login url
try:
    post = session.post(url, data=payload)
    print("Loggon was successful")
except:
    print("Failed to login to Walmart!")


get_data = session.get("https://www.walmart.com/cp/playstation-5/3475115")

print(get_data)
