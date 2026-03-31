def minim(arr):
    if not arr:
        return None
    minNum = arr[0]
    for num in arr:
        if arr[num] < minNum:
            minNum = arr[num]
    return minNum

# try:
#     count = int(input("укажите количество переменных списка: "))
#     nums = []
#     for i in range(count):
#         num = int(input("введите число: "))
#         nums.append(num)
    
#     if nums:
#         print("минимальное число: ", minim(nums))
#     else:
#         print("список пуст")

# except ValueError:
#     print("Пожалуйста, вводите только целые числа")

def fibon(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for _ in range(3, n+1):
        temp = a
        a = b
        b = temp + b
    return b

# try:
#     count = int(input("введите число n число фиббоначи: "))
#     if count < 0 :
#         print("введите положительное число")
#     else:
#         print("ваше число: ", fibon(count))

# except ValueError:
#     print("введите целое число")

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 


class LinkedList:
    def __init__(self):
        self.head = None 
    
    def count(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
    
    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False
    
    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes) if nodes else "Пустой список"

if __name__ == "__main__":
    my_list = LinkedList()
    
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(20)
    
    print(f"Список: {my_list}")
    print(f"Количество элементов: {my_list.count()}")
    
    test_values = [10, 20, 40]
    for value in test_values:
        found = my_list.search(value)
        print(f"Значение {value}: {'найдено' if found else 'не найдено'}")