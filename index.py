from sys import argv
import requests
import base64

def readOpts(argv):
    opts = {}
    while argv:
        if argv[0][0] == '-':
            opts[argv[0]] = argv[1]
        argv = argv[1:]
    return opts

args = readOpts(argv)
public_key = args["-public_key"]
private_key = args["-private_key"]
destination = args["-destination"]
url = "http://api.messagemedia.com/v1/messages"
data = '''{
  "messages": [
    {
      "content": "I want a PS4!",
      "destination_number": "%s",
      "format": "SMS",
      "metadata": {
        "language": "python",
        "character": "Obi-wan Kenobi"
      }
    }
  ]
}'''%(destination, )

username_password = public_key + ":" + private_key
token = base64.b64encode(bytes(username_password, 'utf-8'))

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Basic " + str(token,'utf-8')
    }

response = requests.post(url, data=data, headers= headers)


print("!~~~~~~~~~~~~~~~~~~~!")
print("headers: " + str(response.text))
print("!~~~~~~~~~~~~~~~~~~~!")
