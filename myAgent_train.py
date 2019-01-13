import numpy as np
import keras
from keras.models import Sequential, Model
from keras.layers import Input, Dense, Activation, Conv2D, MaxPooling2D, Flatten, Dropout

# define constants
NUM_EPOCHS = 3
NUM_CLASSES = 4 # four directions
BATCH_SIZE = 64
INPUT_SHAPE = (4, 4, 16)

def onehot(arr):
    match_table = {2**i: i for i in range(1,16)}
    match_table[0] = 0
    ret = np.zeros((4,4,16), dtype=bool)
    for i in range(4):
        for j in range(4):
            ret[i,j,match_table[arr[i,j]]] = 1
    
    return ret

# initialize neural network
inputs = Input(shape=INPUT_SHAPE)
layer1_tensor1 = Conv2D(512, (2, 1), strides=(1, 1), activation='relu')(inputs)
layer1_tensor2 = Conv2D(512, (1, 2), strides=(1, 1), activation='relu')(inputs)
layer2_tensor1 = Conv2D(256, (1, 2), strides=(1, 1), activation='relu')(layer1_tensor1)
layer2_tensor2 = Conv2D(256, (2, 1), strides=(1, 1), activation='relu')(layer1_tensor2)
layer2_tensor3 = Conv2D(256, (1, 2), strides=(1, 1), activation='relu')(layer1_tensor1)
layer2_tensor4 = Conv2D(256, (2, 1), strides=(1, 1), activation='relu')(layer1_tensor2)
layer2_tensor5 = Conv2D(256, (1, 2), strides=(1, 1), activation='relu')(layer1_tensor1)
layer2_tensor6 = Conv2D(256, (2, 1), strides=(1, 1), activation='relu')(layer1_tensor2)
layer2 = keras.layers.concatenate([layer2_tensor1, layer2_tensor2, layer2_tensor3, layer2_tensor4, layer2_tensor5, layer2_tensor6])
layer3 = Flatten()(layer2)
layer4 = Dense(2048, activation='relu')(layer3)
layer5 = Dense(512, activation='relu')(layer4)
outputs = Dense(NUM_CLASSES, activation='softmax')(layer5)
model = Model(inputs=inputs, outputs=outputs)

# compile the network
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
print("Compile Complete")
f1 = open("dataset_512_3.txt")
#f2 = open("dataset_1024_3.txt")
#f3 = open("dataset_2048_3.txt")
for epoch in range(NUM_EPOCHS):
    
    for k in range(10):
        # save boards and directions
        boards = []
        directions = []
        
        # read data
        for j in range(1000000):
            num = f1.readline()
            if not num: # end of file
                break
            num = float(num)
            # the 4 * 4 board is changed into a 16 * 16 one hot encoding board
            # every row corresponds to one number in the original board
            # num is represented by setting board[i, int(log2(num))] to 1
            # as there are 16 columns in every block, the maximum number that can be represented is 32768
            # since there is no 1s in the board, we can use board[i, 0] = 1 to represent units that are empty
            board = np.zeros((4, 4, 16)) 
            for p in range(4):
                for q in range(4):
                    # if num == 0:
                    #     board[p, q, 0] = 1
                    # else:
                    #     board[p, q, int(np.log2(num))] = 1
                    # num = float(f1.readline())
                    board[p,q] = num
                    num = float(f1.readline())
            borad = onehot(board)
            boards.append(borad) # save the board
            direction = int(num)
            directions.append(direction) # save the direction
        # convert to numpy array
        boards = np.array(boards)
        directions= np.array(directions)
        # convert to one-hot encoding
        directions = keras.utils.to_categorical(directions, num_classes=NUM_CLASSES)
        # train
        model.fit(boards, directions, epochs=NUM_EPOCHS, batch_size=BATCH_SIZE, validation_split=0.1)
    f1.close()
    
# save the model
model.save('myAgent_512.h5')

