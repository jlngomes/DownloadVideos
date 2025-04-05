import yt_dlp
import os


def downloadYouTube(videourl, path):
    if not os.path.exists(path):
        os.makedirs(path)

    try:
        ydl_opts = {
            'outtmpl': f'{path}/%(title)s.%(ext)s',
            'format': 'mp4[height<=1080]'  # Seleciona vídeos MP4 até 1080p
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([videourl])
        print(f"Download concluído! O vídeo foi salvo em {path}.")
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")


url = input("\nDigite a URL do vídeo do YouTube: ")
path = f'{os.getcwd()}\\download'

downloadYouTube(videourl=url, path=path)
