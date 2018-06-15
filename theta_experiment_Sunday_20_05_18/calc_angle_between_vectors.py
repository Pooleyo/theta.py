def run(vector_1, vector_2):

    import numpy as np
    import math    
    
    dot_prod = np.dot(vector_1, vector_2)
    
    norm_vector_1 = np.linalg.norm(vector_1)
    norm_vector_2 = np.linalg.norm(vector_2)
    
    scalar_prod = norm_vector_1 * norm_vector_2
    ratio = dot_prod/scalar_prod
    
    if abs(ratio) > 1.0: # There is a quirk which means this has to be included such that the central pixel plane, crossed with itself, will resolve correctly.
        angle_rad = 0.0       

    else:          
        
        angle_rad = math.acos(ratio)
        
    angle_deg = angle_rad * 180 / np.pi
    
    # This next section determines whther the angle is positive or negative.
    if angle_deg == 0.0:
        pass    

    
    else:
        cross_product = np.cross(vector_1, vector_2)
        unit_vector_cross_product = cross_product/np.linalg.norm(cross_product)
        
        
        direction_indicator = unit_vector_cross_product[0] + unit_vector_cross_product[1] + unit_vector_cross_product[2]
        
        if direction_indicator > 0:
            angle_deg = -angle_deg
            

        else:
            angle_deg = angle_deg
            

    return angle_deg
