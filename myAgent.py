import numpy as np
from keras.models import load_model

class Agent:
    '''Agent Base.'''
    
    def __init__(self, game, display=None):
        self.game = game
        self.display = display
    def step(self):
        global direction
        direction = int(input("0: left, 1: down, 2: right, 3: up = ")) % 4
        return direction

    def play(self, max_iter=np.inf, verbose=False):
        n_iter = 0
        while (n_iter < max_iter) and (not self.game.end):
            direction = self.step()
            self.game.move(direction)
            n_iter += 1
            if verbose:
                print("Iter: {}".format(n_iter))
                print("======Direction: {}======".format(
                    ["left", "down", "right", "up"][direction]))
                if self.display is not None:
                    self.display.display(self.game)

    

class myAgent(Agent):
    def step(self):
        global direction
        inputboard = np.zeros((1, 4, 4, 16))
        maxNum = 0
        for i in range(4):
            for j in range(4):
                num = self.game.board[i, j]
                if num > maxNum:
                    maxNum = num
                if num == 0:
                    inputboard[0, i, j, 0] = 1
                else:
                    inputboard[0, i, j, int(np.log2(num))] = 1
        if maxNum <= 256:
            direction = self.model_256.predict(inputboard).tolist()[0]
        if maxNum == 512:
            direction = self.model_512.predict(inputboard).tolist()[0]
        elif maxNum == 1024:
            direction = self.model_1024.predict(inputboard).tolist()[0]
        return direction.index(max(direction))
    def __init__(self, game, display=None):
        if game.size != 4:
            raise ValueError(
                "`%s` can only work with game of `size` 4." % self.__class__.__name__)
        super().__init__(game, display)
        self.game = game
        self.model_256 = load_model('myAgent_256.h5')
        self.model_512 = load_model('myAgent_512.h5')
        self.model_1024 = load_model('myAgent_1024.h5')

    
