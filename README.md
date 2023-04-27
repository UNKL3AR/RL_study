# RL_study
# 环境安装与配置
1、前提条件
Stable-Baselines3 需要
```bash
python version > 3.7, PyTorch version >= 1.11
```

2、Windows 或 Linux
如果你使用 Windows 或 Linux 作为开发环境，那么推荐你使用 Anaconda 或 miniconda，以便管理自己的环境。

创建带有特定 Python 版本的 Conda 虚拟环境

```bash
conda create -n sb3 python=3.8.12
```
说明: 上述命令中的 sb3 为你所创建的虚拟环境的名字；python=3.8.12 为创建虚拟环境的同时安装 3.8.12 版本的 Python.
激活虚拟环境

```bash
conda activate sb3
```

说明: 上述激活你所创建的虚拟环境 sb3 后即可进入虚拟环境 sb3.

安装 SB3 库

使用 pip 安装 Stable Baselines3, 执行以下命令:

```bash
pip install stable-baselines3[extra]
```


说明: 使用上述命令安装包括了可选的依赖，比如 Tensorboard, OpenCV or atari-py. 如果你不需要这些，你可以使用下面的命令。

```bash
pip install stable-baselines3
```


安装 gym 库

使用 pip 安装 Stable Baselines3, 执行以下命令:

```bash
pip install gym[box2d]
```
