
#Консольний бот помічник, який розпізнаватиме команди, що вводяться з клавіатури, та буде відповідати відповідно до введеної команди.



def input_error(func):                    # Декоратор для обробки помилок
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."     # Обробка винятку KeyError
        except ValueError:
            return "Give me name and phone please."     # Обробка винятку ValueError
        except IndexError:
            return "Invalid number of arguments."       # Обробка винятку IndexError

    return inner

def parse_input(user_input):           # Функція для розбору введеного користувачем рядка
    cmd, *args = user_input.split()    # Розбиває введений рядок на слова
    cmd = cmd.strip().lower()          # Видаляє зайві пробіли та переводить команду до нижнього регістру
    return cmd, *args

@input_error
def add_contact(args, contacts):      # Функція для додавання нового контакту
    name, phone = args                # Розпаковка аргументів
    contacts[name] = phone            # Додавання контакту до словника
    return "Contact added."           # Повідомлення про успішне додавання

@input_error
def change_contact(args, contacts):    # Функція для зміни контакту
    name, phone = args
    if name in contacts:              # Перевірка чи існує контакт з таким ім'ям
        contacts[name] = phone        # Зміна номера телефону для вказаного контакту
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def show_all(contacts):               # Функція для виведення усіх контактів
    if contacts:                                  # Перевірка чи існують контакти
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        return "No contacts found."

def main():
    contacts = {}                               # Ініціалізація словника контактів
    print("Welcome to the assistant bot!")
    while True:                                      # Безкінечний цикл для введення команд користувачем
        user_input = input("Enter a command: ")         # Зчитування команди від користувача
        command, *args = parse_input(user_input)        # Розбір команди на окремі частини


        if command in ["close", "exit"]:
            print("Good bye!")             # Виведення повідомлення про завершення роботи
            break
        elif command == "hello":
            print("How can I help you?")          # Виведення привітання
        elif command == "add":
            print(add_contact(args, contacts))         # Виклик функції для додавання контакту
        elif command == "change":
            print(change_contact(args, contacts))      # Виклик функції для зміни контакту
        elif command == "all":
            print(show_all(contacts))                  # Виклик функції для виведення усіх контактів
        else:
            print("Invalid command.")                  # Повідомлення про невірну команду

if __name__ == "__main__":
    main()  


    