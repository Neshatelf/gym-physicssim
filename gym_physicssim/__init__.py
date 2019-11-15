from gym.envs.registration import register
 
register(id='physicssim-v0', 
entry_point='gym.envs.gym_physicssim:PhysicsSimEnv', 
kwargs={ 'draw_tiles': 1},
reward_threshold=(3266 - 40),
nondeterministic=True,
)
