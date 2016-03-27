#==============================================================================
# Visualization functions for the model
#
# By Johnny Lin
# May 2015
#==============================================================================


#------------------------------------------------------------------------------
import numpy as N
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


#------------------------------------------------------------------------------
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
    #  mapped to black, 1 to blue, 2 to white, 3 to gray, and 4 to darker
    #  gray.  The colors in the cmap corresponds to environment, Susceptible, 
    #  Infected, Recovered, Processed.  For information about color codes, 
    #  see:  http://matplotlib.org/api/colors_api.html:

    data = N.zeros((aFarm.length, aFarm.width, 3), dtype='f')
    cmap = ['k', 'b', 'w', '0.5', '0.1']
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


#------------------------------------------------------------------------------
def plot_ranch(modelobj, use_objs=None):
    """Plot the entire ranch given a model object.
   
    See the comments in plot_farm for more information.

    Parameters
    ----------
    use_objs : tuple, list
        Three element Tuple or list giving the Figure (first element),
        Axes (next element, a tuple of n elements), and Image objects
        (next element, a tuple of n elements), where n is the number of
        farms modelobj.num_farms, on which to draw another plot on top of.

    Returns
    -------
        The Figure, Axes, and Image objects of the plot.

    Notes
    -----
        In order for the plot to work, you have to manually pick where the 
        subplots are in the frame using add_axes (see http://matplotlib.org/
        users/artists.html).  Note imshow needs to set the aspect keyword to 
        "auto".  See: http://stackoverflow.com/a/13390798.
    """
    #- Preliminaries:  The colors in each cmap corresponds to environment, 
    #  Susceptible, Infected, Recovered, Processed.

    cmap_farm = ['0.0', 'b', 'w', '0.5', '0.1']   #+ Default (element 0) color
    cmap_road = ['0.8', 'b', 'w', '0.5', '0.1']   #  for an environment must
    cmap_stock = ['0.5', 'b', 'w', '0.5', '0.1']  #  be a gray
    cmap_sale = ['0.2', 'b', 'w', '0.5', '0.1']
    cmap_feed = ['0.4', 'b', 'w', '0.5', '0.1']
    cmap_abat = ['0.9', 'b', 'w', '0.5', '0.1']
    convert = matplotlib.colors.ColorConverter()

    if use_objs == None:
        fig = plt.figure(figsize=(6,7))
        axs = []
        imgs = []


        #+ Abbreviations:

        l_farm = modelobj.list_farms[0].length
        w_farm = modelobj.list_farms[0].width
        l_stock = modelobj.stocker.length
        w_stock = modelobj.stocker.width
        l_road = modelobj.roadeast.length
        w_road = modelobj.roadeast.width
        l_sale = modelobj.salebarn.length
        w_sale = modelobj.salebarn.width
        l_feed = modelobj.feedlot.length
        w_feed = modelobj.feedlot.width
        l_abat = modelobj.abattoir.length
        w_abat = modelobj.abattoir.width

        tot_horiz = (w_farm * 6) + 5
        tot_vert = l_farm + l_road + l_stock + 2
        tot_horiz = float(tot_horiz)
        tot_vert = float(tot_vert)

        #+ Setup farms subplots:

        axs.append(fig.add_axes( (0.0, 
                                 (l_stock+l_road+1)/tot_vert,
                                 w_farm/tot_horiz, l_farm/tot_vert),
                                 frameon=False ))
        axs.append(fig.add_axes( ((w_farm+1)/tot_horiz,
                                 (l_stock+l_road+1)/tot_vert,
                                 w_farm/tot_horiz, l_farm/tot_vert),
                                 frameon=False ))
        axs.append(fig.add_axes( ((w_farm+1)*2/tot_horiz,
                                 (l_stock+l_road+1)/tot_vert,
                                 w_farm/tot_horiz, l_farm/tot_vert),
                                 frameon=False ))
        axs.append(fig.add_axes( ((w_farm+1)*3/tot_horiz,
                                 (l_stock+l_road+1)/tot_vert,
                                 w_farm/tot_horiz, l_farm/tot_vert),
                                 frameon=False ))
        axs.append(fig.add_axes( ((w_farm+1)*4/tot_horiz,
                                 (l_stock+l_road+1)/tot_vert,
                                 w_farm/tot_horiz, l_farm/tot_vert),
                                 frameon=False ))
        axs.append(fig.add_axes( ((w_farm+1)*5/tot_horiz,
                                 (l_stock+l_road+1)/tot_vert,
                                 w_farm/tot_horiz, l_farm/tot_vert),
                                 frameon=False ))


        #+ Setup roadeast and roadwest subplots:

        axs.append(fig.add_axes( (0.0,
                                 (l_stock+1)/tot_vert,
                                 (w_road+2)/tot_horiz, l_road/tot_vert),
                                 frameon=False ))
        axs.append(fig.add_axes( ((w_road+2+w_sale)/tot_horiz,
                                 (l_stock+1)/tot_vert,
                                 (w_road+2)/tot_horiz, l_road/tot_vert),
                                 frameon=False ))


        #+ Setup stocker subplots:

        axs.append(fig.add_axes( (0.0, 0.0,
                                 (w_stock+2)/tot_horiz, l_stock/tot_vert),
                                 frameon=False ))


        #+ Setup salebarn, feedlot, and abattoir subplots:

        axs.append(fig.add_axes( ((w_stock+2)/tot_horiz, 0.0,
                                 w_sale/tot_horiz, (l_stock+2)/tot_vert),
                                 frameon=False ))

        axs.append(fig.add_axes( ((w_stock+2+w_sale)/tot_horiz, 0.0,
                                 w_feed/tot_horiz, l_feed/tot_vert),
                                 frameon=False ))

        axs.append(fig.add_axes( ((w_stock+2+w_sale+w_feed)/tot_horiz, 0.0,
                                 w_abat/tot_horiz, l_abat/tot_vert),
                                 frameon=False ))


        #+ Setup annotation subplot:

        axs.append(fig.add_axes( ((w_stock+2+w_sale+w_feed+w_abat)/tot_horiz,
                         0.0,
                         (tot_horiz-w_stock+2+w_sale+w_feed+w_abat)/tot_horiz,
                         l_abat/tot_vert),
                         frameon=False ))

    else:
        fig = use_objs[0]
        axs = use_objs[1]
        imgs = use_objs[2]


    #- Plot farms (note that you need to reverse the width position for
    #  farms to the east of the salebarn):

    for ifcount in range(len(modelobj.list_farms)):
        iFarm = modelobj.list_farms[ifcount]
        data = N.ones((iFarm.length, iFarm.width, 3), dtype='f') \
             * float(cmap_farm[0])

        for i in iFarm.list_cattle:
            temp = N.array( convert.to_rgb( cmap_farm[i.state_as_int()] ) )
            if ifcount >= 3:
                data[i.loc_in_environ[0], 
                    iFarm.width-1-i.loc_in_environ[1], :] = temp[:]
            else:
                data[i.loc_in_environ[0], i.loc_in_environ[1], :] = temp[:]
            if id(iFarm) != id(i.environ):
                raise ValueError, "Cattle not all on same farm"

        if use_objs == None:
            ax = axs[ifcount]
            imgs.append( ax.imshow(data, interpolation='none',
                                   extent=[0, iFarm.width, 0, iFarm.length],
                                   aspect="auto",
                                   zorder=0) )
            ax.axis('off')
        else:
            img = imgs[ifcount]
            img.set_data(data)
            plt.draw()


    #- Plot roads (note that you need to reverse the width position for
    #  roadwest which is to the east of the salebarn):

    data_re = N.ones((modelobj.roadeast.length, modelobj.roadeast.width, 3), 
                     dtype='f') * float(cmap_road[0])
    for i in modelobj.roadeast.list_cattle:
        temp = N.array( convert.to_rgb( cmap_road[i.state_as_int()] ) )
        data_re[i.loc_in_environ[0], i.loc_in_environ[1], :] = temp[:]

    data_rw = N.ones((modelobj.roadwest.length, modelobj.roadwest.width, 3), 
                     dtype='f') * float(cmap_road[0])
    for i in modelobj.roadwest.list_cattle:
        temp = N.array( convert.to_rgb( cmap_road[i.state_as_int()] ) )
        data_rw[i.loc_in_environ[0],  
            modelobj.roadwest.width-1-i.loc_in_environ[1], :] = temp[:]

    if use_objs == None:
        imgs.append( axs[6].imshow(data_re, interpolation='none',
               extent=[0, modelobj.roadeast.width, 0, modelobj.roadeast.length],
               aspect="auto",
               zorder=0) )
        axs[6].axis('off')

        imgs.append( axs[7].imshow(data_rw, interpolation='none',
               extent=[0, modelobj.roadwest.width, 0, modelobj.roadwest.length],
               aspect="auto",
               zorder=0) )
        axs[7].axis('off')

    else:
        imgs[6].set_data(data_re)
        imgs[7].set_data(data_rw)
        plt.draw()


    #- Plot stocker:

    data = N.ones((modelobj.stocker.length, modelobj.stocker.width, 3), 
                  dtype='f') * float(cmap_stock[0])
    for i in modelobj.stocker.list_cattle:
        temp = N.array( convert.to_rgb( cmap_stock[i.state_as_int()] ) )
        data[i.loc_in_environ[0], i.loc_in_environ[1], :] = temp[:]

    if use_objs == None:
        imgs.append( axs[8].imshow(data, interpolation='none',
               extent=[0, modelobj.stocker.width, 0, modelobj.stocker.length],
               aspect="auto",
               zorder=0) )
        axs[8].axis('off')

    else:
        imgs[8].set_data(data)
        plt.draw()


    #- Plot salebarn:

    data = N.ones((modelobj.salebarn.length, modelobj.salebarn.width, 3), 
                  dtype='f') * float(cmap_sale[0])
    for i in modelobj.salebarn.list_cattle:
        temp = N.array( convert.to_rgb( cmap_sale[i.state_as_int()] ) )
        data[i.loc_in_environ[0], i.loc_in_environ[1], :] = temp[:]

    if use_objs == None:
        imgs.append( axs[9].imshow(data, interpolation='none',
               extent=[0, modelobj.salebarn.width, 0, modelobj.salebarn.length],
               aspect="auto",
               zorder=0) )
        axs[9].axis('off')

    else:
        imgs[9].set_data(data)
        plt.draw()


    #- Plot feedlot:

    data = N.ones((modelobj.feedlot.length, modelobj.feedlot.width, 3), 
                  dtype='f') * float(cmap_feed[0])
    for i in modelobj.feedlot.list_cattle:
        temp = N.array( convert.to_rgb( cmap_feed[i.state_as_int()] ) )
        data[i.loc_in_environ[0], i.loc_in_environ[1], :] = temp[:]

    if use_objs == None:
        imgs.append( axs[10].imshow(data, interpolation='none',
               extent=[0, modelobj.feedlot.width, 0, modelobj.feedlot.length],
               aspect="auto",
               zorder=0) )
        axs[10].axis('off')

    else:
        imgs[10].set_data(data)
        plt.draw()


    #- Plot abattoir:

    data = N.ones((modelobj.abattoir.length, modelobj.abattoir.width, 3), 
                  dtype='f') * float(cmap_abat[0])
    for i in modelobj.abattoir.list_cattle:
        temp = N.array( convert.to_rgb( cmap_abat[i.state_as_int()] ) )
        data[i.loc_in_environ[0], i.loc_in_environ[1], :] = temp[:]

    if use_objs == None:
        imgs.append( axs[11].imshow(data, interpolation='none',
               extent=[0, modelobj.abattoir.width, 0, modelobj.abattoir.length],
               aspect="auto",
               zorder=0) )
        axs[11].axis('off')

    else:
        imgs[11].set_data(data)
        plt.draw()


    #- Plot text:  On removing text:  http://stackoverflow.com/a/5600964:
    
    if use_objs == None:
        imgs.append( axs[12].text( 0.05, 0.5, 
                     "t = " + str(modelobj.sim_day) + " d" ) )
        axs[12].axis('off')
    else:
        imgs[12].remove()
        imgs[12] = axs[12].text( 0.05, 0.5, 
                     "t = " + str(modelobj.sim_day) + " d" )
        axs[12].axis('off')
        plt.draw()
   

    #- Pause (on my Ubuntu 12.04 Linux box, it runs so slow that there's
    #  no need to include a pause):

    #plt.pause(0.05)

    return fig, axs, imgs
