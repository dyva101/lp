import data
import utils as use

# print(data.people_data)

# print("\n\nQuestão 1: ")

# dados_atualizados = use.add_person(data.people_data, "Gabi", 31, "Palmeira dos Índios", ["ler", "cantar no coral", "matemática"])
# dados_atualizados = use.add_person(data.people_data, "Gabi", 31, "Palmeira dos Índios", ["ler", "cantar no coral", "matemática"])
# print(use.add_person.__doc__)

# for pessoa in dados_atualizados:
#     print(pessoa, sep="\n")
    
# print("\n\nQuestão 2: ")

# dados_atualizados = use.remove_person(data.people_data, "Charlie")

# print(use.remove_person.__doc__)

# for pessoa in dados_atualizados:
#     print(pessoa, sep="\n")

print("\n\nQuestão 3: ")

print("\n", use.get_ages(data.people_data))
