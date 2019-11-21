#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 19:42:49 2017

@author: dave
"""

import os
from multiprocessing import Pool
from argparse import ArgumentParser

#from itertools import product
from glob import glob
import numpy as np
#import pandas as pd
import matplotlib as mpl
import matplotlib.ticker as ticker
from wetb.prepost import (windIO, mplutils)
#from matplotlib import pyplot as plt
#plt.rc('text', usetex=True)


def example():
    labels = [None]
    base = '/some/path/to/hawc2sim/iea10mw/B0005'
    fnames = [os.path.join(base,
              'res/dlc12_iec61400-1ed3/dlc12_wsp08_wdir000_s1003')]
    figname = os.path.join(base, 'res/dlc12_iec61400-1ed3/', 'test.png')
    dashboard2(fnames, labels, figname=figname)


def dashboard2(fnames, labels=None, figname=None):

    if not isinstance(fnames, list):
        fnames = [fnames]
    if not isinstance(labels, list):
        labels = [labels]

    nrows = 6
    ncols = 4
    fig, axes = mplutils.subplots(nrows=nrows, ncols=ncols, figsize=(24,14),
                                  dpi=120)
    if len(fnames) > 1:
        colors = [['k-','k-'], ['r-','r-'], ['b-','b-'], ['g-','g-'], ['m-','m-']]
        alphas = [1.0, 0.8, 0.6, 0.5, 0.5]
    else:
        colors = [['k-','r-']]
        alphas = [1.0]

    for fname, color, alpha, label in zip(fnames, colors, alphas, labels):
        print(fname)
        dashboard(fname, axes, colors=color, alpha=alpha, label1=label)

    if not isinstance(figname, str):
        figname = fname

    # only plot new files
    if os.path.isfile(figname + '.png'):
        return

    fig.suptitle(figname)
    fig.tight_layout()
    fig.subplots_adjust(top=0.92)
    print('saving: %s' % (figname + '.png'))
    fig.savefig(figname + '.png')


def dashboard(fname, axes, colors=['k-','r-'], alpha=1.0, label1=None):

    p1 = os.path.dirname(fname)
    p2 = os.path.basename(fname)

    # only plot new files
    if os.path.isfile(fname + '.png'):
        return

    try:
        res = windIO.LoadResults(p1, p2)
    except Exception as e:
        print('failed loading:', fname)
        print(e)
        return

    df = res.ch_df.copy()
    df['chi'] = df.index
    df.set_index('unique_ch_name', inplace=True)
    time = res.sig[:,0]

    # =========================================================================
    # ADD CHANNEL : METHOD B
    # yaw error
#    yaw_angle = res.sig[:,df.loc['bearing-yaw_ang-angle-deg', 'chi']]
#    wdir = res.sig[:,df.loc['windspeed-global-Vdir_hor-0.00-0.00--119.00', 'chi']]
#    yaw_error = wdir - (360 - yaw_angle)
#    tmp = [['' for k in range(len(df.columns))]]
#    df_tmp = pd.DataFrame(tmp, columns=df.columns)
#    df_tmp['chi'] = [res.sig.shape[1]]
#    df_tmp.index = ['yaw-error']
#    df = df.append(df_tmp)
#    res.sig = np.append(res.sig, yaw_error.reshape((len(yaw_error),1)), axis=1)
    # =========================================================================

#    for k in sorted(df.index): print(k)

    plot_chans = {}
    plot_chans['RPM'] = ['bearing-shaft_rot-angle_speed-rpm']
#    plot_chans['$P_e$'] = ['DLL-generator_servo-inpvec-2']
#    plot_chans['$Torsion_{7.39}$'] = ['Tors_e-1-7.36']
    plot_chans['$TB_{SS}$'] = ['tower-tower-node-001-momentvec-y']
    plot_chans['$TB_{FA}$'] = ['tower-tower-node-001-momentvec-x']
#    plot_chans['brake'] = ['DLL-mech_brake-inpvec-1']
    plot_chans['$Q_{gen}$'] = ['DLL-generator_servo-inpvec-1']
#    plot_chans['$shaft_{torsion}$'] = ['shaft-shaft-node-004-momentvec-z']
    plot_chans['$B1_{pitch}$'] = ['bearing-pitch1-angle-deg']
#    plot_chans['status'] = ['DLL-dtu_we_controller-inpvec-22']
#    plot_chans['$V_{hub}$'] = ['windspeed-global-Vy-0.00-0.00--25.36']

    plot_chans['$Broot_{flap}$'] = ['blade1-blade1-node-004-momentvec-x']
    plot_chans['$Broot_{edge}$'] = ['blade1-blade1-node-004-momentvec-y']
    plot_chans['$Broot_{torsion}$'] = ['blade1-blade1-node-004-momentvec-z']
#    plot_chans['$\\alpha_{9.7}$'] = ['Alfa-1-9.7']

#    plot_chans['$Torsion_{9.7}$'] = ['Tors_e-1-9.7']
#    plot_chans['$\\alpha_{9.6}$'] = ['Alfa-1-9.6']
#    plot_chans['$Torsion_{9.6}$'] = ['Tors_e-1-9.6']

    # =========================================================================
    # ADD CHANNEL : METHOD A
#    new = np.zeros((res.sig.shape[0],1))
#    chan = 'tower-top-acc-xy'
#    ch1 = res.sig[:,df.loc['tower-tower-elem-021-zrel-1.00-State acc-x', 'chi']]
#    ch2 = res.sig[:,df.loc['tower-tower-elem-021-zrel-1.00-State acc-y', 'chi']]
#    new[:,0] = np.sqrt(ch1*ch1 + ch2*ch2)
#    res.sig = np.append(res.sig, new, axis=1)
#    df.loc[chan, 'chi'] = res.sig.shape[1] - 1
#    plot_chans['$TT_{xy,acc}$'] = [chan]
    # =========================================================================

    # plots withouth PSD
    nonpsd = {}

    nonpsd['$P_e$'] = ['DLL-generator_servo-inpvec-2']
#    nonpsd['$B1_{pitch}$'] = ['bearing-pitch1-angle-deg']
    nonpsd['$\\alpha_{76.07}$'] = ['Alfa-1-76.07']
    nonpsd['$shaft_{torsion}$'] = ['shaft-shaft-node-004-momentvec-z']
    nonpsd['$V_{hub}$'] = ['windspeed-global-Vy-0.00-0.00--119.00']

#    nonpsd['$B1_{pitch}$'] = ['bearing-pitch1-angle-deg']
#    nonpsd['status'] = ['DLL-dtu_we_controller-inpvec-22']
    nonpsd['$TT_{acc}$'] = ['DLL-dtu_we_controller-inpvec-27']
    nonpsd['brake'] = ['DLL-mech_brake-inpvec-1']
    nonpsd['tower clearance'] = ['DLL-towerclearance_mblade-inpvec-1']
    nonpsd['status'] = ['DLL-dtu_we_controller-inpvec-22']

    rpm_mean = res.sig[:,df.loc[plot_chans['RPM'] , 'chi']].mean()

    psd_freq_lim = 5

    nrows = axes.shape[0]
    ncols = axes.shape[1]
    col = 0
    colors = colors*ncols*nrows
#    for i, (ax, (label, chans)) in enumerate(zip(axes, plot_chans.items()):
    for i, (label, chans) in enumerate(sorted(plot_chans.items())):
        row = int(np.floor(i/ncols))
        ax = axes[row*2, col]
        axp = axes[row*2+1, col]
        cs = colors[i]
#        print(i, row, col)
        chan = chans[0]
        sig = res.sig[:,df.loc[chan, 'chi']]
#        ax.set_title(chan.replace('_', '\\_'))
        ax.set_title(label + ' : ' + chan)
        if label1 is None:
            _label = label
        else:
            _label = label1
        ax.plot(time, sig, cs, label=_label, alpha=alpha)
        ax.set_xlim([time[0], time[-1]])
        # clear all the labels
        # ax.set_xticklabels([])
        # alternatively, make the labels invisible
        mpl.artist.setp(ax.get_xticklabels(), visible=False)
        axp = mplutils.psd(axp, time, sig, res_param=250, f0=0, f1=psd_freq_lim,
                           nr_peaks=10, min_h=15, mark_peaks=True, col=cs,
                           label=None, alpha=alpha/2, ypos_peaks=0.9,
                           ypos_peaks_delta=0.12)

        axp.set_xlim([0, psd_freq_lim])
        axp.set_yscale('log')
        axp = mplutils.p4psd(axp, rpm_mean, ps=[1, 3, 6, 9])
        # set PSD plot to grey
        axp.spines['bottom'].set_color('grey')
        axp.spines['top'].set_color('grey')
        axp.spines['right'].set_color('grey')
        axp.spines['left'].set_color('grey')
        axp.tick_params(axis='x', colors='grey', which='both')
        axp.tick_params(axis='y', colors='grey', which='both')
        axp.xaxis.set_ticks(np.arange(0, psd_freq_lim, 0.5))
        axp.xaxis.set_ticks(np.arange(0, psd_freq_lim, 0.1), minor=True)
        # hide the labels
#        if row*2+1 < nrows-2:
#            mpl.artist.setp(axp.get_xticklabels(), visible=False)
#        else:
#            axp.xaxis.set_major_formatter(ticker.FormatStrFormatter('%1.0f'))
        axp.xaxis.set_major_formatter(ticker.FormatStrFormatter('%1.1f'))
        axp.grid(True, which='minor')

        ax.grid(True)
        ax.legend(loc='best', borderaxespad=0)
        col += 1
        if col >= ncols:
            col = 0

    j = len(plot_chans)
    col = 0
    for i, (label, chans) in enumerate(sorted(nonpsd.items())):
        if label1 is None:
            _label = label
        else:
            _label = label1
        row = int(np.floor((i+j*2)/ncols))
        ax = axes[row, col]
        cs = colors[i+j]
        chan = chans[0]
        sig = res.sig[:,df.loc[chan, 'chi']]
        ax.set_title(label + ' : ' + chan)
        ax.plot(time, sig, cs, label=_label, alpha=alpha)
        ax.set_xlim([time[0], time[-1]])
        ax.grid(True)
        ax.legend(loc='best', borderaxespad=0)

        col += 1
        if col >= ncols:
            col = 0


def plot_all_h2(cpus=2, chunksize=80):

    combis = glob(os.path.join('**', '*.hdf5'), recursive=True)
    pool = Pool(processes=cpus)
    for ind, res in enumerate(pool.imap(dashboard2, combis), chunksize):
        print(ind)


if __name__ == '__main__':

    parser = ArgumentParser(description = '')
    parser.add_argument('-n', type=int, default=2, action='store',
                        dest='cpus', help='Number of CPUs to use on the node')
    parser.add_argument('-c', type=int, default=80, action='store',
                        dest='chunksize', help='Chunksize Pool.')
    opt = parser.parse_args()

    plot_all_h2(cpus=opt.cpus, chunksize=opt.chunksize)

