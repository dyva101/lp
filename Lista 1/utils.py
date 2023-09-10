"""Módulo

This module contains the asked functions, and in its whole, completes
the Set 1 (Lista 1, by Almir Sater). It presumes you're the module __data__, 
which contains a list of dictionaries, base for the set of exercises!

The following structures and concepts were key for the full comprehension of
the set:
    1. Lists of dictionaries (how we acess their itens)
    2. Exception Treatment
    3. Temporary variables in loops
    4. List Comprehension

"""

def add_person(base_dados_pessoas, nome, idade, cidade, hobbies) -> dict:
    """add_person
    It modifies your database (list) in order to include a new person
    
    Parameters
    ----------
    base_dados_pessoas: list
    nome: str
    idade: int
    cidade: str
    hobbies: list
    
    Returns
    ----------
    base_dados_pessoas : list
    """
    nova_pessoa = {"name": nome, "age": idade, "city": cidade, "hobbies": hobbies}
    
    #Notar que a ordem das exceções é importante, porque se colocarmos
    #o erro de duplicação de nome ANTES, ele irá mostrar já a base de
    #dados como se não tivesse problema, mas na verdade temos que 
    #garantir que os dados inseridos estão dentro do padrão esperado
    #de tipos.
    
    
    if idade > 100 or idade < 0 :
        raise ValueError("A idade deve ser um inteiro entre 0 e 100\n\n")
        
    if type(cidade) != str:
        raise TypeError("Tipo de dados do campo 'Cidade' inválido\n\n")
    
    if len(hobbies) == 0:
        print(base_dados_pessoas, "\n\n")
        raise ValueError()
    
    for pessoa in base_dados_pessoas:
        if pessoa["name"] == nome:
            print("\n\nAtenção: essa pessoa já se encontra incluída entre os dados!\n\n")
            return base_dados_pessoas
        
    base_dados_pessoas.append(nova_pessoa)
        
    return base_dados_pessoas

def remove_person(base_dados_pessoas, nome):
    """remove_person
    It modifies your database (list) in order to exclude a person
    
    Parameters
    ----------
    base_dados_pessoas: list
    nome: str

    Returns
    ----------
    base_dados_pessoas : list
    """
    checar_existencia = False
    
    for pessoa in base_dados_pessoas:
        if pessoa["name"] == nome:
            checar_existencia = True
    
    if checar_existencia == False:
        print("Pessoa não incluída ainda na base de dados. Para incluí-la, ver método add_person.")
        return base_dados_pessoas
    
    base_dados_pessoas = [pessoa for pessoa in base_dados_pessoas if pessoa["name"] != nome]
    
    return base_dados_pessoas

def get_ages(base_dados_pessoas):
    """get_ages
    It provides the following information about the ages colleted:
        max and min values
        average value of the values
    
    Parameters
    ----------
    base_dados_pessoas: list

    Returns
    ----------
    info_ages : tupla
    """
    
    idades = []
    for pessoa in base_dados_pessoas:
        for chave in pessoa.keys():
            if chave == "age":
                idades.append(pessoa["age"])
    
    menor_idade = min(idades)
    maior_idade = max(idades)
    media_idade = int(sum(idades)/len(idades))  
    
    return (menor_idade, maior_idade, media_idade)

def get_hobbies(base_dados_pessoas):
    """get_hobbies
    

    Parameters
    ----------
    base_dados_pessoas : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """ 
    hobbies_conjunto = {}
    
    for pessoa in base_dados_pessoas:
        for chave in pessoa.keys():
            if chave == "hobbies":
                hobbies_conjunto.append(pessoa["hobbies"])
                
    return hobbies_conjunto