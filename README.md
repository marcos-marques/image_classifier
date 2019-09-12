# image_classifier

Este projeto apresenta um notebook com os passos necessários para treinar um modelo de classificação de imagens. 

O projeto esta organizado da seguinte forma:

* diretório **dataset** possui um conjunto de imagens de dividas em 5 tipos de flores divididas em **train**, **test** e **val** (o dataset original pode ser encontrado nesse [link](http://www.robots.ox.ac.uk/~vgg/data/flowers/17/)
* diretório **utils** possui quatro scripts para auxiliar no pré-processamento: 
    * copy_random_files.py
    * increased_data.py
    * rename_file.py
    * split_dataset.py
* Pipifile
* image_classifier.ipynb

### Treinando um modelo de reconhecimento de flores

Para testar a estrutura da rede treinei um modelo para classificar 5 flores de tipos diferentes, o dataset utilizado para treinar o modelo foi dividido da seguinte forma:

* dataset
    * train (192 exemplos de cada)
        * crocus 
        * dandelion
        * fritillary
        * tigerlily
        * tulip
    * test (25 exemplos de cada)
        * crocus
        * dandelion
        * fritillary
        * tigerlily
        * tulip
    * val (24 exemplos de cada)
        * crocus
        * dandelion
        * fritillary
        * tigerlily
        * tulip

### Resultado do Treino:

#### Input

* **Dataset:**  [17 Category Flower Dataset](http://www.robots.ox.ac.uk/~vgg/data/flowers/17/)
* **Finalidade:** Classificar imagens de flores em 5 categorias

#### Estrutura da rede

![Estrutura da rede](images/structure_image_classifier.png)

### Treino

![Gráfico do Treino](images/trainning.png)

### Output

* Acurácia do modelo: **0.968**
* Matriz de Confusão:

![Matriz de confusão](images/matriz_confusao.png)


### Classificando algumas imagens:
|![Predi1](images/pred1.png)|![Pred2](images/pred2.png)|![Pred3](images/pred3.png)|

### Convertendo o modelo para Tensorflow

Para converter o modelo de *.h5* para um modelo Tensorflow e disponibilizá-lo no Tf Serving você deve executar o seguinte código:

``` 
tf.keras.backend.set_learning_phase(0)  # Ignore dropout at inference

export_path = path_to_save_model_tensorflow


with tf.keras.backend.get_session() as sess:
    sess.run(tf.global_variables_initializer())
    model = load_model(path_to_save_model_keras)
    tf.saved_model.simple_save(
        sess,
        export_path,
        inputs={'input_image': model.input},
        outputs={t.name: t for t in model.outputs})

```

**OBS:** O código para conversão do modelo esta disponível na última célula do notebook.

### Servindo o modelo no tf serving

Para servir o modelo gerado basta subir um container docker e utilizando o seguinte comando:

```
docker pull tensorflow/serving && \

docker run -p 8501:8501 -d -v absolut_path_to_model:/models/flowers_classifier -e MODEL_NAME=document_classifier -t tensorflow/serving

 ```

--------------------------
| [**Portifólio**](https://marcos-marques.github.io/) | [**Blog**](https://medium.com/@marcosrlmarques) | [**GitHub**](https://github.com/marcos-marques?tab=repositories) |


