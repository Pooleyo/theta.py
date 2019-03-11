def run(working_height, working_width, wavelength, a_lattice, norm_view_x, norm_view_y, central_point,
        width_mm_per_pixel, height_mm_per_pixel, vector_origin_to_central_point, unit_vector_source_to_origin,
        adjust_to_centre_of_pixel, phi_plane_normal, normal, filter_angles_deg, gsqr, phi, vector_origin_to_pixels,
        polarisation_angles_deg, phi0_vector, bragg_angles_deg):

    import calc_angle_between_vectors
    import find_vector_component_in_phi_plane

    import numpy as np

    for i in range(working_height):

        for j in range(working_width):

            # numpy arrays have shape = (working_height, working_width)

            current_pixel = [i, j]

            pixel_difference = [0, 0]

            pixel_difference[0] = - (current_pixel[0] - central_point[0])

            pixel_difference[1] = current_pixel[1] - central_point[1]

            mm_difference = [pixel_difference[0] * height_mm_per_pixel, pixel_difference[1] * width_mm_per_pixel]

            mm_difference_centre_to_current = [mm_difference[0] * norm_view_y, mm_difference[1] * norm_view_x]

            vector_origin_to_current_pixel_top_left = vector_origin_to_central_point + mm_difference_centre_to_current[0] + \
                                                       mm_difference_centre_to_current[1]

            vector_origin_to_current_pixel_centre = vector_origin_to_current_pixel_top_left + \
                                                    adjust_to_centre_of_pixel[0] + adjust_to_centre_of_pixel[1]

            distance_origin_to_current_pixel_centre = np.linalg.norm(vector_origin_to_current_pixel_centre)

            unit_vector_origin_to_current_pixel_centre = vector_origin_to_current_pixel_centre / distance_origin_to_current_pixel_centre

            g = (unit_vector_origin_to_current_pixel_centre - unit_vector_source_to_origin) * (1 / wavelength)

            g = np.linalg.norm(g) / (1.0 / a_lattice)

            current_gsqr = g ** 2

            unit_vector_component_in_phi_plane = find_vector_component_in_phi_plane.run(vector_origin_to_current_pixel_centre, phi_plane_normal)

            current_bragg_angle = 0.5 * abs(calc_angle_between_vectors.run(unit_vector_source_to_origin, unit_vector_origin_to_current_pixel_centre))

            current_phi_deg = calc_angle_between_vectors.run(unit_vector_component_in_phi_plane, phi0_vector)

            current_filter_angle_deg = calc_angle_between_vectors.run(vector_origin_to_current_pixel_centre, normal)

            current_polarisation_angle = abs(calc_angle_between_vectors.run(unit_vector_source_to_origin,
                                                                            vector_origin_to_current_pixel_centre))

            if current_polarisation_angle > 90.0:
                # This corrects for the case where the polarisation angle > 90.0. This angle should have a maximum value
                #  of 90.0.

                current_polarisation_angle = 90.0 - abs(current_polarisation_angle - 90.0)

            filter_angles_deg[i][j] = abs(current_filter_angle_deg)
            gsqr[i][j] = current_gsqr
            phi[i][j] = current_phi_deg
            vector_origin_to_pixels[(i * working_width) + j] = vector_origin_to_current_pixel_centre
            polarisation_angles_deg[i][j] = abs(current_polarisation_angle)
            bragg_angles_deg[i][j] = current_bragg_angle

    return filter_angles_deg, gsqr, phi, vector_origin_to_pixels, polarisation_angles_deg, bragg_angles_deg
