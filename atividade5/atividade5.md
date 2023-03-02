<img src="../assets/logo-inteli.png" alt="Logo do Inteli"/>

# Atividade 5: Desenvolvimento de filtros

## Instruções:

Resolver todas as questões e apresentar as entregas já no Github do Estudante.

## Questões:

Desenvolva um programa em Python utilizando a biblioteca OpenCV para aplicar filtros simples ou de efeitos artísticos em uma imagem. O programa deve permitir que o usuário selecione uma imagem de entrada e escolha o tipo de filtro desejado.

- Para os filtros simples, o programa deve permitir que o usuário escolha entre os filtros de média, mediana ou gaussiano, e especifique o tamanho da janela do filtro.

- Para os filtros de efeitos artísticos, o programa deve permitir que o usuário escolha entre os filtros de cor, contorno ou estilização.

O programa deve exibir a imagem resultante na tela e permitir que o usuário salve a imagem em um arquivo. Como sugestão de implementação do programa:

- Utilizar a função cv2.imread() para carregar a imagem de entrada.
- Permitir que o usuário selecione o tipo de filtro desejado (simples ou de efeitos artísticos).
- Implementar a aplicação do filtro escolhido utilizando as funções cv2.filter2D() para a média, cv2.medianBlur() para a mediana, cv2.GaussianBlur() para o filtro gaussiano, cv2.cvtColor() para o filtro de cor, cv2.Canny() para o filtro de contorno e cv2.stylization() para o filtro de estilização.
- Exibir a imagem resultante na tela utilizando a função cv2.imshow().
- Permitir que o usuário salve a imagem resultante em um arquivo utilizando a função cv2.imwrite().

Consulte a [documentação](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html) da OpenCV implementada em Python para verificar como esses elementos são implementados na biblioteca. Realize está implementação utilizando o paradigma orientado a objetos e a linguagem Python.
