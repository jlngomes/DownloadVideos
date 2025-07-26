import os
from datetime import datetime
from date_manipulation import DataManagement, DateFormat
from folder_manipulation import FolderManager
from selenium_pack import ActionSelenium

if __name__ == '__main__':
    # date = datetime.today().date()
    # teste = DataManagement(date_actual=date)
    # print(teste.format_date())

    # path = f'{os.getcwd()}\\Download\\'
    # teste = FolderManager(path)
    # try:
    #     teste.unzip_file()
    # except Exception as e:
    #     print(f"erro de gay {e}")

    chrome = ActionSelenium(download_dir='{os.getcwd()}\\Download\\', background=False)

    chrome.open_chrome("https://gustavoguanabara.github.io/javascript/exercicios/ex009/index.html")

    chrome.click_xpath("/html/body/button[1]")

    chrome.close_driver()