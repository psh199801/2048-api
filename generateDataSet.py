GAME_SIZE = 4
SCORE_TO_WIN1 = 512
SCORE_TO_WIN2 = 1024
SCORE_TO_WIN3 = 2048
SCORE_TO_WIN0 = 256
from game2048.game import Game
from game2048.agents import ExpectiMaxAgent


# save the dataset
f1 = open("dataset_256_3.txt", "w")
f2 = open("dataset_512_3.txt", "w")
f3 = open("dataset_1024_3.txt", "w")

# for i in range(100):
#     print("i = ", i)
#     game = Game(size=GAME_SIZE,score_to_win=SCORE_TO_WIN1)
#     agent = ExpectiMaxAgent(game=game)
#     while True:
#         direction = agent.step()
#         if (game.end != 0):
#             break
# #        print (game.board)
# #        print ("direction: ", direction)
#         for i in range(4):
#             for j in range(4):
#                 #f.write(game.board[i,j])
#                 print(game.board[i, j], file = f1)
#         print(direction, file = f1)
#         #f.write(direction)
        
#         game.move(direction)
    
#     #f.write('\n')

# for i in range(100):
#     print("i = ", i)
#     game = Game(size=GAME_SIZE,score_to_win=SCORE_TO_WIN2)
#     agent = ExpectiMaxAgent(game=game)
#     while True:
#         direction = agent.step()
#         if (game.end != 0):
#             break
# #        print (game.board)
# #        print ("direction: ", direction)
#         for i in range(4):
#             for j in range(4):
#                 #f.write(game.board[i,j])
#                 print(game.board[i, j], file = f2)
#         print(direction, file = f2)
#         #f.write(direction)
        
#         game.move(direction)
    
#     #f.write('\n')

for i in range(300):
    print("i = ", i)
    game = Game(size=GAME_SIZE,score_to_win=SCORE_TO_WIN0)
    agent = ExpectiMaxAgent(game=game)
    while True:
        direction = agent.step()
        if (game.end != 0):
            break
#        print (game.board)
#        print ("direction: ", direction)
        if game.board.max() <256:

            for i in range(4):
                for j in range(4):
                    #f.write(game.board[i,j])
                    print(game.board[i, j], file = f1)
            print(direction, file = f1)

        elif game.board.max() <512:

            for i in range(4):
                for j in range(4):
                    #f.write(game.board[i,j])
                    print(game.board[i, j], file = f2)
            print(direction, file = f2)

        else:

            for i in range(4):
                for j in range(4):
                    #f.write(game.board[i,j])
                    print(game.board[i, j], file = f3)
            print(direction, file = f3)
        #f.write(direction)
        
        game.move(direction)
    
    #f.write('\n')
