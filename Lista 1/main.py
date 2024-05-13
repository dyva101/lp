import data
import utils as use

print(data.people_data)

print("\n\nQuestão 1: ")

dados_atualizados = use.add_person(data.people_data, "Gabi", 31, "Palmeira dos Índios", ["rir", "comer cuscuz", "cantar funk"])
    
dados_atualizados = use.add_person(data.people_data, "Isabelli", 31, "Palmeira dos Índios", ["ler", "cantar no coral", "matemática"])

for pessoa in dados_atualizados:
    print(pessoa, sep="\n")
    

dados_atualizados = use.add_person(data.people_data, "Gabi", 31, "Palmeira dos Índios", ["rir", "comer cuscuz", "cantar funk"])

print(use.add_person.__doc__)

for pessoa in dados_atualizados:
    print(pessoa, sep="\n")
    
print("\n\nQuestão 2: ")

dados_atualizados = use.remove_person(data.people_data, "Charlie")

print(use.remove_person.__doc__)

for pessoa in dados_atualizados:
    print(pessoa, sep="\n")

print("\n\nQuestão 3: ")

print("\n", use.get_ages(data.people_data))

print("\n\nQuestão 4: ")

print("\n", use.get_hobbies(data.people_data))

print("\n\nQuestão 5: ")

print("\n", use.get_people_by_hobbies(data.people_data, ["ler", "rir"]))

print("\n\nQuestão 6: ")

print("\n", use.tinder(base_dados_pessoas=data.people_data, name="Isabelli", min_age=33, max_age=32, hobbies=["ler", "cantar no coral", "matemática"]))

print("\n\nQuestão 5: ")

print("\n", use.get_people_by_hobbies(data.people_data, {"ler", "cooking", "matemática"}))
