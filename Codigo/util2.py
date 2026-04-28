from datetime import datetime
# from cryptography.fernet import Fernet
import random
import string

def salvar_log(texto):
    """Salva log com timestamp no formato [YYYY-MM-DD HH:MM:SS]"""
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open("historico.txt", "a", encoding="utf-8") as arq:
        arq.write(f"{timestamp} {texto}\n")

def validar_cpf(cpf):
    """Valida CPF matematicamente. Retorna True se válido."""
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os dígitos são iguais (CPF inválido)
    if cpf == cpf[0] * 11:
        return False
    
    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    
    # Verifica o primeiro dígito
    if int(cpf[9]) != digito1:
        return False
    
    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    
    # Verifica o segundo dígito
    if int(cpf[10]) != digito2:
        return False
    
    return True

def validar_titulo(titulo):
    titulo = ''.join(filter(str.isdigit, titulo))

    #verificar se tem os 12 digitos 
    if len(titulo) != 12: 
        return false
    
    #verificar se os digitos sao iguais 
    if titulo == titulo[0] * 12:
        return false
    
    soma = 0 
    pesos = [7,8,9]
    #range(8) porque no titulo, o primeiro digito verificador é calculado usando os 8 primeiros numeros 
    for i in range (8): 
        soma += int(titulo{i}) * pesos[i % 3]

    resto = soma % 11 

    if resto < 2: 
        digito1 = 0 
    else: 
        digito1 = 11 - resto 

    #verifica o primeiro digito
    if int(titulo[10]) != digito1: 
        return false 
    
    #calcula o segundo digito 
    soma = 0 

    for i in range(8): 
        soma += int(titulo[i]) * ((i % 3) + 7)

    #calculo dos 2 numeros do estado UF e do 1 digito verificador
    soma += int(titulo[8]) * 7 
    soma += int(titulo[9]) * 8 
    soma += digito1 * 9 

    resto = soma % 11 

    if resto < 2: 
        digito2 = 0
    else: 
        digito2 = 11 - resto 

    #verifica o segundo digito 
    if int(titulo[11]) != digito2: 
        return false 
    
    return true 
        
             
   
def gerar_chave_acesso():
    """Gera uma chave de acesso única de 8 caracteres alfanuméricos."""
    caracteres = string.ascii_uppercase + string.digits
    return ''.join(random.choice(caracteres) for _ in range(8))
