import os

caminho_pasta = input("Digite o caminho da pasta: ")

for nome_arquivo in os.listdir(caminho_pasta):
    caminho_completo = os.path.join(caminho_pasta, nome_arquivo)
    nome_sem_extensao, extensao = os.path.splitext(nome_arquivo)
    
    # Verifica se a extensão é ".mp3"
    if extensao != ".mp3":
        novo_nome = nome_sem_extensao + ".mp3"
        novo_caminho = os.path.join(caminho_pasta, novo_nome)
        os.rename(caminho_completo, novo_caminho)

print("Arquivos renomeados com sucesso!")
