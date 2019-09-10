import split_folders

# Pré-requisitos

# Instalar a biblioteca split-folders: pip install split-folders

# CONFIGURAÇÕES PARA DIVIDIR DATASET

# Disposição dos arquivos no input:

# input/
#    class1/
#        img1.jpg
#        img2.jpg
#        ...
#    class2/
#        imgWhatever.jpg
#        ...
#        ...

# Disposição dos arquivos no output:

# output/
#    train/
#        class1/
#            img1.jpg
#            ...
#        class2/
#            imga.jpg
#            ...
#    val/
#        class1/
#            img2.jpg
#            ...
#        class2/
#            imgb.jpg
#            ...
#    test/
#        class1/
#            img3.jpg
#           ...
#        class2/
#            imgc.jpg
#            ...


# 1. Informe o diretório de entrada, ou seja, onde os arquivos de imagem se encontram
# 2. Informe o diretório de saída, onde as imagens devem ser dispostas depois de divididas
# 3. Execute o script "split_dateaset.py"

# CONFIGURAÇÕES ADICIONAIS

# Há duas formas de divisão dos dados:
# - train, test, val
# - train, test
# - Para utilizar a segunda opção basta remover o comentário da linha 61 desse arquivo e comentar a linha 58

input_folder = '/home/marcosmarques/Learning/github-p/image_classifier/default_dataset/'
output = '/home/marcosmarques/Learning/github-p/image_classifier/dataset/'

# Dividindo em test, val e train (10%, 10%, 80%)
split_folders.ratio(input_folder, output=output, seed=1337, ratio=(.8, .1, .1))

# Dividindo em test e train (20% e 80%)
# split_folders.ratio(input_folder, output=output, seed=1337, ratio=(.8, .2))
