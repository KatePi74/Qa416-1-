import curses

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
        elif key == ord('q'):
            break  # Выход из программы при нажатии 'q'

# Инициализация curses
curses.wrapper(main)
