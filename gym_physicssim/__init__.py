from gym.envs.registration import register
 
register(id='PhysicsSim-v0', 
    entry_point='gym_physicssim.envs:PhysicsSimEnv', 
)
