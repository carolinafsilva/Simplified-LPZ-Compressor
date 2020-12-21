# Trabalho 1 - Teoria da Informação
## Ana Carolina Silva
### up202004100

## Dependências
De modo a correr qualquer um dos scripts é necessário instar a biblioteca *bitstring*.

## Como comprimir um ficheiro?
De modo a comprimir um ficheiro deve executar o seguinte comando onde indica o nome do ficheiro a comprimir e o nome do ficheiro de destino.
```sh
python3 compress.py ficheiro.txt ficheiro.lz
```
ou
```sh
pypy3 compress.py ficheiro.txt ficheiro.lz
```

## Como descomprimir um ficheiro?
De modo a descomprimir um ficheiro deve executar o seguinte comando onde indica o nome do ficheiro a descomprimir e o nome do ficheiro de destino.
```sh
python3 decompress.py ficheiro.lz ficheiro.txt
```
ou
```sh
pypy3 decompress.py ficheiro.lz ficheiro.txt
```

## Detalhes de implementação
- O *padding* é feito recorrendo à adição de uma string binária do tipo *(0)\*1* de modo a tornar o ficheiro de compressão byte aligned.
- O ficheiro é lido em blocos de 4096 bytes, uma vez que este é o tamanho de blocos *standard* utilizado pela maior parte dos sistemas operativos.
- A codificação dos bits sobrantes foi feita através da utilização da posição desta sequência no dicionário.
    Ou seja, considerando *w* como a sequência de bits sobrantes, e sendo D o dicionário utilizado na codificação, codifica-se w concatenando ao *output* a posição da ocorrência de w no dicionário, D[w].
