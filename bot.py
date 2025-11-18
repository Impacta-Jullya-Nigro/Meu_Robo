import datetime
import pandas
import csv


def coletar_dados():
    return [
        {"data": datetime.date.today(), "evento": "Processamento finalizado", "status": "OK"},
    ]

def salvar_relatorio(dados):
    df = pandas.DataFrame(dados)
    df.to_csv('dados/relatorio.csv', index=False)
    print("Relatório salvo com sucesso!")

if __name__ == '__main__':
    print("Iniciando Robô...")
    dados = coletar_dados()
    salvar_relatorio(dados)