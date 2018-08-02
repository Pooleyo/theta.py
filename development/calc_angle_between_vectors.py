def run(vector_1, vector_2):

    import numpy as np

    dot_prod = np.dot(vector_1, vector_2)

    norm_vector_1 = np.linalg.norm(vector_1)

    norm_vector_2 = np.linalg.norm(vector_2)

    cos_angle = dot_prod/(norm_vector_1 * norm_vector_2)

    angle_rad = np.arccos(cos_angle)

    angle_deg = np.rad2deg(angle_rad)

    return angle_deg
