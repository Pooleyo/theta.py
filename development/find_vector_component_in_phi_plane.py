def run(vector, phi_plane_normal):

    import numpy as np

    unit_vector = vector / np.linalg.norm(vector)

    unit_normal = phi_plane_normal / np.linalg.norm(phi_plane_normal)

    dot_prod = np.dot(unit_vector, unit_normal)

    component_normal_to_plane = [unit_normal[0] * dot_prod, unit_normal[1] * dot_prod, unit_normal[2] * dot_prod]

    component_in_plane = unit_vector - component_normal_to_plane

    return component_in_plane