import gempy
import os
import numpy as np
input_path = os.path.dirname(__file__)+'/../input_data'


def test_rescaled_marching_cube(interpolator):
    """
    2 Horizontal layers with drift 0
    """
    # Importing the data from csv files and setting extent and resolution
    geo_data = gempy.create_data('Simple interpolator', [0, 10, 0, 10, -10, 0], [50, 50, 50],
                                 path_o=input_path + "/GeoModeller/test_a/test_a_Foliations.csv",
                                 path_i=input_path + "/GeoModeller/test_a/test_a_Points.csv")

    geo_data.set_theano_function(interpolator)

    # Compute model
    sol = gempy.compute_model(geo_data, compute_mesh_options={'rescale': True})
    print(sol.vertices)

    return geo_data


def test_custom_grid_solution(model_horizontal_two_layers):
    """
    Integration test for a gempy model using a custom grid

    2 Horizontal layers with drift 0

    :param interpolator_islith_nofault:
    :return:
    """
    geo_model = model_horizontal_two_layers
    # add a custom grid
    cg = np.array([[5, 5, -9],
                   [5, 5, -5],
                   [5, 5, -5.1],
                   [5, 5, -5.2],
                   [5, 5, -1]])
    values = geo_model.set_custom_grid(cg)
    assert geo_model._grid.active_grids[1]
    # set the theano function

    # Compute model
    sol = gempy.compute_model(geo_model, compute_mesh=False)
    assert sol.custom.shape == (2,1,5)