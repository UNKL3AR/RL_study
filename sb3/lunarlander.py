import gym
env = gym.make('LunarLander-v2')
env.reset()

for step in range(200):
    env.render('human')
    # env.step(env.action_space.sample())
    obs, reward, done, info = env.step(env.action_space.sample())
    print(reward,done)
env.close()