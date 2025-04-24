import os
import time

salario : float
salario_irrf : float
desconto_irrf = 0

def limpar_terminal():
    # Limpando o terminal
    os.system("cls || clear")

def inss(salario):
    if salario <= 1320.0:
        desconto_inss = salario * 0.075
    elif salario >= 1320.01 and salario <= 2571.29:
        desconto_inss = salario * 0.09
    elif salario >= 2571.20 and salario <= 3856.94:
        desconto_inss = salario * 0.12
    elif salario >= 3856.95 and salario <= 7507.49:
        desconto_inss = salario * 0.14
    return min(desconto_inss, 1051.05)

def irrf(salario, dependente):
    deducao_dependente = 189.59 * dependente
    salario_irrf = salario - deducao_dependente
    if salario_irrf >= 2112.01:
        desconto_irrf = salario_irrf * 0.075
    if salario_irrf >= 2826.25:
        desconto_irrf = salario_irrf * 0.15
    if salario_irrf >= 3544.01:
        desconto_irrf = salario_irrf * 0.225
    if salario_irrf >= 4256.01:
        desconto_irrf = salario_irrf * 0.275
    return desconto_irrf

# Login
limpar_terminal()
print("== Bem vindo ao sistema de folha de pagamento ==\n")
matricula = input("Digite o seu RA/Matrícula: ")
senha = input("Digite a sua senha: ")

# Entrada de dados
limpar_terminal()
print("== Vales e Sálario ==\n")

salario_base = float(input("Digite o seu sálario base: R$ "))
vale_transporte = int(input("Deseja receber o valor transporte? Digite '1' para sim e '2' para não: "))
valor_vale_refeicao = float(input("Digite o valor do vale refeição fornecido pela sua empresa: R$ "))

# Cálculos dos descontos
dependente = 1
desconto_inss = inss(salario_base)
desconto_irrf = irrf(salario_base, dependente)
if vale_transporte == 1:
    vale_transporte = salario_base * 0.06
else:
    0
vale_refeicao = valor_vale_refeicao * 0.20
plano_saude = 150.00 * dependente

desconto_total = desconto_inss + desconto_irrf + vale_transporte + vale_refeicao + plano_saude
salario_liquido = salario_base - desconto_total

# Exibindo os resultados
limpar_terminal()
print("== Segue a sua Folha de Pagamento ==\n")
time.sleep(2)
print(f"Matrícula inserida: {matricula}")
print(f"Seu sálario base: {salario_base:.2f}\n")
print("-- INSS e IRRF --")
print(f"Desconto do INSS: {desconto_inss:.2f}")
print(f"Desconto do IRRF: {desconto_irrf:.2f}\n")
print("-- Outros Descontos --")
print(f"Desconto Vale Transporte: {vale_transporte:.2f}")
print(f"Desconto Vale Refeição: {vale_refeicao:.2f}")
print(f"Desconto Plano de Saúde: {plano_saude:.2f}\n")
print("-- Resultado --")
print(f"Desconto Total: {desconto_total:.2f}")
print(f"Sálario Líquido: {salario_liquido:.2f}")