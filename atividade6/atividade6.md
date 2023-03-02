<img src="../assets/logo-inteli.png" alt="Logo do Inteli"/>

# Atividade 6: Localização de Objetos

## Instruções:

Resolver todas as questões e apresentar as entregas já no Github do Estudante.

## Questões:

Desenvolva um programa em Python utilizando as bibliotecas YOLO e OpenCV para localizar objetos em uma imagem. O programa deve permitir que o usuário selecione uma imagem de entrada, fornencendo o caminho completo até a imagem no computador e especifique qual objeto ele deseja localizar. O usuário pode optar por localizar todos os objetos presentes na imagem. O programa deve exibir a imagem resultante na tela com as localizações dos objetos detectados e permitir que o usuário salve a imagem resultante em um arquivo.

Para implementar o programa, você deve:

- Utilizar a biblioteca YOLO para detectar objetos na imagem. Para isso, você pode utilizar o modelo pré-treinado YOLOv3, que é capaz de detectar objetos em diversas categorias, como pessoas, carros, animais, etc. O YOLOv3 é implementado em Python através da biblioteca Darknet e existem diversas bibliotecas Python que permitem utilizar o YOLOv3 em conjunto com o OpenCV, como a "pydarknet" e "darkflow".
- Permitir que o usuário especifique qual objeto ele deseja localizar. O usuário pode optar por localizar todos os objetos presentes na imagem. Como referência de lista de objetos disponíveis, utilizar os objetos na lista COCO, que é a lista de objetos utilizada para treinar o YOLOv3. Se nenhuma opção válido for fornecida, localizar todos os objetos presentes na imagem.
- Exibir a imagem resultante na tela com as localizações dos objetos detectados, utilizando a função cv2.rectangle() para desenhar um retângulo em volta de cada objeto.
- Permitir que o usuário salve a imagem resultante em um arquivo utilizando a função cv2.imwrite(). Para isso, o usuário deve fornecer o nome do arquivo de saída.

Consulte a [documentação](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html) da OpenCV implementada em Python para verificar como esses elementos são implementados na biblioteca. Para a biblioteca YOLO, consulte a [documentação](https://pjreddie.com/darknet/yolo/) do YOLOv3. Realize está implementação utilizando o paradigma orientado a objetos e a linguagem Python. Já para a lista COCO de objetos, consulte o [link](https://cocodataset.org/#home).
