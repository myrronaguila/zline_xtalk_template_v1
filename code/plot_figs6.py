# -*- coding: utf-8 -*-
"""
Created on Thurs 20251113

Figs6 - Effect of unwanted frequency detuning on single-qubit gate errors
1. figs6a - Sequence fidelity (single-qubit gate errors) vs Frequency detuning
2. figs6b - Sequence fidelity vs gate counts at varying frequency detuning

@author: Mai
"""

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import sys
import os

"""For loading figures, plotting and saving"""
from util_functions import set_font_default, xr_load_nc_to_dict

# retrieve files
dir_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
#print(dir_common_path)
sys.path.append(dir_data_path)

loc_path = 'fig_s6'
dir_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                             '..', loc_path))
sys.path.append(dir_data_path)
loc_figs6_ = dir_data_path + '\\' + 'data_figs6_.nc'
loc_figs6a = dir_data_path + '\\' + 'data_figs6a.nc'
loc_figs6b = dir_data_path + '\\' + 'data_figs6b.nc'

dict_figs6_ = xr_load_nc_to_dict(loc_figs6_) # format
dict_figs6a = xr_load_nc_to_dict(loc_figs6a) # line-chart, Q1
dict_figs6b = xr_load_nc_to_dict(loc_figs6b) # line-plot, Q1

# save files to png /or svg / set directory for saving.
dir_figures_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'figures'))
dir_save = dir_figures_path + '\\editable_source\\'
# save files to png /or svg
fname_figs6_png = dir_save + 'figs6ab.png'
fname_figs6_svg = dir_save + 'figs6ab.svg'

# global
figsize, lgd_loc = dict_figs6_['figsize'], dict_figs6_['lgd_loc'], 
frameon = dict_figs6_['frameon']
fsize = dict_figs6a['font_size']
set_font_default(fsize) # set default settings for plots
xlabel = dict_figs6a['xlabel']


"""----------------figs6a Detuning-------------------------------------------"""
# device
figs6a_x_det_1d = dict_figs6a['x_det_(MHz)']
figs6a_y_fid_1d = dict_figs6a['y_Fid']
figs6a_y2_err_1d = dict_figs6a['y2_err']
figs6a_vlines, figs6a_vlines_cls = dict_figs6a['vlines_loc'], dict_figs6a['vlines_cls']

# format
figs6a_xlabel, figs6a_ylabel = dict_figs6a['xlabel'], dict_figs6a['ylabel']
figs6a_y2label = dict_figs6a['y2label']
figs6a_xlim, figs6a_ylim = dict_figs6a['xlim'], dict_figs6a['ylim']
figs6a_y2lim = dict_figs6a['y2lim']
figs6a_xticks, figs6a_yticks = dict_figs6a['xticks'], dict_figs6a['yticks']
figs6a_y2ticks = dict_figs6a['y2ticks']
"""----------------figs6b Fidelity vs repetition at various detuning--------"""
# device
figs6b_x_m_1d = dict_figs6b['x_counts']
figs6b_y_fid_1d = dict_figs6b['y_Fid']

# format
figs6b_xlabel, figs6b_ylabel = dict_figs6b['xlabel'], dict_figs6b['ylabel']
figs6b_data_lgd = dict_figs6b['data_lgd']
figs6b_xlim, figs6b_ylim = dict_figs6b['xlim'], dict_figs6b['ylim']
figs6b_xticks, figs6b_yticks = dict_figs6b['xticks'], dict_figs6b['yticks']
figs6b_ncols, figs6b_ncols_lbl = dict_figs6b['lgdcols'], dict_figs6b['lgdcols_label']
figs6b_data_lgd = dict_figs6b['data_lgd']
figs6b_fsize, figs6b_lsize = dict_figs6b['font_size'], dict_figs6b['lgd_size']
figs6b_color_arr = dict_figs6b['c_arr'] #color array
"""----------------vertical plot (desired output plots)---------------------"""
fig = plt.figure(constrained_layout=True, figsize=figsize)
spec = gridspec.GridSpec(ncols=1, nrows=2, figure=fig, hspace=-0.5, wspace=-0.1)
ax0 = fig.add_subplot(spec[0, 0]) # line-plot from literature and compare with model
ax0t = ax0.twinx() # twin y
ax1 = fig.add_subplot(spec[1, 0]) # line-plot

# Coherent errors
ax0.plot(figs6a_x_det_1d, figs6a_y_fid_1d, 'k-')
ax0.set_xlabel(figs6a_xlabel, labelpad=-1)
ax0.set_ylabel(figs6a_ylabel, labelpad=0)
ax0.set_ylim(figs6a_ylim)
ax0.grid(True, which="major", ls=":", color='tab:gray')

# add twinx axis
# CRITICAL: Set the same limits as primary axis
ax0t.set_ylim(ax0.get_ylim())
ax0t.set_yticks(figs6a_yticks)
ax0t.set_yticklabels([f'{figs6a_y2ticks[3-i]:.2f}' for i in range(len(figs6a_y2ticks))])
ax0t.set_ylabel(figs6a_y2label)
ymin = 0.7
ax0.vlines(x=figs6a_vlines[0], ymin=ymin, ymax=1, 
            colors=figs6a_vlines_cls[0,0], linestyles=figs6a_vlines_cls[0,1], 
              label='Q1')
ax0.vlines(x=figs6a_vlines[1], ymin=ymin, ymax=1, 
            colors=figs6a_vlines_cls[1,0], linestyles=figs6a_vlines_cls[1,1], 
              label='C1')
ax0.set_ylim(ax0.get_ylim())
ax0.tick_params(axis = 'both', which ='both', direction='in', top=True)
ax0t.tick_params(axis = 'both', which ='both', direction='in', top=True)

# effect of repetiton on different devices.
# coherent error acumulation from detuning
for i in range(len(figs6b_y_fid_1d)):
    ax1.plot(figs6b_x_m_1d, figs6b_y_fid_1d[i], c=figs6b_color_arr[i], 
             label=figs6b_data_lgd[i])
ax1.set_xlabel(figs6b_xlabel, labelpad=-1)
ax1.set_ylabel(figs6b_ylabel, labelpad=-1)
ax1.set_xlim(figs6b_xlim)
ax1.set_ylim(figs6b_ylim)
ax1.tick_params(axis = 'both', which ='both', direction='in', top=True, 
                right = True)
ax1.legend(loc='best', frameon=False, ncols=figs6b_ncols[0], fontsize=figs6b_lsize,
            columnspacing=figs6b_ncols[1])

plt.savefig(fname_figs6_png, dpi=300)
plt.show()

# done with the plotting.