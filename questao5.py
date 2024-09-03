def inverter_string(s):
    resultado = ''

    # metodo range(comeco, fim, tamanho_do_passo)
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    return resultado

entrada_usuario = input("Digite uma string para inverter: ")
string_invertida_usuario = inverter_string(entrada_usuario)
print(f"String invertida (entrada do usuário): {string_invertida_usuario}")
