
def Tictactoe():
    #board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    numpad = ['1','2','3','4','5','6','7','8','9']
    global p_one
    p_one = True

    # wyświetlanie tablicy
    def display(b):
        print(f" {b[0]} | {b[1]} | {b[2]} ")
        print("-----------")
        print(f" {b[3]} | {b[4]} | {b[5]} ")
        print("-----------")    
        print(f" {b[6]} | {b[7]} | {b[8]} ")

    # sprawdzenie jaki gracz i ustawienie znaku X albo O
    def p_numb(p_on):
        if p_on:
            char = 'X'
            print("Player 1 is moving...")
        else:
            char = 'O'
            print("Player 2 is moving...")
        return char    
    
    # ruch gracza
    def p_move(p_on,board):
        global p_one 
        #print(f"P_on {p_on}, p_one {p_one}")
        char = p_numb(p_on)
        check = ''
        while (check) not in ['1','2','3','4','5','6','7','8','9']:
            check = input(f"Podaj numer wolnego pola (1-9), gdzie postawisz {char}: ")
            print('\n'*90)
        else:
            if board[int(check)-1] == ' ':
                p_one = not p_on
                board[int(check)-1] = char
            else:
                print("To pole już jest zajęte! Spróbuj inne.")
                p_move(p_on,board)
        #print(f"3 P_on {p_on}, p_one {p_one}")
        return not p_one, board
    
    # sprawdzenie czy ktoś wygrał
    def is_won(board):
        list_of_win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for cond in list_of_win:
            if board[cond[0]]==board[cond[1]]==board[cond[2]]=='X':
                print("!!!!!     Player 1 is the winner     !!!!!")
                return True            
            elif board[cond[0]]==board[cond[1]]==board[cond[2]]=='O':
                print("!!!!!     Player 2 is the winner     !!!!!")
                return True
            
    
    # szkielet całej gry
    def game():
        pagain = True
        
        while pagain:
            board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            ruch = 1
            while ruch < 5:
                p_move(p_one,board)
                display(board)
                ruch += 1
                #display(board)
            else:
                while ruch <9:
                    p_move(p_one,board)
                    display(board)
                    if is_won(board):
                        break
                    ruch += 1
                else:
                    p_move(p_one,board)
                    display(board)
                    if is_won(board):
                        pass
                    else:
                        print("Gra nierozstrzygnięta, skończyły się wolne pola!")
            # po skończonej rozgrywce możliwość zagrania jeszcze raz        
            again = 'a'
            while again not in ['T','t','N','n']:
                again = input("Czy chcesz zagrać jeszcze raz (T/N):")
            else:
                if again == 'T' or again == 't':
                    pagain = True
                else:
                    pagain = False
           
    
    print("Witaj w grze TicTacToe. Gra dla dwóch graczy. Pole gry ma numery:")
    display(numpad)
    print("Powodzenia!")
    print("Aby kontynuować, naciśnij Enter!")
    input("")
    
    game()
Tictactoe()