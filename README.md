# huffman-code-images

## Grupo
- Felipe Reyel Feitosa
- Leonardo Gomes

## Instrucoes de como rodar
O projeto tem uma versao online e uma local
### Versao Online [Preferencial]
O projeto original se encontra no [Google Colab](https://colab.research.google.com/drive/1YG0zfJtsOE1sR1qa3Yh2mLSKNtJyQjj0?usp=sharing)

O projeto foi quebrado em 4 blocos que nao se comunicam, a nao ser pelos arquivos no runtime:
- Login com o Google para baixar os arquivos direto do Classroom
- Codificacao das images
- Decodificacao
- Calcululo do PSNR 

Para executar basta rodar todas as celulas em sequencia (aba Runtime > Run All)

A etapa de decodificacao demora um pouco, por volta de 50 segundos

Os resultados e conclusoes se encontram tambem no corpo do notebook

### Versao Local
Para facilitar, deixei uma versao modificada para rodar direto no python local (testado com 3.9). 

#### Dependecias:
- numpy

#### Passos
1) Entre na pasta `python_files`, nela ja estao as imagens da lena e do baboon:
``` sh
cd python_files
```

2) Rode o arquivo que codifica:
```  sh
python codificador.py
```
No Terminal sera exibido o valor dos comprimentos medios:

> O comprimento medio do codeword para lena.ascii.pgm eh: 7.467304229736328

> O comprimento medio do codeword para baboon_ascii.pgm eh: 7.380626678466797

O programa ira gerar os arquivos codificados `lena.ascii.pgm.huff` e `baboon_ascii.pgm.huff` no diretorio, contendo a informacao necessaria para decodificacao

3) Rode o arquivo que decodifica:
``` sh
python decodificador.py
```

Essa etapa e demorada, por volta de 50 segundos, e nao emite nada no Terminal.

O programa ira gerar os arquivos decodificados `lena.ascii.pgm.huff.pgm` e `baboon_ascii.pgm.huff.pgm` no diretorio, contendo as imagens decodificadas

4) Rode o arquivo que calcula o PSNR:
``` sh
python psnr.py
```

No Terminal sera exibido o valor dos PSNR:

> O PSNR do processo para lena.ascii.pgm eh: infinito

> O PSNR do processo para baboon_ascii.pgm eh: infinito

## Resultados
Comentario dos resultados

### lena.ascii.pgm
O comprimento medio do codeword foi 7.467304229736328

O PSNR do processo foi infinito
### baboon_ascii.pgm
O comprimento medio do codeword foi 7.380626678466797

O PSNR do processo foi infinito

### Analise
Obteve-se o valor do PSNR infinito, ou seja, a compressão é do tipo sem perdas, visto que a codificação de Huffman altera apenas a forma de armazenar a mesma informação.
