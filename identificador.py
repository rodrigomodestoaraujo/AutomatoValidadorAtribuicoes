def identificador(string):
    string = list(string)
    validade = False
    if (((ord(string[0]) > 96) and (ord(string[0]) < 123)) and (ord(string[0]) != 95)):
        for i in range(len(string)):
            for j in range (97, 123):
                if ((ord(string[i]) > 96 and ord(string[i]) < 123) or (ord(string[i]) > 47 and ord(string[i]) < 58) or (ord(string[i]) == 95)):
                    validade = True;
                    break;
                else:
                    validade = False;
                    break;
            if (validade == False):
                break;
    return validade

def numero(numero): 
    numero = list(numero)
    validade = False
    if (numero.count('.') > 1): 
        return validade
    if (((ord(numero[0]) > 47 and ord(numero[0]) < 58))):
        for i in range(len(numero)):
            for j in range (47, 58):
                if ((ord(numero[i]) > 47 and ord(numero[i]) < 58) or (ord(numero[i]) == 46)): 
                    validade = True;
                    break;
                else:
                    validade = False
                    break
            if (validade == False):
                break;  
    return validade

def main(string): 
    
    string = string.replace(" ", "")
    
    if (string.count("//") > 0 or string.count("**") > 0 or string.count("++") > 0 or string.count("--") > 0):
        return ('Automato não validado')
    
    if (string[-1] != ';' ):
        return ('Automato não validado')
    
    string = string.replace(";","")
    string = string.replace("+",",")
    string = string.replace("-",",")
    string = string.replace("*",",")
    string = string.replace("/",",")
    string = string.split(",")

    if ((string)) == ([""]) :
        return ('Automato não validado')
    
    for i in range (len(string)): 
        if (identificador(string[i]) == False and numero((string[i])) == False):
            return ('Automato não validado')
        
    return ('Automato validado')


print(main(' '))
        
'asdasd + asdasdas ++ asdsadasd;'
# '0a;' , 'a+++sasa;' ';' , ' '
    

    



        
    
    

