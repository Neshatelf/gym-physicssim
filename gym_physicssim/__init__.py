from gym.envs.registration import register
 
register(id='physicssim-v0', 
    entry_point='gym_physicssim.envs:PhysicsSimEnv', 
)
