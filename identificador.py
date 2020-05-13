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


#FUNÇÃO PARA VALIDAR UM IDENTIFICADOR
def identificador(string):
    inicial = ord(string[0])
    if not( inicial > 96 and inicial < 123 ):
        return False
    
    for caracter in string:
        decimal = ord( caracter )
        if not( ( decimal > 96 and decimal < 123 ) or (decimal > 47 and decimal < 58) or (decimal == 95)):
            return False
    return True

#FUNÇÃO PRA VALIDAR SEQUÊNCIA DE NÚMERO
# ( [0-9]([0-9])* ) | ( [0-9] ([0-9])* '.' [0-9]([0-9])* )
def numero(string):
    if (string[0] == '.' or string[-1] == '.' or string.count('.') > 1):
        return False
        
    for caracter in string:
        decimal = ord( caracter )
        if not( ( decimal > 47 and decimal < 58 ) or decimal == 46):
            return False
    return True

#FUNÇÃO PRA VALIDAR SE A PALAVRA SE O PADRÃO
def validador(string):
    if (string.count(' ') > 0 or string.count('//') > 0 or string.count('**') > 0 or string.count('++') > 0 or string.count('--') > 0):
        return False
    if( (string == '' ) or (string == ';') or (string[-1] != ';') ):
        return False

    string = string.replace("+",",")
    string = string.replace("-",",")
    string = string.replace("*",",")
    string = string.replace("/",",")
    string = string.replace(";","")
    lista = string.split(",")
   
    return lista

def main( string ):
    lista = validador(string)
    if not lista:
        print( "\nWARN: Fora do padrão" )
        return False
        
    for palavra in lista:
        if( identificador( palavra ) == False and numero( palavra ) == False):
            print( "\nWARN: Fora do padrão" )
            return False
    print('\nEssa palavra é Válida')

while(True):
    main(input(str('\nDigite uma palavra: ')))


