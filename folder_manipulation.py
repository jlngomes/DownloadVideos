import os
from zipfile import ZipFile

class FolderManager:
    def __init__(self, path: str):
        self.path = path

    def create_folder(self) -> bool:
        if not os.path.exists(self.path):
            os.makedirs(self.path)
            return True
        return False

    def check_file_zip(self) -> bool:
        if not any(file.endswith('.zip') for file in os.listdir(self.path)):
            print("Nenhum arquivo ZIP encontrado no diretório")
            return False
        return True

class UnzipFile(FolderManager):
    def __init__(self, path: str):
        super().__init__(path)

    def unzip_file(self):
        if self.check_file_zip():
            for file in os.listdir(self.path):
                if file.endswith('.zip'):
                    zip_path = os.path.join(self.path, file)
                    with ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(self.path)
                    os.remove(zip_path)
                    break
