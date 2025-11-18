# -*- coding: utf-8 -*-
"""
Created on Sat Nov  8 15:45:11 2025

Fig5 - Effect of Flux Crosstalk Cancellation on CZ gate experiments
covered figures
1. fig5b - CZ SWAP experiment - before flux crosstalk cancel
2. fig5c - CZ SWAP experiment - after flux crosstalk cancel
3. fig5d - CZ SWAP experiment - digital twin
4. fig5e - Extracted CZ coupling strength vs coupler flux
5. fig5ei - Residual of CZ coupling strength between compensated and uncompensated

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

loc_fig5_ = dir_data_path + '\\' + 'data_fig5_.nc'
loc_fig5b = dir_data_path + '\\' + 'data_fig5b.nc'
loc_fig5c = dir_data_path + '\\' + 'data_fig5c.nc'
loc_fig5d = dir_data_path + '\\' + 'data_fig5d.nc'
loc_fig5e = dir_data_path + '\\' + 'data_fig5e.nc'
loc_fig5f = dir_data_path + '\\' + 'data_fig5ei.nc'

dict_fig5_ = xr_load_nc_to_dict(loc_fig5_) # format
dict_fig5b = xr_load_nc_to_dict(loc_fig5b) # colormap, Q1-C2-Q2 before compensation
dict_fig5c = xr_load_nc_to_dict(loc_fig5c) # colormap, Q1-C2-Q2 after compensation
dict_fig5d = xr_load_nc_to_dict(loc_fig5d) # colormap, Q1-C2-Q2 theory
dict_fig5e = xr_load_nc_to_dict(loc_fig5e) # colormap, |geff| vs C2-flux
dict_fig5ei = xr_load_nc_to_dict(loc_fig5f) # colormap, del_geff vs C2-flux

# save files to png /or svg / set directory for saving.
dir_figures_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'figures'))
dir_save = dir_figures_path + '\\editable_source\\'
fname_fig5bcdei_png = dir_save + 'fig5bcdeei.png'
fname_fig5bcdei_svg = dir_save + 'fig5bcdeei.svg'

# format
figsize = dict_fig5_['figsize']
frameon = dict_fig5_['frameon']
cmap = dict_fig5b['cmap']
zlabel = dict_fig5b['zlabel']
fsize = dict_fig5b['font_size']
set_font_default(fsize) # set default settings for plots
lsize = dict_fig5b['lgd_size']
pad = dict_fig5b['pad']

# figure limits
fig5_xlim = dict_fig5b['xlim']

fig5bcd_ylim = dict_fig5b['ylim']
fig5e_ylim = dict_fig5e['ylim']
fig5ei_ylim = dict_fig5ei['ylim']

# labels
fig5_xlabel = dict_fig5b['xlabel']
fig5bcd_ylabel = dict_fig5b['ylabel']
fig5e_ylabel = dict_fig5e['ylabel']
fig5bc_zlabel = dict_fig5b['zlabel']
fig5d_zlabel = dict_fig5d['zlabel']

"""-------------Fig5b-CZ gate before flux compensation---------"""
# colormap
fig5b_x_norm_1d = dict_fig5b['x_norm_phi']
fig5b_y_time_1d = dict_fig5b['y_time_(ns)']
fig5b_z_vrms_2d = dict_fig5b['z_vrms_(uV)']

# format Q1
fig5b_xticks, fig5b_yticks = dict_fig5b['xticks'], dict_fig5b['yticks']
fig5b_zticks = dict_fig5b['zticks']

# colorbar labels
# # cbar_dim = ['x-loc', 'y-loc', 'width' 'height']
fig5b_cbar_locs = dict_fig5b['cbar_locs']
fig5b_cbar_ori = dict_fig5b['cbar_ori']
fig5b_title = dict_fig5b['title']

"""-------------Fig5c-CZ gate after flux compensation----------"""
# colormap
fig5c_x_norm_1d = dict_fig5c['x_norm_phi']
fig5c_y_time_1d = dict_fig5c['y_time_(ns)']
fig5c_z_vrms_2d = dict_fig5c['z_vrms_(uV)']

# format
fig5c_xticks, fig5c_yticks = dict_fig5c['xticks'], dict_fig5c['yticks']
fig5c_zticks = dict_fig5c['zticks']

# colorbar labels
# # cbar_dim = ['x-loc', 'y-loc', 'width' 'height']
fig5c_cbar_locs = dict_fig5c['cbar_locs']
fig5c_cbar_ori = dict_fig5c['cbar_ori']
fig5c_title = dict_fig5c['title']

"""-------------Fig5d-CZ gate simulated by Empirical Rabi Oscillation---------"""
# colormap
fig5d_x_norm_1d = dict_fig5d['x_norm_phi']
fig5d_y_time_1d = dict_fig5d['y_time_(ns)']
fig5d_z_amp_2d = dict_fig5d['z_amp_(arb)']

# format
fig5d_xticks, fig5d_yticks = dict_fig5d['xticks'], dict_fig5d['yticks']
fig5d_zticks = dict_fig5d['zticks']

# colorbar labels
# # cbar_dim = ['x-loc', 'y-loc', 'width' 'height']
fig5d_cbar_locs = dict_fig5d['cbar_locs']
fig5d_cbar_ori = dict_fig5d['cbar_ori']
fig5d_title = dict_fig5d['title']

"""-------------Fig5e-g_eff vs coupler bias---------"""
# line-plot
fig5e_x_norm_1d = dict_fig5e['x_norm_phi']
fig5e_y_geff_bc_1d = dict_fig5e['y_geff_(MHz)'][0] #before compensation
fig5e_y_geff_ac_1d = dict_fig5e['y_geff_(MHz)'][1] #after compensation
fig5e_yfit_geff_1d = dict_fig5e['yfit_geff_(MHz)'] #fit

# format
fig5e_xticks, fig5e_yticks = dict_fig5e['xticks'], dict_fig5e['yticks']
fig5e_data_lgd = dict_fig5e['data_lgd']
fig5e_fit_cls = dict_fig5e['fit_cls'] #[0 - before compensate, 1 - after compensate, 2, fit]

# colorbar labels
# # cbar_dim = ['x-loc', 'y-loc', 'width' 'height']

"""-------------Fig5ei-residual of fig5ei-----------"""
fig5ei_x_norm_1d = dict_fig5e['x_norm_phi']
fig5ei_y_resid_bc_1d = dict_fig5ei['y_del_geff_(MHz)'][0] #before compensation - fit
fig5ei_y_resid_ac_1d = dict_fig5ei['y_del_geff_(MHz)'][1] #after compensation - fit

# format
fig5ei_xticks, fig5ei_yticks =dict_fig5ei['xticks'], dict_fig5ei['yticks']
fig5ei_inset_loc = dict_fig5ei['inset_loc']
fig5ei_fit_cls = dict_fig5ei['fit_cls']
fig5ei_data_lgd = dict_fig5ei['data_lgd']

"""----------------vertical plot (desired output plots)---------------------"""
fig = plt.figure(constrained_layout=True, figsize=figsize)

# # main text, v2, gridspec, row, col
gs = gridspec.GridSpec(4, 1, figure=fig, wspace=0.05, hspace=0.05) 
ax0 = fig.add_subplot(gs[0, 0]) # bridge prior to correction, with title
ax1 = fig.add_subplot(gs[1, 0]) # corrected bridge
ax2 = fig.add_subplot(gs[2, 0]) # simulated bridge
ax3 = fig.add_subplot(gs[3, 0]) # cross-section fit

"""Shared colorbar for two meshes"""
# Set a common color range for each gridspec
vmin1 = min(fig5b_z_vrms_2d.min(), fig5c_z_vrms_2d.min()) 
vmax1 = max(fig5b_z_vrms_2d.max(), fig5c_z_vrms_2d.max())
vmin1t, vmax1t = fig5d_z_amp_2d.min(), fig5d_z_amp_2d.max()

# fig 5b
ax0.set_title(fig5b_title, fontsize=fsize)
mesh0 = color_map(fig=fig, ax=ax0, x_dat=fig5b_x_norm_1d, y_dat=fig5b_y_time_1d, 
                  z_dat=fig5b_z_vrms_2d, 
                  axs_lbl=['', fig5bcd_ylabel, ''], cmap=cmap, 
                  ticks_2D=[[], fig5b_yticks, []], 
                  pad_dat=pad, font_size=fsize, 
                  prop_colbar=[fig5c_cbar_locs,fig5c_cbar_ori], 
                  norm='N', cbar=False)
mesh0.set_clim(vmin=vmin1, vmax=vmax1)

ax0.set_xticks(ticks=fig5b_xticks, labels="") # # axes.ytickslabel off
ax0.set_xlim(fig5_xlim)
ax0.set_ylim(fig5bcd_ylim)

# fig 5c
ax1.set_title(fig5c_title, fontsize=fsize)
mesh1 = color_map(fig=fig, ax=ax1, x_dat=fig5c_x_norm_1d, y_dat=fig5c_y_time_1d, 
                  z_dat=fig5c_z_vrms_2d, 
                  axs_lbl=['', fig5bcd_ylabel, fig5bc_zlabel], cmap=cmap, 
                  ticks_2D=[[], fig5c_yticks, []], 
                  pad_dat=pad, font_size=fsize, 
                  prop_colbar=[fig5c_cbar_locs,fig5c_cbar_ori], 
                  norm='N', cbar=False)
mesh1.set_clim(vmin=vmin1, vmax=vmax1)
ax1.set_xticks(ticks=fig5c_xticks, labels="") # # axes.ytickslabel off
ax1.set_xlim(fig5_xlim)
ax1.set_ylim(fig5bcd_ylim)

cbar1 = fig.colorbar(mesh1, ax=[ax0, ax1], orientation=fig5c_cbar_ori,
                     shrink=fig5c_cbar_locs[0], 
                     fraction=fig5c_cbar_locs[1], 
                     aspect=fig5c_cbar_locs[2]) # resize to have same value as others
cbar1.set_label(fig5bc_zlabel)

# fig 5d
ax2.set_title(fig5d_title, fontsize=fsize)
mesh2 = color_map(fig=fig, ax=ax2, x_dat=fig5d_x_norm_1d, y_dat=fig5d_y_time_1d, 
                  z_dat=fig5d_z_amp_2d, 
                  axs_lbl=['', fig5bcd_ylabel, fig5d_zlabel], cmap=cmap, 
                  ticks_2D=[[], fig5d_yticks, []], 
                  pad_dat=pad, font_size=fsize, 
                  prop_colbar=[fig5d_cbar_locs,fig5d_cbar_ori], 
                  norm='N', cbar=False)
mesh2.set_clim(vmin=vmin1t, vmax=vmax1t)
ax2.set_xticks(ticks=fig5c_xticks, labels="") # # axes.ytickslabel off
ax2.set_xlim(fig5_xlim)
ax2.set_ylim(fig5bcd_ylim)

cbar2 = fig.colorbar(mesh1, ax=ax2, orientation=fig5d_cbar_ori,
                     shrink=fig5d_cbar_locs[0], 
                     fraction=fig5d_cbar_locs[1], 
                     aspect=fig5d_cbar_locs[2]) # resize to have same value as others
cbar2.set_label(fig5d_zlabel)

# fig 5e
ax3.plot(fig5e_x_norm_1d, fig5e_y_geff_bc_1d , fig5e_fit_cls[0], 
         label=fig5e_data_lgd[0]) # uncompensated
ax3.plot(fig5e_x_norm_1d, fig5e_y_geff_ac_1d , fig5e_fit_cls[1], 
         label=fig5e_data_lgd[1]) # flux compensated
ax3.plot(fig5e_x_norm_1d, fig5e_yfit_geff_1d,  fig5e_fit_cls[2], 
         label=fig5e_data_lgd[2]) # fit
ax3.tick_params(axis = 'both', which ='both', direction='in', top=True, 
                right = True)
ax3.set_yticks(ticks=fig5e_yticks)
ax3.set_xlabel(fig5_xlabel)
ax3.set_ylabel(fig5e_ylabel)
ax3.set_xlim(fig5_xlim)
ax3.set_ylim(fig5e_ylim)
ax3.legend(loc='upper left', frameon=True, fontsize=lsize, ncols=1)

# fig 5ei
ax_inset = ax3.inset_axes(fig5ei_inset_loc)
ax_inset.plot(fig5ei_x_norm_1d , fig5ei_y_resid_bc_1d, 
              fig5ei_fit_cls[0], label=fig5ei_data_lgd[0]) # uncompensated
ax_inset.plot(fig5ei_x_norm_1d , fig5ei_y_resid_ac_1d, 
              fig5ei_fit_cls[1], label=fig5ei_data_lgd[1]) # Flux compensated
ax_inset.tick_params(axis = 'both', which ='both', direction='in', top=True, 
                      right = True)
ax_inset.set_xlim(fig5_xlim) # Set specific limits for the inset
ax_inset.set_ylim(fig5ei_ylim)
ax_inset.tick_params(axis='both', which='major', labelsize=lsize)

plt.savefig(fname_fig5bcdei_png, dpi=300)
plt.show()