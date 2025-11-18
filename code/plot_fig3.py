# -*- coding: utf-8 -*-
"""
Created on Sat Nov  8 15:45:11 2025

Fig3 - Demonstration of Flux Crosstalk Characterization and Compensation using MZLC
covered figures
1. fig3b - Received signals of Source (C1) flux vs Probe (Q1) flux - before cancel
2. fig3c - Received signals of Source (C1) flux vs Probe (Q1) flux - after cancel
3. fig3d - Received signals of Source (Q1) flux vs Probe (C1) flux - before cancel
4. fig3e - Received signals of Source (Q1) flux vs Probe (C1) flux - after cancel
5. fig3f - Received signals of Source (Q2) flux vs Probe (C1) flux - Detuning 1
6. fig3g - Received signals of Source (Q2) flux vs Probe (C1) flux - Detuning 2

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

loc_fig3_ = dir_data_path + '\\' + 'data_fig3_.nc'
loc_fig3b = dir_data_path + '\\' + 'data_fig3b.nc'
loc_fig3c = dir_data_path + '\\' + 'data_fig3c.nc'
loc_fig3d = dir_data_path + '\\' + 'data_fig3d.nc'
loc_fig3e = dir_data_path + '\\' + 'data_fig3e.nc'
loc_fig3f = dir_data_path + '\\' + 'data_fig3f.nc'
loc_fig3g = dir_data_path + '\\' + 'data_fig3g.nc'

dict_fig3_ = xr_load_nc_to_dict(loc_fig3_) # format
dict_fig3b = xr_load_nc_to_dict(loc_fig3b) # colormap, Q1
dict_fig3c = xr_load_nc_to_dict(loc_fig3c) # colormap, Q1
dict_fig3d = xr_load_nc_to_dict(loc_fig3d) # colormap, C1
dict_fig3e = xr_load_nc_to_dict(loc_fig3e) # colormap, Q2
dict_fig3f = xr_load_nc_to_dict(loc_fig3f) # colormap, C2
dict_fig3g = xr_load_nc_to_dict(loc_fig3g) # colormap, C2

# save files to png /or svg / set directory for saving.
dir_figures_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'figures'))
dir_save = dir_figures_path + '\\editable_source\\'

# save files to png /or svg
fname_fig3bcdefg_png = dir_save + 'fig3bcdefg.png'
fname_fig3bcdefg_svg = dir_save + 'fig3bcdefg.svg'

# format
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
fig3de_xlim = dict_fig3d['xlim']

# figure 3bc
fig3bc_xlabel = dict_fig3b['xlabel']
fig3bc_ylabel = dict_fig3b['ylabel']

# figure 3de
fig3de_xlabel = dict_fig3d['xlabel']
fig3de_ylabel = dict_fig3d['ylabel']

# figure 3fg
fig3fg_xlabel = dict_fig3f['xlabel']
fig3fg_ylabel = dict_fig3f['ylabel']

# xlims
fig3f_xlim = dict_fig3f['xlim']
fig3g_xlim = dict_fig3g['xlim']

# ylims
fig3b_ylim = dict_fig3b['ylim']
fig3c_ylim = dict_fig3c['ylim']
fig3d_ylim = dict_fig3d['ylim']
fig3e_ylim = dict_fig3e['ylim']
fig3f_ylim = dict_fig3f['ylim']
fig3g_ylim = dict_fig3g['ylim']

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

"""-------------Fig3d-SFlux-Q1, P-Flux-C1, before flux compensation---------"""
# colormap, Source=C1, Probe=Q1, data
fig3d_x_norm_1d = dict_fig3d['x_norm_phi']
fig3d_y_norm_1d = dict_fig3d['y_norm_phi']
fig3d_z_vrms_2d = dict_fig3d['z_vrms_(uV)']

# line fit, 
fig3d_xfit_norm_1d = dict_fig3d['xfit_norm_phi']
fig3d_yfit_norm_1d = dict_fig3d['yfit_norm_phi']
fig3d_data_lgd = dict_fig3d['data_lgd']

# format
fig3d_xticks, fig3d_yticks = dict_fig3d['xticks'], dict_fig3d['yticks']
fig3d_zticks = dict_fig3d['zticks']

# colorbar labels
# # cbar_dim = ['x-loc', 'y-loc', 'width' 'height']
fig3d_cbar_locs = dict_fig3d['cbar_locs']
fig3d_cbar_ori = dict_fig3d['cbar_ori']

"""--------------Fig3e-SFlux-Q1, P-Flux-C1, after flux compensation---------"""
# colormap, Source=C1, Probe=Q1, data
fig3e_x_norm_1d = dict_fig3e['x_norm_phi']
fig3e_y_norm_1d = dict_fig3e['y_norm_phi']
fig3e_z_vrms_2d = dict_fig3e['z_vrms_(uV)']

# line fit, 
fig3e_xfit_norm_1d = dict_fig3e['xfit_norm_phi']
fig3e_yfit_norm_1d = dict_fig3e['yfit_norm_phi']
fig3e_data_lgd = dict_fig3e['data_lgd']

# format
fig3e_xticks, fig3e_yticks = dict_fig3e['xticks'], dict_fig3e['yticks']
fig3e_zticks = dict_fig3e['zticks']

# colorbar labels
# # cbar_dim = ['x-loc', 'y-loc', 'width' 'height']
fig3e_cbar_locs = dict_fig3e['cbar_locs']
fig3e_cbar_ori = dict_fig3e['cbar_ori']

"""-------------Fig3f-SFlux-Q1, P-Flux-C1, flux0---------"""
# colormap, Source=C1, Probe=Q1, data
fig3f_x_norm_1d = dict_fig3f['x_norm_phi']
fig3f_y_norm_1d = dict_fig3f['y_norm_phi']
fig3f_z_vrms_2d = dict_fig3f['z_vrms_(uV)']

# line fit, 
fig3f_xfit_norm_1d = dict_fig3f['xfit_norm_phi']
fig3f_yfit_norm_1d = dict_fig3f['yfit_norm_phi']
fig3f_data_lgd = dict_fig3f['data_lgd']

# format
fig3f_xticks, fig3f_yticks = dict_fig3f['xticks'], dict_fig3f['yticks']
fig3f_zticks = dict_fig3d['zticks']

# colorbar labels
# # cbar_dim = ['x-loc', 'y-loc', 'width' 'height']
fig3f_cbar_locs = dict_fig3f['cbar_locs']
fig3f_cbar_ori = dict_fig3f['cbar_ori']

"""--------------Fig3g-SFlux-Q1, P-Flux-C1, flux1---------"""
# colormap, Source=C1, Probe=Q1, data
fig3g_x_norm_1d = dict_fig3g['x_norm_phi']
fig3g_y_norm_1d = dict_fig3g['y_norm_phi']
fig3g_z_vrms_2d = dict_fig3g['z_vrms_(uV)']

# line fit, 
fig3g_xfit_norm_1d = dict_fig3g['xfit_norm_phi']
fig3g_yfit_norm_1d = dict_fig3g['yfit_norm_phi']
fig3g_data_lgd = dict_fig3g['data_lgd']

# format
fig3g_xticks, fig3g_yticks = dict_fig3g['xticks'], dict_fig3g['yticks']
fig3g_zticks = dict_fig3g['zticks']

# colorbar labels
# # cbar_dim = ['x-loc', 'y-loc', 'width' 'height']
fig3g_cbar_locs = dict_fig3g['cbar_locs']
fig3g_cbar_ori = dict_fig3g['cbar_ori']

"""----------------vertical plot (desired output plots)---------------------"""
fig = plt.figure(constrained_layout=True, figsize=figsize)

gsp = gridspec.GridSpec(nrows=2, ncols=1, figure=fig, width_ratios=[1],
                        height_ratios=[2,1],
                        wspace=0.1, hspace=0.05)  # Adjusting spacing

# # First group (ax0 (ul), ax1 (ur), ax2 (ll), ax3 (lr))
gsp0 = gridspec.GridSpecFromSubplotSpec(nrows=2, ncols=2, hspace=0., wspace=0,
                                        width_ratios=[1,1],
                                        subplot_spec=gsp[0])
gsp1 = gridspec.GridSpecFromSubplotSpec(nrows=1, ncols=2, hspace=0, wspace=0,
                                        width_ratios=[1,1],
                                        subplot_spec=gsp[1])

ax0 = fig.add_subplot(gsp0[0, 0]) # before cancellation, sc1=>pq1
ax1 = fig.add_subplot(gsp0[0, 1]) # after cancellation, sc1=>pq1 

# Second group (ax2 and ax3)
ax2 = fig.add_subplot(gsp0[1, 0]) # before cancellation, sq1=>pc1
ax3 = fig.add_subplot(gsp0[1, 1]) # after cancellation, sq1=>pc1

# gs1 = gridspec.GridSpecFromSubplotSpec(2, 1, hspace=-0.1, subplot_spec=gs[1])
# # Third group (ax4 and ax5 stacked with different y-labels)
ax4 = fig.add_subplot(gsp1[0, 0]) # sq1=>pc1, far-detuned
ax5 = fig.add_subplot(gsp1[0, 1]) # sq2=>pc1, near-detuned

# fig 3b
color_map(fig=fig, ax=ax0, x_dat=fig3b_x_norm_1d, y_dat=fig3b_y_norm_1d, 
          z_dat=fig3b_z_vrms_2d, 
          axs_lbl=[fig3bc_xlabel, fig3bc_ylabel, zlabel], 
          cmap=cmap, ticks_2D=[fig3b_xticks, fig3b_yticks, fig3b_zticks], pad_dat=pad, 
          font_size=fsize, prop_colbar=[fig3b_cbar_locs, fig3b_cbar_ori], norm='N')
ax0.plot(fig3b_xfit_norm_1d, fig3b_yfit_norm_1d, ls_col, 
         label=fig3b_data_lgd)
ax0.legend(loc=lgd_loc[0], frameon=frameon[0], fontsize=lsize)

# fig 3c
color_map(fig=fig, ax=ax1, x_dat=fig3c_x_norm_1d, y_dat=fig3c_y_norm_1d, 
          z_dat=fig3c_z_vrms_2d, 
          axs_lbl=[fig3bc_xlabel, '', zlabel], 
          cmap=cmap, ticks_2D=[fig3c_xticks, fig3c_yticks, fig3c_zticks], pad_dat=pad, 
          font_size=fsize, prop_colbar=[fig3c_cbar_locs, fig3c_cbar_ori], norm='N')
ax1.plot(fig3c_xfit_norm_1d, fig3c_yfit_norm_1d, ls_colm, 
         label=fig3b_data_lgd)
ax1.legend(loc=lgd_loc[1], frameon=frameon[1], fontsize=lsize)

# fig 3d
color_map(fig=fig, ax=ax2, x_dat=fig3d_x_norm_1d, y_dat=fig3d_y_norm_1d, 
          z_dat=fig3d_z_vrms_2d, 
          axs_lbl=[fig3de_xlabel, fig3de_ylabel, zlabel], 
          cmap=cmap, ticks_2D=[fig3d_xticks, fig3d_yticks, fig3d_zticks], pad_dat=pad, 
          font_size=fsize, prop_colbar=[fig3d_cbar_locs, fig3d_cbar_ori], norm='N')
ax2.plot(fig3d_xfit_norm_1d, fig3d_yfit_norm_1d, ls_col, 
         label=fig3d_data_lgd)
ax2.legend(loc=lgd_loc[2], frameon=frameon[2], fontsize=lsize)

# fig 3e
color_map(fig=fig, ax=ax3, x_dat=fig3e_x_norm_1d, y_dat=fig3e_y_norm_1d, 
          z_dat=fig3e_z_vrms_2d, 
          axs_lbl=[fig3de_xlabel, '', zlabel], 
          cmap=cmap, ticks_2D=[fig3e_xticks, fig3e_yticks, fig3e_zticks], pad_dat=pad, 
          font_size=fsize, prop_colbar=[fig3e_cbar_locs, fig3e_cbar_ori], norm='N')
ax3.plot(fig3e_xfit_norm_1d, fig3e_yfit_norm_1d, ls_colm, 
         label=fig3e_data_lgd)
ax3.legend(loc=lgd_loc[3], frameon=frameon[3], fontsize=lsize)

# fig 3f
color_map(fig=fig, ax=ax4, x_dat=fig3f_x_norm_1d, y_dat=fig3f_y_norm_1d, 
          z_dat=fig3f_z_vrms_2d, 
          axs_lbl=[fig3fg_xlabel, fig3fg_ylabel, zlabel], 
          cmap=cmap, ticks_2D=[fig3f_xticks, fig3f_yticks, fig3f_zticks], pad_dat=pad, 
          font_size=fsize, prop_colbar=[fig3f_cbar_locs, fig3f_cbar_ori], norm='N')
ax4.plot(fig3f_xfit_norm_1d, fig3f_yfit_norm_1d, ls_col, 
         label=fig3f_data_lgd)
ax4.legend(loc=lgd_loc[4], frameon=frameon[4], fontsize=lsize)

# fig 3g
color_map(fig=fig, ax=ax5, x_dat=fig3g_x_norm_1d, y_dat=fig3g_y_norm_1d, 
          z_dat=fig3g_z_vrms_2d, 
          axs_lbl=[fig3fg_xlabel, '', zlabel], 
          cmap=cmap, ticks_2D=[fig3g_xticks, fig3g_yticks, fig3g_zticks], pad_dat=pad, 
          font_size=fsize, prop_colbar=[fig3g_cbar_locs, fig3g_cbar_ori], norm='N')
ax5.plot(fig3g_xfit_norm_1d, fig3g_yfit_norm_1d, ls_col, 
         label=fig3g_data_lgd)
ax5.legend(loc=lgd_loc[5], frameon=frameon[5], fontsize=lsize)

plt.savefig(fname_fig3bcdefg_png, dpi=300) # png
plt.show()