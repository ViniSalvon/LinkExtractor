# LinkExtractor
Extrator de links do site casadosdados.com.br

### Introdução:

O site casadosdados.com.br é uma ferramenta útil para extrair informações de empresas.

Entretanto, ao utilizar a busca avançada, deparamos-nos com os seguintes problemas:

- A quantidade máxima de páginas é limitada em 50, sendo que cada página mostra no máximo 20 resultados. Ou seja, em pesquisas cuja quantidade supera 1000 resultados, a busca fica limitada.
- Os resultados são ordenados de uma forma aleatória. Ou seja, muitas vezes, um mesmo link existente na página 1 pode ser mostrado na página 2 e assim por diante.


### Solução

A fim de se obter todos os links desejados, foram propostas as seguintes soluções:

a) A fim de não esbarrar no problema da quantidade de páginas, foi proposta uma busca baseada em datas. Assim, a cada busca, seriam retornados poucos resultados, que possivelmente não excederão a 1000.
b) Para cada data, serão varridas todas as páginas da busca de forma automatizada.


### Requisitos

- Python 3
- Selenium
- PyAutoGUI
- Pandas (é um leftover de versões anteriores, com poucas mudanças ele não é mais necessário)
- Mozilla Firefox (pode ser facilmente alterado para outro navegador através do código e baixando o seu respectivo WebDriver)


### Entradas

- Arquivo DATAS.csv: especifica todas as datas nas quais será feita a busca (coloque uma data por linha).
- FILENAME: o nome + extensão do arquivo de saída. Deve ser um arquivo no formato .csv.


### Instruções

- Configure o arquivo de datas, colocando cada data (no formato DD/MM/AAAA) em cada linha do arquivo. (obs: use 01/01/2000 em vez de 1/1/2000
- Execute o arquivo LinkExtractor.py. Digite S e aperte Enter caso queiras criar um novo arquivo (se o arquivo já existir, todos os dados serão excluídos).
- Mantenha sempre a janela no topo. Quando o programa chegar à última data e parar de executar a busca, volte ao terminal do Python e verifique se o programa foi executado com sucesso.
- Verifique o arquivo de saída.

Caso queiras testar se não houve nenhum dado repetido na busca, edite o arquivo TestesDadosRepetidos.py colocando o arquivo de saída no lugar de "linksExtraidos26.csv" e execute-o. Se houver algum item com duplicidade, ele será printado.









