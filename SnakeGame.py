import curses 
from random import randint
#import tensorflow
import numpy as np
#model=tensorflow.keras.models.load_model("best_model")

# setup window
def game(_agent,gen_num=None):
    moves=set()
    time=0
    score=0
    time_without_apple=0
    curses.initscr()
    win = curses.newwin(20, 30, 0, 0) # y,x
    win.clear()
    win.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1) # -1

    # snake and food
    snake = [(4, 10), (4, 9), (4, 8)]
    food = (randint(1,18), randint(1,28))

    win.addch(food[0], food[1], '#')
    win.refresh()
    # game logic
    score = 0

    ESC = 27
    #key = curses.KEY_RIGHT
    key = 3
    key_hot_encoder = [0,0,0,1]
    agent_data=np.array([snake[0][0],snake[0][1],30-snake[0][0],20-snake[0][1],snake[0][0]-snake[-1][0],snake[0][1]-snake[-1][1],snake[0][0]-food[0],snake[0][1]-food[1]])
    agent_data=np.append(agent_data,key_hot_encoder)


    while key != ESC:
        win.addstr(0, 2, 'generation:{} agent_num:{}'.format(gen_num,_agent.index))
        win.timeout(150 - (len(snake)) // 5 + len(snake)//10 % 120) # increase speed
        #next_key = np.argmax(model.predict(agent_data.reshape((-1,10))),axis=-1)[0]
        next_key=_agent.key(agent_data)
        #key =  next_key
       # print(key)
        if key !=4:
            key_hot_encoder=[0,0,0,0]
            key_hot_encoder[key]=1
        #event=-1

        #prev_key = key
        #event = win.getch()
        key = next_key if next_key != 4 else key
       # print(key)
        #if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
         #   key = prev_key
        moves.add(key)
        # calculate the next coordinates
        y = snake[0][0]
        x = snake[0][1]
        if key ==1:# curses.KEY_DOWN:
            y += 1
        if key == 0:#curses.KEY_UP:
            y -= 1
        if key == 2:#curses.KEY_LEFT:
            x -= 1
        if key == 3:#curses.KEY_RIGHT:
            x += 1

        snake.insert(0, (y, x)) # append O(n)

        # check if we hit the border
        if y == 0 or y == 19 or x == 0 or x == 29:
            if time < 30 or len(moves)< 3:
                score-=50
            _agent.scores+=score
            break
        # if snake runs over itself
        if snake[0] in snake[1:] or time_without_apple==100:
            _agent.scores+=score
            break

        if snake[0] == food:
            # eat the food
            score += 100
            time_without_apple=0
            food = ()
            while food == ():
                food = (randint(1,18), randint(1,28))
                if food in snake:
                    food = ()
            win.addch(food[0], food[1], '#')
        else:
            # move snake
            last = snake.pop()
            win.addch(last[0], last[1], ' ')

        win.addch(snake[0][0], snake[0][1], '*')
        score+=0.1
        time+=1
        time_without_apple+=1
        win.refresh()
        agent_data=np.array([snake[0][0],snake[0][1],30-snake[0][0],20-snake[0][1],snake[0][0]-snake[-1][0],snake[0][1]-snake[-1][1],snake[0][0]-food[0],snake[0][1]-food[1]])
        agent_data=np.append(agent_data,key_hot_encoder)


    curses.endwin()
#game(model)
    #print(f"Final score = {score}")
