usuario_correto = "admin"
senha_correta = "senha123"
tentativas_max = 3

for tentativa in range(tentativas_max):
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    if usuario == usuario_correto and senha == senha_correta:
        print("Bem-vindo!")
        break
    else:
        tentativas_restantes = tentativas_max - tentativa - 1
        print(f"Credenciais incorretas. Você tem mais {tentativas_restantes} tentativa(s).")

else:
    for _ in range(3):
        print("Acesso bloqueado")