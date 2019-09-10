import os
import random
from scipy import ndarray

# CONFIGURAÇÕES PARA GERAÇÃO DE NOVAS IMAGENS

# 1. Informar o caminho do diretório das imagens de origem (folder_path)
# 2. Informar o número de imagens que deseja gerar (num_files_desired)
# 3. Adicionar o label que diz respeito a classe para qual novas imagens serão criadas (label)
# 4. Definir a partir de qual número as imagens precisam ser renomeadas, por exemplo: Se no dataset atual há imagens
# com o seguinte nome assinatura_1.jpg e assinatura_2.jpg, a variável seq_image deverá ser "3" que é o próximo número
# 5. Em seguida basta executar o comando "python increased_data.py"

# Bibliotecas para processamento de imagem
import skimage as sk
from skimage import transform
from skimage import util
from skimage import io

folder_path = '/home/marcosmarques/Learning/github-p/image_classifier/default_dataset/tulip'
num_files_desired = 160
label = 'tulip_'
seq_image = 80

# Obtém o caminho de todos os arquivos em um diretório
images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]


def random_rotation(image_array: ndarray):
    # Aplica um grau de rotação aleatório entre 25% à esquerda e 25% à direita
    random_degree = random.uniform(-25, 25)
    return sk.transform.rotate(image_array, random_degree)


def random_noise(image_array: ndarray):
    # Adiciona um noise randomico a imagem
    return sk.util.random_noise(image_array)


def horizontal_flip(image_array: ndarray):
    # Aplica um flip horizontal a imagem
    return image_array[:, ::-1]


# Dicionário com as funções de transformação
available_transformations = {
    'rotate': random_rotation,
    'noise': random_noise,
    'horizontal_flip': horizontal_flip
}

num_generated_files = 0
while num_generated_files <= num_files_desired:
    # Imagem randomica de um diretório
    image_path = random.choice(images)
    # Lê a imagem como uma matriz bidimensional
    image_to_transform = sk.io.imread(image_path)
    # Aplica transformações aleatórias ao conjunto de imagens
    num_transformations_to_apply = random.randint(1, len(available_transformations))

    num_transformations = 0
    transformed_image = None
    while num_transformations <= num_transformations_to_apply:
        # Aplica a transformação aleatória em uma imagem
        key = random.choice(list(available_transformations))
        transformed_image = available_transformations[key](image_to_transform)
        num_transformations += 1
    print(image_path)
    ext = (image_path.split('/')[-1]).split('.')[-1]
    if not ext:
        ext = 'jpg'
    new_file_path = '{}/{}_{}.{}'.format(folder_path, label, seq_image, ext)

    # Salva as imagens no disco
    io.imsave(new_file_path, transformed_image)
    num_generated_files += 1
    seq_image += 1
