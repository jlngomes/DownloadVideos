from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
from datetime import datetime
import yt_dlp
import os

PATH = f'{os.getcwd()}\\download'

def data_tratatamento(data):
    data_str = str(data)
    data_lista = data_str.split('-')
    dict = {
            "01":"Jan",
            "02":"Fev",
            "03":"Mar",
            "04":"Abr",
            "05":"Mai",
            "06":"Jun",
            "07":"Jul",
            "08":"Ago",
            "09":"Sep",
            "10":"Oct",
            "11":"Nov",
            "12":"Dec",
    }
    return data_lista[2], dict.get(data_lista[1]), data_lista[0]

def baixar_primeiro_video(link: str):
    data_atual = datetime.today().date()

    dia, mes, ano = data_tratatamento(data=data_atual)

    # Configura o modo headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Não mostra a interface gráfica
    chrome_options.add_argument("--disable-gpu") # Melhora compatibilidade em alguns sistemas
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("--window-size=1920,1080")  # Define um tamanho de janela padrão
    chrome_options.add_argument("--log-level=3")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(link)
    sleep(5)

    driver.maximize_window()

    sleep(1)
    print("\nAbrindo o canal do Provai e Vede...")

    for aba in driver.find_elements(By.CLASS_NAME, 'yt-tab-shape-wiz__tab'):
        if aba.text == 'Vídeos':
            aba.click()
            sleep(3)
            break

    sleep(1)
    print("\nFiltrando/Procurando o video de hoje...")

    for video in driver.find_elements(By.CLASS_NAME,"style-scope.ytd-rich-grid-renderer"):
        if 'Provai e Vede' in  video.text:
            if f'{ano} ({dia}/{mes})' in video.text and not 'Libras' in video.text:
                video.click()
                sleep(3)

    print("\nPegando o link...\n")

    link_video = driver.current_url

    driver.quit()

    return link_video

def downloadYouTube(videourl, path):
    """
    Função que realiza o download de videos do Youtube que ultilizando a biblioteca "yt_dlp"

    :parameter
    - URL de video desejado
    - Path de redirecionamento do video instalado

    """
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

while True:
    choice = input('\n[1] = Informativo mundial das missões\n'
                       '[2] = Provai e Vede\n'
                       '[3] = Musíca\n'
                       '[4] = Sair\n'
                       'O que deseja fazer: ')

    if not choice.isdigit():
        print("\nOpção inválida, tente novamente\n")
        continue

    choice = int(choice)

    opcao = [1,2,3,4]
    if not choice in opcao:
        print("\nOpção inválida, tente novamente\n")
        continue

    if choice == 1:
        # link_informativo = ""
        # link = baixar_primeiro_video()
        # downloadYouTube(videourl=link, path=PATH)
        print("\nEm desenvolvimento...\n")
        continue

    if choice == 2:
        link_provai = "https://www.youtube.com/@provaivedeoficial"
        link = baixar_primeiro_video(link=link_provai)
        downloadYouTube(videourl=link, path=PATH)
        continue

    if choice == 3:
        url = input("\nDigite a URL do vídeo do YouTube: ")
        downloadYouTube(videourl=url, path=PATH)
        continue

    else:
        print("\nObrigado por escolher nossos serviços! ❤️️\n"
              "\nBy: Jean Luca Novaes Gomes\n")
        break

