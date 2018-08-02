import calc_angle_between_vectors
import give_phi_sign
import compensate_for_sample_attenuation


def test_calc_angle_between_vectors():

    assert calc_angle_between_vectors.run(
        [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]) == 90.0
    assert calc_angle_between_vectors.run(
        [2.0, 1.0, 3.0], [-2.0, -1.0, -3.0]) == 180.0
    assert calc_angle_between_vectors.run(
        [-2.0, -1.0, -3.0], [2.0, 1.0, 3.0]) == 180.0


def test_give_phi_sign():

    assert give_phi_sign.run(
        90.0, [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]) == -90.0
    assert give_phi_sign.run(
        90.0, [-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]) == 90.0

"""
def test_compensate_for_sample_attenuation():

    assert compensate_for_sample_attenuation.run(
        [1.0,0.0,1.0], [0.0, 0.0, 1.0], 90.0, 1.0) == (1.4142135623730949, 1.4142135623730949)
    assert compensate_for_sample_attenuation.run(
        [1.0, 0.0, 1.0], [0.0, 0.0, 1.0], 45.0, 1.0) == (1.0, 1.0)
    # This development looks at what happens if the pixel is in the plane of the sample, i.e infinite path length.
    assert compensate_for_sample_attenuation.run(
        [1.0, 0.0, 1.0], [0.0, 0.0, 1.0], 135.0, 1.0) == (8063664102031864.0, 8063664102031864.0)
"""


