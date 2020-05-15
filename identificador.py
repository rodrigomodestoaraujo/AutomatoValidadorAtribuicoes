''' CASO:
Modelar e implementar um autômato que faça valicação de atribuições, essa atribuição dese ter a seguinte sintaxe:

Sintaxe:  INDENTIFICAR OP_ATRIB ( IDENTIFICADOR | NÚMERO ) ( OP_ATRIB ( IDENTIFICADOR | NÚMERO )  )*  PV

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

# IDENTIFICADOR: [a-z] ( [a-z] | [0-9] | [_] )*
# NÚMERO: ( [0-9]([0-9])* ) | ( [0-9] ([0-9])* '.' [0-9]([0-9])* )

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
