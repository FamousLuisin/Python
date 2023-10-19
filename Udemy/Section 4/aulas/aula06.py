# Closure

def criar_saudacao(mensagem):
    
    def saudar(nome):
        return f"{mensagem}, {nome}"
    # Quando fazemos isso, o python nn termina de executar a ultima função "saudar()" 
    # Por isso ele deixa os argumentos salvos, para caso precise terminar
    return saudar 

falar_bom_dia = criar_saudacao("Bom dia")
falar_boa_noite = criar_saudacao("Boa noite")

# Aqui ele esta terminando de executar a função "saudar()"
# É devolvido para falar_bom_dia o nome/localização da função, e quando colocado em parenteses ele a executa
# Isso serve para poder adiar a execução logo, adiando nesse caso o parametro ("nome")
print(falar_bom_dia("Luis")) 
print(falar_boa_noite("Luis"))

for nome in ["Noc", "Flinston", "Jhonson"]:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))