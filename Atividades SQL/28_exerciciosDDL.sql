USE EMPRESA;
GO

-- =============================================
-- PARTE 1: DDL (Data Definition Language)
-- =============================================

-- Criação das colunas adicionais logo no início (evita aviso de Intellisense no VS Code)
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'FUNCIONARIO' AND COLUMN_NAME = 'Cargo')
BEGIN
    ALTER TABLE FUNCIONARIO ADD Cargo VARCHAR(100);
END;
GO

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'FUNCIONARIO' AND COLUMN_NAME = 'ativo')
BEGIN
    ALTER TABLE FUNCIONARIO ADD ativo BIT NOT NULL DEFAULT 1;
END;
GO

-- 1. Tabela de Auditoria
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Historico_Salario')
BEGIN
    CREATE TABLE Historico_Salario (
        id_historico INT IDENTITY(1,1) CONSTRAINT PK_Historico_Salario PRIMARY KEY,
        id_emp VARCHAR(11) NOT NULL,
        salario_antigo DECIMAL(10,2),
        salario_novo DECIMAL(10,2),
        data_alteracao DATETIME DEFAULT GETDATE(),
        CONSTRAINT FK_Historico_Salario_Funcionario FOREIGN KEY (id_emp) REFERENCES FUNCIONARIO(CPF)
    );
END;
GO

-- 2. Restrição CHECK
IF NOT EXISTS (SELECT * FROM sys.check_constraints WHERE name = 'CHK_FUNCIONARIO_SALARIO')
BEGIN
    ALTER TABLE FUNCIONARIO
    ADD CONSTRAINT CHK_FUNCIONARIO_SALARIO CHECK (Salario >= 1412.00);
END;
GO

-- 3. ON DELETE CASCADE
IF EXISTS (SELECT * FROM sys.foreign_keys WHERE name = 'FK_TRABALHA_EM_PROJETO')
BEGIN
    ALTER TABLE TRABALHA_EM DROP CONSTRAINT FK_TRABALHA_EM_PROJETO;
END;
GO

ALTER TABLE TRABALHA_EM
ADD CONSTRAINT FK_TRABALHA_EM_PROJETO
FOREIGN KEY (P_Numero) REFERENCES PROJETO(PNumero)
ON DELETE CASCADE;
GO

-- 4. Índice Composto (Execução Segura)
IF NOT EXISTS (SELECT * FROM sys.indexes WHERE name = 'IX_FUNCIONARIO_SNOME_PNOME' AND object_id = OBJECT_ID('FUNCIONARIO'))
BEGIN
    EXEC('CREATE INDEX IX_FUNCIONARIO_SNOME_PNOME ON FUNCIONARIO (SNome, PNome);');
END;
GO

-- 5. Alteração de Coluna e Valor Padrão
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'DEPARTAMENTO' AND COLUMN_NAME = 'orcamento_anual')
BEGIN
    ALTER TABLE DEPARTAMENTO
    ADD orcamento_anual DECIMAL(12, 2) CONSTRAINT DF_DEPARTAMENTO_ORCAMENTO DEFAULT 100000.00;
END;
GO

-- 6. Modelagem Temporal (SCD Tipo 2)
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Historico_Cargo_Empregado')
BEGIN
    CREATE TABLE Historico_Cargo_Empregado (
        id_historico INT IDENTITY(1,1) CONSTRAINT PK_Historico_Cargo PRIMARY KEY,
        id_emp VARCHAR(11) NOT NULL,
        cargo VARCHAR(100) NOT NULL,
        data_inicio DATE NOT NULL,
        data_fim DATE NULL,
        atual BIT NOT NULL DEFAULT 1,
        CONSTRAINT FK_Historico_Cargo_Funcionario FOREIGN KEY (id_emp) REFERENCES FUNCIONARIO(CPF)
    );
END;
GO

-- 7. Reestruturação de Chave Composta
IF EXISTS (SELECT * FROM sys.key_constraints WHERE name = 'PK_TRABALHA_EM')
BEGIN
    ALTER TABLE TRABALHA_EM DROP CONSTRAINT PK_TRABALHA_EM;
END;
GO

IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'TRABALHA_EM' AND COLUMN_NAME = 'data_alocacao')
BEGIN
    ALTER TABLE TRABALHA_EM ADD data_alocacao DATE NOT NULL DEFAULT GETDATE();
END;
GO

IF NOT EXISTS (SELECT * FROM sys.key_constraints WHERE name = 'PK_TRABALHA_EM')
BEGIN
    ALTER TABLE TRABALHA_EM
    ADD CONSTRAINT PK_TRABALHA_EM PRIMARY KEY CLUSTERED (F_CPF ASC, P_Numero ASC, data_alocacao ASC);
END;
GO

-- 8. Chave Única (UNIQUE)
IF NOT EXISTS (SELECT * FROM sys.key_constraints WHERE name = 'UNQ_DEPARTAMENTO_DNOME')
BEGIN
    ALTER TABLE DEPARTAMENTO ADD CONSTRAINT UNQ_DEPARTAMENTO_DNOME UNIQUE (DNome);
END;
GO

-- 9. Desativação Temporária de Constraint
ALTER TABLE FUNCIONARIO NOCHECK CONSTRAINT FK_FUNCIONARIO_SUPERVISOR;
GO
ALTER TABLE FUNCIONARIO CHECK CONSTRAINT FK_FUNCIONARIO_SUPERVISOR;
GO


-- =============================================
-- PARTE 2: DML (Data Manipulation Language)
-- =============================================

-- 1. Reajuste Condicional de Salário
UPDATE F
SET F.Salario = F.Salario * 1.12
FROM FUNCIONARIO F
WHERE EXISTS (
    SELECT 1 
    FROM TRABALHA_EM T
    INNER JOIN PROJETO P ON T.P_Numero = P.PNumero
    WHERE T.F_CPF = F.CPF AND P.DNum = F.DNR
);
GO

-- 2. Transferência de Setor e Gestão
UPDATE F
SET F.DNR = (SELECT DNumero FROM DEPARTAMENTO WHERE DNome = 'TI'),
    F.Supervisor_CPF = (SELECT Gerente_CPF FROM DEPARTAMENTO WHERE DNome = 'TI')
FROM FUNCIONARIO F
WHERE F.DNR = (SELECT DNumero FROM DEPARTAMENTO WHERE DNome = 'Recursos Humanos');
GO

-- 3. Inserção Condicional
INSERT INTO TRABALHA_EM (F_CPF, P_Numero, Horas, data_alocacao)
SELECT F.CPF, P.PNumero, 10.00, GETDATE()
FROM FUNCIONARIO F
CROSS JOIN PROJETO P
WHERE F.CPF = (SELECT TOP 1 CPF FROM FUNCIONARIO)
  AND P.PNumero = (SELECT TOP 1 PNumero FROM PROJETO)
  AND (
      SELECT ISNULL(SUM(Horas), 0) 
      FROM TRABALHA_EM 
      WHERE F_CPF = F.CPF
  ) <= 34;
GO

-- 4. Exclusão com Subquery
DELETE FROM TRABALHA_EM
WHERE P_Numero IN (
    SELECT P.PNumero
    FROM PROJETO P
    WHERE P.Localizacao NOT LIKE '%São Paulo%'
);
GO

-- 5. Promoção Automatizada (via SQL dinâmico para evitar aviso no VS Code)
EXEC('
UPDATE FUNCIONARIO
SET Cargo = ''Supervisor de Equipe''
WHERE CPF IN (
    SELECT Supervisor_CPF
    FROM FUNCIONARIO
    WHERE Supervisor_CPF IS NOT NULL
    GROUP BY Supervisor_CPF
    HAVING COUNT(*) >= 2
);
');
GO

-- 6. Limpeza de Dados Inativos
DELETE FROM DEPARTAMENTO
WHERE DNumero NOT IN (SELECT DISTINCT DNR FROM FUNCIONARIO WHERE DNR IS NOT NULL)
  AND DNumero NOT IN (SELECT DISTINCT DNum FROM PROJETO WHERE DNum IS NOT NULL);
GO

-- 7. Normalização de Limite Salarial
UPDATE FUNCIONARIO
SET Salario = 15000.00
WHERE (Salario * 1.15) > 15000.00;
GO

-- 8. Carga em Lote (Snapshot)
INSERT INTO Historico_Salario (id_emp, salario_antigo, salario_novo, data_alteracao)
SELECT F.CPF, F.Salario, F.Salario, GETDATE()
FROM FUNCIONARIO F
INNER JOIN DEPARTAMENTO D ON F.DNR = D.DNumero
WHERE D.DNome = 'Financeiro';
GO

-- 9. Upsert (MERGE)
MERGE TRABALHA_EM AS Target
USING (
    SELECT 
        (SELECT TOP 1 CPF FROM FUNCIONARIO) AS F_CPF, 
        (SELECT TOP 1 PNumero FROM PROJETO) AS P_Numero, 
        15.00 AS Horas
) AS Source
ON (Target.F_CPF = Source.F_CPF AND Target.P_Numero = Source.P_Numero)
WHEN MATCHED THEN
    UPDATE SET Target.Horas = Target.Horas + Source.Horas
WHEN NOT MATCHED THEN
    INSERT (F_CPF, P_Numero, Horas, data_alocacao)
    VALUES (Source.F_CPF, Source.P_Numero, Source.Horas, GETDATE());
GO

-- 10. Soft Delete (via SQL dinâmico)
EXEC('
UPDATE FUNCIONARIO
SET ativo = 0
WHERE YEAR(DataNasc) < 1980;
');
GO


-- =============================================
-- PARTE 3: DQL (Data Query Language) / CONSULTAS
-- =============================================

-- 1. Agregação e Filtro de Grupo (HAVING)
SELECT D.DNome
FROM DEPARTAMENTO D
INNER JOIN FUNCIONARIO F ON D.DNumero = F.DNR
GROUP BY D.DNumero, D.DNome
HAVING AVG(F.Salario) > (SELECT AVG(Salario) FROM FUNCIONARIO);
GO

-- 2. Auto-Relacionamento (Self-Join)
EXEC('
SELECT 
    F.PNome + '' '' + F.SNome AS Nome_Colaborador,
    F.Cargo,
    ISNULL(S.PNome + '' '' + S.SNome, ''Sem Supervisor'') AS Nome_Supervisor,
    S.Salario AS Salario_Supervisor
FROM FUNCIONARIO F
LEFT JOIN FUNCIONARIO S ON F.Supervisor_CPF = S.CPF;
');
GO

-- 3. Subquery Correlacionada
SELECT 
    F.PNome + ' ' + F.SNome AS Nome_Empregado,
    F.Salario
FROM FUNCIONARIO F
WHERE F.Salario > (
    SELECT AVG(F2.Salario)
    FROM FUNCIONARIO F2
    WHERE F2.DNR = F.DNR
);
GO

-- 4. Funções de Janela (Ranking)
SELECT 
    F.PNome + ' ' + F.SNome AS Nome_Empregado,
    D.DNome AS Departamento,
    F.Salario,
    DENSE_RANK() OVER (PARTITION BY F.DNR ORDER BY F.Salario DESC) AS Posicao_Ranking
FROM FUNCIONARIO F
INNER JOIN DEPARTAMENTO D ON F.DNR = D.DNumero;
GO

-- 5. Desvio Salarial (Window Frame)
SELECT 
    F.PNome + ' ' + F.SNome AS Nome_Empregado,
    D.DNome AS Departamento,
    F.Salario,
    MAX(F.Salario) OVER (PARTITION BY F.DNR) - F.Salario AS Diferenca_Para_Maior_Salario
FROM FUNCIONARIO F
INNER JOIN DEPARTAMENTO D ON F.DNR = D.DNumero;
GO

-- 6. Divisão Relacional
SELECT F.PNome + ' ' + F.SNome AS Nome_Empregado
FROM FUNCIONARIO F
WHERE NOT EXISTS (
    SELECT P.PNumero
    FROM PROJETO P
    INNER JOIN DEPARTAMENTO D ON P.DNum = D.DNumero
    WHERE D.DNome = 'TI'
    EXCEPT
    SELECT T.P_Numero
    FROM TRABALHA_EM T
    WHERE T.F_CPF = F.CPF
);
GO

-- 7. Agregação Condicional
SELECT 
    D.DNome AS Departamento,
    COUNT(F.CPF) AS Total_Funcionarios,
    COUNT(CASE WHEN F.Salario > 7000.00 THEN 1 END) AS Total_Acima_7k,
    CAST(
        (COUNT(CASE WHEN F.Salario > 7000.00 THEN 1 END) * 100.0) / NULLIF(COUNT(F.CPF), 0)
        AS DECIMAL(5,2)
    ) AS Percentual_Acima_7k
FROM DEPARTAMENTO D
LEFT JOIN FUNCIONARIO F ON D.DNumero = F.DNR
GROUP BY D.DNumero, D.DNome;
GO

-- 8. Detecção de Sobrecarga de Jornada
SELECT 
    F.PNome + ' ' + F.SNome AS Nome_Funcionario,
    COUNT(T.P_Numero) AS Qtd_Projetos,
    SUM(T.Horas) AS Total_Horas
FROM FUNCIONARIO F
INNER JOIN TRABALHA_EM T ON F.CPF = T.F_CPF
GROUP BY F.CPF, F.PNome, F.SNome
HAVING COUNT(T.P_Numero) > 1 
   AND SUM(T.Horas) > 40
ORDER BY SUM(T.Horas) DESC;
GO














