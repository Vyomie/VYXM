from vyxm.protocol.prebuilt_tools import SpotifySearch, SendEmail

song_url = SpotifySearch("lofi hip hop")
email_result = SendEmail("user@example.com", "Your music", f"Check this out: {song_url}")

print(email_result)