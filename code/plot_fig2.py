# -*- coding: utf-8 -*-
"""
Created on Thurs 20251113

Fig2 - qubit and coupler frequency vs voltage spectra
covered figures
1. fig2c - Q1 voltage / flux vs fq_q1
2. fig2d - C1 voltage / flux vs fq_c1
3. fig2e - Q2 voltage / flux vs fq_q2
4. fig2f - C2 voltage / flux vs fq_c2

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

loc_fig2_ = dir_data_path + '\\' + 'data_fig2_.nc'
loc_fig2c = dir_data_path + '\\' + 'data_fig2c.nc'
loc_fig2d = dir_data_path + '\\' + 'data_fig2d.nc'
loc_fig2e = dir_data_path + '\\' + 'data_fig2e.nc'
loc_fig2f = dir_data_path + '\\' + 'data_fig2f.nc'

dict_fig2_ = xr_load_nc_to_dict(loc_fig2_) # format
dict_fig2c = xr_load_nc_to_dict(loc_fig2c) # colormap, Q1
dict_fig2d = xr_load_nc_to_dict(loc_fig2d) # colormap, C1
dict_fig2e = xr_load_nc_to_dict(loc_fig2e) # colormap, Q2
dict_fig2f = xr_load_nc_to_dict(loc_fig2f) # colormap, C2

# save files to png /or svg / set directory for saving.
dir_figures_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'figures'))
dir_save = dir_figures_path + '\\editable_source\\'
fname_fig2cdef_png = dir_save + 'fig2cdef.png'
fname_fig2cdef_svg = dir_save + 'fig2cdef.svg'

# format
figsize, lgd_loc = dict_fig2_['figsize'], dict_fig2_['lgd_loc']
frameon = dict_fig2_['frameon']
cmap = dict_fig2c['cmap']
ls_col = dict_fig2c['fit_cls']
xlabel, x2label = dict_fig2c['xlabel'], dict_fig2c['x2label']
ylabel, zlabel = dict_fig2c['ylabel'], dict_fig2c['zlabel']
fsize = dict_fig2c['fsize']
set_font_default(fsize) # set default settings for plots
lsize = dict_fig2c['lsize']
pad = dict_fig2c['pad']

# global, figs2b,2d,
q1q2_xlim = dict_fig2c['xlim']
c1c2_xlim = dict_fig2d['xlim']

q1_ylim = dict_fig2c['ylim']
c1_ylim = dict_fig2d['ylim']
q2_ylim = dict_fig2e['ylim']
c2_ylim = dict_fig2f['ylim']

"""------------------Fig2c-Q1-----------------------------------------------"""
# colormap, Q1, data
q1_x_V_1d = dict_fig2c['x_V_(volts)']
q1_x2_norm_phi_1d = dict_fig2c['x2_norm_phi']
q1_y_fxy_1d = dict_fig2c['y_fxy_(MHz)']
q1_z_vrms_2d = dict_fig2c['z_vrms_(uV)']

# line fit, Q1
q1_xfit_V_1d = dict_fig2c['xfit_V_(volts)']
q1_yfit_V_1d = dict_fig2c['yfit_fxy_(MHz)']
q1_data_lgd = dict_fig2c['data_lgd']

# format Q1
q1_xticks, q1_x2ticks = dict_fig2c['xticks'], dict_fig2c['x2ticks']
q1_yticks, q1_zticks = dict_fig2c['yticks'], dict_fig2c['zticks']
# align q1_x2ticks with x axis
q1_x2ticks_p = dict_fig2c['x2ticks_p']
# colorbar labels
q1_cbar_locs = dict_fig2c['cbar_locs']
q1_cbar_ori = dict_fig2c['cbar_ori']

"""------------------Fig2d-C1-----------------------------------------------"""
# colormap, C1, data
c1_x_V_1d = dict_fig2d['x_V_(volts)']
c1_x2_norm_phi_1d = dict_fig2d['x2_norm_phi']
c1_y_fxy_1d = dict_fig2d['y_fxy_(MHz)']
c1_z_vrms_2d = dict_fig2d['z_vrms_(uV)']

# line fit, C1
c1_xfit_V_1d = dict_fig2d['xfit_V_(volts)']
c1_yfit_V_1d = dict_fig2d['yfit_fxy_(MHz)']
c1_data_lgd = dict_fig2d['data_lgd']

# format C1
c1_xticks, c1_x2ticks = dict_fig2d['xticks'], dict_fig2d['x2ticks']
c1_yticks, c1_zticks = dict_fig2d['yticks'], dict_fig2d['zticks']
# align c1_x2ticks with x axis
c1_x2ticks_p = dict_fig2d['x2ticks_p']
# colorbar labels
c1_cbar_locs = dict_fig2d['cbar_locs']
c1_cbar_ori = dict_fig2d['cbar_ori']

"""------------------Fig2e-Q2-----------------------------------------------"""
# colormap, Q2, data
q2_x_V_1d = dict_fig2e['x_V_(volts)']
q2_x2_norm_phi_1d = dict_fig2e['x2_norm_phi']
q2_y_fxy_1d = dict_fig2e['y_fxy_(MHz)']
q2_z_vrms_2d = dict_fig2e['z_vrms_(uV)']

# line fit, Q2
q2_xfit_V_1d = dict_fig2e['xfit_V_(volts)']
q2_yfit_V_1d = dict_fig2e['yfit_fxy_(MHz)']
q2_data_lgd = dict_fig2e['data_lgd']

# format Q2
q2_xticks, q2_x2ticks = dict_fig2e['xticks'], dict_fig2e['x2ticks']
q2_yticks, q2_zticks = dict_fig2e['yticks'], dict_fig2e['zticks']
# align q2_x2ticks with x axis
q2_x2ticks_p = dict_fig2e['x2ticks_p']
# colorbar labels
q2_cbar_locs = dict_fig2e['cbar_locs']
q2_cbar_ori = dict_fig2e['cbar_ori']

"""------------------Fig2f-C2-----------------------------------------------"""
# colormap, C2, data
c2_x_V_1d = dict_fig2f['x_V_(volts)']
c2_x2_norm_phi_1d = dict_fig2f['x2_norm_phi']
c2_y_fxy_1d = dict_fig2f['y_fxy_(MHz)']
c2_z_vrms_2d = dict_fig2f['z_vrms_(uV)']

# line fit, C2
c2_xfit_V_1d = dict_fig2f['xfit_V_(volts)']
c2_yfit_V_1d = dict_fig2f['yfit_fxy_(MHz)']
c2_data_lgd = dict_fig2f['data_lgd']

# format C2
c2_xticks, c2_x2ticks = dict_fig2f['xticks'], dict_fig2f['x2ticks']
c2_yticks, c2_zticks = dict_fig2f['yticks'], dict_fig2f['zticks']
# align q2_x2ticks with x axis
c2_x2ticks_p = dict_fig2f['x2ticks_p']
# colorbar labels
c2_cbar_locs = dict_fig2f['cbar_locs']
c2_cbar_ori = dict_fig2f['cbar_ori']

"""----------------Original Plot (desired output plots)---------------------"""
fig = plt.figure(constrained_layout=True, figsize=figsize)
spec = gridspec.GridSpec(ncols=2, nrows=2, figure=fig, hspace=-0.15, wspace=-0.1)
ax0 = fig.add_subplot(spec[0, 0]) # fig2c, Q1, volts
ax1 = fig.add_subplot(spec[0, 1]) # fig2d, C1, volts
ax2 = fig.add_subplot(spec[1, 0]) # fig2e, Q2, volts
ax3 = fig.add_subplot(spec[1, 1]) # fig2f, C2, volts

ax0t = ax0.twiny() # create twin x axis for Q1, flux
ax1t = ax1.twiny() # create twin x axis for C1, flux
ax2t = ax2.twiny() # create twin x axis for Q2, flux
ax3t = ax3.twiny() # create twin x axis for C2, flux

# fig2c, Q1
color_map(fig=fig, ax=ax0, x_dat=q1_x_V_1d, y_dat=q1_y_fxy_1d, 
          z_dat=q1_z_vrms_2d, axs_lbl=['', ylabel, zlabel], 
          cmap=cmap, ticks_2D=[q1_xticks, q1_yticks,q1_yticks], 
          pad_dat=pad, font_size=fsize, prop_colbar=[q1_cbar_locs, q1_cbar_ori], norm='N')
ax0.set_xlim(q1q2_xlim)
ax0.set_ylim(q1_ylim)
ax0.tick_params(axis='both', which='major', direction='in', top=False, 
                right=True, labelsize=fsize)
# add twinx axis
# CRITICAL: Set the same limits as primary axis
ax0t.set_xlim(ax0.get_xlim())
ax0t.set_xticks(q1_x2ticks_p)
ax0t.set_xticklabels([f'{q1_x2ticks[i]:.1f}' for i in range(len(q1_x2ticks_p))])
ax0t.set_xlabel(x2label)

# put fit label
ax0.plot(q1_xfit_V_1d, q1_yfit_V_1d, ls_col, label=q1_data_lgd)
ax0.legend(loc=lgd_loc[0], frameon=frameon[0])

# fig2d, C1
color_map(fig=fig, ax=ax1, x_dat=c1_x_V_1d, y_dat=c1_y_fxy_1d, 
          z_dat=c1_z_vrms_2d, axs_lbl=['', '', zlabel], 
          cmap=cmap, ticks_2D=[c1_xticks, c1_yticks, c1_zticks], 
          pad_dat=pad, font_size=fsize, prop_colbar=[c1_cbar_locs, c1_cbar_ori], norm='N')
ax1.set_xlim(c1c2_xlim)
ax1.set_ylim(c1_ylim)
ax1.tick_params(axis='both', which='major', direction='in', top=False, 
                right=True, labelsize=fsize)
# add twinx axis
# CRITICAL: Set the same limits as primary axis
ax1t.set_xlim(ax1.get_xlim())
ax1t.set_xticks(c1_x2ticks_p)
ax1t.set_xticklabels([f'{c1_x2ticks[i]:.1f}' for i in range(len(c1_x2ticks_p))])
ax1t.set_xlabel(x2label)

# put fit label
ax1.plot(c1_xfit_V_1d, c1_yfit_V_1d, ls_col, label=c1_data_lgd)
ax1.legend(loc=lgd_loc[1], frameon=frameon[1])

# fig2e, Q2
color_map(fig=fig, ax=ax2, x_dat=q2_x_V_1d, y_dat=q2_y_fxy_1d, 
          z_dat=q2_z_vrms_2d, axs_lbl=[xlabel, ylabel, zlabel], 
          cmap=cmap, ticks_2D=[q2_xticks, q2_yticks, q2_zticks], 
          pad_dat=pad, font_size=fsize, prop_colbar=[q2_cbar_locs, q2_cbar_ori], norm='N')
ax2.set_xlim(q1q2_xlim)
ax2.set_ylim(q2_ylim)
ax2.tick_params(axis='both', which='major', direction='in', top=False, 
                right=True, labelsize=fsize)
# add twinx axis
# CRITICAL: Set the same limits as primary axis
ax2t.set_xlim(ax2.get_xlim())
ax2t.set_xticks(q2_x2ticks_p)
ax2t.set_xticklabels([f'{q2_x2ticks[i]:.1f}' for i in range(len(q1_x2ticks_p))])

# put fit label
ax2.plot(q2_xfit_V_1d, q2_yfit_V_1d, ls_col, label=q2_data_lgd)
ax2.legend(loc=lgd_loc[2], frameon=frameon[2])

# fig2f, C2
color_map(fig=fig, ax=ax3, x_dat=c2_x_V_1d, y_dat=c2_y_fxy_1d, 
          z_dat=c2_z_vrms_2d, axs_lbl=[xlabel, '', zlabel], 
          cmap=cmap, ticks_2D=[c2_xticks, c2_yticks, c2_zticks], 
          pad_dat=pad, font_size=fsize, prop_colbar=[c2_cbar_locs, c2_cbar_ori], norm='N')
ax3.set_xlim(c1c2_xlim)
ax3.set_ylim(c2_ylim)
ax3.tick_params(axis='both', which='major', direction='in', top=False, 
                right=True, labelsize=fsize)
# add twinx axis
# CRITICAL: Set the same limits as primary axis
ax3t.set_xlim(ax3.get_xlim())
ax3t.set_xticks(c2_x2ticks_p)
ax3t.set_xticklabels([f'{c2_x2ticks[i]:.1f}' for i in range(len(c2_x2ticks_p))])

# put fit label
ax3.plot(c2_xfit_V_1d, c2_yfit_V_1d, ls_col, label=c2_data_lgd)
ax3.legend(loc=lgd_loc[3], frameon=frameon[3])
plt.savefig(fname_fig2cdef_png, dpi=300) # png
# plt.savefig(fname_fig2cdef_svg) # save in .svg (tens of MB files)
plt.show()