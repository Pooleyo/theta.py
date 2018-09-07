import calc_angle_between_vectors
import give_phi_sign
import calc_integrated_intensity_per_phi
import calc_phi_deg
import calc_plane_from_two_vectors
import calc_theta_phi
import compensate_for_sample_attenuation

import numpy as np


def test_calc_angle_between_vectors():

    assert calc_angle_between_vectors.run(
        [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]) == 90.0
    assert calc_angle_between_vectors.run(
        [2.0, 1.0, 3.0], [-2.0, -1.0, -3.0]) == 180.0
    assert calc_angle_between_vectors.run(
        [-2.0, -1.0, -3.0], [2.0, 1.0, 3.0]) == 180.0


def test_calc_integrated_intensity_per_phi():

    assert calc_integrated_intensity_per_phi.run(
        [0.0, 1.0], [0.0, 10.0], [[0.0, 0.0, [1,2], 100.0], [0.0, 10.0, [], 0.0], [1.0, 0.0, [], 0.0], [1.0, 10.0, [], 0.0]]) ==\
           [10.0, 0.0]
    assert calc_integrated_intensity_per_phi.run(
        [0.0, 0.5, 1.0], [0.0, 2.0, 4.0], [[0.0, 0.0, [1, 2], 100.0], [0.0, 2.0, [3], 10.0], [0.0, 4.0, [4], 10.0], [0.5, 0.0, [6,7], 200.0], [0.5, 2.0, [], 0.0], [0.5, 4.0, [], 0.0], [1.0, 0.0, [], 0.0], [1.0, 2.0, [], 0.0], [1.0, 4.0, [], 0.0]]) == \
           [20.0, 100.0, 0.0]


def test_calc_phi_deg():

    assert calc_phi_deg.run([1.0, 0.0, 1.0], [0.0, 0.0, 1.0], [-1.0, 0.0, 0.0]) == \
        180.0
    assert calc_phi_deg.run([1.0, 0.0, 1.0], [0.0, 0.0, 1.0], [-1.0, 0.01, 0.0]) == \
        179.42706130231738
    assert calc_phi_deg.run([1.0, 0.0, 1.0], [0.0, 0.0, 1.0], [-1.0, -0.01, 0.0]) == \
        -179.42706130231738


def test_calc_plane_from_two_vectors():

    assert (calc_plane_from_two_vectors.run([1.0, 0.0, 0.0], [0.0, 1.0, 0.0]) == \
        np.asarray([0.0, 0.0, 1.0])).all()
    assert (calc_plane_from_two_vectors.run([0.5, 0.5, 0.0], [0.0, 1.0, 0.0]) == \
        np.asarray([0.0, 0.0, 0.5])).all()

"""
def test_calc_theta_phi():

    from PIL import Image

    image_file_location = "test_files/2x2_pixel_value_1.tif"

    image = Image.open(image_file_location)
    pix = image.load()

    assert calc_theta_phi.run(2, 2, pix, [-180.0, 180.0], [0.0, 100.0], 2.0, 3.0, [0.0, -1.0, 0.0], [-1.00, 0.0, 0.0], [0.0, 0.0, 1.0], [0, 0], 1.0, 1.0, [0.0, -1.0, 0.0], [0.0, 0.0, 1.0], [0.0, 0.0], )
"""

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


