# Challenges Jobs

## Sobre

- Um conversor de algarismos romanos, de **inteiro para romano** e de **romano para inteiro**.
- O TreeMap para análise de variação de criptomoeda (em Python) e o TreeMap em PHP que realiza análise do clima de algumas capitais em tempo real diretamente de uma API.  
No TreeMap em Python é possível converter o gráfico para PDF.

Para executar o TreeMap, use o Virtualenv e o Python PIP para instalar as dependências.

O uso do Plotly é um pacote de visualização de dados que oferece uma variedade de ferramentas para criar gráficos e painéis interativos, dentro de um ambiente baseado em navegador. O seu uso é aberto e está disponível para diversas linguagens de programação, como Javascript, Julia, R, e, claro, o Python.

Que seria velho conhecido meu nas minhas atividades de análise de dados e seria muito difícil não usar este pacote. Pois o Plotly (ele não está sozinho com quase 100 linhas de código para mais instruções) torna o gráfico possível e interativo. Todos (Python e Plotly) são utilizados com frequência em inteligência artificial, ciência de dados, estatísticas e BI.

O uso de Requests para requisições na API, sendo um dos pacotes da linguagem Python mais baixados, com mais de 300 milhões de downloads mensais. Ele mapeia o protocolo HTTP na semântica orientada a objetos do Python. Isso reforça o tão útil ele é e torna possível as requisições em qualquer API que sem ele não seria possível.

OBS: O TK é nativo do Python e está sendo usado em ambos para criar uma UI (user interface).

A ideia seria criar algo de execução rápida no computador, bastando ter o Python instalado, com ambiente isolado e por isso o uso de Virtualenv.

## Comandos úteis

`pip install virtualenv`  
`virtualenv venv`  
`pip install -r requirements`  
`venv\Scripts\activate` ou `. venv/bin/activate`  
`python treemap.py`  

### A execução do conversor

Para executar rode o comando `python conversor_numbers.py`.

WARN: No Windows, se caso ocorrer o erro `não pode ser carregado porque a execução de scripts foi desabilitada neste sistema`, execute o comando `Set-ExecutionPolicy RemoteSigned` para mudar a política no PowerShell e depois execute `venv\Scripts\activate` novamente.

## Execução do TreeMap PHP

Análise da temperatura de algumas capitais do mundo.

```bash
docker compose -f docker-compose.yml up
```

Link: <http://localhost:8080/public>  
Para entrar no container: `docker exec -it containerid /bin/bash`.
