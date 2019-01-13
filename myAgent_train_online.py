import numpy as np
import keras
from keras.models import load_model
from game2048.game import Game
from game2048.agents import ExpectiMaxAgent

# define the constants
NUM_EPOCHS = 1
NUM_CLASSES = 4
BATCH_SIZE = 1000

model_256 = load_model('myAgent_256.h5')
model_512 = load_model('myAgent_512.h5')
model_1024 = load_model('myAgent_1024.h5')

boards_256 = []
boards_512 = []
boards_1024 = []
directions_256 = []
directions_512 = []
directions_1024 = []

for i in range(30000):
    print('i = ', i)
    game = Game(size=4)
    expectiMaxAgent = ExpectiMaxAgent(game=game)
    while True: # one turn
        rightDirection = expectiMaxAgent.step()
        if (game.end == True): # game over
            break
        maxNum = 0
        for p in range(4):
            for q in range(4):
                if game.board[p, q] > maxNum:
                    maxNum = game.board[p, q]
        if maxNum == 2048: # start the next turn
            break
        inputboard = np.zeros((1, 4, 4, 16))
        for p in range(4):
            for q in range(4):
                num = game.board[p, q]
                if num == 0:
                    inputboard[0, p, q, 0] = 1
                else:
                    inputboard[0, p, q, int(np.log2(num))] = 1
        if maxNum <= 256:
            boards_256.append(inputboard[0])
            directions_256.append(rightDirection)
            myDirection = model_256.predict(inputboard).tolist()[0]
        elif maxNum == 512:
            boards_512.append(inputboard[0])
            directions_512.append(rightDirection)
            myDirection = model_512.predict(inputboard).tolist()[0]
        elif maxNum == 1024:
            boards_1024.append(inputboard[0])
            directions_1024.append(rightDirection)
            myDirection = model_1024.predict(inputboard).tolist()[0]
        game.move(myDirection.index(max(myDirection)))
    print ('len(boards_256) = ', len(boards_256))
   # print ('len(boards_512) = ', lesourcn(boards_512))
    print ('len(boards_512) = ', len(boards_512))
    print ('len(boards_1024) = ', len(boards_1024))
    if len(boards_256) >= 200000:
        # convert to numpy array
        boards_256 = np.array(boards_256)
        directions_256 = np.array(directions_256)
        # convert to one-hot encoding
        directions_256 = keras.utils.to_categorical(directions_256, num_classes=NUM_CLASSES)
        # train
        print("training on model_256")
        model_256.fit(boards_256, directions_256, epochs=NUM_EPOCHS, batch_size=BATCH_SIZE, validation_split=0.05)
        model_256.save('myAgent_256.h5')
        boards_256 = []
        directions_256 = []
    if len(boards_512) >= 200000:
        # convert to numpy array
        boards_512 = np.array(boards_512)
        directions_512 = np.array(directions_512)
        # convert to one-hot encoding
        directions_512 = keras.utils.to_categorical(directions_512, num_classes=NUM_CLASSES)
        # train
        print("training on model_512")
        model_512.fit(boards_512, directions_512, epochs=NUM_EPOCHS, batch_size=BATCH_SIZE, validation_split=0.05)
        model_512.save('myAgent_512.h5')
        boards_512 = []
        directions_512 = []
    if len(boards_1024) >= 200000:
        # convert to numpy array
        boards_1024 = np.array(boards_1024)
        directions_1024 = np.array(directions_1024)
        # convert to one-hot encoding
        directions_1024 = keras.utils.to_categorical(directions_1024, num_classes=NUM_CLASSES)
        # train
        print("training on model_1024")
        model_1024.fit(boards_1024, directions_1024, epochs=NUM_EPOCHS, batch_size=BATCH_SIZE, validation_split=0.05)
        model_1024.save('myAgent_1024.h5')
        boards_1024 = []
        directions_1024 = []
