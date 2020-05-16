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
    print('RECEBE[PV] = "' + string + '"')
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

    string = string.replace(" ",",")
    string = string.replace(";",",;")    
    lista  = string.split(",")

    print('\nESTADO INICIAL: [Q0]')
    print('ESTADO LIMBO  : [Q5]')
    print('ESTADO FINAL  : [Q4]')
    
    lista = filter(None, lista)
    
    for tipo in lista:
        print('\nEM ESTADO Q' + str(estado) + ':')
 
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
        
    if (estado == 4 ):
        (print("\n\n--- a operação de atribuição foi aceita ---\n\n"))
    else: 
        print("\n\n--- a operação de atribuição não foi aceita ---\n\n")
        


while(True):
    main(input(str('\nDigite uma palavra: ')))