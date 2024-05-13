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
    5. Set and manipulation of sets

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
    base_dados_pessoas : list

    Returns
    -------
    hobbies_conjunto : set.

    """ 
    hobbies_conjunto = set()
    hobbies_conjunto = set()
    
    for pessoa in base_dados_pessoas:
        for chave in pessoa.keys():
            if chave == "hobbies":
                hobbies_conjunto.update(pessoa["hobbies"])
                
    return hobbies_conjunto


def get_people_by_hobbies(base_dados_pessoas, hobbies_list):
    """get_people_by_hobbies
    

    Parameters
    ----------
    base_dados_pessoas : list
    hobbies_list: list

    Returns
    -------
    people_list: list

    """ 
    people_list = list()
    
    for pessoa in base_dados_pessoas:
        for hobby in hobbies_list: 
            for x in pessoa["hobbies"]:
                if hobby == x:  
                    people_list.append(pessoa["name"])

                
    return people_list  

def tinder(base_dados_pessoas, name=None, min_age=None, max_age=None, city=None, hobbies=[]):
    """match_people

    Parameters
    ----------
    base_dados_pessoas : list
    name: string
    min_age: int
    max_age: int
    city: string
    hobbies: list

    Returns
    -------
    tinder_list: list

    """
    tinder_list = list()

    if min_age > max_age:
        raise ValueError("Ô querido, vamos estar sendo coerentes? Menor idade é a menor das contas inferiores do conjunto de idade, portanto, é menor do a máxima idade, que é a maior das cotas superiores")

    for pessoa in base_dados_pessoas:
        if (pessoa["age"] < max_age and pessoa["age"] > min_age) or (bool(min_age) == False and pessoa["age"] < max_age) or (bool(max_age) == False and pessoa["age"] > min_age) or (bool(max_age) == False and bool(min_age) == False):
            if (pessoa["name"] == name) or (bool(name) == False):
                if (pessoa["city"] == city) or (bool(city) == False):
                    if set(hobbies).issubset(set(pessoa["hobbies"])):
                        tinder_list.append(pessoa["name"])
    
    return tinder_list


def get_people_by_hobbies(base_dados_pessoas, hobbies):
    """get_people_by_hobbies
    

    Parameters
    ----------
    base_dados_pessoas : list
        
    hobbies : string
        

    Returns
    -------
    ordered_list_people_by_hobbies : list

    """
    list_people_by_hobbies = list()
    
    def get_age(nome):
        for pessoa in base_dados_pessoas:
            if pessoa["name"] == nome:
                age = pessoa["age"]
                
        return age 
    
    for hobby in hobbies:
        for pessoa in base_dados_pessoas:
            for hobby_from_list in pessoa["hobbies"]:
                if hobby == hobby_from_list and pessoa["name"] != (name for name in list_people_by_hobbies):
                    list_people_by_hobbies.append(pessoa["name"])
                    list_people_by_hobbies.sort(key=get_age)
                    
    return list_people_by_hobbies
                    
    