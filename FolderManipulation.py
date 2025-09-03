import os
import zipfile
import shutil

class FolderManager:
    def __init__(self):
        self.path = f'{os.getcwd()}\\download'

    def create_folder(self) -> None:
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def check_file_zip(self) -> bool:
        if not any(file.endswith('.zip') for file in os.listdir(self.path)):
            print("Nenhum arquivo ZIP encontrado no diretório")
            return False
        return True

class UnzipFile(FolderManager):

    def unzip_file(self):
        for file in os.listdir(self.path):
            if self.check_file_zip():
                file_path = os.path.join(self.path, file)
                extract_path = os.path.join(self.path, file.replace(".zip", ""))

                print(f"\nDescompactando: {file_path} -> {extract_path}")

                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(self.path)

                os.remove(file_path)

                path_extracted_folder = extract_path

                for item in os.listdir(path_extracted_folder):
                    src = os.path.join(path_extracted_folder, item)
                    dst = os.path.join(self.path, item)
                    shutil.move(src, dst)

                shutil.rmtree(path_extracted_folder)