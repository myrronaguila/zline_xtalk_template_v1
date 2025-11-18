# -*- coding: utf-8 -*-
"""
Created on Thurs 20251113

Figs5 - Demonstration of flux-dependent inhomogeneous broadening
1. figs5a - Normalized Rabi angles of Q1 and C1 vs flux bias
2. figs5b - Rabi Drive Amplitude vs flux bias (C1, dotted lines, Q1, solid lines)
3. figs5c - FWHM vs flux bias for C1 and Q1
4. figs5d - 2D color of flux-induced broadening at swept XY frequency and normalizedt

@author: Mai
"""

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import sys
import os

"""For loading figures, plotting and saving"""
from util_functions import set_font_default, xr_load_nc_to_dict, color_map

# retrieve files
dir_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
#print(dir_common_path)
sys.path.append(dir_data_path)
loc_figs5_ = dir_data_path + '\\' + 'data_figs5_.nc'
loc_figs5a = dir_data_path + '\\' + 'data_figs5a.nc'
loc_figs5b = dir_data_path + '\\' + 'data_figs5b.nc'
loc_figs5c = dir_data_path + '\\' + 'data_figs5c.nc'
loc_figs5d = dir_data_path + '\\' + 'data_figs5d.nc'

dict_figs5_ = xr_load_nc_to_dict(loc_figs5_) # format
dict_figs5a = xr_load_nc_to_dict(loc_figs5a) # lineplot, dipole matrix Q1, C1
dict_figs5b = xr_load_nc_to_dict(loc_figs5b) # lineplot, rabi amplitude Q1, C1
dict_figs5c = xr_load_nc_to_dict(loc_figs5c) # lineplot, FWHM Q1, C1
dict_figs5d = xr_load_nc_to_dict(loc_figs5d) # colormap, FWHM Q1 

# save files to png /or svg / set directory for saving.
dir_figures_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'figures'))
dir_save = dir_figures_path + '\\editable_source\\'
# save files to png /or svg
fname_figs5_png = dir_save + 'figs5abcd.png'
fname_figs5_svg = dir_save + 'figs5abcd.svg'

# format
figsize, lgd_loc = dict_figs5_['figsize'], dict_figs5_['lgd_loc']
frameon = dict_figs5_['frameon']
fsize = dict_figs5a['font_size']
set_font_default(fsize) # set default settings for plots
lsize = dict_figs5a['lgd_size']
xlabel = dict_figs5a['xlabel']

"""----------------Figs5a-phi vs Rabi_angle---------------------------------"""
# line-plot
figs5a_x_norm_1d = dict_figs5a['x_flux_(nflux)']
figs5a_q1_theta_1d = dict_figs5a['y_ntheta'][0]
figs5a_c1_theta_1d = dict_figs5a['y_ntheta'][1]

# format
figs5a_ylabel = dict_figs5a['ylabel']
figs5a_xlim, figs5a_ylim = dict_figs5a['xlim'], dict_figs5a['ylim'] 
figs5a_xticks, figs5a_yticks = dict_figs5a['xticks'], dict_figs5a['yticks']
figs5a_q1_lgd, figs5a_c1_lgd = dict_figs5a['data_lgd'][0], dict_figs5a['data_lgd'][1]
figs5a_q1_cls, figs5a_c1_cls = dict_figs5a['data_cls'][0], dict_figs5a['data_cls'][1]
 
"""-------------Figs5a-phi vs Rabi amplitude--------------------------------"""
# lineplot, Q1[0-3], solid line, with legend
figs5b_x_norm_1d = dict_figs5b['x_flux_(nflux)']
figs5b_y_q1rabi_list = dict_figs5b['y_rabi_(MHz)'] #0-3, Q1, 4-7, C1
figs5b_q1data_lgd = dict_figs5b['data_lgd'][:4]
figs5b_q1data_cls = dict_figs5b['data_cls'][:4] # only q1 has legend

# lineplot C1, C1[4-7],
figs5b_y_c1rabi_list = dict_figs5b['y_rabi_(MHz)'][4:]
figs5b_c1data_cls = dict_figs5b['data_cls'][4:] # only q1 has legend


# format
figs5b_xlabel, figs5b_ylabel = dict_figs5b['xlabel'], dict_figs5b['ylabel']
figs5b_xticks, figs5b_yticks = dict_figs5b['xticks'], dict_figs5b['yticks']
figs5b_xlim, figs5b_ylim = dict_figs5b['xlim'], dict_figs5b['ylim'] 

# """--------------Fig3c-SFlux-C1, P-Flux-Q1, after flux compensation---------"""
# FWHM
figs5c_x_norm_1d = dict_figs5c['x_flux_(nflux)']
figs5c_y_q1fwhm_1d = dict_figs5c['y_fwhm_(MHz)'][0]
figs5c_y_c1fwhm_1d = dict_figs5c['y_fwhm_(MHz)'][1]
figs5c_y_rffwhm_1d = dict_figs5c['yref_fwhm_(MHz)']

# # format
figs5c_q1_lgd = dict_figs5c['data_lgd'][0]
figs5c_c1_lgd = dict_figs5c['data_lgd'][1]

figs5c_q1_cls = dict_figs5c['data_cls'][0]
figs5c_c1_cls = dict_figs5c['data_cls'][1]

figs5c_xlim, figs5c_ylim = dict_figs5c['xlim'], dict_figs5c['ylim']

figs5c_xticks, figs5c_yticks = dict_figs5c['xticks'], dict_figs5c['yticks']
figs5c_ylabel = dict_figs5c['ylabel']

# """-------------Fig3d-SFlux-Q1, P-Flux-C1, before flux compensation---------"""
# colormap, Source=C1
figs5d_x_norm_1d = dict_figs5d['x_flux_(nflux)']
figs5d_y_fxy_1d = dict_figs5d['y_fxy_(MHz)']
figs5d_z_pop_2d = dict_figs5d['z_pop_(%)']

# format
figs5d_xlim, figs5d_ylim = dict_figs5d['xlim'], dict_figs5d['ylim']
figs5d_xticks, figs5d_yticks = dict_figs5d['xticks'], dict_figs5d['yticks']
figs5d_zticks = dict_figs5d['zticks']

pad = dict_figs5d['pad']
cmap = dict_figs5d['cmap']
ylabel = dict_figs5d['ylabel']
zlabel = dict_figs5d['zlabel']


# # colorbar labels
# # # cbar_dim = ['x-loc', 'y-loc', 'width' 'height']
figs5d_cbar_locs = dict_figs5d['cbar_locs']
figs5d_cbar_ori = dict_figs5d['cbar_ori']

"""----------------vertical plot (desired output plots)---------------------"""
fig = plt.figure(constrained_layout=True, figsize=figsize)
# # main text, v2, gridspec, row, col 
spec = gridspec.GridSpec(ncols=2, nrows=2, figure=fig, hspace=-0.15, wspace=-0.1)
ax0 = fig.add_subplot(spec[0, 0]) # top left, theta/theta_0
ax1 = fig.add_subplot(spec[0, 1]) # top right, Q1 and Q2, rabi amplitude at different angle
ax2 = fig.add_subplot(spec[1, 0]) # mid left, Q1, C1 - FWHM, dotted, spectroscopy, thresholding, fit
ax3 = fig.add_subplot(spec[1, 1]) # mid right, C1 - Rabi-induced broadening

# figs5a
ax0.plot(figs5a_x_norm_1d[0], figs5a_q1_theta_1d, c=figs5a_q1_cls[0], 
         ls=figs5a_q1_cls[1], label=figs5a_q1_lgd)
ax0.plot(figs5a_x_norm_1d[1], figs5a_c1_theta_1d, c=figs5a_c1_cls[0],
         ls=figs5a_c1_cls[1], label=figs5a_c1_lgd)
# ax0.set_xlabel(xlabel, labelpad=-1)
ax0.set_ylabel(figs5a_ylabel, labelpad=-1)
ax0.set_xticks(figs5a_xticks)
ax0.set_yticks(figs5a_yticks)
ax0.tick_params(axis = 'both', which ='both', direction='in', top=True, 
                right = True)
ax0.legend(loc=lgd_loc[0], frameon=frameon[0], fontsize=lsize)

# figs5b, Q1
ax1.plot(figs5b_x_norm_1d, figs5b_y_q1rabi_list[0], c=figs5b_q1data_cls[0,0], 
         ls=figs5b_q1data_cls[0,1], label=figs5b_q1data_lgd[0])
ax1.plot(figs5b_x_norm_1d, figs5b_y_q1rabi_list[1], c=figs5b_q1data_cls[1,0], 
         ls=figs5b_q1data_cls[1,1], label=figs5b_q1data_lgd[1])
ax1.plot(figs5b_x_norm_1d, figs5b_y_q1rabi_list[2], c=figs5b_q1data_cls[2,0], 
         ls=figs5b_q1data_cls[2,1], label=figs5b_q1data_lgd[2])
ax1.plot(figs5b_x_norm_1d, figs5b_y_q1rabi_list[3], c=figs5b_q1data_cls[3,0], 
         ls=figs5b_q1data_cls[3,1], label=figs5b_q1data_lgd[3])
# figs5b, C1
ax1.plot(figs5b_x_norm_1d, figs5b_y_c1rabi_list[0], c=figs5b_c1data_cls[0,0], 
         ls=figs5b_c1data_cls[0,1])
ax1.plot(figs5b_x_norm_1d, figs5b_y_c1rabi_list[1], c=figs5b_c1data_cls[1,0], 
         ls=figs5b_c1data_cls[1,1])
ax1.plot(figs5b_x_norm_1d, figs5b_y_c1rabi_list[2], c=figs5b_c1data_cls[2,0], 
         ls=figs5b_c1data_cls[2,1])
ax1.plot(figs5b_x_norm_1d, figs5b_y_c1rabi_list[3], c=figs5b_c1data_cls[3,0], 
         ls=figs5b_c1data_cls[3,1])
# ax0.set_xlabel(xlabel, labelpad=-1)
ax1.set_ylabel(figs5b_ylabel, labelpad=-1)
ax1.set_xticks(figs5b_xticks)
ax1.set_yticks(figs5b_yticks)
ax1.tick_params(axis = 'both', which ='both', direction='in', top=True, 
                right = True)
ax1.legend(loc=lgd_loc[1], frameon=frameon[1], fontsize=lsize)

# figs5c
ax2.plot(figs5c_x_norm_1d, figs5c_y_q1fwhm_1d, c=figs5c_q1_cls[0], 
         ls=figs5c_q1_cls[1], label=figs5c_q1_lgd)
ax2.plot(figs5c_x_norm_1d, figs5c_y_c1fwhm_1d, c=figs5c_c1_cls[0], 
         ls=figs5c_c1_cls[1], label=figs5c_c1_lgd)
ax2.plot(figs5c_x_norm_1d, figs5c_y_rffwhm_1d, 'k:')
ax2.set_xlabel(xlabel, labelpad=-1)
ax2.set_ylabel(figs5c_ylabel, labelpad=-1)
ax2.set_xticks(figs5c_xticks)
ax2.set_yticks(figs5c_yticks)
ax2.tick_params(axis = 'both', which ='both', direction='in', top=True, 
                right = True)
ax2.legend(loc=lgd_loc[2], frameon=frameon[2], fontsize=lsize)


# # figs5d
color_map(fig=fig, ax=ax3, x_dat=figs5d_x_norm_1d, y_dat=figs5d_y_fxy_1d, 
          z_dat=figs5d_z_pop_2d, axs_lbl=[xlabel, ylabel, zlabel], 
          cmap=cmap, ticks_2D=[figs5d_xticks, figs5d_yticks, figs5d_zticks], 
          pad_dat=pad, font_size=fsize, 
          prop_colbar=[figs5d_cbar_locs, figs5d_cbar_ori], norm='N')
ax3.set_xlim(figs5d_xlim)
ax3.set_ylim(figs5d_ylim)
ax3.tick_params(axis = 'both', which ='both', direction='in', top=True, 
                right = True)
ax3.legend(loc=lgd_loc[3], frameon=frameon[3], fontsize=fsize)
plt.savefig(fname_figs5_png, dpi=300) # png
plt.show()