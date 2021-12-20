import discord
import requests
import  json
from discord import *
from discord.ext import commands

API_ENDPOINT = 'https://discord.com/api/v8'
CLIENT_ID = 'Your Discord Applications Client ID'
CLIENT_SECRET = 'Your Discord Applications Client Secret'
REDIRECT_URI = 'https://google.com' #You can use any redirection url (make sure to mentpion the same in the dev portal)


def exchange_code(code):
  data = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': REDIRECT_URI
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = requests.post(str(API_ENDPOINT) + '/oauth2/token' , data=data, headers=headers)
  r.raise_for_status()
  print(REDIRECT_URI)
  return r.json()


# ain function to add the user to the guild
# Guild Id - Discord server ID
# User Id - the id of the user thta you want to add to a discord server
# Access_token - the token u get after authorization of the user

def add_to_guild(access_token, userID , guild_Id ):
        url = f"{API_ENDPOINT}/guilds/{guild_Id}/members/{userID}"

        botToken = "Your bot token here"
        data = {
        "access_token" : access_token,
    }
        headers = {
        "Authorization" : f"Bot {botToken}",
        'Content-Type': 'application/json'

    }
        response = requests.put(url=url, headers=headers, json=data)
        print(response.text)
        print(REDIRECT_URI)

code = exchange_code('The access code they get after authorization')['access_token']
add_to_guild(access_token=code, userID="The users id that you wanna move" , guild_Id="The server id for the server you wanna move them to")




