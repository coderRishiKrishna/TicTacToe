def game_board(rState, kState):
    board = []
    for i in range (9):
        if rState[i]:
            board.append('R')
        elif kState[i]:
            board.append('K')
        else:
            board.append(str(i))

    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"--|---|---")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"--|---|---")
    print(f"{board[6]} | {board[7]} | {board[8]}") 

def check_sum(a, b, c):
    return a+ b+ c

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

        if sum(rState) + sum(kState) == 9:
            print("It's a draw!")
            print("Match over")
            break
        
        turn = 1 - turn