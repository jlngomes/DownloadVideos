import yt_dlp
import os

class DownloadUrlYoutube:
    def __init__(self, url: str, path: str):
        self.url = url
        self.path = path

    def download_url_youtube(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        try:
            ydl_opts = {'outtmpl': f'{self.path}/%(title)s.%(ext)s','format': 'mp4[height<=720]'}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.url])

            print(f'Download concluído! O vídeo foi salvo em {self.path}.')

        except Exception as e:
            print(f"Erro ao baixar o vídeo: {e}")







