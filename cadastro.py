import json
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu(people: list) -> None:
    print("""
[1] Cadastrar uma pessoa
[2] Listar pessoas
[3] Buscar pessoa
[4] Apagar pessoa
[5] Sair
""")
    print(f"Total de pessoas cadastradas: {len(people)}")


def register(people: list) -> None:
    name = input("Digite o nome: ").strip()

    if not name:
        print("Nome não pode ser vazio.")
        return

    if any(p['name'].lower() == name.lower() for p in people):
        print("Pessoa já cadastrada.")
        return

    while True:
        try:
            age = int(input("Digite a idade: "))
            if age > 0:
                break
            print("Digite uma idade válida.")
        except ValueError:
            print("Digite um número inteiro válido.")

    people.append({"name": name, "age": age})
    print("Pessoa cadastrada com sucesso.")


def list_people(people: list) -> None:
    if not people:
        print("Nenhuma pessoa cadastrada.")
        return

    print(f"\n{'Nome':<20} | Idade")
    print("-" * 30)
    for person in people:
        print(f"{person['name']:<20} | {person['age']}")


def find(people: list) -> None:
    search = input("Digite o nome da pessoa: ").strip().lower()
    results = [p for p in people if search in p['name'].lower()]

    if not results:
        print("Pessoa não encontrada.")
        return

    for person in results:
        print(f"Nome: {person['name']}  |  Idade: {person['age']}")


def delete(people: list) -> None:
    search = input("Digite o nome da pessoa: ").strip().lower()

    for person in people:
        if person['name'].lower() == search:
            people.remove(person)
            print("Pessoa removida com sucesso.")
            return

    print("Pessoa não encontrada.")


def save(people: list) -> None:
    with open("people.json", "w", encoding="utf-8") as f:
        json.dump(people, f, indent=4, ensure_ascii=False)


def load() -> list:
    try:
        with open("people.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def main():
    people = load()

    actions = {
        1: (register, True),  
        2: (list_people, False),
        3: (find, False),
        4: (delete, True),
    }

    while True:
        menu(people)
        try:
            choice = int(input("Digite a opção: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if choice == 5:
            print("Fim do programa.")
            break

        if choice not in actions:
            print("Opção inválida.")
            continue

        clear_screen()
        func, should_save = actions[choice]
        func(people)

        if should_save:
            save(people)


if __name__ == "__main__":
    main()