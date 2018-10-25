def run(width, height, x_scale, y_scale, view_x, view_y, offset, normal, source_position):

    import numpy as np
    
    central_point = [height/2.0, width/2.0]

    height_mm_per_pixel = float(y_scale)/height
    width_mm_per_pixel = float(x_scale) / width

    norm_view_y = view_y/(np.sqrt(view_y[0]**2 + view_y[1]**2 + view_y[2]**2))
    norm_view_x = view_x/(np.sqrt(view_x[0]**2 + view_x[1]**2 + view_x[2]**2))

    canonical_offset_mm = [norm_view_y * offset[1], norm_view_x * offset[0]] # Gives the offset in mm. This can now be used to find the central position of the image plate.

    adjust_to_centre_of_pixel = [0.5 * height_mm_per_pixel * (-norm_view_y), 0.5 * width_mm_per_pixel * norm_view_x] # Moves the vector terminal to the centre of the pixel, rather than the top left corner.
    
    vector_origin_to_central_point = normal + canonical_offset_mm[0] + canonical_offset_mm[1]

    vector_source_to_origin = np.negative(source_position)
    
    norm_source_to_origin = np.linalg.norm(vector_source_to_origin)

    unit_vector_source_to_origin = vector_source_to_origin / norm_source_to_origin 

    return central_point, width_mm_per_pixel, height_mm_per_pixel, norm_view_x, norm_view_y, vector_origin_to_central_point, unit_vector_source_to_origin, adjust_to_centre_of_pixel
