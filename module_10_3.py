import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            with self.lock:
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}")
            with self.lock:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
            time.sleep(0.001)

# Создание объекта банка
bk = Bank()

# Измерение времени до начала выполнения потоков
start_time = time.time()

# Создание потоков для операций пополнения и снятия средств
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

# Запуск потоков
th1.start()
th2.start()

# Ожидание завершения потоков
th1.join()
th2.join()

# Измерение времени после завершения потоков
end_time = time.time()

# Итоговый баланс
print(f'Итоговый баланс: {bk.balance}')

# Вычисление и вывод времени выполнения программы
elapsed_time = end_time - start_time
print(f'Время работы программы: {elapsed_time:.4f} секунд')
