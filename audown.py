import yt_dlp
import time
import pyfiglet
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.progress import (
    Progress, SpinnerColumn, BarColumn, TextColumn,
    TransferSpeedColumn, TimeRemainingColumn, DownloadColumn
)
from rich.table import Table

console = Console()


def header():
    console.clear()
    banner = pyfiglet.figlet_format("Audown", font="slant")
    console.print(f"[bold cyan]{banner}[/]")
    console.print("[dim]Youtube audio downloader • v1.0[/]\n")

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

def input_link():
    while True:
        link = Prompt.ask("[bold green]Paste the youtube link[/]")
        if link.startswith(("http://", "https://")):
            return link
        console.print("[red]Invalid link, please try again.[/]")

if __name__ == "__main__":
    header()
    link = input_link()
    download_audio(link)