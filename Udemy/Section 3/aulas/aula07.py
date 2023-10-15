# id é para onde uma variavel esta apontando;

id_iguais_1 = "a"
id_iguais_2 = "a"

id_diferentes_1 = "b"
id_diferentes_2 = "c"

print(f"Iguais = {id(id_iguais_1)} e {id(id_iguais_2)}") # Eles apontam para o mesmo lugar pois isso facilita
print(f"Diferentes = {id(id_diferentes_1)} e {id(id_diferentes_2)}")

