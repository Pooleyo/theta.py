def run(phi, phi_0_vector, origin_pixel_vector_in_plane, unit_phi_plane_normal):

    # This function checks the cross product of origin_pixel_vector_in_plane X phi_0_vector then finds the dot product
    # of this vector along the unit_phi_plane_normal. If the result is positive, the angle is assigned a positive value
    # and vice versa.

    import numpy as np

    cross_prod = np.cross(origin_pixel_vector_in_plane, phi_0_vector)

    dot_prod = np.dot(cross_prod, unit_phi_plane_normal)

    if dot_prod >= 0.0:

        phi = phi

    elif dot_prod < 0.0:

        phi = -phi

    else:

        raise ValueError("Phi was not given a sign correctly!")

    return phi