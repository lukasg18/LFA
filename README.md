# Conversão Mealy e Moore
Trabalho desenvolvido como uma atividade na disciplina de Linguagens Formais e Autômatos do curso de Sistemas de Informações ofertado pelo IFES - Campus Serra foi implementado pelo aluno Lucas Gomes. A atividade consiste em converter uma máquina de Mealy para uma máquina de Moore ou vice-versa.

## Máquina de Mealy
A máquina de mealy foi criada por George H. Mealy. <br>
Em ciências da computação, uma máquina de Mealy é uma máquina de estado finito que produz um resultado (saída de dados) baseando-se no estado em que se encontra e na entrada de dados. Isto significa que o diagrama de estados irá incluir tanto o sinal de entrada como o de saída para cada vértice de transição. Em contraste, a saída de uma máquina de Moore depende apenas do estado actual da máquina, sendo que as transições não possuem qualquer sinal em anexo. Mesmo assim, por cada máquina de Mealy existe uma máquina de Moore equivalente cujos estados consistem na união dos estados da máquina de Mealy e o produto cartesiano dos estados da máquina de Mealy com o alfabeto de entrada de sinais.
<br>A máquina de mealy é aplicada em leitor de códigos de barra, Semáforos, máquinas de vendas e relógio com temporizador.
<br>Exemplo de máquina de mealy: <br>
![Alt text](https://github.com/helenfranca/lfa/blob/master/prints/MaqMealy.PNG)

<br>Represetado em arquivo como: <br> 
![Alt text](https://github.com/helenfranca/lfa/blob/master/prints/mealy.PNG)

## Máquina de Moore
Na teoria da computação, uma máquina de Moore é um autômato de estado finito onde as saídas são determinadas pelo estado corrente apenas (e não pela entrada). O diagrama de estado para uma máquina de Moore inclui um sinal de saída para cada estado.
<br>Exemplo de máquina de Moore:<br>
![Alt text](https://github.com/helenfranca/lfa/blob/master/prints/MaqMoore.PNG)
<br>Represetado em arquivo como: <br>
![Alt text](https://github.com/helenfranca/lfa/blob/master/prints/moore.PNG)

### Código fonte

 Arquivo principal que realiza a chamada da função de conversão. O mesmo se encontra dentro do diretório "Codigo"

```
    conversor.py
```

Biblioteca com as funções para a conversão das máquinas, entre elas estão a função de tratar S-Expressions e fazer a conversão das máquinas de Mealy pra Moore e de Moore pra Mealy. O mesmo se encontra dentro do diretório "Codigo"

``` 
    conversorBib.py
```

Funções da biblioteca:
* le_arquivo(nomeArq): Lê o arquivo informado como entrada;
    
* remove_caracter(texto): Remove caracteres especiais ao ler o arquivo, como "()" e "\n";
    
* remove_arg_especifico(vetor_generico,*args): Remove argumentos especificos de um vetor, como por exemplo, espaços em branco;
    
* quebra_lista(lista, n): Quebra uma lista em tamanhos determinados;
    
* lista_para_caracter(lista): Converte uma lista para uma string, colocando um espaço vazio entre as posições;
    
* escreve_arquivo(texto, nome_saida): Escreve um texto no arquivo;
    
* separa_informacoes(matriz_generica, nome_saida): Transforma uma matriz em um dicionário de dados, de acordo com a sintaxe definida pela maquina de moore ou de mealy;
    
* cria_texto(dicionario, nome_saida): Transforma um dicionário de dados em texto, de acordo com a sintaxe definida pela maquina de moore ou de mealy;
    
* moore_to_mealy(dicionario, nome_saida): Transforma o dicionário com as informaçoes de moore para mealy;
    
* mealy_to_moore(dicionario, nome_saida): Transforma o dicionário com as informaçoes de mealy para moore;

### Procedimento para compilação

No prompt de comando:
```
    conversor.py -i <nome_do_arquivo_de_entrada.txt> -o <nome_do_arquivo_de_saida.txt>
    
    Exemplo: python conversor.py -i ../Exemplos/mealy1.txt -o saida.txt
    
```

### Referências

* [https://pt.wikipedia.org/wiki/M%C3%A1quina_de_Moore](https://pt.wikipedia.org/wiki/M%C3%A1quina_de_Moore)

* [https://pt.wikipedia.org/wiki/M%C3%A1quina_de_Mealy](https://pt.wikipedia.org/wiki/M%C3%A1quina_de_Mealy).

* [http://www3.ifrn.edu.br/~jurandy/fdp/doc/aprenda-python/capitulo_10.html](http://www3.ifrn.edu.br/~jurandy/fdp/doc/aprenda-python/capitulo_10.html).
