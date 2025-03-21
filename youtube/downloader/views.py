from django.shortcuts import render
from django.http import HttpResponse
import yt_dlp
import os

def index(request):
    return render(request, 'downloader/index.html')

def download(request):
    if request.method == "POST":
        link = request.POST.get('link', '')

        if not link:
            return HttpResponse("⚠️ No link provided!")

        try:
            # Set download options
            ydl_opts = {
                'format': 'best',  # Highest quality
                'outtmpl': 'downloads/%(title)s.%(ext)s',  # Save format
                'quiet': False,
                'no_warnings': True,
                'noplaylist': True,
                'ignoreerrors': True,
            }

            # Download the video
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])

            return HttpResponse("✅ Video downloaded successfully!")

        except Exception as e:
            return HttpResponse(f"❌ Error: {str(e)}")

    return HttpResponse("⚠️ Invalid request method")
