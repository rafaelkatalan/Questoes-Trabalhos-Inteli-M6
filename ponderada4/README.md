## Projeto de Detecção de Rachaduras e Armazenamento de Dados

O objetivo deste projeto é detectar imagens de rachaduras na tela do dispositivo e enviar tanto a imagem quanto o resultado da detecção por meio do protocolo MQTT. Em seguida, um cliente MQTT recebe essa mensagem, salva a imagem em uma pasta específica e armazena o endereço do arquivo juntamente com o resultado da predição em um banco de dados SQL.

Ao executar o script, ele captura screenshots da tela em intervalos regulares. Em seguida, utiliza o algoritmo YOLOv8, treinado previamente, para realizar a detecção de objetos. Se alguma rachadura for detectada, a imagem é codificada em base64 e combinada com o resultado da detecção.

Essa mensagem, contendo a imagem codificada e o resultado, é enviada para um tópico específico em um broker MQTT. O cliente MQTT conectado ao mesmo broker e inscrito no mesmo tópico recebe a mensagem.

Ao receber a mensagem, o cliente MQTT decodifica a imagem e a salva em uma pasta designada no sistema de arquivos. Ele também extrai o resultado da detecção da mensagem e armazena-o no banco de dados SQL. O banco de dados possui uma tabela com três colunas: ID, endereço do arquivo de imagem e resultado da predição.

Essa abordagem permite o monitoramento contínuo da tela em busca de rachaduras. Sempre que uma rachadura é detectada, a imagem correspondente é armazenada em uma pasta específica e as informações da detecção são registradas no banco de dados para referência futura.

### Especificações Técnicas do Projeto:

- **Linguagem de Programação:** Python 3.6
- **Bibliotecas e Frameworks:**
   - pyautogui
   - cv2 (OpenCV)
   - numpy
   - paho.mqtt.client
   - ultralytics.YOLO
   - base64
   - pickle
   - time
   - sqlalchemy
   - os
- **Protocolo MQTT:**
   - Broker: broker.hivemq.com
   - Porta: 1883
- **Detecção de Rachaduras:**
   - Algoritmo YOLOv8
   - Modelo pré-treinado: best.pt (diretório: ../ponderada3/)
- **Codificação e Envio de Mensagens:**
   - Captura de screenshots em formato JPEG (qualidade: 100)
   - Codificação em base64 das imagens JPEG
   - Serialização das mensagens usando a biblioteca pickle
   - Codificação adicional em base64 das mensagens serializadas
   - Tópico MQTT: python/mqtt/katalan
- **Recebimento e Processamento de Mensagens:**
   - Conexão com broker MQTT
   - Assinatura do tópico python/mqtt/katalan
   - Decodificação e salvamento das imagens em formato JPEG
   - Armazenamento dos resultados da detecção em um banco de dados SQLite
   - Tabela: predictions (colunas: id, image, result)
- **Banco de Dados SQLite:**
   - Armazenamento dos resultados da detecção
   - Uso do SQLAlchemy para interagir com o banco de dados

Demonstração: https://photos.app.goo.gl/Q8LpbwrcCe3dvcnu9
