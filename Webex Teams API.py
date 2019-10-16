### API info at: https://webexteamssdk.readthedocs.io/en/latest/user/api.html#messages

from webexteamssdk import WebexTeamsAPI, ApiError
import json

### get token here https://developer.webex.com/docs/api/getting-started/accounts-and-authentication
kempton_at = "NjMyZmIwNTAtMjBlNC00NjgyLTkyN2MtM2VjMDlkMWUxMDA0ODViYjY2NmMtZDkw_PF84_9111cd88-67b1-44d9-a475-e716faaad1e5"
api = WebexTeamsAPI(access_token=kempton_at)

################################################
### get info about me
me = api.people.me()
print(me)

#################################################
### pull room info for all rooms you are a member of
"""
try:
    rooms = api.rooms.list()
except ApiError as e:
    print(e)

#print(list(rooms)) # list of rooms and attributes

for room in rooms:
    print(room.title)
"""
#################################################
### pull messages from a conversation (aka a room)
"""
try:
    messages = api.messages.list(roomId="Y2lzY29zcGFyazovL3VzL1JPT00vY2FiYWQzNGEtYmM3ZS0zNjkwLWJiMDYtOGFjMDcwY2ZhMTI0")
except ApiError as e:
    print(e)


#print(list(messages)) # list of rooms and attributes

for message in messages:
    print(message.personEmail, " | ", message.text)
"""
################################################
### pull team info
"""
try:
    teams = api.teams.list()
except ApiError as e:
    print(e)

print(list(teams)) # list of rooms and attributes
"""
###############################################
# send message to person by email

#api.messages.create(toPersonEmail="michial.miller@npd.com",text="Test Message")


