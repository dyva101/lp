def add_person(base_dados_pessoas, nome, idade, cidade, hobbies) -> list:
    pessoa = {nome, idade, cidade, hobbies}
    
    for pessoa in base_dados_pessoas:
        if base_dados_pessoas["name"] == nome:
            return print(base_dados_pessoas)
            break
        
    if idade > 100 or idade < 0 :
        raise ValueError("A idade deve ser um inteiro entre 0 e 100\n\n")
        
    if type(cidade) == str:
        raise TypeError("Tipo de dados inválido\n\n")
    
    if len(hobbies) == 0:
        print(base_dados_pessoas, "\n\n")
        raise ValueError()
        
    base_dados_pessoas.append(pessoa)
    
    return base_dados_pessoas
                