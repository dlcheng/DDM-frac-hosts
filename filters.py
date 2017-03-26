# name filter comflicts with the build-in method of Python, so here is filters.
import vals

import numpy as np

def select(data):
	cond = data[:,1] == -1            # only hosts
	data_eff = data[cond, :]
	return data_eff	

def select_hosts():
	vals.vk_0050_50p = select(vals.vk_0050_50p) 
	vals.vk_0100_10p = select(vals.vk_0100_10p) 
	vals.vk_0100_30p = select(vals.vk_0100_30p) 
	vals.vk_0100_50p = select(vals.vk_0100_50p) 
	vals.vk_0200_10p = select(vals.vk_0200_10p) 
	vals.vk_0200_30p = select(vals.vk_0200_30p) 
	vals.vk_0200_50p = select(vals.vk_0200_50p) 
	vals.vk_0500_10p = select(vals.vk_0500_10p) 
	vals.vk_0500_30p = select(vals.vk_0500_30p) 
	vals.vk_0500_50p = select(vals.vk_0500_50p) 
	vals.vk_1000_10p = select(vals.vk_1000_10p)
	vals.vk_1000_30p = select(vals.vk_1000_30p)
	vals.vk_1000_50p = select(vals.vk_1000_50p)	