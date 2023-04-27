import gym
env = gym.make('LunarLander-v2')
env.reset()
print("sample action",env.action_space.sample())
print("abservation space shape",env.observation_space.shape)
print("sample observation:",env.observation_space.sample())
env.close()