# Atividade - Lista de Tarefas:
A atividade (valendo 60% da nota da disciplina) consiste em criar um aplicativo de lista de tarefas com interface gráfica para desktop (preferencialmente usando GTK que é visto em aula, outra opção é Qt). Seu aplicativo deve ser de única janela e deve permitir as seguintes operações:

- Visualizar uma lista de itens
    - Dica: use ListBox onde cada linha contém a Label e pode conter também outros botões necessários
- Inserir item
    - Dica: Use uma Entry abaixo da lista de itens
- Remover item
    - Dica: Adicione um botão com um X vermelho ou ícone em cada linha da ListBox
- Marcar item como feito
    - Dica use uma CheckBox ou Switch
- Sua lista deve persistir, mesmo fechando o programa
    - Dica: Há várias maneiras de persistir o dado:
        - Use um banco de dados, algo simples como sqlite pode ser útil
        - Salve em um arquivo de texto, cada linha do arquivo é um item da lista, use o primeiro caractere da linha como uma flag para completo/incompleto

# Exigências

É necessário usar os itens abaixo para rodar a aplicação.

- [Linux Ubuntu LTS](https://ubuntu.com/download/desktop).
- [Docker](https://docs.docker.com/engine/installation/).
- [Docker Compose](https://docs.docker.com/compose/).

# Execução

Alterar permissões:
```sh
sudo chown -R $USER:$USER .
```

Pode ser necessário parar o serviço postgresql, se o mesmo já estiver em uso:
```sh
sudo service postgresql stop
```

Com o docker e docker-compose instalados, execute o comando abaixo na pasta raiz do projeto:
```sh
sudo docker-compose up --build
```

Abra outro terminal e execute os seguintes comandos para exibir a tela:
```sh
xhost + "local:docker@"
```
```sh
docker run --rm -ti --net=host -e DISPLAY=$DISPLAY atividade_lista_de_tarefas_app
```
