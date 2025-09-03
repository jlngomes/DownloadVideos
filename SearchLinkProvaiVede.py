import os
from time import sleep
from SeleniumDriver import Chrome
from selenium.webdriver.common.by import By
from DateManipulation import DateFormat

class CatchLinkProvaiVede:

    link_provai = "https://www.youtube.com/@provaivedeoficial"

    def __init__(self, download_dir: str, background: bool):
        self.chrome = Chrome(download_dir=download_dir, background=background)
        self.data = DateFormat()

    def enter_link(self):
        return self.chrome.driver.get(self.link_provai)

    def get_link_provai(self):
        if not self.data.its_saturday():
            print('Hoje não é sábado, não consegue realizar o download')
            return None
        else:
            self.enter_link()
            sleep(5)
            self.chrome.driver.maximize_window()
            sleep(1)
            print("\nAbrindo o canal do Provai e Vede...")

            for aba in self.chrome.driver.find_elements(By.CLASS_NAME, 'yt-tab-shape-wiz__tab'):
                if aba.text == 'Vídeos':
                    aba.click()
                    sleep(3)
                    break

            sleep(1)
            print("\nFiltrando/Procurando o video de hoje...")

            for video in self.chrome.driver.find_elements(By.CLASS_NAME, "style-scope.ytd-rich-grid-renderer"):
                if 'Provai e Vede' in video.text:
                    if (f'{self.data.date_year} ({self.data.date_day}/{self.data.date_month})' in video.text
                            and not 'Libras' in video.text):
                        video.click()
                        sleep(3)

            print("\nPegando o link...\n")

            link_video = self.chrome.driver.current_url

            self.chrome.driver.quit()

            return link_video


