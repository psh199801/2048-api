# 2048-api
A 2048 game api for training supervised learning (imitation learning) or reinforcement learning agents

# Code structure
* [`game2048/`](game2048/): the main package.
    * [`game.py`](game2048/game.py): the core 2048 `Game` class.
    * [`agents.py`](game2048/agents.py): the `Agent` class with instances.
    * [`displays.py`](game2048/displays.py): the `Display` class with instances, to show the `Game` state.
    * [`expectimax/`](game2048/expectimax): a powerful ExpectiMax agent by [here](https://github.com/nneonneo/2048-ai).
* [`explore.ipynb`](explore.ipynb): introduce how to use the `Agent`, `Display` and `Game`.
* [`static/`](static/): frontend assets (based on Vue.js) for web app.
* [`webapp.py`](webapp.py): run the web app (backend) demo.
* [`evaluate.py`](evaluate.py): evaluate your self-defined agent.

# Requirements
* code only tested on linux system (ubuntu 16.04)
* Python 3 (Anaconda 3.6.3 specifically) with numpy and flask

# To define your own agents
```python
from game2048.agents import Agent

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

```

# 如何运行代码
* 代码的基本结构如上，具体代码在文件夹下的myAgent.py中
* 需要运行的model在百度云链接： https://pan.baidu.com/s/1i8F4H4Te1Ai3x4Te7_YZnA     ，下载后放到2048-api文件夹下即可。myAgent_256.h5对应0-512，myAgent_512.h5对应512-1024，myAgent_1024.h5对应1024-2048
* 以下是其他部分各个代码的运行
	* python generateDataSet.py  将三个模型训练的数据保存到文档中。
	* python myAgent_train.py  选择上一个函数中产生的三个数据集之一来分别完成三个不同的分层模型。
	* python myAgent_train_online.py  会在线训练三个模型，具体训练时的参数可以自行更改。

# To compile the pre-defined ExpectiMax agent

```bash
cd game2048/expectimax
bash configure
make
```

# To run the web app
```bash
python webapp.py
```
![demo](preview2048.gif)

# LICENSE
The code is under Apache-2.0 License.

# For EE369 students from SJTU only
Please read [here](EE369.md).
