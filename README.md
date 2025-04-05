# YouTubeDownloader.py → English 🌐

# What Does This Code Do?
- It's a "YouTube video downloader"! This script downloads videos from YouTube and saves them as MP4 files on your computer.
- It was created to solve a real problem: at my church, where I work with the sound team, we needed to download videos for the big screen, but every website we tried either crashed or gave errors. So, I made this script to fix that!

# How to Use?
First step: Run the script in Python (make sure you have the `yt_dlp` library installed with `pip install yt-dlp`).  
Second step: When it asks, paste the YouTube video URL (the link from the browser).  
What happens next:  
- It creates a "download" folder in your current directory (if it doesn’t exist already).  
- Downloads the video in MP4 format (up to 1080p quality).  
- Tells you when it’s done or shows an error if something goes wrong.

# How Does It Work Inside?
If the download starts:  
- It uses the `yt_dlp` library (a tool that grabs videos from YouTube).  
- Checks if the "download" folder exists; if not, it creates one.  
- Tries to download the video with the settings I chose (MP4, max 1080p).  
- If successful, saves the video and says "Download concluído!" with the folder location.  
- If there’s an error (like a bad link or no internet), it shows what went wrong.

# YouTubeDownloader.py → Português (Brasil)

# O que este código faz?
- É um "baixador de vídeos do YouTube"! Esse script baixa vídeos do YouTube e salva eles como arquivos MP4 no seu computador.
- Ele nasceu de um problema real: na minha igreja, eu faço parte da sonoplastia, e precisamos baixar vídeos para passar no telão. Tentamos vários sites em diferentes navegadores, mas sempre dava erro ou o site caía. Então, pensei numa solução e criei esse script para resolver!

# Como usar?
Primeiro passo: Rode o script no Python (você precisa instalar a biblioteca `yt_dlp` com `pip install yt-dlp` antes).  
Segundo passo: Quando ele pedir, cole a URL do vídeo do YouTube (o link que você vê no navegador).  
O que acontece depois:  
- Ele cria uma pasta chamada "download" no lugar onde você está rodando o script (se ela não existir ainda).  
- Baixa o vídeo em formato MP4 (com qualidade até 1080p).  
- Avisa quando terminou ou mostra um erro se algo deu errado.

# Como funciona internamente?
Se o download começar:  
- Usa a biblioteca `yt_dlp` (um ajudante que pega vídeos do YouTube).  
- Verifica se a pasta "download" existe; se não, cria ela.  
- Tenta baixar o vídeo com as configurações que eu escolhi (MP4, até 1080p).  
- Se der certo, salva o vídeo e fala "Download concluído!" com o lugar onde foi salvo.  
- Se tiver um problema (como link errado ou sem internet), ele mostra o que aconteceu.
