# prebuilt_tools.py

from .tools import Tool

@Tool(Name="GoogleMaps", Description="Search location on Google Maps", Inputs={"Query": "str"}, Category="Location")
def GoogleMaps(Query):
    return f"https://www.google.com/maps/search/{Query.replace(' ', '+')}"

@Tool(Name="SpotifySearch", Description="Search music on Spotify", Inputs={"Query": "str"}, Category="Music")
def SpotifySearch(Query):
    return f"https://open.spotify.com/search/{Query.replace(' ', '%20')}"

@Tool(Name="SendEmail", Description="Mock send email", Inputs={"To": "str", "Subject": "str", "Body": "str"}, Category="Communication")
def SendEmail(To, Subject, Body):
    return f"Email sent to {To} with subject '{Subject}' and body: {Body}"
