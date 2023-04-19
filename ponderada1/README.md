<img src="../assets/logo-inteli.png" alt="Logo do Inteli"/>

# Atividade 1: Instalação do Ambiente ROS 2 de Desenvolvimento

## Instruções:

Resolver todas as questões e apresentar as entregas já no Github do Estudante.

1. Uso de containers, instalando o WSL2 no Windows:
- Abra o PowerShell com privilégios administrativos.
- Execute o seguinte comando: 

```dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart```

- Execute o seguinte comando: 

```dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart```

- Reinicie o computador.
- Abra a Microsoft Store.
- Pesquise e selecione uma distribuição Linux para instalar (por exemplo, Ubuntu, Debian ou OpenSUSE).
- Clique em "Obter" e aguarde a instalação ser concluída.
- Abra o PowerShell com privilégios administrativos.
- Execute o seguinte comando: 

```wsl --set-default-version 2```

- Execute o seguinte comando para definir a versão do WSL para uma distribuição Linux específica: 

```wsl --set-version <DistributionName> 2 (substitua <DistributionName> pelo nome da distribuição que você instalou). ```

- Abra a distribuição Linux instalada no passo 2.
- Abra um terminal na distribuição Linux.
- Execute os seguintes comandos:

```sudo apt update```

```sudo apt install -y apt-transport-https ca-certificates curl gnupg lsb-release```

```curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg```

```echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null```

```sudo apt update```

```sudo apt install -y docker-ce docker-ce-cli containerd.io```

```sudo usermod -aG docker $USER```

- Feche e abra novamente o terminal para aplicar as alterações.
- Abra o terminal na distribuição Linux.
- Execute o seguinte comando: 

```docker run hello-world```

- Se tudo estiver funcionando corretamente, você deverá ver uma saída similar a esta:

<img src="../assets/saida-docker.png" alt="Saída Docker"/>

- Abra um terminal e execute o seguinte comando: 

```docker pull ros:foxy```

- Aguarde o download da imagem do ROS2 ser concluído. Isso pode levar alguns minutos, dependendo da velocidade da sua conexão com a Internet.

Agora, para criar um container com o ROS2 e o TurtleBot, abra um terminal e execute o seguinte comando:

```docker run -it --name my_turtlebot --privileged --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" ros:foxy /bin/bash```

- Este comando cria um novo container chamado "my_turtlebot" com o ROS2 instalado e o ambiente gráfico configurado para exibir a interface do TurtleBot.

- Para instalar o pacote do TurtleBot, no terminal do container, execute o seguinte comando: 

```apt update && apt install -y ros-foxy-turtlebot3 ros-foxy-turtlebot3-simulations```

- Aguarde a instalação dos pacotes ser concluída.

- Para testar o TurtleBot, no terminal do container, execute os seguintes comandos:

```source /opt/ros/foxy/setup.bash```
```export TURTLEBOT3_MODEL=burguer```
```roslaunch turtlebot3_gazebo turtlebot3_world.launch```

- Este comando lança uma simulação do ambiente do TurtleBot no Gazebo.
- Abra um novo terminal e execute os seguintes comandos:

```source /opt/ros/foxy/setup.bash```
```export TURTLEBOT3_MODEL=burguer```
```roslaunch turtlebot3_teleop turtlebot3_world.launch```

- Este comando lança um teleop para controlar o robô simulado no ambiente do TurtleBot. Use as teclas de seta para mover o robô simulado pelo ambiente do TurtleBot.
- Se tudo estiver funcionando corretamente, você deverá ver a interface gráfica do TurtleBot no seu computador e poderá controlar o robô simulado.
