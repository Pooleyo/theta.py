def run(width, height, x_scale, y_scale, view_x, view_y, offset, normal, source_position, debug):

 
    import math
    import numpy as np


    print "Working out common results..."

    
    central_pixel = [int(math.ceil(width/2.0) - 1), int(math.ceil(height/2.0) - 1)]


    width_mm_per_pixel = float(x_scale)/width


    height_mm_per_pixel = float(y_scale)/height

    
    norm_view_x = view_x/(np.sqrt(view_x[0]**2 + view_x[1]**2 + view_x[2]**2))


    norm_view_y = view_y/(np.sqrt(view_y[0]**2 + view_y[1]**2 + view_y[2]**2))


    canonical_offset_mm = [norm_view_x * offset[0], norm_view_y * offset[1]] # Gives the offset in mm. This can now be used to find the central position of the image plate.
    

    adjust_to_centre_of_pixel =  [0.5 * width_mm_per_pixel * norm_view_x, 0.5 * height_mm_per_pixel * norm_view_y] # Moves the vector terminal to the centre of the pixel, rather than the top left corner.
    

    vector_origin_to_central_pixel = normal + canonical_offset_mm[0] + canonical_offset_mm[1]
    

    if width % 2 == 0:

        vector_origin_to_central_pixel = vector_origin_to_central_pixel + adjust_to_centre_of_pixel[0]
        

    if height % 2 == 0:

        vector_origin_to_central_pixel = vector_origin_to_central_pixel + adjust_to_centre_of_pixel[1]
    

    vector_source_to_origin = np.negative(source_position)

    
    norm_source_to_origin = np.linalg.norm(vector_source_to_origin)


    unit_vector_source_to_origin = vector_source_to_origin / norm_source_to_origin 



    
    debug_message = ("\n\n~~~~~~~~~~~~~\nFILENAME = " + __name__ + ".py"
    
    + "\n\nINPUTS:"
    + "\nworking_width = " + str(width)
    + "\nworking_height = " + str(height)
    + "\nx_scale = " + str(x_scale)
    + "\ny_scale = " + str(y_scale)
    + "\nview_x = " + str(view_x)
    + "\nview_y = " + str(view_y)
    + "\noffset = " + str(offset)
    + "\nnormal = " + str(normal)
    + "\nsource_position = " + str(source_position)
    + "\ndebug = " + str(debug)
    
    + "\n\nOUTPUTS:"
    + "\ncentral_pixel = " + str(central_pixel)
    + "\nwidth_mm_per_pixel = " + str(width_mm_per_pixel)
    + "\nheight_mm_per_pixel = " + str(height_mm_per_pixel)
    + "\nnorm_view_x = " + str(norm_view_x)
    + "\nnorm_view_y = " + str(norm_view_y)
    + "\nvector_origin_to_central_pixel = " + str(vector_origin_to_central_pixel)
    + "\nunit_vector_source_to_origin = " + str(unit_vector_source_to_origin)
    + "\nadjust_to_centre_of_pixel = " + str(adjust_to_centre_of_pixel)

    + "\n~~~~~~~~~~~~~~~")
    
    
    if debug:
    
        print debug_message

    


    return central_pixel, width_mm_per_pixel, height_mm_per_pixel, norm_view_x, norm_view_y, vector_origin_to_central_pixel, unit_vector_source_to_origin, adjust_to_centre_of_pixel
