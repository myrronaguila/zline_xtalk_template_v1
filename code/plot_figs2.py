# -*- coding: utf-8 -*-
"""
Created on Thurs 20251113

Figs2 - Ramsey Sequence Characterization of Flux crosstalk
1. figs2a - Raw data of Ramsey (x and y-axes expressed in volts), signals in voltage
2. figs2b - Inverse transform of Ramsey (x and y-axes expressed in V-1), signals in arbitrary units

@author: Mai
"""

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import sys
import os

"""For loading figures, plotting and saving"""
from util_functions import set_font_default, color_map, xr_load_nc_to_dict

# retrieve files
dir_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
#print(dir_common_path)
sys.path.append(dir_data_path)

loc_figs2_ = dir_data_path + '\\' + 'data_figs2_.nc'
loc_figs2a = dir_data_path + '\\' + 'data_figs2a.nc'
loc_figs2b = dir_data_path + '\\' + 'data_figs2b.nc'

dict_figs2_ = xr_load_nc_to_dict(loc_figs2_) # format
dict_figs2a = xr_load_nc_to_dict(loc_figs2a) # colormap, Q1
dict_figs2b = xr_load_nc_to_dict(loc_figs2b) # colormap, Q1

# save files to png /or svg / set directory for saving.
dir_figures_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'figures'))
dir_save = dir_figures_path + '\\editable_source\\'
fname_figs2_png = dir_save + 'figs2ab.png'
fname_figs2_svg = dir_save + 'figs2ab.svg'

# format
figsize, lgd_loc = dict_figs2_['figsize'], dict_figs2_['lgd_loc']
pad = dict_figs2a['pad']
cmap = dict_figs2a['cmap']
frameon = dict_figs2_['frameon']
fsize = dict_figs2a['font_size']
set_font_default(fsize) # set default settings for plots
lsize = dict_figs2a['lgd_size']

"""-------------Figs2a-Raw Ramsey Data and Fit---------"""
# colormap
figs2a_x_sV_1d = dict_figs2a['x_volts']
figs2a_y_pV_1d = dict_figs2a['y_volts']
figs2a_z_vrms_2d = dict_figs2a['z_vrms_(uV)']

# fit line
figs2a_xfit_sV_1d = dict_figs2a['xfit_volts']
figs2a_yfit_pV_1d = dict_figs2a['yfit_volts']
figs2a_data_lgd, figs2a_lscol = dict_figs2a['data_lgd'], dict_figs2a['yfit_cls'] 

# format fig lim, ticks and labels
figs2a_xlabel, figs2a_ylabel =  dict_figs2a['xlabel'], dict_figs2a['ylabel']
figs2a_zlabel =  dict_figs2a['zlabel']
figs2a_xlim, figs2a_ylim = dict_figs2a['xlim'], dict_figs2a['ylim']
figs2a_xticks, figs2a_yticks = dict_figs2a['xticks'], dict_figs2a['yticks']
figs2a_zticks = dict_figs2a['zticks']

# format colorbar
figs2a_cbar_locs, figs2a_cbar_ori = dict_figs2a['cbar_locs'], dict_figs2a['cbar_ori']
"""-------------Figs2a-Raw Ramsey Data and Fit---------"""
# colormap
figs2a_x_sV_1d = dict_figs2a['x_volts']
figs2a_y_pV_1d = dict_figs2a['y_volts']
figs2a_z_vrms_2d = dict_figs2a['z_vrms_(uV)']

# fit line
figs2a_xfit_1d = dict_figs2a['xfit_volts']
figs2a_yfit_1d = dict_figs2a['yfit_volts']
figs2a_data_lgd, figs2a_lscol = dict_figs2a['data_lgd'], dict_figs2a['yfit_cls'] 

# format fig lim, ticks and labels
figs2a_xlabel, figs2a_ylabel =  dict_figs2a['xlabel'], dict_figs2a['ylabel']
figs2a_zlabel =  dict_figs2a['zlabel']
figs2a_xlim, figs2a_ylim = dict_figs2a['xlim'], dict_figs2a['ylim']
figs2a_xticks, figs2a_yticks = dict_figs2a['xticks'], dict_figs2a['yticks']
figs2a_zticks = dict_figs2a['zticks']

# format colorbar
figs2a_cbar_ori, figs2a_cbar_ori = dict_figs2a['cbar_locs'], dict_figs2a['cbar_ori']

"""--------------Figs2b-Ramsey k-space-------------------"""
# colormap
figs2b_x_k_1d = dict_figs2b['x_k_(1_V)']
figs2b_y_k_1d = dict_figs2b['y_k_(1_V)']
figs2b_z_amp_2d = dict_figs2b['z_amp_(arb)']

# format fig lim, ticks and labels
figs2b_xlabel, figs2b_ylabel =  dict_figs2b['xlabel'], dict_figs2b['ylabel']
figs2b_zlabel =  dict_figs2b['zlabel']
figs2b_xlim, figs2b_ylim = dict_figs2b['xlim'], dict_figs2b['ylim']
figs2b_xticks, figs2b_yticks = dict_figs2b['xticks'], dict_figs2b['yticks']
figs2b_zticks = dict_figs2b['zticks']

# format colorbar
figs2b_cbar_locs, figs2b_cbar_ori = dict_figs2b['cbar_locs'], dict_figs2b['cbar_ori']

"""----------------vertical plot (desired output plots)---------------------"""
fig = plt.figure(constrained_layout=True, figsize=figsize)
spec = gridspec.GridSpec(ncols=2, nrows=1, figure=fig, hspace=0.0, wspace=0.02)
ax0 = fig.add_subplot(spec[0, 0]) # 2D map of Ramsey signal with slope
ax1 = fig.add_subplot(spec[0, 1]) # inverse transform of Ramsey

# ax0 -> ramsey in volts
color_map(fig=fig, ax=ax0, x_dat=figs2a_x_sV_1d, y_dat=figs2a_y_pV_1d, 
          z_dat=figs2a_z_vrms_2d, 
          axs_lbl=[figs2a_xlabel, figs2a_ylabel, figs2a_zlabel], 
          cmap=cmap, ticks_2D=[figs2a_xticks, figs2a_yticks, figs2a_zticks], 
          pad_dat=pad, font_size=fsize, 
          prop_colbar=[figs2a_cbar_locs, figs2a_cbar_ori], norm='N', 
          cbar=True)
ax0.plot(figs2a_xfit_1d, figs2a_yfit_1d, figs2a_lscol, 
         label=figs2a_data_lgd)
ax0.set_xlim(figs2a_xlim)
ax0.set_ylim(figs2a_ylim)
ax0.legend(loc=lgd_loc[0], frameon=frameon[0], fontsize=lsize)

# ax1 -> ramsey in inverse of volts
color_map(fig=fig, ax=ax1, x_dat=figs2b_x_k_1d, y_dat=figs2b_y_k_1d, 
          z_dat=figs2b_z_amp_2d, 
          axs_lbl=[figs2b_xlabel, figs2b_ylabel, figs2b_zlabel], 
          cmap=cmap, ticks_2D=[figs2b_xticks, figs2b_yticks, figs2b_zticks], 
          pad_dat=pad, font_size=fsize, 
          prop_colbar=[figs2b_cbar_locs, figs2b_cbar_ori], norm='N', 
          cbar=True)
ax1.set_xlim(figs2b_xlim)
ax1.set_ylim(figs2b_ylim)
plt.savefig(fname_figs2_png, dpi=300)
plt.show()