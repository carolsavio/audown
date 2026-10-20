import yt_dlp

def download_audio(url):
    options = {
        "format": "bestaudio/best",
        "outtmpl": "audios/%(title)s.%(ext)s",
        "noplaylist": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

        print("Audio downloaded successfully!")

    except Exception as erro:
        print(f"Error downloading the audio: {erro}")


if __name__ == "__main__":
    link = input("Paste the YouTube link: ").strip()
    download_audio(link)