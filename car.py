import os
import time
import random
import msvcrt # Для Windows, якщо потрібно зчитувати натискання клавіш без Enter
import sys    # Для кросплатформного зчитування, якщо не використовується msvcrt

# Функція для очищення консолі
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Функція для отримання натиснутої клавіші (базовий кросплатформний підхід)
# Для більш надійного зчитування без Enter на Windows використовуйте msvcrt.getch()
# Для Linux/macOS використовуйте термінальні бібліотеки, наприклад, curses або tty
def get_key_press():
    if os.name == 'nt': # Для Windows
        if msvcrt.kbhit():
            return msvcrt.getch().decode('utf-8').lower()
        return ''
    else: # Для Linux/macOS (простий підхід, який вимагає Enter)
        # Цей підхід менш інтерактивний, для справжньої інтерактивності потрібні бібліотеки (наприклад, termios)
        return input().lower()


def run_game():
    road_width = 21 # Ширина дороги (непарне число краще для центру)
    player_pos = road_width // 2 # Початкова позиція машинки (центр)
    score = 0
    game_over = False
    
    print("Ласкаво просимо до гри 'Машинки'!")
    print("Використовуйте 'a' для руху вліво, 'd' для руху вправо. Натисніть 'q' для виходу.")
    print("Натисніть Enter, щоб почати (або будь-яку клавішу на Windows)")
    if os.name != 'nt': # Для Unix-подібних систем
        input() 
    else: # Для Windows
        while not msvcrt.kbhit():
            time.sleep(0.1) # Чекаємо натискання клавіші
    
    while not game_over:
        clear_screen()
        
        # Генерація дороги та машинки
        road = ['|'] * road_width
        road[player_pos] = 'V' # Машинка гравця
        
        # Генерація перешкод (дуже просто)
        if random.random() < 0.1: # 10% шанс появи перешкоди
            obstacle_pos = random.randint(1, road_width - 2) # Перешкода не на краях
            if obstacle_pos != player_pos: # Щоб не генерувати перешкоду прямо на машинці
                road[obstacle_pos] = 'X' 
        
        print("+" + "-" * (road_width - 2) + "+") # Верхня межа
        print("".join(road))
        print("+" + "-" * (road_width - 2) + "+") # Нижня межа
        print(f"Рахунок: {score}")
        
        # Перевірка зіткнення (якщо машинка "наїхала" на X)
        if 'X' in "".join(road) and "".join(road).index('X') == player_pos:
            game_over = True
            print("Ви розбилися! Гра закінчена.")
            break

        # Читання вводу
        key = ''
        if os.name == 'nt':
            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8').lower()
        else:
            # Для Unix-подібних систем без termios, потрібно вводити Enter після кожної клавіші
            # Це зробить гру менш динамічною
            # Для кращої інтерактивності потрібно використовувати бібліотеки на кшталт termios (складніше)
            # Тому для простоти, на Unix-подібних, можемо просто чекати ентра
            # Або зробити гру покроковою без миттєвого зчитування
            pass # Не зчитуємо тут, щоб не блокувати гру на Unix
            
        if key == 'a' and player_pos > 1: # Рух вліво (не до краю)
            player_pos -= 1
        elif key == 'd' and player_pos < road_width - 2: # Рух вправо (не до краю)
            player_pos += 1
        elif key == 'q':
            game_over = True
            print("Вихід з гри.")
            break
            
        score += 1
        time.sleep(0.2) # Швидкість гри (чим менше, тим швидше)

    print(f"Ваш фінальний рахунок: {score}")

if __name__ == "__main__":
    run_game()
