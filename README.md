#Renomear 

Tive a ideia desse código enquanto estava utilizando um conversor do Youtube para MP3, esse conversor era o que executava o Download de maneira mais veloz, porém incluia o nome do WebSite no ínicio de cada arquivo, e isso me incomodou um pouco, então:

Este script em Python recebe o caminho de uma pasta via entrada do usuário e renomeia todos os arquivos dessa pasta, removendo os primeiros 10 caracteres do nome de cada arquivo. 

Pré-requisitos
Este script foi desenvolvido utilizando Python 3 e não requer a instalação de bibliotecas adicionais.

Como utilizar
Para utilizar o script, basta executar o arquivo renomear_arquivos.py em um ambiente Python 3. Ao ser executado, o script solicitará ao usuário que digite o caminho da pasta a ser renomeada. O caminho deve ser digitado no formato absoluto ou relativo.

Como funciona
O script utiliza a biblioteca padrão os do Python para manipular os arquivos da pasta informada. O processo de renomeação dos arquivos é feito por meio da função os.rename(), que renomeia um arquivo no sistema de arquivos.

O script percorre todos os arquivos da pasta informada utilizando a função os.listdir(), que retorna uma lista com o nome de todos os arquivos da pasta. Para cada arquivo, o script cria um novo nome removendo os 10 primeiros caracteres do nome original e utiliza a função os.rename() para renomear o arquivo com o novo nome.

Ao final, o script exibe uma mensagem informando que os arquivos foram renomeados com sucesso.

Limitações
O script não renomeia arquivos em subpastas da pasta informada. Se desejar renomear arquivos em subpastas, execute o script separadamente em cada subpasta.

Contribuição
Este script foi desenvolvido com o objetivo de ser simples e genérico. Caso deseje contribuir com o projeto, sinta-se à vontade para criar uma "issue" ou enviar um "pull request" no GitHub.
