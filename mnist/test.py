# import os

# caminhos = [os.path.join('./train', nome) for nome in os.listdir('./train')]
# arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
# jpgs = [arq for arq in arquivos if arq.lower().endswith(".jpg")]
import os

def files_path04(path):
    for p, _, files in os.walk(os.path.abspath(path)):
        for file in files:
            print(os.path.join(p, file))

files_path04('./train')