# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# Positional-only Parameters (/) - Tudo antes da barra deve
# ser APENAS posicional.
# Keyword-Only Arguments (*) - * sozinho NÃO SUGA valores.
# Tudo depois do * tem q ser nomeado

def soma(a, b, /, *, c, **kwargs):
    print(kwargs)
    print(a + b + c)


soma(1, 2, c=3, nome='teste')