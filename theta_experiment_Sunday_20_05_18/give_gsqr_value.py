def run(i, j, wavelength, a_lattice, normal, norm_view_x, norm_view_y, central_pixel, width_mm_per_pixel, height_mm_per_pixel, vector_origin_to_central_pixel, unit_vector_source_to_origin, adjust_to_centre_of_pixel, width, height):
    
    import numpy as np
    
    current_pixel = [i, j]
    
    pixel_difference = [0,0]
    
    pixel_difference[0] = central_pixel[0] - current_pixel[0]
    
    
    pixel_difference[1] = central_pixel[1] - current_pixel[1]
    
    mm_difference = [pixel_difference[0] * width_mm_per_pixel, pixel_difference[1] * height_mm_per_pixel]

    mm_difference_centre_to_current = [mm_difference[0] * norm_view_x, mm_difference[1] * norm_view_y]

    vector_origin_to_current_pixel = vector_origin_to_central_pixel + mm_difference_centre_to_current[0] + mm_difference_centre_to_current[1]
    
    if width % 2 == 0:
        vector_origin_to_current_pixel = vector_origin_to_current_pixel + adjust_to_centre_of_pixel[0]
        
    if height % 2 == 0:
        vector_origin_to_current_pixel = vector_origin_to_current_pixel + adjust_to_centre_of_pixel[1]
     

    distance_origin_to_current_pixel = np.linalg.norm(vector_origin_to_current_pixel) 

    unit_vector_origin_to_current_pixel = vector_origin_to_current_pixel/distance_origin_to_current_pixel 

    g = ( unit_vector_origin_to_current_pixel - unit_vector_source_to_origin ) * (1/wavelength)
    
    g = np.linalg.norm(g) / (1.0/a_lattice)
    
    gsqr = g ** 2

    return gsqr, vector_origin_to_current_pixel
