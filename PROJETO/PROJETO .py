possiveis_saidas = ["A", "B", "C", "D", "E", "F", "G", "H"]
somar = " + "
virgula = ","
negado = "'"
nulo = "-"
ESPACO = " "
binario_0 = "0"
BINARIO_1 = "1"
bsbinaria = 2
compara_por_vez = 2


def mudar_para_binario(termos):

    #Transforma os termos, em binarios.

    binarios = []

    for termo in termos:
        aux = ""
        for t in range(len(termo)):
            if termo[t] != negado:
                if t + 1 <= len(termo) - 1 and termo[t + 1] == negado:
                    aux += binario_0
                else:
                    aux += BINARIO_1
        binarios.append(aux)

    binarios.sort()

    return binarios


def variaveis_possiveis(binarios):

    #Conta o tanto de variáveis que a expressao tem, analisando pelo primeiro termo da lista de termos.

    termo = binarios[0]
    qntd_variaveis = len(termo)

    return qntd_variaveis


def transformar_decimal(binario):

    #Para transformar em decimal é preciso fazer o somatorio de cada um multiplicado por 2 (a base em binário), elevado a quantidade de elementos -1.

    qntd_numeros = len(binario)
    decimal = 0
    for numero in binario:
        decimal += (int(numero) * (bsbinaria ** (qntd_numeros - 1)))
        qntd_numeros -= 1

    return decimal


def separa_binario(binarios):
    # quantidade de 1's que o número tem e separar

    maior_indice = 0
    indice_correspondente = []
    indices = []

    for binario in binarios:
        indice = binario.count(BINARIO_1)
        if indice > maior_indice:
            maior_indice = indice

        indice_correspondente.append((binario, indice))

    for l in range(maior_indice + 1):
        indices.append([])

    for i in indice_correspondente:
        indices[i[1]].append(i[0])

    for m in indices:
        if len(m) == 0:  # avaliar isso: or m[0] == BINARIO_0*numero_variaveis(binarios)
            indices.remove(m)

    return indices


def verifica_se_pode_transformar_em_decimal(qntd_variaveis, termo):
    #Observa a string inteira, se houver o caractere diferente, significa que nao tem como transformar, e nem eh preciso.

    pode_transformar_em_decimal = True
    for f in range(qntd_variaveis):  # so transforma os valores para decimal, caso eles possam ser valores inteiros
        if termo[f] == nulo:
            pode_transformar_em_decimal = False

    return pode_transformar_em_decimal


def adiciona_no_dicionario_os_termos_comparados(qntd_variaveis, decimais_comparados, termo_i_aux, termo_i=0,termo_i_mais_1=0):

    #Adiciona no dicionario os termos que foram comparados

    if termo_i == 0 and termo_i_mais_1 == 0:
        pode_transformar_em_decimal = verifica_se_pode_transformar_em_decimal(qntd_variaveis, termo_i_aux)
        if pode_transformar_em_decimal:
            decimais_comparados[termo_i_aux] = [transformar_decimal(termo_i_aux)]
    else:
        pode_transformar_em_decimal_1 = verifica_se_pode_transformar_em_decimal(qntd_variaveis, termo_i)
        pode_transformar_em_decimal_2 = verifica_se_pode_transformar_em_decimal(qntd_variaveis, termo_i_mais_1)

        if pode_transformar_em_decimal_1 and pode_transformar_em_decimal_2:
            decimais_comparados[termo_i_aux] = ([transformar_decimal(termo_i), transformar_decimal(termo_i_mais_1)])
            if termo_i in decimais_comparados:
                del decimais_comparados[termo_i]
            if termo_i_mais_1 in decimais_comparados:
                del decimais_comparados[termo_i_mais_1]
        else:  # Se nao puder transformar em binario, significa que a compracao ja esta em outra tabela, logo os valores que eram para serem transformados em decimais ja foram, e agora e so juntar esses numeros para o px termo
            decimais_comparados[termo_i_aux] = []
            for w in range(compara_por_vez):
                decimais_comparados[termo_i_aux].append(decimais_comparados[termo_i][w])
                decimais_comparados[termo_i_aux].append(decimais_comparados[termo_i_mais_1][w])

    return decimais_comparados


def add_temos_n_interacao(termo, sairam_da_interacao):

    #Se o termo nao sair da lista de comparacao da funcao de comparar indices, entao ele e adicionado em uma lista.

    if termo not in sairam_da_interacao:
        sairam_da_interacao.append(termo)

    return sairam_da_interacao


def compara_indices(qntd_variaveis, binarios, nao_sairam=[], decimais_comparados={}):
# comparar o indice ate que nao exista com oq comparar.

    indices = separa_binario(binarios)
    tamanho_indices = len(indices)
    sairam_da_interacao = []
    lista_para_ser_comparada_novamente = []

    for binarios_indice_i in indices:  # pega as listas dentro da lista de indices
        indice_da_px_lista = indices.index(binarios_indice_i) + 1  # pega o indice da px lista da lista de indices

        if indice_da_px_lista <= tamanho_indices - 1:  # verifica se esse px indice existe na lista
            binarios_indice_i_mais_1 = indices[indice_da_px_lista]  # pega a lista no px indice

            for termo_i in binarios_indice_i:  # pega cada termo que tem dentro da lista
                for termo_i_mais_1 in binarios_indice_i_mais_1:  # pega cada termo dentro da px lista
                    cont = 0
                    termo_i_aux = ""
                    for interador in range(qntd_variaveis):  # vai olhar cada numero dos termos comparando
                        if termo_i[interador] != termo_i_mais_1[interador]:
                            cont += 1
                            termo_i_aux += nulo
                        else:
                            termo_i_aux += termo_i[interador]

                    if cont == 1:  # so pode ter um termo diferente para poder sair
                        lista_para_ser_comparada_novamente.append(termo_i_aux)

                        sairam_da_interacao = add_temos_n_interacao(termo_i,
                                                                    sairam_da_interacao)
                        sairam_da_interacao = add_temos_n_interacao(termo_i_mais_1,
                                                                    sairam_da_interacao)

                        decimais_comparados = adiciona_no_dicionario_os_termos_comparados(qntd_variaveis,
                                                                                          decimais_comparados,
                                                                                          termo_i_aux, termo_i,
                                                                                          termo_i_mais_1)

                    else:
                        decimais_comparados = adiciona_no_dicionario_os_termos_comparados(qntd_variaveis,
                                                                                          decimais_comparados, termo_i)
                        decimais_comparados = adiciona_no_dicionario_os_termos_comparados(qntd_variaveis,
                                                                                          decimais_comparados,
                                                                                          termo_i_mais_1)

        for b_i in binarios_indice_i:
            if b_i not in sairam_da_interacao:
                nao_sairam.append(b_i)

    return lista_para_ser_comparada_novamente, nao_sairam, decimais_comparados


def compara_n_vezes(qntd_variaveis, binarios,):

    #Enquanto ainda houver elementos na lista que foi comparada, ela deve ser comparada novamente.


    lista_para_ser_comparada, nao_sairam, decimais_comparados = compara_indices(qntd_variaveis, binarios)
    while len(lista_para_ser_comparada) != 0:
        lista_para_ser_comparada, nao_sairam, decimais_comparados = compara_indices(qntd_variaveis,
                                                                                    lista_para_ser_comparada,
                                                                                    nao_sairam, decimais_comparados)

    decimais_comparados_so_com_termos_nao_sairam = {}
    for elem in nao_sairam:
        if elem in decimais_comparados:
            decimais_comparados_so_com_termos_nao_sairam[elem] = decimais_comparados[elem]

    return nao_sairam, decimais_comparados_so_com_termos_nao_sairam


def todos_os_decimais_comparados(decimais_comparados):

    #Faz uma lista com os valores de todas as chaves, para poder ser analisado quando tiver montando o mapa de crivo.

    todos_decimais = []
    for elem in decimais_comparados:
        for decimal in decimais_comparados[elem]:
            todos_decimais.append(decimal)  # faz uma lista com todos os decimais que estao sendo usados

    return todos_decimais


def crivo_generico(decimais_comparados, todos_decimais, decimais_depois_do_crivo):

    #Faz a primeira comparacao do crivo, analisando quais numeros que participaram da expressao final.

    dic_contribuicoes = {}
    simplificados = []
    precisa_ordenar = []

    for elem in decimais_comparados:  # Percorre o dicionario
        num_contribuicoes = 0
        validador = False
        for decimal in decimais_comparados[elem]:
            contador = todos_decimais.count(decimal)
            if contador < compara_por_vez:
                validador = True

        if validador:
            for decimal in decimais_comparados[elem]:
                if decimal not in decimais_depois_do_crivo:
                    num_contribuicoes += 1
                    decimais_depois_do_crivo.append(decimal)

            simplificados.append(elem)  # Lista so com as chaves do dicionario que foram simplificados ao maximo

            if elem not in dic_contribuicoes:
                dic_contribuicoes[elem] = num_contribuicoes
        else:
            precisa_ordenar.append(elem)
    print()
    return simplificados, decimais_depois_do_crivo, dic_contribuicoes, precisa_ordenar


def compara_termos_ordenados(decimais_comparados, precisa_ordenar, decimais_crivo, dic_contribuicoes):

   # Depois que foi percorrido pela primeira vez o crivo, uma nova verificacao precisa ser feita.

    for termo in precisa_ordenar:
        num_contribuicoes = 0
        for decimal in decimais_comparados[termo]:
            if decimal not in decimais_crivo:
                num_contribuicoes += 1

        if termo not in dic_contribuicoes:
            dic_contribuicoes[termo] = num_contribuicoes

    return dic_contribuicoes


def compara_ordenados(ordenados, decimais_comparados, decimais_crivo, simplificados):
    #Round 2 do crivo, analisando os termos que já estão ordenados

    simplificados_2 = []
    for ordenado in ordenados:
        for decimal in decimais_comparados[ordenado]:
            if decimal not in decimais_crivo:
                decimais_crivo.append(decimal)
                if ordenado not in simplificados:
                    simplificados_2.append(ordenado)

    return simplificados_2


def repete_crivo_nas_duas_opcoes(decimais_comparados, todos_decimais):
    #Chamada da funcao nos dois casos mencionados


    simplificados_1, decimais_depois_do_crivo, dic_contribuicoes, precisa_ordenar = crivo_generico(decimais_comparados,
                                                                                                   todos_decimais, [])
    dic_contribuicoes = compara_termos_ordenados(decimais_comparados, precisa_ordenar, decimais_depois_do_crivo,
                                                 dic_contribuicoes)
    ordenados = ordena_por_contribuicoes(dic_contribuicoes, precisa_ordenar)
    simplificados_2 = compara_ordenados(ordenados, decimais_comparados, decimais_depois_do_crivo, simplificados_1)
   #print(dic_contribuicoes)
    return simplificados_1, simplificados_2


def ordena_por_contribuicoes(dic_contribuicoes, precisa_ordenar):

    #Analisa o dicionario com as contribuicoes, e ordena de acordo com quem tem mais contribuicoes

    dic_repetidos = {}
    lista_contribuicoes = []
    lista_termos_correspondentes = []

    for elem in precisa_ordenar:
        if dic_contribuicoes[elem] in lista_contribuicoes:
            if dic_contribuicoes[elem] not in dic_repetidos:
                dic_repetidos[dic_contribuicoes[elem]] = []

            indice = lista_contribuicoes.index(dic_contribuicoes[elem])
            if lista_termos_correspondentes[indice] not in dic_repetidos[dic_contribuicoes[elem]]:
                dic_repetidos[dic_contribuicoes[elem]].append(lista_termos_correspondentes[indice])

            dic_repetidos[dic_contribuicoes[elem]].append(elem)

        else:
            lista_contribuicoes.append(dic_contribuicoes[elem])
            lista_termos_correspondentes.append(elem)

    for a in range(len(lista_contribuicoes)):
        for b in range(a + 1, len(lista_contribuicoes)):
            if lista_contribuicoes[a] <= lista_contribuicoes[b]:
                temp = lista_termos_correspondentes[a]
                lista_termos_correspondentes[a] = lista_termos_correspondentes[b]
                lista_termos_correspondentes[b] = temp

                temp2 = lista_contribuicoes[a]
                lista_contribuicoes[a] = lista_contribuicoes[b]
                lista_contribuicoes[b] = temp2

    ordenados = lista_termos_correspondentes.copy()
    for num in dic_repetidos:
        indice = lista_contribuicoes.index(num)
        termo = lista_termos_correspondentes[indice]
        indice_termo = ordenados.index(termo)
        del ordenados[indice_termo]
        for i in range(len(dic_repetidos[num])):
            ordenados.insert(indice_termo + i, dic_repetidos[num][i])

    return ordenados


def cria_dicionario_mais_simplificado(decimais_comparados, simplificados_2):

    #Cria o dicionario que vai ser analisado, ou seja, um mais simplificado que o anterior.

    decimais_comparados_2 = {}
    for elem in decimais_comparados:
        for s in simplificados_2:
            if elem == s:
                decimais_comparados_2[elem] = decimais_comparados[elem]
    print(decimais_comparados)
    return decimais_comparados_2


def repete_processo_do_crivo(decimais_comparados, eh_primeira_vez, simplificados, simplificados_x):

    #O processo do Crivo precisa ser repetido varias vezes dependendo do numero de variaveis

    if not eh_primeira_vez:
        decimais_comparados = cria_dicionario_mais_simplificado(decimais_comparados, simplificados_x)

    todos_decimais = todos_os_decimais_comparados(decimais_comparados)
    simplificados_1, simplificados_2 = repete_crivo_nas_duas_opcoes(decimais_comparados, todos_decimais)
    #print(todos_decimais)
    return simplificados_1, simplificados_2


def calcula_crivo(decimais_comparados):

    #O crivo minimiza ainda mais a expressao.

    lista_com_lista_dos_processos = []
    todos_os_simplificados = []
    simplificados_x = []
    eh_primeira_vez = True
    lista_final = []

    cont = 0
    while True:
        todos_os_simplificados, simplificados_x = repete_processo_do_crivo(decimais_comparados, eh_primeira_vez,
                                                                           todos_os_simplificados, simplificados_x)

        if cont > 0:
            eh_primeira_vez = False

        simplificados_aux = todos_os_simplificados.copy()

        lista_com_lista_dos_processos.append(simplificados_aux)
        cont += 1

        if len(simplificados_x) == 0:
            break

    for lista in lista_com_lista_dos_processos:
        for num in lista:
            lista_final.append(num)
    print()
    return lista_final


def simplificados_por_ordem(numeros_simplificados, crivo):

    #Vai ordenando a partir do primeiro dicionario com todos os termos

    ordenados = []
    for elem in numeros_simplificados:
        if elem in crivo:
            ordenados.append(elem)

    return ordenados


def transforma_em_variaveis(qntd_variaveis, simplificados_ao_maximo):

   # Transforma os elementos que nao sairam da lista de comparacao em variaveis e, consequentemente, termos da expressao.

    variaveis = possiveis_saidas
    expressao_simplificada = ""

    for num in simplificados_ao_maximo:
        aux = ""
        for i in range(qntd_variaveis):
            if num[i] == binario_0:
                aux += variaveis[i] + negado
            elif num[i] == BINARIO_1:
                aux += variaveis[i]

        expressao_simplificada += aux + somar

    return expressao_simplificada.rstrip(somar)


def valida_saida(simplificado_ao_maximo, string_numeros_simplificados, string_crivo):

    if len(simplificado_ao_maximo) != 0:  # se nao pode ser simplificada, recebe a propria expresao
        grava_resul(string_numeros_simplificados, string_crivo, simplificado_ao_maximo)

#
def tabela_verdade(entradas):                   # Essa função determina a tabela verdade do meu problema.
    tabela_vdd = []
    num_casas = (entradas * entradas)
    for x in range(0, num_casas-1):
        tabela_vdd.append(str(bin(x).replace("0b", "")))    # escrever o binario tirando o 0b trocando por espaço vazio
        while len(tabela_vdd[x]) < entradas:                # usado para que o numero binario tenha 4 digitos ate o '7'
            tabela_vdd[x] = "0"+tabela_vdd[x]
    return tabela_vdd

import collections
def tabela_nivel1(entradas, mintermos, tabela_vdd):        # recebe ( inputs , output ,tabela vdd)  (Essa função cria as tabelas iniciais para QuineMcCluskey
    grupo0_binario = []                                     #lista ordenada por numero de 1s(bits)
    grupo0_mintermo = []                                    #lista dos mintermo ( ex: m...)
    for y in range(0, entradas+1):                          # adicionar os inputs para as duas listas para poder subdividilas
        grupo0_binario.append([])
        grupo0_mintermo.append([])
                                                             # ●●●●●(Essa função cria as tabelas iniciais para QuineMcCluskey●●●●●●	#
    casa_tabela_vdd = 0

    for x in tabela_vdd:
        termos = collections.Counter(x)                         #para contar o numero de 1s
        contador_de_1s = 0
        while contador_de_1s <= entradas:
            if (termos['1'] == contador_de_1s) and (str(casa_tabela_vdd) in mintermos): #quando o contador_de_1s for igual ao counter ex( '1':2...)
                grupo0_binario[contador_de_1s].append(x)
                grupo0_mintermo[contador_de_1s].append(""+str(casa_tabela_vdd))        #soma'm' ao numero
            contador_de_1s += 1
        casa_tabela_vdd += 1
    return grupo0_binario, grupo0_mintermo


def tabela_niveln(entradas, grupo0_binario, grupo0_mintermo):       # Essa função cria as tabelas "n" para QMcK
    grupon_binario = []
    grupon_mintermo = []

    for maracuja in range(0, entradas):
        grupon_binario.append([])
        grupon_mintermo.append([])
        for modernoin in range(0, entradas):
            grupon_binario[maracuja].append([])
            grupon_mintermo[maracuja].append([])

    grupon_binario[0] = grupo0_binario.copy()
    grupon_mintermo[0] = grupo0_mintermo.copy()

    for x in range(0, entradas):                                # Grupo X
        for y in range(0, len(grupon_binario[x])-1):            # Iteração Y
            z = 0
            while z < (len(grupon_binario[x][y])):              # Termos comparados
                w = 0
                while w < len(grupon_binario[x][y+1]):          # Termos para comparar
                    igual = 0
                    diferente = 0
                    for k in range(0, entradas):                # Digito do termo
                        if grupon_binario[x][y][z][k] == grupon_binario[x][y+1][w][k]:
                            igual += 1
                        else:
                            diferente = k

                    palavra_pronta = []
                    if igual == (entradas-1):
                        for celtinha in range(0, entradas):
                            if celtinha != diferente:
                                palavra_pronta.append(grupon_binario[x][y][z][celtinha])
                            if celtinha == diferente:
                                palavra_pronta.append("X")
                        palavra_full = "".join([str(item) for item in palavra_pronta])
                        if palavra_full not in grupon_binario[x+1][y]:
                            grupon_binario[x+1][y].append(palavra_full)
                            grupon_mintermo[x+1][y].append(grupon_mintermo[x][y][z]+","+grupon_mintermo[x][y+1][w])

                            # Perceba que a junção com o caractere "m" tem uso mais a frente, para que o código possa
                            # diferenciar mintermos em uma função (Exemplo: Saber a diferença de M1 para M11)

                    w += 1
                z = z + 1
    return grupon_binario, grupon_mintermo


def grava_txt(entradas, saidas, binario, mintermo,simplificado_ao_maximo):

    letras = "A"
    for x in range(1, entradas):
        letras = letras + chr(65 + x)

    print('\n{}Entrada do exercício:{} '.format(cores['branco'], cores['Limpa']))
    print('{}f({}) = Sm({}) {}\n'.format(cores['roxo_ivertido'], str(letras), str(saidas),cores['Limpa']))
    print('{}Saída pela tabela verdade:{}'.format(cores['branco'], cores['Limpa']))
    print('{}f({})= {}\n'.format(cores['roxo_ivertido'], str(letras), cores['Limpa']))

    for y in range(0, entradas-1):
        print("{} GRUPO: {} {} \n".format(cores['branco'], str(y), cores['Limpa']))
        print("{}{: <20} {: <50} {: <10}{}\n".format(cores['amarelo'], "NÚMEROS DE 1'S", "MINTERMOS",
                                                     "REPRESENTAÇÃO BINÁRIA", cores['Limpa']))
        for x in range(0, entradas):
            try:
                print("{} {: <20} {}{: <50} {: <10} {}".format(cores['roxo'], str(x + 1), cores['azul'],
                                                               str(mintermo[y][x + 1]), str(binario[y][x + 1]),
                                                               cores['Limpa']))
            except IndexError:
                print("")


    print("""

        {} SIMPLIFICADO : {} {}

        """.format(cores['verde_invertido'], simplificado_ao_maximo, cores['Limpa']))


#binario e mintermo
def completa_variaveis(binarios):
    """
    transformando em binario
    """
    maior = 0
    for b in binarios:
        if len(b) > maior:
            maior = len(b)

    for b in binarios:
        aux = b
        while len(aux) < maior:
            aux = "0" + aux

        indice = binarios.index(b)
        binarios[indice] = aux

    return binarios


def valida_expressao2(opcao, expressao):
    """
    Função que vai mostrar o binarios e quantidade de min
    """
    lista_minitermos = []
    expressao = expressao.strip()
    expressao = expressao.strip(virgula)
    ultimo_indice = len(expressao) - 1
    aux = ""
    for i in range(len(expressao)):
        eh_caractere_de_separar = False

        try:
            if  opcao == 2:
                int(expressao[i])
            elif not (expressao[i] in possiveis_saidas or expressao[i] == negado):
                eh_caractere_de_separar = True

        except:
            eh_caractere_de_separar = True

        eh_ultimo = False

        if not eh_caractere_de_separar:
            aux += expressao[i]
            if i == ultimo_indice:
                eh_ultimo = True

        if (eh_caractere_de_separar and aux != "") or eh_ultimo:
            if opcao == 2:
                aux = int(aux)
            lista_minitermos.append(aux)
            aux = ""

    eh_valida = True
    mensagem = ""
    qntd_minitermos = len(lista_minitermos)

    if qntd_minitermos == 1:
        mensagem = "Você precisa informar no mínimo dois minitermos para serem comparados!"
        eh_valida = False

    return lista_minitermos, eh_valida, mensagem


def verifica_opcao(opcao, expressao_ou_binario_ou_decimais):
    #retornar o binario e a quantidade de mintermo

    binarios = []
    decimais, eh_valida, mensagem = valida_expressao2(opcao, expressao_ou_binario_ou_decimais)

    for d in decimais:
        binarios.append(str(format(d, "b")))

        binarios = completa_variaveis(binarios)

    return binarios


cores = {'Limpa': '\033[m',           #cores para o print    .format(cores[' '] , cores['Limpa'])
         'branco': '\033[1;30;47m',
         'vermelho': '\033[1;31;40m',
         'verde': '\033[1;32;40m',
         'azul': '\033[1;34;40m',
         'amarelo': '\033[1;33;40m',
         'roxo': '\033[1;35;40m',
         'ciano': '\033[1;36;40m',

         'vermelho_invertido': '\033[1;30;41m',
         'verde_invertido': '\033[1;30;42m',
         'azul_invertido': '\033[1;30;44m',
         'amarelo_invertido': '\033[1;30;43m',
         'roxo_ivertido': '\033[1;30;45m',
         'ciano_ivertido': '\033[1;30;46m',
         'pretoebranco':'\033[1;37;40m',}


print('\n\n{} SEJA BEM-VINDO AO SIMPLIFICADOR QUINE-MCCLUSKEY !{}'.format(cores['branco'], cores['Limpa']))
iniciar = input("{} DIGITE O NUMERO 2 PARA INICIAR O CODIGO : {}  ".format(cores['ciano'],cores['Limpa']))
iniciar = int(iniciar)
entradas = input("{} DIGITE OS MINTERMOS SEPARADOS POR VIRGULA : {}  ".format(cores['ciano'],cores['Limpa']))

binarios = verifica_opcao(iniciar, entradas)
qntd_variaveis = variaveis_possiveis(binarios)
numeros_simplificados = compara_n_vezes(qntd_variaveis, binarios)[1]
crivo = calcula_crivo(numeros_simplificados)
ordenados = simplificados_por_ordem(numeros_simplificados, crivo)
simplificado_ao_maximo = transforma_em_variaveis(qntd_variaveis, ordenados)

tabela_completa = tabela_verdade(qntd_variaveis)
output_formatado = entradas.split(',')
grupinho0_binario, grupinho0_mintermo = tabela_nivel1(qntd_variaveis, output_formatado, tabela_completa)
grupinhos_binario, grupinhos_mintermo = tabela_niveln(qntd_variaveis, grupinho0_binario, grupinho0_mintermo)

string_numeros_simplificados = ""
string_crivo = ""

for nulo in numeros_simplificados:
    string_numeros_simplificados += nulo + ESPACO

for c in crivo:
    string_crivo += c + " "

p= grava_txt(qntd_variaveis, entradas, grupinhos_binario, grupinhos_mintermo,simplificado_ao_maximo)