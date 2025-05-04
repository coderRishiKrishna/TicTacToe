def check_sum(a, b, c):
    return a+ b+ c

def game_board(rState, kState):
    zero = 'R' if rState[0] else ('K' if kState[0] else 0)
    one = 'R' if rState[1] else ('K' if kState[1] else 1)
    two = 'R' if rState[2] else ('K' if kState[2] else 2)
    three = 'R' if rState[3] else ('K' if kState[3] else 3)
    four = 'R' if rState[4] else ('K' if kState[4] else 4)
    five = 'R' if rState[5] else ('K' if kState[5] else 5)
    six = 'R' if rState[6] else ('K' if kState[6] else 6)
    seven = 'R' if rState[7] else ('K' if kState[7] else 7)
    eight = 'R' if rState[8] else ('K' if kState[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ") 


def check_win(rState, kState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(check_sum(rState[win[0]], rState[win[1]], rState[win[2]]) == 3):
            print("R Won the match")
            return 1
        if(check_sum(kState[win[0]], kState[win[1]], kState[win[2]]) == 3):
            print("K Won the match")
            return 0
    return -1


if __name__ == "__main__":
    rState = [0]*9
    kState = [0]*9
    print("Let's play tic-tac-toe Game")
    turn = 1 # 1 for R and 0 for K

    while(True):
        game_board(rState, kState)
        if(turn == 1):
            print("R's Chance")
            value = int(input("Please enter a value: "))
            rState[value] = 1
        else:
            print("K's Chance")
            value = int(input("Please enter a value: "))
            kState[value] = 1
        cwin = check_win(rState, kState)
        if(cwin != -1):
            print("Match over")
            break
        
        turn = 1 - turn