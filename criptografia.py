import numpy as np

def texto_para_vetor(texto):
    # Converte letras para números (A=0, B=1, ...)
    texto = texto.upper().replace(" ", "")
    return [ord(char) - ord('A') for char in texto]

def vetor_para_texto(vetor):
    # Converte números de volta para letras
    return "".join([chr(int(num) + ord('A')) for num in vetor])

# 1. Configuração da Chave (Matriz Inversível)
# Importante: A matriz deve ser inversível em módulo 26
chave = np.array([[3, 3], [2, 5]])

# 2. O Texto Original (deve ter tamanho par para uma matriz 2x2)
mensagem = "HELP"
vetor_msg = texto_para_vetor(mensagem)
# Reshape para matriz: cada linha é um par de letras
matriz_msg = np.array(vetor_msg).reshape(-1, 2)

# 3. Criptografia
# Multiplicação de matrizes: (Mensagem * Chave) mod 26
resultado_cripto = np.dot(matriz_msg, chave) % 26
msg_final = vetor_para_texto(resultado_cripto.flatten())

print(f"Mensagem Original: {mensagem}")
print(f"Mensagem Criptografada: {msg_final}")