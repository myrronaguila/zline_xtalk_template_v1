# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 12:20:12 2025

util_functions.py
-> shared plotting or data utility functions. 
# Core function for standardized NetCDF data retrieval.

@author: Myrron Albert Callera Aguila, https://orcid.org/0000-0002-7910-8609
"""

import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
from seaborn import heatmap # for confusion matrix
from matplotlib.colors import SymLogNorm # for confusion matrix

"""-------------------------Retrieve data using xarray functions------------"""
def xr_load_nc_to_dict(filename):
    """
    Load a NetCDF file back into a dictionary using xarray.
    
    Args:
        filename: Input .nc filename
        
    Returns:
        Dictionary with the same structure as original
    """
    ds = xr.open_dataset(filename)
    data_dict = {}
    
    # Load attributes (strings)
    for attr_name, attr_value in ds.attrs.items():
        data_dict[attr_name] = attr_value
    
    # Load data variables
    for var_name in ds.data_vars:
        data = ds[var_name].values
        
        # Convert to appropriate type
        if data.ndim == 0:
            data_dict[var_name] = data.item()
        else:
            data_dict[var_name] = data
    
    ds.close()
    print(f"Loaded dictionary from {filename}")
    return data_dict

"""-------------------------Plotting functions------------------------------"""
def cm_to_inch(x):
    return x/2.54

def set_font_default(font_size):
    """
    Set font size to figures

    Parameters
    ----------
    font_size : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Arial']
    plt.rc('xtick', labelsize=font_size) 
    plt.rc('ytick', labelsize=font_size)
    plt.rcParams.update({'font.size': font_size})
    return

def color_map(fig, ax, x_dat, y_dat, z_dat, axs_lbl, cmap, ticks_2D, pad_dat, 
              font_size, prop_colbar, norm='N', **kwargs):
    """
    2D color map

    Parameters
    ----------
    fig : figure
        figure of drawing
    ax : axes
        ax.
    x_dat : 1D numpy array
        x_data.
    y_dat : 1D numpy array
        y_data.
    z_dat : 2D numpy array
        z_data.
    axs_lbl : list of strings
        axs_lbl[0] = x_label.
        axs_lbl[1] = y_label.
    cmap : string
        color map.
    ticks_2D : list of 1D numpy array
        ticks_2D[0] = xticks
        ticks_2D[1] = yticks
        ticks_2D[2] = zticks
    pad_dat : TYPE
        pad_dat[0] = x-label pads
        pad_dat[1] = y-label pads 
        pad_dat[2] = xticks pad
        pad_dat[3] = yticks pad
        pad_dat[4] = z-label pads
    font_size : integer
        font size.
    prop_colbar : list of list and string
        color bar within 2D map
        prop_colbar[0] = [x_coord (fraction of image (max=1)), 
                          y_coord (fraction of image (max=1)), 
                          width fraction (fraction of image (max=1)), 
                          length fraction (fraction of image (max=1))]
        prop_colbar[1] = 'horizontal' or vertical
    norm : string
        norm='Y' => set to zero value

    Returns
    -------
    None.

    """
    
    set_font_default(font_size=font_size)
    
    """Plot Data"""
    if norm=='Y':
        """Setting data"""
        """TwoSlopeNorm non-existent in Matplotlib 3.1.3"""
        # norm = mcolors.TwoSlopeNorm(vcenter=0, vmin=np.amin(z_dat), vmax=np.amax(z_dat))
        # im = ax.pcolormesh(x_dat, y_dat, z_dat, cmap=cmap, norm=norm, 
        #                    vmin=np.amin(z_dat), vmax=np.amax)
        """Matplotlib 3.1.3."""
        if np.abs(np.amin(z_dat)) > np.abs(np.amax(z_dat)):
            max_val = np.abs(np.amin(z_dat))
        else:
            max_val = np.abs(np.amax(z_dat))
        im = ax.pcolormesh(x_dat, y_dat, z_dat, cmap=cmap, 
                           vmin=-1*max_val, vmax=max_val) 
    else:
        if 'pow_norm' in kwargs:
            #norm = mcolors.PowerNorm(gamma=kwargs['pow_norm'])
            
            im = ax.pcolormesh(x_dat, y_dat, z_dat, cmap=cmap,
                               vmin=z_dat.min()*(1-kwargs['pow_norm']),
                               vmax=z_dat.max()*(1+kwargs['pow_norm']))
        else:
            im = ax.pcolormesh(x_dat, y_dat, z_dat, shading="auto", cmap=cmap)
        
    """Set x and y-labels"""
    ax.set_xlabel(axs_lbl[0], labelpad=pad_dat[0])
    ax.set_ylabel(axs_lbl[1], labelpad=pad_dat[1])
    
    """Set ticks based on input criteria"""
    if len(ticks_2D[0]) > 0:
        ax.set_xticks(ticks_2D[0])
    if len(ticks_2D[1]) > 0:
        ax.set_yticks(ticks_2D[1])
    
    """ticks_params Pad Data"""
    ax.tick_params('x', pad=pad_dat[2])
    ax.tick_params('y', pad=pad_dat[3])
    ax.tick_params(axis='both', which='major', direction='in', top=True, 
                   right=True, labelsize=font_size)
    
    def show_cbar(prop_colbar, pad_dat):
        # configure cbar per pcolormesh
        
        """Put color bar with ax1 but smaller"""
        # divider = make_axes_locatable(ax)
        cax = fig.add_axes(prop_colbar[0])
        # cax = divider.append_axes('right', size='5%', pad=0.05)
        if len(pad_dat) < 5:
            fig.colorbar(im, cax=cax, orientation=prop_colbar[1], label=axs_lbl[2])
        else:    
            fig.colorbar(im, cax=cax, orientation=prop_colbar[1], label=axs_lbl[2],
                         pad=pad_dat[4], ticks=ticks_2D[2])
        return
    
    if 'cbar' in kwargs:
        # toggle cbar properties
        if kwargs['cbar']==True:
            show_cbar(prop_colbar, pad_dat)
        else:
            return im
    else:
        # use default cbar properties, no mesh output
        show_cbar(prop_colbar, pad_dat)        
        return

def conf_matrix_standard(fig, ax, conf_matrix, ax_lbls, ax_tick_lbls, annot, 
                         cbar_ticks, cmap="bwr", norm=["Normalize", None, None, None],
                         font_size=9, **kwargs):
    """
    20250323 Standard confusion matrix
    
    Use cases:
        1. Readout fidelity of 1Q, 2Q and qudit states
        2. Flux Crosstalk Matrix 
        3. Microwave Crosstalk Matrix
        
    Parameters:
        ax : axes
        
        conf_matrix : 2D npy array
            2D matrix of values (col, rows) (nominal)
        ax_lbls : list of strings
            ax_lbls[0] = x-axis labels
            ax_lbls[1] = y-axis labels
            ax_lbls[2] = z-axis labels
        ax_tick_lbls : list of strings
            ax_tick_lbls[0] = x-tick labels (C1, Q1, C2, Q2)
            ax_tick_lbls[1] = y-tick labels (C1, Q1, C2, Q2)
        annot : 2D npy array of strings
            annot[:,0] => column (outside, either %, numeral, etc)
            annot[0,:] => rows
        cbar_ticks : list of list
            cbar_ticks[0] = boolean [False, Turn off Cbar], Default = True
            cbar_ticks[1] = cbar.set_ticks[]
            cbar_ticks[2] = cbar.set_ticklabels[]
        cmap : string
            cmap value
        norm : list of values
            norm[0] = "SymLogNorm"
            norm[1] = #vmin (vcenter for "CenteredNorm")
            norm[2] = #vmax
            norm[3] = #linthresh_val (SymLogNorm)
            norm[4] = #linscale
        # no need for pads for now
    """    
    if norm[0]=="SymLogNorm":
        # issue with SymLogNorm with sns.heatmap.
        norm1 = SymLogNorm(linthresh=norm[3], linscale=norm[4], vmin=norm[1], 
                           vmax=norm[2], base=10)
        
        """ heatmap from sns not working well for sym-log-norm"""
        ax = heatmap(conf_matrix, ax=ax, annot=annot, fmt="", cmap=cmap,
                      xticklabels=ax_tick_lbls[0], yticklabels=ax_tick_lbls[1],
                      linewidth=2, linecolor='k', square=False, edgecolors='k',
                      cbar=cbar_ticks[0], norm=norm1)
        
    else: 
        ax = heatmap(conf_matrix, ax=ax, annot=annot, fmt="", cmap=cmap, 
                      xticklabels=ax_tick_lbls[0], yticklabels=ax_tick_lbls[1],
                      linewidth=2, linecolor='k', square=False, edgecolors='k',
                      cbar=cbar_ticks[0])
    
    # Set X and Y axes labels
    set_font_default(font_size=font_size)
    ax.set(xlabel=ax_lbls[0], ylabel=ax_lbls[1])
    
    if (cbar_ticks[0]==True):
        cbar = ax.collections[0].colorbar
        cbar.set_label(ax_lbls[2])
        # cbar.orientation('vertical')

        # Define custom tick locations (log scale)
        cbar.set_ticks(cbar_ticks[1]) #e.g. [-1, -1E-1, 0, 1E-1, 1] 
        cbar.set_ticklabels(cbar_ticks[2])  # LaTeX formatting
    return 

