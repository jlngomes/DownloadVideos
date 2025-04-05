# Importa a biblioteca yt_dlp, que serve para baixar vídeos do YouTube
import yt_dlp
# Importa a biblioteca os, que ajuda a mexer com pastas e arquivos no computador
import os


# Define uma função chamada downloadYouTube, que vai baixar o vídeo
# Ela precisa de dois "ingredientes": a URL do vídeo (videourl) e o lugar onde o vídeo vai ser salvo (path)
def downloadYouTube(videourl, path):
    # Verifica se a pasta onde o vídeo vai ser salvo existe
    # Se não existir, cria ela com o comando os.makedirs
    if not os.path.exists(path):
        os.makedirs(path)

    # Aqui começa o "tentar fazer o download"
    try:
        # Cria um dicionário (uma lista de opções) chamado ydl_opts
        # Ele diz como o vídeo deve ser baixado
        ydl_opts = {
            # Define o nome do arquivo como: "caminho/nome_do_vídeo.extensão"
            # Exemplo: "download/Música Legal.mp4"
            'outtmpl': f'{path}/%(title)s.%(ext)s',
            # Escolhe o formato MP4 e limita a qualidade até 1080p (para não ser muito pesado)
            'format': 'mp4[height<=1080]'
        }
        # Usa a biblioteca yt_dlp para baixar o vídeo com as opções que definimos
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Faz o download do vídeo usando a URL que o usuário deu
            ydl.download([videourl])
        # Se tudo der certo, avisa que o download terminou e onde o vídeo está
        print(f"Download concluído! O vídeo foi salvo em {path}.")

    # Se algo der errado (como a URL estar errada ou a internet cair), entra aqui
    except Exception as e:
        # Mostra uma mensagem de erro com o problema que aconteceu
        print(f"Erro ao baixar o vídeo: {e}")


# Pede para o usuário digitar a URL do vídeo do YouTube
url = input("\nDigite a URL do vídeo do YouTube: ")
# Define o caminho onde o vídeo vai ser salvo
# Usa o lugar atual do computador (os.getcwd) e adiciona uma pasta chamada "download"
path = f'{os.getcwd()}\\download'

# Chama a função downloadYouTube com a URL e o caminho que definimos
downloadYouTube(videourl=url, path=path)