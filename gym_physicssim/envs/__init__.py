from gym_physicssim.envs.physicssim_env import PhysicsSimEnv

from gym.envs.registration import register
 
register(id='physicssim-v0', 
entry_point='gym.envs.gym_physicssim:PhysicsSimEnv', 
)




