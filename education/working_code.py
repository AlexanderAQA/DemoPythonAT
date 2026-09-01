inventory = []

def add_item():
    object = input("Ввести название предмета: ")
    Quantity_g = int(input("Ввести количество: "))
    item = ({
     "name": object,
     "quantity": Quantity_g
 })
    inventory.append(item)


def show_inventory():
    for i, item in enumerate(inventory, start=1):
        print(f"{i}. {item['name']} - {item['quantity']} шт.")



def remove_item():
    show_inventory()
    if not inventory:
        return
    while True:
        try:
            index = int(input("Введите номер предмета, который нужно убрать: ")) - 1
            if index < 0 or index >= len(inventory):
                print("Неверный номер. Попробуйте ещё раз.")
                continue
            break
        except ValueError:
            print("Введите целое число.")
    while True:
        try:
            amount = int(input("Сколько убрать: "))
            if amount < 0:
                print("Нельзя убрать отрицательное число.")
                continue
            break
        except ValueError:
            print("Введите целое число.")
    if amount > inventory[index]["quantity"]:
        print("Недостаточно предметов.")
    else:
        inventory[index]["quantity"] -= amount
        print(f"После удаления осталось: {inventory[index]['quantity']} шт.")
        # Если количество стало 0, удаляем предмет из списка
        if inventory[index]["quantity"] == 0:
            del inventory[index]
add_item()
add_item()
add_item()
remove_item()



