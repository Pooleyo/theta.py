def run(vector_origin_pixel, unit_phi_plane_normal, phi_0_vector):

    import numpy as np
    import calc_angle_between_vectors
    import give_phi_sign
    # First collapse the vector_origin_pixel onto the phi_0_plane:

    length_vector_origin_pixel = np.linalg.norm(
        vector_origin_pixel)

    unit_vector_origin_pixel = vector_origin_pixel / length_vector_origin_pixel

    dot_prod = np.dot(
        unit_vector_origin_pixel, unit_phi_plane_normal)

    parallel_component_origin_pixel = [unit_phi_plane_normal[0] * dot_prod, unit_phi_plane_normal[1] * dot_prod, unit_phi_plane_normal[2] * dot_prod]

    origin_pixel_vector_in_plane = unit_vector_origin_pixel - parallel_component_origin_pixel

    # Then calculate the angle between these vectors:

    phi_deg = calc_angle_between_vectors.run(
        origin_pixel_vector_in_plane, phi_0_vector)

    phi_deg = give_phi_sign.run(phi_deg, phi_0_vector, origin_pixel_vector_in_plane, unit_phi_plane_normal)

    return phi_deg