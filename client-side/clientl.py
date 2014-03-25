# Basic web services example

# import the client libraries
import gdata.youtube
import gdata.youtube.service

# YouTubeService() used to generate the object so that we can communicate with the YouTube API
youtube_service = gdata.youtube.service.YouTubeService()

# prompt the user to enter the Youtube User ID
user_id = raw_input("Please enter the user ID: ")

# setup the actual API call
url = "http://gdata.youtube.com/feeds/api/users/"
playlist_url = url + user_id + "/playlists"

# retrieve Youtube playlist and video list
playlist_feed = youtube_service.GetYouTubePlaylistVideoFeed(playlist_url)
print "\nPlaylists for " + str.format(user_id) + ":\n"

# display each playlist to screen
for playlist in playlist_feed.entry:
    print playlist.title.text
    playlistid = playlist.id.text.split('/')[-1]
    video_feed = youtube_service.GetYouTubePlaylistVideoFeed(playlist_id = playlistid)
    for video in video_feed.entry:
        print "\t"+video.title.text
