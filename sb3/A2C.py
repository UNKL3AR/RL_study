import gym
from stable_baselines3 import A2C
#创建环境
env = gym.make('LunarLander-v2')

env.reset()
#定义模型去运行环境，每回合学习10000步
model = A2C('MlpPolicy',env,verbose=1)
model.learn(total_timesteps=10000)

episodes = 10

for ep in range(episodes):
    obs = env.reset()
    done = False
    while not done:
        action,_states = model.predict(obs)
        obs,rewards,done,info = env.step(action)
        env.render('human')
        print(rewards)
        
env.close()