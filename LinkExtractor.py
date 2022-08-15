'''
Instruções:

1) Preencha o arquivo DATAS.csv com as datas desejadas.
2) No bloco condicional if __name__ == "__main__", coloque o link de pesquisa contendo a região/cidade desejada.
3) Defina também o navegador a ser utilizado.
3) Execute este programa.
4) O resultado será salvo no arquivo linksExtraidos26.csv
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pandas as pd
import csv
import pyautogui as pya


# Esta função clicará no campo DDD. (OK)
def clica_no_ddd():
    try:
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         '/html/body/div[2]/div/div/div[2]/section/div[4]/div[1]/div/div/div/div/div[1]/input')))  # Aguarda ddd existir
        navegador.find_element(by=By.XPATH,
                               value='/html/body/div[2]/div/div/div[2]/section/div[4]/div[1]/div/div/div/div/div[1]/input').click()  # clica no DDD
    except Exception:
        print("Erro ao clicar no DDD, tentando novamente...")
        clica_no_ddd()


# Esta função recebe uma data de uma linha, no fomrato DD/MM/AAAA e preencherá os campos do dia automaticamente. (OK)
def preencher_data(data):
    pya.press('tab')
    pya.press('tab')  # TAB 2x pra cair na data de abertura
    for i in range(0, 10):
        pya.press(data[i])
    pya.press('tab')
    pya.press('tab')  # TAB 2x pra cair na data até
    for i in range(0, 10):
        pya.press(data[i])


# Esta função clicará no botão Pesquisar. (OK)
def clicar_no_botao_pesquisar():
    try:
        navegador.find_element(by=By.XPATH,
                               value='/html/body/div[2]/div/div/div[2]/section/div[6]/div/div[1]/button[1]').click()
    except Exception:
        print("Erro ao tentar clicar em pesquisar, tentando novamente...")
        clicar_no_botao_pesquisar()


# Esta função verifica se existem resultados na data especificada. Se existirem, retorna a quantidade de resultados.
# Caso contrário, retornará 0.                                                                                      (OK)
def verificar_existencia():
    time.sleep(1.5)
    try:
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         '/html/body/div[2]/div/div/div[2]/section/div[9]/div[1]/div/div/div/div/p')))  # Aguarda resultados existir
        if (navegador.find_element(by=By.XPATH,
                                   value='/html/body/div[2]/div/div/div[2]/section/div[9]/div[1]/div/div/div/div/p').text) != 'Nenhum resultado para sua pesquisa':
            total_resultados = navegador.find_element(by=By.XPATH,
                                                      value='/html/body/div[2]/div/div/div[2]/section/div[9]/div[1]/div/div/div/div/p/b').text  # captura o valor dos resultados
            total_resultados = int(total_resultados.replace('.', ''))
            return total_resultados
        else:
            return 0
    except Exception:
        print("Erro ao tentar verificar o resultado existe, tentando novamente...")
        verificar_existencia()


# Esta função define o número de páginas de acordo com a quantidade total de elementos no dia.      (OK)
def numero_de_paginas(elementos):
    if elementos > 1000:
        return 50
    elif (elementos <= 20) and (elementos > 0):
        return 1
    elif elementos == 0:
        return 0
    return int(math.ceil(elementos / 20))


# Esta função inspecionará os itens de uma página, e acrescentará à lista os itens que não estiverem presentes
# (através da função "extrair_elemento").                                                                       (OK)
def inspecionar_elementos(lista, contagem_atual):
    for i in range(1, 21):
        try:
            endereco = navegador.find_element(by=By.XPATH,
                                              value='/html/body/div[2]/div/div/div[2]/section/div[9]/div[1]/div/div/div/div/div[%d]/article/div/div/p/a' % (
                                                  i))
            print("Aqui deveria imprimir o endereco: ")
            print(endereco)

            lista, contagem_atual = extrair_elemento(endereco, lista, contagem_atual)


        except Exception:
            print("Erro ao tentar pegar o link n " + str(i))

    return lista, contagem_atual


# Esta função executa a extração de um link, adicionando-o à lista atual.           (OK)
def extrair_elemento(endereco, lista_principal, contador):
    lista_principal.add(endereco.get_attribute('href'))
    contador = len(lista_principal)

    return lista_principal, contador


# Esta função faz o papel de avançar para a próxima página.                 (OK)
def avancar_pagina():
    time.sleep(1)
    try:
        element = wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/section/div[8]/div/nav/a[2]")))
        navegador.find_element(by=By.XPATH,
                               value='/html/body/div[2]/div/div/div[2]/section/div[8]/div/nav/a[2]').click()  # clica para avançar pagina
    except Exception:
        print("Erro ao tentar avançar a página, tentando novamente...")
        avancar_pagina()


# Esta função retorna à página 1.           (OK)
def voltar_pagina_1():
    time.sleep(1)
    try:
        wait2 = WebDriverWait(navegador, timeout=1, poll_frequency=1)
        element = wait2.until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[2]/div/div/div[2]/section/div[8]/div/nav/ul/li[1]/a")))
        navegador.find_element(by=By.XPATH,
                               value='/html/body/div[2]/div/div/div[2]/section/div[8]/div/nav/ul/li[1]/a').click()  # clica para retroceder pagina 1
    except Exception:
        print(
            "Erro ao tentar voltar para página 1---------------------------------------------------------------------------")
        voltar_pagina_1()


# Esta função faz o papel de mudança de página, avançando ou retornando à primeira de acordo com a necessidade.     (OK)
def rotacionar_pagina(pagina_atual, ultima_pagina):
    if pagina_atual < ultima_pagina:
        avancar_pagina()
        pagina_atual += 1
        return pagina_atual

    voltar_pagina_1()
    pagina_atual = 1
    return pagina_atual


# Esta função avança o scroll da página para baixo.     (OK)
def rolar_para_baixo():
    navegador.execute_script("window.scrollTo(0,600)")


# Construção dos dados de saída (OK)
def saida(all_data):
    """
    :all_data (list): lista obtida com os dados de saída
    """

    with open(FILENAME, mode='a', newline='') as saida:
        escritor_csv = csv.writer(saida)
        for linha in all_data:
            escritor_csv.writerow([linha])

    '''
    dados_panda = pd.DataFrame()

    for j in range(0, len(all_data)):
        d = {'LINKS': all_data[j]}
        dados_panda = dados_panda.append(d, ignore_index=True)

    with pd.ExcelWriter('linksExtraidos26.xlsx', mode='a', if_sheet_exists='overlay') as writer:
        startrow = writer.sheets['Sheet1'].max_row + 1
        dados_panda.to_excel(writer, index=False, startrow=startrow)'''

    print(f'Foram salvos {str(len(all_data))} registros na planilha.')


# Iteração secundária. Gerencia a pesquisa de um determinado dia.       (OK)
def realiza_pesquisa():
    # Verifica a quantidade de dados existentes na data atual
    total_de_dados = verificar_existencia()

    # Se não houver dados na pesquisa atual, retorna um valor Falso.
    if total_de_dados == 0:
        return False

    # Define o número de páginas
    paginas = numero_de_paginas(total_de_dados)

    # Procedimento para uma única página
    if paginas == 1:
        lista_atual, contador_local = pesquisa_unica(total_de_dados)
        print(lista_atual)
        print(contador_local)
        return lista_atual, contador_local

    # Procedimento para múltiplas páginas
    else:
        lista_atual, contador_local = pesquisa_multipla(total_de_dados, paginas)
        print(lista_atual)
        print(contador_local)
        return lista_atual, contador_local


# Monta a lista caso exista uma única página.       (OK)
def pesquisa_unica(total_dados):
    contagem = 0
    lista = set()

    while len(lista) < total_dados:
        lista, contagem = inspecionar_elementos(lista, 0)

    lista = tuple(lista)

    return lista, contagem


# Monta a lista caso exista mais de uma página.         (OK)
def pesquisa_multipla(total_dados, max_paginas):
    contagem = 0
    lista = set()
    pagina_atual = 1

    while len(lista) < total_dados:
        print(f"Página atual: {pagina_atual}/{max_paginas}")
        lista, contagem = inspecionar_elementos(lista, contagem)
        pagina_atual = rotacionar_pagina(pagina_atual, max_paginas)

    if pagina_atual != 1:
        voltar_pagina_1()

    lista = tuple(lista)

    return lista, contagem


# Programa principal. Faz a iteração sobre os dias.     (OK)
def main():
    contador_global = 0

    for linha in linhas:

        # Estrutura a data atual
        linhas2 = "".join(linha)
        print(linhas2)

        time.sleep(1)

        # Pesquisa a data atual
        clica_no_ddd()
        preencher_data(linhas2)
        clicar_no_botao_pesquisar()
        rolar_para_baixo()

        # Iteração da pesquisa atual
        resultado_pesquisa = realiza_pesquisa()

        # Caso existam resultados, os adiciona à lista final. Caso contrário, só prossegue.
        if resultado_pesquisa:
            dados_locais, contagem_local = resultado_pesquisa
            contador_global += contagem_local

            saida(dados_locais)

            print(f"Foram salvos {contagem_local} registros no dia {linhas2}.")
        else:
            print(f"Não foram encontrado registros no dia {linhas2}.")

    print(f"Programa finalizado. Foram salvos um total de {contador_global} dados na planilha.")


# Parâmetros iniciais do programa.
if __name__ == "__main__":

    FILENAME = 'linksExtraidos26.csv'
    print("Desejas criar um novo arquivo de saída? DADOS ORIGINAIS SERÃO EXCLUÍDOS!! [S/N]")
    answer = input('OBS: caso o arquivo não exista, escreva S.\n').upper()
    if answer == "S":
        criar_arquivo = pd.DataFrame(columns=["LINKS"])
        criar_arquivo.to_csv(FILENAME, index=False)

    # DADOS ENTRADA:
    link = "https://casadosdados.com.br/solucao/cnpj/pesquisa-avancada?id=fUlrvTtLutCXXqoxb7LI6dVP6w7wiugg4L-MWVB2OMU="
    navegador = webdriver.Firefox()

    datas = open('DATAS.csv')
    linhas = csv.reader(datas)  # IMPORTAR DATAS PARA VARIAVEL

    # SETUP INICIAL:
    navegador.get(link)
    navegador.maximize_window()
    navegador.execute_script("window.scrollTo(50,document.body.scrollHeight)")
    wait = WebDriverWait(navegador, timeout=10, poll_frequency=1)

    main()

'''
OBS: Houve algumas alterações no escopo, como a função de rotação de página que foi transformada em 3, dentre outras.

O código foi testado com os dados de entrada originais e retornaram o resultado esperado.

Alguns ajustes de automatização (especialmente de scrolling) poderão ser necessários.
'''

'''
ESCOPO DA ITERAÇÃO PRINCIPAL: 
# OBJETIVO: A iteração principal tem como objetivo fazer a rotação de datas. 

Pré-iteração: definir dados de entrada (cidade, lista de datas, etc.)

Iteração:
1) Digitar as datas correspondentes nos respectivos campos e realizar a rolagem da página para baixo.
Funções:
    clica_no_ddd        (OK)
    preencher_data      (OK)

2) Clicar no botão pesquisar e realizar a rolagem da página para baixo.
Funções:
    clicar_no_botao_pesquisar   (OK)

3) Iteração secundária:
    OBJETIVO: fazer a rotação de páginas e incorporar elementos aos dados de saída.
    Pré-iteração:
        - Verificar se existem elementos nesta data.
            FALSE: BREAK. Retorna direto para a iteração principal.
            TRUE: Prosseguir
            Função:
                verificar_existência    (OK)

        - Verificar o número de elementos. OBJETIVO: Determinar o número de páginas.
            Menor ou igual a 20: páginas = 1
            Superior a 1000: páginas = 50
            Entre 21 e 1000: páginas = int(ceil(elementos/20))
            Função:
                definir_numero_de_paginas   (OK)

    Para cada página:
        a) Verificar cada elemento da página. Se não estiver na lista de saída, incorporar.
        Funções: (TBD)
            inspecionar_elementos   (OK)
            extrair_dados           (OK)

        b) Verificar se a quantidade de dados incorporados nesta seção é igual à quantidade de elementos desta data.
            TRUE: Incorporar os dados obtidos à lista geral. BREAK. (pode ser um return)
            FALSE: prosseguir
        Funções: não necessita


        c) Rotacionar página (avançar página ou, caso seja a última página, voltar à primeira)
            Funções (ambos os casos):
                rotacionar_pagina    (OK)


4) Verificar se a data atual é a última.
    TRUE: Escrever dados de saída. FIM DO PROGRAMA.
        Funções:
            saida   (OK)

    FALSE: ir para a próxima data.
        Funções: não necessita 

'''

# DONE:
#  1) iteração principal (itera sobre datas):   (provável função main())
#  2) iteração secundária (itera sobre páginas e elementos. Incorpora elementos à saída):

#       - FUNÇÃO: rolar_para_baixo (automatiza o scrolling da página. Não há retorno).
#       - FUNÇÃO: verificar_existencia (verifica se existem elementos nesta data. RETURN: quantidade de elementos.).
#       - FUNÇÃO: definir_numero_de_paginas (IN: quantidade de elementos. RETURN: quantidade de páginas).
#       - FUNÇÃO: inspecionar_elementos (inspeciona todos os elementos da página atual, verificando se o elemento foi
#       incorporado à lista principal).
#       - FUNÇÃO: incorpora o elemento não-incorporado à lista principal.
#       - FUNÇÃO: clica_avancar_pagina (parcialmente completa, precisa criar a função de voltar à página 1).

