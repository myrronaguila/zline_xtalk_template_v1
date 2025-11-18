# -*- coding: utf-8 -*-
"""
Created on Thurs 20251113

Figs4 - Flux crosstalk as a function of rectangular flux pulse duration
1. figs4 - Flux crosstalk (in permille) as a function of flux pulse duration.
Initialization time for the experiment => 200 us.

@author: Mai
"""

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import sys
import os

"""For loading figures, plotting and saving"""
from util_functions import set_font_default, xr_load_nc_to_dict
from matplotlib.ticker import (MultipleLocator)

# retrieve files
dir_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
#print(dir_common_path)
sys.path.append(dir_data_path)
loc_figs4 = dir_data_path + '\\' + 'data_figs4.nc'
dict_figs4 = xr_load_nc_to_dict(loc_figs4) # format

# save files to png /or svg / set directory for saving.
dir_figures_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'figures'))
dir_save = dir_figures_path + '\\editable_source\\'
# save files to png /or svg
fname_figs4_png = dir_save + 'figs4.png'
fname_figs4_svg = dir_save + 'figs4.svg'

"""---------------Format----------------------------------------------------"""
figsize, lgd_loc = dict_figs4['figsize'], dict_figs4['lgd_loc']
frameon = dict_figs4['frameon']

xlabel, ylabel = dict_figs4['xlabel'], dict_figs4['ylabel']
fsize = dict_figs4['font_size']
set_font_default(fsize) # set default settings for plots
lsize = dict_figs4['lgd_size']

"""--------Source (Q2), Probe (C1)--------------------"""
# line plot
figs4_x_time_1d = dict_figs4['x_t_(us)']
figs4_y_xtalk_1d = dict_figs4['y_xtalk_(permille)']

# fit line
figs4_xfit_time_1d = dict_figs4['xfit_t_(us)']
figs4_yfit_xtalk_1d = dict_figs4['yfit_xtalk_(permille)']

# format
figs4_data_lgd, figs4_fit_lgd = dict_figs4['data_lgd'], dict_figs4['fit_lgd']
# major and minor ticks
figs4_yticks_maj, figs4_yticks_min = dict_figs4['yticks_major'], dict_figs4['yticks_minor']
# xlim, ylim
figs4_xlim, figs4_ylim = dict_figs4['xlim'], dict_figs4['ylim']
# data design
figs4_datacls, figs4_fitcls = dict_figs4['data_cls'], dict_figs4['fit_cls']


"""----------------vertical plot (desired output plots)---------------------"""

fig = plt.figure(constrained_layout=True, figsize=figsize)

spec = gridspec.GridSpec(ncols=1, nrows=1, figure=fig, hspace=-0.15, wspace=-0.1)
ax0 = fig.add_subplot(spec[0, 0]) # top left, Q3 => Q1

ax0.plot(figs4_x_time_1d, figs4_y_xtalk_1d, figs4_datacls, 
         label=figs4_data_lgd)
ax0.plot(figs4_xfit_time_1d, figs4_yfit_xtalk_1d, figs4_fitcls, 
         label=figs4_fit_lgd)
ax0.set_xscale('log')
ax0.tick_params(axis = 'both', which ='both', direction='in', top=True, 
                right = True)
ax0.set_yticks(figs4_yticks_maj)

# For the minor ticks, use no labels; default NullFormatter.
ax0.yaxis.set_minor_locator(MultipleLocator(figs4_yticks_min))

ax0.set_xlabel(xlabel)
ax0.set_ylabel(ylabel)
ax0.legend(loc=lgd_loc, frameon=frameon[0])
plt.savefig(fname=fname_figs4_png, dpi=300)
plt.show()