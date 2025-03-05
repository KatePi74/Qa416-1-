import curses
import time

# ASCII-арт пингвина
penguin = r"""
       .--.  
      |o_o |  
      |:_/ |  
     //   \ \  
    (|     | )  
   /'\_   _/`\  
   \___)=(___/  
"""


def main(stdscr):
    # Очищаем экран и отключаем курсор
    curses.curs_set(0)
    stdscr.clear()

    # Получаем начальные размеры окна
    max_y, max_x = stdscr.getmaxyx()

    # Начальная позиция пингвина
    x = max_x // 2 - len(penguin.splitlines()[0]) // 2
    y = max_y // 2 - len(penguin.splitlines()) // 2

    jump_height = 5  # Высота прыжка (3 строки)
    is_jumping = False  # Флаг, чтобы знать, что пингвин сейчас в прыжке

    while True:
        # Очищаем экран
        stdscr.clear()

        # Рисуем пингвина в новой позиции
        for i, line in enumerate(penguin.splitlines()):
            stdscr.addstr(y + i, x, line)

        # Обновляем экран
        stdscr.refresh()

        # Получаем ввод с клавиатуры
        key = stdscr.getch()

        # Управление движением пингвина
        if key == curses.KEY_RIGHT:
            x += 1  # Двигаем вправо
        elif key == curses.KEY_LEFT:
            x -= 1  # Двигаем влево
        elif key == ord(' ') and not is_jumping:  # Пробел для подпрыгивания
            is_jumping = True
            for _ in range(jump_height):
                y -= 1  # Подпрыгиваем вверх
                time.sleep(0.05)  # Задержка для имитации прыжка
                stdscr.clear()  # Очищаем экран, чтобы плавно происходил переход
                # Рисуем пингвина на новой высоте
                for i, line in enumerate(penguin.splitlines()):
                    stdscr.addstr(y + i, x, line)
                stdscr.refresh()
            # После того как пингвин достиг вершины, спускаем его обратно
            for _ in range(jump_height):
                y += 1  # Спускаемся вниз
                time.sleep(0.05)
                stdscr.clear()
                # Рисуем пингвина на новой высоте
                for i, line in enumerate(penguin.splitlines()):
                    stdscr.addstr(y + i, x, line)
                stdscr.refresh()
            is_jumping = False  # Сброс флага после завершения прыжка

        elif key == 27:  # Выход из программы при нажатии 'Esc'
            break


# Инициализация curses
curses.wrapper(main)
