def run(vector_1, vector_2):
    
    import numpy as np
    
    normal_to_plane = np.cross(vector_1, vector_2)
    
    return normal_to_plane
   
