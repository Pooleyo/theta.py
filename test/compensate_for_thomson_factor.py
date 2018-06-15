def run(angles_deg, pixel_value):

    import numpy as np

    new_pixel_value = []

    thomson_factor_list = []

    for i in range(len(pixel_value)):

        current_angle_rad = np.deg2rad(angles_deg[i])
    
        current_thomson_factor = ( 1.0 + np.cos(current_angle_rad) ) / 2.0
    
        current_thomson_correction = 1.0/current_thomson_factor
    
        current_new_pixel_value = current_thomson_correction * pixel_value[i]
    
        new_pixel_value.append(current_new_pixel_value)
        thomson_factor_list.append(current_thomson_correction)
    
    return new_pixel_value, thomson_factor_list
