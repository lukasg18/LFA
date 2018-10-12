# Conversão Mealy e Moore
Trabalho desenvolvido como uma atividade na disciplina de Linguagens Formais e Autômatos do curso de Sistemas de Informações ofertado pelo IFES - Campus Serra foi implementado pelo aluno Lucas Gomes. A atividade consiste em converter uma máquina de Mealy para uma máquina de Moore ou vice-versa.

## Máquina de Mealy
A máquina de mealy foi criada por George H. Mealy. <br>
"Em ciências da computação, uma máquina de Mealy é uma máquina de estado finito que produz um resultado (saída de dados) baseando-se no estado em que se encontra e na entrada de dados. Isto significa que o diagrama de estados irá incluir tanto o sinal de entrada como o de saída para cada vértice de transição. Em contraste, a saída de uma máquina de Moore depende apenas do estado actual da máquina, sendo que as transições não possuem qualquer sinal em anexo. Mesmo assim, por cada máquina de Mealy existe uma máquina de Moore equivalente cujos estados consistem na união dos estados da máquina de Mealy e o produto cartesiano dos estados da máquina de Mealy com o alfabeto de entrada de sinais" Fonte:[Wikipédia](https://pt.wikipedia.org/wiki/M%C3%A1quina_de_Mealy).
<br>A máquina de mealy é aplicada em leitor de códigos de barra, Semáforos, máquinas de vendas e relógio com temporizador.
<br>Exemplo de máquina de mealy: <br>
![Alt text](https://github.com/helenfranca/lfa/blob/master/prints/MaqMealy.PNG)

<br>Represetado em arquivo como: <br> 
![Alt text](https://github.com/helenfranca/lfa/blob/master/prints/mealy.PNG)

## Máquina de Moore
"Na teoria da computação, uma máquina de Moore é um autômato de estado finito onde as saídas são determinadas pelo estado corrente apenas (e não pela entrada). O diagrama de estado para uma máquina de Moore inclui um sinal de saída para cada estado." Fonte: [Wikipédia](https://pt.wikipedia.org/wiki/M%C3%A1quina_de_Moore)
<br>Exemplo de máquina de Moore:<br>
![Alt text](https://github.com/helenfranca/lfa/blob/master/prints/MaqMoore.PNG)
<br>Represetado em arquivo como: <br>
![Alt text](https://github.com/helenfranca/lfa/blob/master/prints/moore.PNG)

### Código fonte

 Arquivo principal que realiza a chamada da função de conversão.

```
    conversor.py
```

Biblioteca com as funções para a conversão das máquinas, entre elas estão a função de tratar S-Expressions e fazer a conversão das máquinas de Mealy pra Moore e de Moore pra Mealy.

``` 
    conversorBib.py
```

Funções:
```
    > leArquivo(nomeArq) -> Lê o arquivo informado como entrada
    
    > tokens(texto) -> Recebe um texto e retorna uma lista com todos os tokens
    
    > maquina(lista,arquivoSaida) -> Recebe uma lista e o aquivo de saída informado; Nessa função decide-se qual 
    a máquina será convertida.
    
    > maqMealy(lstMealy) -> Recebe uma lista com os tokens da maquina de Mealy e retorna as listas correspondentes 
    as palavras-chaves
    
    > maqMoore(lstMoore) -> Recebe uma lista com os tokens da maquina de Moore e retorna as listas correspondentes 
    as palavras-chaves
    
    > comumMaq(lstMealy,index,lstIN,lstOUT,lstEstados,lstFinal,start) -> Recebe as listas correpondentes e em comum 
    as máquinas e as modifica
    
    > transMealy(DicFn,lstTran) -> Recebe um dicionário com os "out-fn" e uma lista com as transições de Moore e 
    retorna uma lista com as transições em Mealy
    
    > transMoore(lstTran) -> Recebe uma lista com as transições de Mealy e retorna um dicionário com os "out-fn" e 
    uma lista com as transições de Moore
    
    > escreve(nome,lst,arquivoSaida) -> Recebe o nome da máquina, uma lista com a máquina a ser escrita e o nome do 
    arquivo de saída que será criado e escreve as informações nele
    
    > formaTexto(x,lst) -> Recebe uma string x e uma lista com a máquina e retorna uma string formada com as 
    informações em comum das máquinas.
    
```
### Procedimento para compilação

No prompt de comando:
```
    conversor.py -i <nome_do_arquivo_de_entrada.txt> -o <nome_do_arquivo_de_saida.txt>
    
    Exemplo: conversor.py -i moore.txt -o saida.txt
    
```

