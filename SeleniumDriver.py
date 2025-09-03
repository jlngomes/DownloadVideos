from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Chrome:
    def __init__(
            self,
            download_dir: str,
            background: bool
        ) -> None:

        self.driver = self.init_driver(download_dir=download_dir, background=background)

    def init_driver(self, download_dir: str, background: str):

        chrome_options = Options()
        if background:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")  # Melhora compatibilidade em alguns sistemas
        chrome_options.add_argument("--mute-audio")
        chrome_options.add_argument("--window-size=1920,1080")  # Define um tamanho de janela padrão
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": download_dir,  # Caminho customizado
            "download.prompt_for_download": False,  # Não perguntar onde salvar
            "directory_upgrade": True,
            "safebrowsing.enabled": True  # Evita bloqueio do Chrome
        })
        driver = webdriver.Chrome(options=chrome_options,
                                  # executable_path=r'C:\\Users\\' + os.getlogin() + '\\Documents\\chromedriver.exe'
                                  )
        driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior',
                  'params': {'behavior': 'allow', 'downloadPath': download_dir}}
        # command_result = driver.execute("send_command", params)
        driver.execute("send_command", params)
        driver.set_network_conditions(
            offline=False,
            latency=0,  # additional latency (ms)
            download_throughput=500000 * 1024,  # maximal throughput
            upload_throughput=500000 * 1024
        )
        return driver

