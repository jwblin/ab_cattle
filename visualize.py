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
        http://stackoverflow.com/a/19591764 (some code from there, except 
        their solutions is slightly incorrect in that they do not account 
        for the fact that the colormap is normalized.  See http://
        matplotlib.org/api/colors_api.html#matplotlib.colors.Colormap for 
        details regarding colormap normalization.  As a result, I create 
        the RGB triples for each data location.
    """
    #- Initialize data for the farm: where cattle state values of 0 are 
    #  mapped to black, 1 to blue, 2 to red, and 3 to white.  For 
    #  information about color codes, see: http://matplotlib.org/api/
    #  colors_api.html.  For some reason, on my computer, green, gray,
    #  and magenta are not converting properly to RGB, so I choose
    #  different coloring:

    data = N.zeros((aFarm.length, aFarm.width, 3), dtype='l')
    cmap = ['k', 'b', 'r', 'w']
    convert = matplotlib.colors.ColorConverter()

    if len(list_of_cattle) != 0:       #- data for a non-empty farm
        for i in list_of_cattle:
            temp = N.array( convert.to_rgb( cmap[i.state_as_int()] ) )
            data[i.loc_in_environ[0], i.loc_in_environ[1], :] = temp[:]

            if id(aFarm) != id(i.environ):
                raise ValueError, "Cattle not all on same farm"
    else:                              #- data for empty farm
        pass


    #- Create figure and axes objects:

    fig, ax = plt.subplots(1, 1)


    #- Plot the image, turn off the axes labels, and (maybe) show the plot:

    ax.imshow(data, interpolation='none',
              extent=[0, aFarm.width, 0, aFarm.length],
              zorder=0)
    ax.axis('off')

    if show == True:
        plt.show()


    #- Return values:

    return fig, ax
