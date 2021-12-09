import requests

# Start the session
session = requests.Session()

# Create the payload
payload = {'email':'<YOUR  EMAIL>',
          'password':'<YOUR  PASSWORD>'
         }

# Post the payload to the site to log in
s = session.post("https://www.walmart.com/account/login?vid=oaoh", data=payload)

# Navigate to the next page and scrape the data
s = session.get('https://www.walmart.com/cp/playstation-5/3475115')
