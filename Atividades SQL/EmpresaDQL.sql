-- ============================================================
-- SCRIPT DE CRIAÇÃO E POVOAMENTO ROBUSTO DO BANCO DE DADOS
-- Banco de Dados: EMPRESA_DQL (MS SQL Server)
-- ============================================================

IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'EMPRESA_DQL')
BEGIN
    CREATE DATABASE EMPRESA_DQL;
END;
GO

USE EMPRESA_DQL;
GO

-- PROJETA TODOS OS CAMPOS
select * from DEPARTAMENTO

-- PROJETA APENA NOME NUMERO
select dNome, Dnumero from DEPARTAMENTO

select * from FUNCIONARIO

-- CALCULO EM TEMPO DE EXECUÇÃO
select PNome,Salario,
    (Salario * 1.16) as discidio
    from FUNCIONARIO

--TRAZER APENAS DUAS CASAS DECIMAIS
select PNome,Salario,
    round((Salario * 1.16),2) as discidio
    from FUNCIONARIO

--FILTROS DENTRO DO SELECT
SELECT * FROM FUNCIONARIO

-- TODOS OS FUNCIONARIOS QUE GANHAM MAIS QUE 6000
-- maior igual
SELECT * FROM FUNCIONARIO
WHERE Salario >= 8679.16

SELECT * FROM FUNCIONARIO
WHERE Salario > 8679.16


--menor
--menor igual

--diferente
select * from FUNCIONARIO
where SNome <> 'Ferreira'

--igualdade
select * from FUNCIONARIO
where SNome = 'Ferreira'


--LOGICA BOOLEANA
select * FROM FUNCIONARIO
WHERE SNome = 'Ferreira' and
Salario > 10000

--UTILIZANDO O OU
select * FROM FUNCIONARIO
WHERE SNome = 'Ferreira' or
Salario > 10000

--COMBINANDO MAIS DE UM OPERADOR LOGICO
select * FROM FUNCIONARIO
WHERE
(SNome = 'Ferreira' or SNome = 'Rodrigues')
and Salario > 10000

--PROJETO APENAS ALGUNS CAMPOS
select PNome,SNome,Salario fROM FUNCIONARIO
WHERE
(SNome = 'Ferreira' or SNome = 'Rodrigues')
and Salario > 10000

--agregadores
-- totalizador/count
select count(*) as 'totalFuncionario'  
from FUNCIONARIO

select sum(Salario) as 'SomaDoSalario'
from FUNCIONARIO

select min(salario) as 'MenorSalario',
max(salario) as 'MaiorSalario',
avg(salario) as 'Salario médio'
 from FUNCIONARIO

--AGRUPANDO POR CIDADE
select Cidade from FUNCIONARIO
group by Cidade

--QUANTOS FUNCIONARIOS NOS TEMOS POR CIDADE
SELECT cidade,count(*) from FUNCIONARIO
group by Cidade
order by count(*)

--QUANTO É O TOTAL DE SALARIO POR CIDADE
SELECT cidade,count(*) AS 'QTD_FUNC',
    SUM(Salario) as somaCidade
from FUNCIONARIO
group by Cidade
order by sum(Salario) desc

SELECT cidade,count(*) AS 'QTD_FUNC',
    SUM(Salario) as somaCidade,
    avg(salario)
from FUNCIONARIO
group by Cidade
order by sum(Salario) desc

--QUANTAS HORAS CADA CPF
-- TRABALHOU NOS PROJETOS
select * from TRABALHA_EM

select F_CPF,
sum(Horas) from TRABALHA_EM
group by F_CPF
order by sum(horas)

--quantos departamentos
-- possuem projeto

select * from PROJETO

select distinct(dnum) from projeto

select dnum,count(dnum) from projeto
group by DNum

select count(distinct(dnum))
from projeto

