from game2048.game import Game
from game2048.displays import Display
import tensorflow as tf
from keras import backend as K

def single_run(size, score_to_win, AgentClass, **kwargs):
    game = Game(size, score_to_win)
    agent = AgentClass(game, display=Display(), **kwargs)
    agent.play(verbose=True)
    return game.score


if __name__ == '__main__':
    GAME_SIZE = 4
    SCORE_TO_WIN = 2048
    N_TESTS = 50

    '''====================
    Use your own agent here.'''
    #from game2048.agents import ExpectiMaxAgent as TestAgent
    from myAgent import myAgent as TestAgent
    '''===================='''

    scores = []
    for _ in range(N_TESTS):
        score = single_run(GAME_SIZE, SCORE_TO_WIN,
                           AgentClass=TestAgent)
        scores.append(score)
        K.clear_session()
        tf.reset_default_graph()
    print("Average scores: @%s times" % N_TESTS, sum(scores) / len(scores))
