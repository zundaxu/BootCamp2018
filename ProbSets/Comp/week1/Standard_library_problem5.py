import box
import random
import time
import sys

def game (name, t):
    remaining = list(range(1,10))
    flag = True

    time1 = time.time()
    t_remain = t
    while flag & (len(remaining)!=0) & (t_remain>0):
        r = roll(sum(remaining))
        if not box.isvalid(r, remaining):
            flag = False
        else:
            print(f"Numbers left: {remaining}")
            print(f"Roll: {r}")
            time2 = time.time()
            t_remain = round(t+(time1-time2), 2)
            print(f"Seconds left: {t_remain}")
            inp = input("Numbers to eliminate: ")
            choices = box.parse_input(inp,remaining)
            while len(choices)==0 or sum(choices)!=r:
                print("Choice not successful, please try again. ")
                inp = input("Numbers to eliminate: ")
                choices = box.parse_input(inp,remaining)
            remaining = box.kick(remaining, choices)

    if len(remaining)==0:
        print(f"Score for player {name}: 0 points")
        print(f"Time played: {-time1+time2} seconds")
        print("Congratulations!! You shut the box!")
    elif t_remain<=0:
        print("You lose. You're outta time.")
    else:
        print(f"No selection is possible.")
        print(f"Score for player {name}: {sum(remaining)} points")
        print(f"Time played: {-time1+time2} seconds")

def roll(s):
    if s<=6:
        min = 1
        max = 6
    else:
        min = 2
        max = 12
    return random.randint(min, max)

def valid_input(arg1, arg2):
    flag = True
    try:
        t = float(arg2)
    except ValueError:
        print("second one is not float")
        flag = False
    return flag

    
if __name__ == "__main__":

    if (len(sys.argv) != 3) or not  (valid_input(sys.argv[1],sys.argv[2])):
        print("Input not correct.")
    else:
        name = sys.argv[1]
        t = float(sys.argv[2])
        game(name, t)