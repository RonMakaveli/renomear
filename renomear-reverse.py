import os

caminho_pasta = input("Digite o caminho da pasta: ")

for nome_arquivo in os.listdir(caminho_pasta):
    caminho_completo = os.path.join(caminho_pasta, nome_arquivo)
    novo_nome = nome_arquivo[:-10]
    novo_caminho = os.path.join(caminho_pasta, novo_nome)
    os.rename(caminho_completo, novo_caminho)

print("Arquivos renomeados com sucesso!")
