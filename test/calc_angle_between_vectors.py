def run(vector_1, vector_2):

    import numpy as np
    import math    
    
    dot_prod = np.dot(vector_1, vector_2)    
    cross_prod = np.cross(vector_1, vector_2)
    norm_cross_prod = np.linalg.norm(cross_prod)
    
    angle_rad = math.atan2(norm_cross_prod, dot_prod) 
    angle_deg = np.deg2rad(angle_rad)

    return angle_deg
