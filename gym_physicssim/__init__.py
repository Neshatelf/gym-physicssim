import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)
 
register(
    id='Physicssim-v0', 
    entry_point='gym_physicssim.envs:PhysicssimEnv',          
)
