import pyodbc
import os

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-4B3UC4A\SQLEXPRESS;"
    "Database=CalculoIMC;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão bem sucedida!")

cursor = conexao.cursor()

nome = str(input("Digite seu nome: "))
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))
resultado = 1

imc = peso / altura**2
print("Seu IMC é: %.4f" % imc)


if imc < 16:
    resultado = "Magreza grave"
    print("Magreza grave")
elif imc < 17:
    resultado = "Magreza moderada"
    print("Magreza moderada")
elif imc < 18.5:
    resultado = "Magreza leve"
    print("Magreza leve")
elif imc < 25:
    resultado = "Saudável"
    print("Saudável")
elif imc < 30:
    resultado = "Sobrepeso"
    print("Sobrepeso")
elif imc < 35:
    resultado = "Obesidade Grau I"
    print("Obesidade Grau I")
elif imc < 40:
    resultado = "Obesidade Grau II (severa)"
    print("Obesidade Grau II (severa)")
else:
    resultado = "Obesidade Grau III (mórbida)"
    print("Obesidade Grau III (mórbida)")

os.system("pause")



comando = f"""INSERT INTO Dados(nome, peso, altura, resultadoIMC, resultadoFinal)
VALUES
    ('{nome}', {peso}, {altura}, {imc}, '{resultado}')"""

cursor.execute(comando)
cursor.commit()