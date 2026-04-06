CREATE DATABASE sistema_eleicao;
USE sistema_eleicao;
-- Tabela de Candidatos (Necessária para validar o número do voto)
CREATE TABLE candidatos (
    numero INT PRIMARY KEY,
    nome_candidato VARCHAR(100) NOT NULL,
    partido VARCHAR(20) NOT NULL
);
-- Tabela de Usuários (Eleitores)
CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    cpf VARCHAR(11) UNIQUE NOT NULL,
    -- UNIQUE impede CPFs repetidos
    nome_completo VARCHAR(100) NOT NULL,
    login VARCHAR(50) UNIQUE NOT NULL,
    -- UNIQUE impede logins repetidos
    senha VARCHAR(255) NOT NULL,
    -- Recomenda-se salvar como Hash
    numero_voto INT DEFAULT NULL,
    -- O número que ele votou
    ja_votou BOOLEAN DEFAULT FALSE,
    -- Controle de voto único
    FOREIGN KEY (numero_voto) REFERENCES candidatos(numero)
);
-- Tabela de Mesários
CREATE TABLE mesarios (
    id_mesario INT AUTO_INCREMENT PRIMARY KEY,
    cpf VARCHAR(11) UNIQUE NOT NULL,
    nome_completo VARCHAR(100) NOT NULL,
    login VARCHAR(50) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL
)