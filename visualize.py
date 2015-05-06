#==============================================================================
# Visualization functions for the model
#
# By Johnny Lin
# May 2015
#==============================================================================


import numpy as N
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def plot_farm(aFarm, list_of_cattle=[], show=False):
    """Plot a farm.

    Parameters
    ----------
    show : boolean
        If True, the show function of pyplot is called to show the plot.

    Returns
    -------
    Figure, Axes
        The matplotlib Figure and Axes objects defining this plot are
        returned.

    Notes
    -----
        For information on plotting grids and gridlines, see:
        http://stackoverflow.com/a/19591764.  Code below is based on that
        source.
    """
    #- Initialize data for the farm:

    data = N.zeros((aFarm.length, aFarm.width), dtype='i')

    if len(list_of_cattle) != 0:       #- data for a non-empty farm
        for i in list_of_cattle:
            data[i.loc_in_environ[0], i.loc_in_environ[1]] = i.state_as_int()
    else:                              #- data for empty farm
        pass


    #- Create figure and axes objects:

    fig, ax = plt.subplots(1, 1)


    #- Create color map where data values of 0 are mapped to black, 1 to blue, 
    #  2 to white, and 3 to grey.  For information about color codes, see:
    #  http://matplotlib.org/api/colors_api.html:

    my_cmap = matplotlib.colors.ListedColormap(['k', 'b', 'w', '0.75'])


    #- Plot the image, turn off the axes labels, and (maybe) show the plot:

    ax.imshow(data, interpolation='none', 
              cmap=my_cmap, 
              extent=[0, aFarm.width, 0, aFarm.length], zorder=0)
    ax.axis('off')

    if show == True:
        plt.show()


    #- Return values:

    return fig, ax
