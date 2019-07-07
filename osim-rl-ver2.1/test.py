# from osim.env import L2M2019Env  # need newest version of osim-rl


from osim.env import L2RunEnv
# from osim.env import Arm2DEnv
# from osim.env import ProstheticsEnv


# env = L2M2019Env(visualize=True)
env = L2RunEnv(visualize=True)
# env = Arm2DEnv(visualize=True)
# env = ProstheticsEnv(visualize=True)

observation = env.reset()
for i in range(200):
    observation, reward, done, info = env.step(env.action_space.sample())