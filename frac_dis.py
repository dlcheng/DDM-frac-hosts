# The strategy is to select a mean mass and a log-mass-bin for vk=100 and scale the mean mass with vk cube for 
# recoil velocites. In the meanwhile, the log-mass-bin is fixed. In each subplot, we show the models with the same vk.
# Notice that the distribution of the ddm fraction is made to the unnormalized values.

import vals
import mass_dep

import numpy as np
import matplotlib.pyplot as plt

def mass_selection(data, mass_left, mass_right):
	cond1 = data[:,4] > mass_left
	cond2 = data[:,4] < mass_right
	cond = np.logical_and(cond1, cond2)
	temp_data = data[cond, :]
	return temp_data

def prepare_data(mass_bin):
	#choose vk=200, fd=0.1 as base
	vals.dis_mass_bin_vk_200 = mass_dep.create_mass_bins(vals.vk_0200_10p, vals.total_mass_bin)
	#for vk = 200, the mass_bin starts from 1
	mass_left, mass_right = vals.dis_mass_bin_vk_200[mass_bin-1], vals.dis_mass_bin_vk_200[mass_bin]
	dis_0200_10p = mass_selection(vals.vk_0200_10p, mass_left, mass_right)
	dis_0200_30p = mass_selection(vals.vk_0200_30p, mass_left, mass_right)
	dis_0200_50p = mass_selection(vals.vk_0200_50p, mass_left, mass_right)
	#correct the last mass release
	dis_0200_10p[:,14] = dis_0200_10p[:,14] / dis_0200_10p[:,15] * 0.1 
	dis_0200_30p[:,14] = dis_0200_30p[:,14] / dis_0200_30p[:,15] * 0.3 
	dis_0200_50p[:,14] = dis_0200_50p[:,14] / dis_0200_50p[:,15] * 0.5
	return dis_0200_10p, dis_0200_30p, dis_0200_50p

