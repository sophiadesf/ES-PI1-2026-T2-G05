# ----------------------------------------------------------------------------------------------
# MATRIZ CHAVE FIXA 2x2
# CHAVE_MESTRA = [[3, 3], 
#                 [2, 5]]
# ----------------------------------------------------------------------------------------------
CHAVE_MESTRA = [[3, 3], [2, 5]]

# Determinante da matriz: (3*5) - (3*2) = 15 - 6 = 9
DET = 9 

# Inverso multiplicativo de 9 em Z26 é 3 (pois 9 * 3 = 27, e 27 % 26 = 1)
DET_INV_26 = 3

# Inverso multiplicativo de 9 em Z10 é 9 (pois 9 * 9 = 81, e 81 % 10 = 1)
DET_INV_10 = 9

# Matriz Adjunta para a inversão: [[d, -b], [-c, a]] -> [[5, -3], [-2, 3]]
MATRIZ_ADJ = [[5, -3], [-2, 3]]


# ----------------------------------------------------------------------------------------------
# FUNÇÕES AUXILIARES DE MATRIZ (SEM NUMPY)
# ----------------------------------------------------------------------------------------------
def multiplicar_matriz_bloco(matriz, bloco, mod):
    """Multiplica uma matriz 2x2 por um vetor 2x1 sob um módulo."""
    x = (matriz[0][0] * bloco[0] + matriz[0][1] * bloco[1]) % mod
    y = (matriz[1][0] * bloco[0] + matriz[1][1] * bloco[1]) % mod
    return [x, y]

def obter_matriz_inversa(mod, det_inv):
    """Calcula a matriz inversa estritamente sob o módulo fornecido."""
    inversa = [
        [(MATRIZ_ADJ[0][0] * det_inv) % mod, (MATRIZ_ADJ[0][1] * det_inv) % mod],
        [(MATRIZ_ADJ[1][0] * det_inv) % mod, (MATRIZ_ADJ[1][1] * det_inv) % mod]
    ]
    return inversa


# ----------------------------------------------------------------------------------------------
# CRIPTOGRAFIA DA CHAVE DE ACESSO (3 Letras em Z26 + 4 Números em Z10)
# ----------------------------------------------------------------------------------------------
def criptografar_chave_acesso(chave):
    # Separar letras e números sem 're'
    letras = "".join([c for c in chave if c.isalpha()]).upper()
    numeros = "".join([c for c in chave if c.isdigit()])
    
    # Validação simples do formato exigido
    if len(letras) != 3 or len(numeros) != 4:
        raise ValueError("A chave de acesso deve conter exatamente 3 letras e 4 números.")
    
    # --- Parte 1: Letras (Z26) ---
    # Adiciona preenchimento (padding) se o bloco não for par (3 letras -> precisa de 4)
    letras_pad = letras + "A" 
    num_letras = [ord(c) - ord('A') for c in letras_pad]
    
    letras_cripto = ""
    for i in range(0, len(num_letras), 2):
        bloco = num_letras[i:i+2]
        res = multiplicar_matriz_bloco(CHAVE_MESTRA, bloco, 26)
        letras_cripto += "".join(chr(n + ord('A')) for n in res)
        
    # --- Parte 2: Números (Z10) ---
    num_digitos = [int(n) for n in numeros]
    
    numeros_cripto = ""
    for i in range(0, len(num_digitos), 2):
        bloco = num_digitos[i:i+2]
        res = multiplicar_matriz_bloco(CHAVE_MESTRA, bloco, 10)
        numeros_cripto += "".join(str(n) for n in res)
        
    return letras_cripto + numeros_cripto

def descriptografar_chave_acesso(chave_cripto):
    # Separar os blocos resultantes (4 letras e 4 números)
    letras = chave_cripto[:4]
    numeros = chave_cripto[4:]
    
    # --- Parte 1: Decifrar Letras (Z26) ---
    matriz_inv_26 = obter_matriz_inversa(26, DET_INV_26)
    num_letras = [ord(c) - ord('A') for c in letras]
    
    letras_decifradas = ""
    for i in range(0, len(num_letras), 2):
        bloco = num_letras[i:i+2]
        res = multiplicar_matriz_bloco(matriz_inv_26, bloco, 26)
        letras_decifradas += "".join(chr(n + ord('A')) for n in res)
    
    # Remove a letra de preenchimento 'A' colocada no final
    letras_originais = letras_decifradas[:-1]
    
    # --- Parte 2: Decifrar Números (Z10) ---
    matriz_inv_10 = obter_matriz_inversa(10, DET_INV_10)
    num_digitos = [int(n) for n in numeros]
    
    numeros_originais = ""
    for i in range(0, len(num_digitos), 2):
        bloco = num_digitos[i:i+2]
        res = multiplicar_matriz_bloco(matriz_inv_10, bloco, 10)
        numeros_originais += "".join(str(n) for n in res)
        
    return letras_originais + numeros_originais


# ----------------------------------------------------------------------------------------------
# CRIPTOGRAFIA DO CPF (Z26 - Converte Números para Letras)
# ----------------------------------------------------------------------------------------------
def criptografar_cpf(cpf):
    # Limpa deixando apenas números
    cpf_limpo = "".join([c for c in str(cpf) if c.isdigit()])
    
    # CPF tem 11 dígitos, adicionamos "0" para virar par (12)
    if len(cpf_limpo) % 2 != 0:
        cpf_limpo += "0"
        
    # Transforma números em letras de A-J para rodar na Cifra de Hill Z26 original
    letras_convertidas = "".join([chr(int(n) + ord('A')) for n in cpf_limpo])
    
    valores_numericos = [ord(char) - ord('A') for char in letras_convertidas]
    resultado = ""
    for i in range(0, len(valores_numericos), 2):
        bloco = valores_numericos[i:i+2]
        res = multiplicar_matriz_bloco(CHAVE_MESTRA, bloco, 26)
        resultado += "".join(chr(n + ord('A')) for n in res)
    return resultado

def descriptografar_cpf(cpf_cripto):
    matriz_inv_26 = obter_matriz_inversa(26, DET_INV_26)
    valores_numericos = [ord(char) - ord('A') for char in cpf_cripto]
    
    resultado_numeros = ""
    for i in range(0, valores_numericos.__len__(), 2):
        bloco = valores_numericos[i:i+2]
        res = multiplicar_matriz_bloco(matriz_inv_26, bloco, 26)
        resultado_numeros += "".join(str(n) for n in res)
        
    # Remove o "0" de padding adicionado no final
    if resultado_numeros.endswith("0"):
        resultado_numeros = resultado_numeros[:-1]
    return resultado_numeros


# ----------------------------------------------------------------------------------------------
# TESTES DE VALIDAÇÃO
# ----------------------------------------------------------------------------------------------
if __name__ == "__main__":
    print("--- TESTE 1: CHAVE DE ACESSO ---")
    chave_original = "ABC1234"
    chave_enc = criptografar_chave_acesso(chave_original)
    chave_dec = descriptografar_chave_acesso(chave_enc)
    
    print(f"Original:      {chave_original}")
    print(f"Criptografado: {chave_enc} (Note que o bloco de letras virou 4 letras devido ao preenchimento)")
    print(f"Decifrado:     {chave_dec}")
    
    print("\n--- TESTE 2: CPF ---")
    cpf_original = "12345678901"
    cpf_enc = criptografar_cpf(cpf_original)
    cpf_dec = descriptografar_cpf(cpf_enc)
    
    print(f"Original:      {cpf_original}")
    print(f"Criptografado: {cpf_enc}")
    print(f"Decifrado:     {cpf_dec}")
