''' CASO:
Modelar e implementar um autômato que faça valicação de atribuições, essa atribuição dese ter a seguinte sintaxe:

Sintaxe:  INDENTIFICAR OP_ATRIB ( IDENTIFICADOR | NÚMERO ) ( OP_ARIT ( IDENTIFICADOR | NÚMERO )  )*  PV

Sendo que:

INDENTIFICAR   = Inicia por uma letra minúscula, seguido por uma quantidade qualquer de letras minúsculas, dígitos
ou underline.

OP_ATRIB       = Representa o caractere   '='

NÚMERO         = inicia por um dígito, seguido por uma quantidade qualquer de dígitos, podendo ter opcionalmente
a parte fracionária. Caso ele tenha a parte fracionária, ele recebe o caractere ‘.’ , seguido de uma sequência
de um ou mais dígitos.

OP_ARIT        = Representa os caracteres ( '+' | '-' | '*' |'/' )

PV             = Representa o caractere   ';'
'''


def identificador(string):
    inicial = ord(string[0])
    if not( inicial > 96 and inicial < 123 ):
        return False
    
    for caracter in string:
        decimal = ord( caracter )
        if not( ( decimal > 96 and decimal < 123 ) or (decimal > 47 and decimal < 58) or (decimal == 95)):
            return False
    print('RECEBE[IDENTIFICADOR] = "' + string + '"')
    return True

def numero(string):
    if (string[0] == '.' or string[-1] == '.' or string.count('.') > 1):
        return False
        
    for caracter in string:
        decimal = ord( caracter )
        if not( ( decimal > 47 and decimal < 58 ) or decimal == 46):
            return False
    print('RECEBE[NÚMERO] = "' + string + '"')
    return True

def operadorAtributo(string):
    if not ( string == '=' and len(string) == 1 ):
        return False
    print('RECEBE[OP. ATRIBUIÇÃO] = "' + string + '"')
    return True

def pv(string):
    if not ( string == ';' and len(string) == 1 ):
        return False
    print('RECEBE[P V] = "' + string + '"')
    return True


def operadorAritmetico(string):
    simbolo = ['+','-','*','/']
    if not ( simbolo.count(string) == 1 and len(string) == 1 ):
        return False
    print('RECEBE[OP.ARITMETICO] = "' + string + '"')
    return True


#--------------------------------------------------------------------------------------------
def main(string):
    estado = 0
    logica = 'I'
    anterior = 'vazio'
    ordem  = 0

    string = string.replace(" ",",")
    string = string.replace(";",",;")    
    lista  = string.split(",")

    print('\nESTADO INICIAL: [Q0]')
    print('ESTADO VAZIO  : [Q5]')
    print('ESTADO FINAL  : [Q4]')
    lista = filter(None, lista)
    for tipo in lista:
        print('\nEM ESTADO Q' + str(estado) + ':')
        ordem+=1


 
        if ( identificador(tipo) ):
            logica = 'I'
            if ( anterior == 'vazio' and estado == 0 ):
                estado = 1
            elif (( anterior == 'AT' or anterior == 'AR') and (estado == 2 or estado == 3) ):
                estado = 3
            else:
                estado = 5
                
        elif ( numero(tipo) ):
            logica = 'N'
            if (( anterior == 'AT' or anterior == 'AR') and (estado == 2 or estado == 3) ):
                estado = 3
            else:
                estado = 5
                
        elif ( operadorAtributo(tipo) ):
            logica = 'AT'
            if ( anterior == 'I' and estado == 1 ):
                estado = 2
            else:
                estado = 5
                
        elif ( operadorAritmetico(tipo) ):
            logica = 'AR'
            if (( anterior == 'N' or anterior == 'I') and estado == 3 ):
                estado = 2
            else:
                estado = 5
                
        elif ( pv(tipo) ):
            logica = 'PV'
            if ( (anterior == 'N' or anterior == 'I') and estado == 3 ):
                estado = 4
            else:
                estado = 5
                
        else:
            print('RECEBE[NÃO IDENTIFICADO] = '+ tipo)
            estado = 5

        if (anterior == 'PV'):
            estado = 5
        print('VAI PARA Q' + str(estado))
        anterior = logica


while(True):
    main(input(str('\nDigite uma palavra: ')))










   





























'''






def main(string):
    dicionario={}
    cont = 0
    simbolo = ['+','-','*','/','.','_','=',';']
    string = string.replace(" ","")
    
    #Verifica se termina com ';' e se só tem 1. Também se só tem 1 operador de atribuição
    if not(string[-1] == ';' and string.count(';') == 1 and string.count('=') == 1):
        print('SEM ; ')
        return False

    #Não deixar ter operadores aritmeticos em sequencia
    if (string.count('//') > 0 or string.count('**') > 0 or string.count('++') > 0 or string.count('--') > 0):
        print('\nWARN: Operador aritmetico em sequência.')
        return False

    #Não deixar ter operadores aritmeticos ser o penultimo caracter
    if (simbolo.count(string[-2]) > 0 ) :
        print('\nWARN: Operador aritmetico fora do padrão.')
        return False
   
    string = string.replace(";",",;")    
    string = string.replace("+",",+,")
    string = string.replace("-",",-,")
    string = string.replace("*",",*,")
    string = string.replace("/",",/,")
    string = string.replace("=",",=,")
    lista = string.split(",")

    #Verifica se inicia 1° = É um identificador, 2° = É um operador de atribuição
    palavra = lista[0]
    inicio  = ord(palavra[0])
    if not( ( inicio > 96 and inicio < 123 ) and ( lista[1] == '=' ) ):
        print('nao atende requisitos;')
        return False

    #Verifica se operador de atribuição não tem um operador aritmetico a frente
    if not( lista[2] != '*' or  lista[2] != '+'  or  lista[2] != '-' or  lista[2] != '/' ):
        print('\nWARN: Operador de atribuição está seguido por um operador aritmetico')
        return False

    for palavra in lista:
        inicial = ord(palavra[0])

        #Não deixar ter pontuação errada caso seja número. Não deixa iniciar com 
        if (palavra[0] == '.' or palavra[-1] == '.' or palavra.count('.') > 1):
            print('FORA DO PADRÃO NUMERO')
            return False

        #Verifica se é o alfabeto usado está de acordo
        for letra in palavra:
            decimal = ord(letra)
            if not( ( decimal > 96 and decimal < 123 ) or (decimal > 47 and decimal < 58) or (simbolo.count(letra) > 0) ):
                print('FORA DO PADRÃO')
                return False
            
        #Verifica se é identificador
        if ( ( inicial > 96 and inicial < 123 )):
            dicionario['Passo ' + str(cont)+ ' - IDENTIFICADOR' ] = palavra
            cont +=1

        #Verifica se é número
        elif ( ( inicial > 47 and inicial < 58 )):
            for letra in palavra:
                letra = ord(letra)
                if not( ( letra > 47 and letra < 58 ) or letra == 46):
                    print('FORA DO PADRÃO')
                    return False
            
            dicionario['Passo ' + str(cont)+ ' - NÚMERO' ] = palavra
            cont +=1

        #Verifica se é um operador de atribuição
        elif (palavra[0] == '='):
            dicionario['Passo ' + str(cont)+ ' - OP.ATRIB' ] = palavra
            cont +=1

        #Verifica se é um ponto e virgula
        elif (palavra[-1] == ';' ):
            dicionario['Passo ' + str(cont)+ ' - PV' ] = palavra
            cont +=1
            
        #Verifica se é um operador de aritmetico
        elif (simbolo.count(palavra) > 0 and len(palavra) == 1 and palavra != '_'):
            dicionario['Passo ' + str(cont)+ ' - OP.ARIT' ] = palavra
            cont +=1
        else:
            print('NÃO FOI CLASSIFICADO')
            return False


    for passos in dicionario:
        print(passos +': '+ '\n' + '"'+dicionario[passos]+'"')

while(True):
    main(input(str('\nDigite uma palavra: ')))
'''
