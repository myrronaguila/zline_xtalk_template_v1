# -*- coding: utf-8 -*-
"""
Created on Sat Nov  8 15:45:11 2025

Fig3 - Demonstration of Flux Crosstalk Characterization and Compensation using MZLC
covered figures
1. fig3b - Received signals of Source (C1) flux vs Probe (Q1) flux - before cancel
2. fig3c - Received signals of Source (C1) flux vs Probe (Q1) flux - after cancel

3. fig4b - Received signals of Source (Q1) flux vs Probe (C1) flux - before cancel
4. fig4c - Received signals of Source (Q1) flux vs Probe (C1) flux - after cancel

5. fig5c - Received signals of Source (Q2) flux vs Probe (C1) flux - Detuning 1
6. fig5d - Received signals of Source (Q2) flux vs Probe (C1) flux - Detuning 2

@author: Mai
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import sys
import os

"""For loading figures, plotting and saving"""
from util_functions import set_font_default, color_map, xr_load_nc_to_dict, cm_to_inch
from util_functions import conf_matrix_standard

# retrieve files
dir_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
#print(dir_common_path)
sys.path.append(dir_data_path)

# first TOC - fig 3 -> pipeline method
loc_fig3_ = dir_data_path + '\\' + 'data_fig3_.nc'
loc_fig3b = dir_data_path + '\\' + 'data_fig3b.nc'
loc_fig3c = dir_data_path + '\\' + 'data_fig3c.nc'
# second TOC - 4 -> pipeline method
loc_fig4_ = dir_data_path + '\\' + 'data_fig4_.nc'
loc_fig4a = dir_data_path + '\\' + 'data_fig4a.nc'
loc_fig4c = dir_data_path + '\\' + 'data_fig4c.nc'
# third TOC - fig 5 -> compare
loc_fig5 = dir_data_path + '\\' + 'data_fig5_.nc'
loc_fig5b = dir_data_path + '\\' + 'data_fig5b.nc'
loc_fig5c = dir_data_path + '\\' + 'data_fig5c.nc'
loc_fig5d = dir_data_path + '\\' + 'data_fig5d.nc'
loc_fig5ei = dir_data_path + '\\' + 'data_fig5ei.nc'

dict_fig3_ = xr_load_nc_to_dict(loc_fig3_) # settings for colormap
dict_fig3b = xr_load_nc_to_dict(loc_fig3b) # colormap, Q1
dict_fig3c = xr_load_nc_to_dict(loc_fig3c) # colormap, Q1

# fig4
dict_fig4_ = xr_load_nc_to_dict(loc_fig4_) # settings for colormap
dict_fig4a = xr_load_nc_to_dict(loc_fig4a) # colormap, Q1
dict_fig4c = xr_load_nc_to_dict(loc_fig4c) # colormap, Q1

dict_fig5_ = xr_load_nc_to_dict(loc_fig5) # settings for colormap
dict_fig5b = xr_load_nc_to_dict(loc_fig5b) # colormap
dict_fig5c = xr_load_nc_to_dict(loc_fig5c) # colormap
dict_fig5d = xr_load_nc_to_dict(loc_fig5d) # colormap
dict_fig5ei = xr_load_nc_to_dict(loc_fig5ei) # line plot

# save files to png /or svg / set directory for saving.
dir_figures_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'figures'))
dir_save = dir_figures_path + '\\editable_source\\'

# save files to png /or svg, toc1 => focused on Rabi plots to be adjusted using gimp
fname_abs_png = dir_save + 'fig_abs.png'
# note. svg editable to difficult to analyze using inkscape due to memory settings

# save 2nd file to svg, toc2 => focused on intensity plots before and after compensate
fname_abs2_png = dir_save + 'fig_abs2.png'

# save 3nd file to svg, toc2 => focused on inset for residual
fname_abs3_png = dir_save + 'fig_abs3.png'


# format # fig3
wfig = 8.6

figsize, lgd_loc = dict_fig3_['figsize'], dict_fig3_['lgd_loc']
frameon = dict_fig3_['frameon']
cmap = dict_fig3b['cmap']
zlabel = dict_fig3b['zlabel']
fsize = dict_fig3b['font_size']
set_font_default(fsize) # set default settings for plots
lsize = dict_fig3b['lgd_size']
pad = dict_fig3b['pad']

ls_col = dict_fig3b['fit_cls']
ls_colm = dict_fig3c['fit_cls']

# figure limits
fig3bc_xlim = dict_fig3b['xlim']

# figure 3bc
fig3bc_xlabel = dict_fig3b['xlabel']
fig3bc_ylabel = dict_fig3b['ylabel']

# ylims
fig3b_ylim = dict_fig3b['ylim']
fig3c_ylim = dict_fig3c['ylim']

"""-------------Fig3b-SFlux-C1, P-Flux-Q1, before flux compensation---------"""
# colormap, Source=C1, Probe=Q1, data
fig3b_x_norm_1d = dict_fig3b['x_norm_phi']
fig3b_y_norm_1d = dict_fig3b['y_norm_phi']
fig3b_z_vrms_2d = dict_fig3b['z_vrms_(uV)']

# line fit, 
fig3b_xfit_norm_1d = dict_fig3b['xfit_norm_phi']
fig3b_yfit_norm_1d = dict_fig3b['yfit_norm_phi']
fig3b_data_lgd = dict_fig3b['data_lgd']

# format Q1
fig3b_xticks, fig3b_yticks = dict_fig3b['xticks'], dict_fig3b['yticks']
fig3b_zticks = dict_fig3b['zticks']

# colorbar labels
# # cbar_dim = ['x-loc', 'y-loc', 'width' 'height']
fig3b_cbar_locs = dict_fig3b['cbar_locs']
fig3b_cbar_ori = dict_fig3b['cbar_ori']

"""--------------Fig3c-SFlux-C1, P-Flux-Q1, after flux compensation---------"""
# colormap, Source=C1, Probe=Q1, data
fig3c_x_norm_1d = dict_fig3c['x_norm_phi']
fig3c_y_norm_1d = dict_fig3c['y_norm_phi']
fig3c_z_vrms_2d = dict_fig3c['z_vrms_(uV)']

# line fit, 
fig3c_xfit_norm_1d = dict_fig3c['xfit_norm_phi']
fig3c_yfit_norm_1d = dict_fig3c['yfit_norm_phi']
fig3c_data_lgd = dict_fig3c['data_lgd']

# format
fig3c_xticks, fig3c_yticks = dict_fig3c['xticks'], dict_fig3c['yticks']
fig3c_zticks = dict_fig3c['zticks']

# colorbar labels
# # cbar_dim = ['x-loc', 'y-loc', 'width' 'height']
fig3c_cbar_locs = dict_fig3c['cbar_locs']
fig3c_cbar_ori = dict_fig3c['cbar_ori']

"""-------------Plot format, simplified fig 4 ac-----------------"""
# xlabel, ylabel
fig4_xlabel = dict_fig4a['xlabel']
fig4_ylabel = dict_fig4a['ylabel']
fig4_zlabel = dict_fig4a['zlabel']
fig4_ax_lbls = [fig4_xlabel, fig4_ylabel, fig4_zlabel]

fig4_xticks = dict_fig4a['x_ticks']
fig4_yticks = dict_fig4a['y_ticks']
fig4_zticks = dict_fig4a['z_ticks']
fig4_ax_ticks = [fig4_xticks, fig4_yticks] # prepare ticks for labels

# fig setting for cbar
fig4_cmap = dict_fig4a['cmap'] 
fig4_fsize = dict_fig4a['fsize']

# fig4_data
fig4_cbar = [dict_fig4_['cbar_loc'][0], fig4_zticks, dict_fig4a['z_ticks_lbl']]
# fig4_cbar = [dict_fig4_['cbar_loc'][0], fig4_zticks, dict_fig4a['z_ticks_lbl']] # [False, ]
# fig4_norm
fig4_norm_1 = dict_fig4a['norm_arr'] # 
fig4_norm = [dict_fig4c['norm_config'], fig4_norm_1[0], fig4_norm_1[1],
             fig4_norm_1[2], fig4_norm_1[3]]

"""-------------Dataset fig4a----------------------------"""
fig4a_zdata = dict_fig4a['z_xtalk_(arb)']
fig4a_annot = dict_fig4a['z_annot']

"""-------------Dataset fig4c----------------------------"""
fig4c_zdata = dict_fig4c['z_xtalk_(arb)']
fig4c_annot = dict_fig4c['z_annot']

"""---------------Fig 5 dataset--------------------------"""
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

# labels
fig5_xlabel = dict_fig5b['xlabel']
fig5bcd_ylabel = dict_fig5b['ylabel']
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
fig5c_xticks, fig5c_yticks = [-1,0,1], [0, 200, 400] # modified ticks
fig5c_zticks = dict_fig5c['zticks']
fig5_yticks = [0, 200, 400]
fig5c_yticks = fig5_yticks
fig5_xticks = fig5c_xticks

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
fig5d_yticks = fig5_yticks

# colorbar labels
# # cbar_dim = ['x-loc', 'y-loc', 'width' 'height']
fig5d_cbar_locs = dict_fig5d['cbar_locs']
fig5d_cbar_ori = dict_fig5d['cbar_ori']
fig5d_title = dict_fig5d['title']

"""------------Fig5ei---------CZ subtraction--------------------------------"""
"""-------------Fig5ei-residual of fig5ei-----------"""
fig5ei_x_norm_1d = dict_fig5ei['x_norm_phi']
fig5ei_y_resid_bc_1d = dict_fig5ei['y_del_geff_(MHz)'][0] #before compensation - fit
fig5ei_y_resid_ac_1d = dict_fig5ei['y_del_geff_(MHz)'][1] #after compensation - fit

# format
fig5ei_ylim = dict_fig5ei['ylim']
fig5ei_xticks, fig5ei_yticks =dict_fig5ei['xticks'], dict_fig5ei['yticks']
fig5ei_inset_loc = dict_fig5ei['inset_loc']
fig5ei_fit_cls = dict_fig5ei['fit_cls']
fig5ei_data_lgd = dict_fig5ei['data_lgd']


"""Shared colorbar for two meshes"""
# Set a common color range for each gridspec
vmin1 = min(fig5b_z_vrms_2d.min(), fig5c_z_vrms_2d.min()) 
vmax1 = max(fig5b_z_vrms_2d.max(), fig5c_z_vrms_2d.max())
vmin1t, vmax1t = fig5d_z_amp_2d.min(), fig5d_z_amp_2d.max()
set_font_default(fsize)
"""----------------vertical plot (desired output plots)---------------------"""
fig = plt.figure(constrained_layout=True, figsize=(2.0*cm_to_inch(wfig),
                                                    1.2*cm_to_inch(wfig)))
spec = gridspec.GridSpec(ncols=3, nrows=2, figure=fig, hspace=-0.3, wspace=-0.1)
# fig 3
ax0 = fig.add_subplot(spec[0, 0]) # r1c1, Crosstalk matrix, elem before cancel
ax1 = fig.add_subplot(spec[1, 0]) # r2c1, Crosstalk matrix, elem after cancel
# fig 4
ax2 = fig.add_subplot(spec[0, 1]) # r1c2, Crosstalk matrix before cancellation
ax3 = fig.add_subplot(spec[1, 1]) # r2c2, Crosstalk matrix after cancellation
# fig 5
ax4 = fig.add_subplot(spec[0, 2]) # r1c3, CZ-after flux
ax5 = fig.add_subplot(spec[1, 2]) # r2c3, CZ-model 

# data analysis for standardized size

# fig3b
color_map(fig=fig, ax=ax0, x_dat=fig3b_x_norm_1d, y_dat=fig3b_y_norm_1d, 
          z_dat=fig3b_z_vrms_2d, 
          axs_lbl=[fig3bc_xlabel, fig3bc_ylabel, zlabel], 
          cmap=cmap, ticks_2D=[fig3b_xticks, fig3b_yticks, fig3b_zticks], pad_dat=pad, 
          font_size=fsize, prop_colbar=[fig3b_cbar_locs, fig3b_cbar_ori], norm='N',
          cbar=False)
ax0.plot(fig3b_xfit_norm_1d, fig3b_yfit_norm_1d, ls_col, 
          label=fig3b_data_lgd)
# ax0.legend(loc=lgd_loc[0], frameon=frameon[0], fontsize=lsize)

# fig3c
color_map(fig=fig, ax=ax1, x_dat=fig3c_x_norm_1d, y_dat=fig3c_y_norm_1d, 
          z_dat=fig3c_z_vrms_2d, 
          axs_lbl=[fig3bc_xlabel, fig3bc_ylabel, zlabel], 
          cmap=cmap, ticks_2D=[fig3c_xticks, fig3c_yticks, fig3c_zticks], pad_dat=pad, 
          font_size=fsize, prop_colbar=[fig3c_cbar_locs, fig3c_cbar_ori], norm='N',
          cbar=False)
ax1.plot(fig3c_xfit_norm_1d, fig3c_yfit_norm_1d, ls_colm, 
          label=fig3b_data_lgd)
# ax1.legend(loc=lgd_loc[1], frameon=frameon[1], fontsize=lsize)

# fig4a
# ax2.set_title(title_prot0 + '\n' + 'Crosstalk Matrix', fontsize=9)
conf_matrix_standard(fig=fig, ax=ax2, conf_matrix=fig4a_zdata, ax_lbls=fig4_ax_lbls, 
                     ax_tick_lbls=fig4_ax_ticks, annot=fig4a_annot, 
                     cbar_ticks=fig4_cbar, cmap=fig4_cmap, 
                     norm=fig4_norm, font_size=fsize)

# fig4c
# ax3.set_title(title_prot1 + '\n' + 'Crosstalk Matrix', fontsize=9)
conf_matrix_standard(fig=fig, ax=ax3, conf_matrix=fig4c_zdata, ax_lbls=fig4_ax_lbls, 
                     ax_tick_lbls=fig4_ax_ticks, annot=fig4c_annot, 
                     cbar_ticks=fig4_cbar, cmap=fig4_cmap, 
                     norm=fig4_norm, font_size=fsize)

# # 20251003 - linear change in uncertainty
ax4.set_title(fig5c_title, fontsize=fsize)
mesh1 = color_map(fig=fig, ax=ax4, x_dat=fig5c_x_norm_1d, y_dat=fig5c_y_time_1d, 
                  z_dat=fig5c_z_vrms_2d, 
                  axs_lbl=[fig5_xlabel, fig5bcd_ylabel, fig5bc_zlabel], cmap=cmap, 
                  ticks_2D=[[], fig5c_yticks, []], 
                  pad_dat=pad, font_size=fsize, 
                  prop_colbar=[fig5c_cbar_locs,fig5c_cbar_ori], 
                  norm='N', cbar=False)
mesh1.set_clim(vmin=vmin1, vmax=vmax1)
# ax4.set_xticks(ticks=fig5c_xticks, labels="") # # axes.ytickslabel off
ax4.set_xlim(fig5_xlim)
ax4.set_ylim(fig5bcd_ylim)

# cbar1 = fig.colorbar(mesh1, ax=[ax0, ax1], orientation=fig5c_cbar_ori,
#                      shrink=fig5c_cbar_locs[0], 
#                      fraction=fig5c_cbar_locs[1], 
#                      aspect=fig5c_cbar_locs[2]) # resize to have same value as others
# cbar1.set_label(fig5bc_zlabel)

# # modified changes in uncertainty according to rules
ax5.set_title(fig5d_title, fontsize=fsize)
mesh2 = color_map(fig=fig, ax=ax5, x_dat=fig5d_x_norm_1d, y_dat=fig5d_y_time_1d, 
                  z_dat=fig5d_z_amp_2d, 
                  axs_lbl=[fig5_xlabel, fig5bcd_ylabel, fig5d_zlabel], cmap=cmap, 
                  ticks_2D=[[], fig5d_yticks, []], 
                  pad_dat=pad, font_size=fsize, 
                  prop_colbar=[fig5d_cbar_locs,fig5d_cbar_ori], 
                  norm='N', cbar=False)
mesh2.set_clim(vmin=vmin1t, vmax=vmax1t)
# ax5.set_xticks(ticks=fig5c_xticks, labels="") # # axes.ytickslabel off
ax5.set_xlim(fig5_xlim)
ax5.set_ylim(fig5bcd_ylim)

plt.savefig(fname=fname_abs_png, dpi=300)
# done - took longer since we wanted to make the design better
plt.show()

"""----Follow-up Figures for Design - Comparison between not compensated and 
uncompensated----"""
fig = plt.figure(constrained_layout=True, figsize=((2.1/3)*cm_to_inch(wfig),
                                                    1.22*cm_to_inch(wfig)))
spec = gridspec.GridSpec(ncols=1, nrows=2, figure=fig, hspace=-0.3, wspace=-0.1)

# making proper resize of figure 5 and 5ei dataset
ax0 = fig.add_subplot(spec[0, 0]) # r1c1, Flux Uncompensated Matrix
ax1 = fig.add_subplot(spec[1, 0]) # r2c1, Flux Compensated Matrix

# Uncompensated Pulses
ax0.set_title(fig5b_title, fontsize=fsize)
mesh0 = color_map(fig=fig, ax=ax0, x_dat=fig5b_x_norm_1d, y_dat=fig5b_y_time_1d, 
                  z_dat=fig5b_z_vrms_2d, 
                  axs_lbl=[fig5_xlabel, fig5bcd_ylabel, fig5bc_zlabel], cmap=cmap, 
                  ticks_2D=[fig5_xticks, fig5_yticks, []], 
                  pad_dat=pad, font_size=fsize, 
                  prop_colbar=[fig5c_cbar_locs,fig5c_cbar_ori], 
                  norm='N', cbar=False)

# Compensated Pulses
ax1.set_title(fig5c_title, fontsize=fsize)
mesh1 = color_map(fig=fig, ax=ax1, x_dat=fig5c_x_norm_1d, y_dat=fig5c_y_time_1d, 
                  z_dat=fig5c_z_vrms_2d, 
                  axs_lbl=[fig5_xlabel, fig5bcd_ylabel, fig5bc_zlabel], cmap=cmap, 
                  ticks_2D=[fig5_xticks, fig5_yticks, []], 
                  pad_dat=pad, font_size=fsize, 
                  prop_colbar=[fig5c_cbar_locs,fig5c_cbar_ori], 
                  norm='N', cbar=False)

# Residual figure ei with more ticks
# fig 5ei

plt.savefig(fname=fname_abs2_png, dpi=300)
plt.show()

"""---- Plot residual vs fit with modified size for further clarity of residual"""
fig = plt.figure(constrained_layout=True, figsize=(0.6*cm_to_inch(wfig),
                                                   0.4*cm_to_inch(wfig)))
spec = gridspec.GridSpec(ncols=1, nrows=1, figure=fig, hspace=-0.3, wspace=-0.1)
ax0 = fig.add_subplot(spec[0, 0]) # residual plot

ax0.plot(fig5ei_x_norm_1d , fig5ei_y_resid_bc_1d, 
              fig5ei_fit_cls[0], label=fig5ei_data_lgd[0]) # uncompensated
ax0.plot(fig5ei_x_norm_1d , fig5ei_y_resid_ac_1d, 
              fig5ei_fit_cls[1], label=fig5ei_data_lgd[1]) # Flux compensated
ax0.tick_params(axis = 'both', which ='both', direction='in', top=True, 
                      right = True)
ax0.set_xlabel(fig5_xlabel, labelpad=-1)
ax0.set_ylabel('Data - Model (MHz)', labelpad=-1)
ax0.set_xlim(fig5_xlim) # Set specific limits for the inset
ax0.set_ylim(fig5ei_ylim)
ax0.tick_params(axis='both', which='major', labelsize=fsize)
ax0.set_xticks(fig5_xticks)

plt.savefig(fname=fname_abs3_png, dpi=300)
plt.show()