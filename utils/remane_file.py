import os
import re

# CONFIGURAÇÕES PARA RENOMEAR ARQUIVOS

# 1. Informar o "path_dir" onde se encontra o diretório que terá os arquivos renomeados
# 2. Informar o label que identifica a classe a qual a imagem pertence
# 3. Executar o escript "python rename_file.py"

all_files = []


path_dir = '/home/marcosmarques/Learning/github-p/image_classifier/default_dataset/tulip/'
label = 'tulip_'

# Obtém o caminho de todos os arquivos de um diretório especifico
for file in os.listdir(path_dir):
    all_files.append(os.path.join(path_dir, file))

# Percorre todas as imagens dentro do diretório e renomeia os arquivos
for i, file in enumerate(all_files):
    pattern = '(jp\w+)|(png)'
    _ext = re.search(pattern, file, re.IGNORECASE)

    if _ext:
        ext = _ext.group()
    else:
        ext = 'jpg'

    print(file)
    old_name = file
    new_name = path_dir + label + str(i) + '.' + ext

    os.rename(old_name, new_name)
