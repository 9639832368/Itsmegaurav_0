from pytube import YouTube

# Provide the YouTube video URL
video_url = 'https://youtu.be/lID5vETRGzk'

# Create a YouTube object
yt = YouTube(video_url)

# Get the highest resolution stream
video_stream = yt.streams.get_highest_resolution()

# Download the video
video_stream.download(output_path='path_to_save_video', filename='video_name.mp4')

print("Download completed!")


