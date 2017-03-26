import vals

import numpy as np

#format of halo_catalog.txt
#(1)HaloID  (2)HostFlag (3)Trusted_Nsub (4)Npart (5)Mvir (6)Rvir (7)cNFW_ahf (8)cNFW_Vmax 
#(9)cNFW_Rmax (10)X (11)Y (12)Z (13)Nbin (14)fs (15)fvir (16)fglobal (17)Nddm 

def create_mass_bins(data, num_bins):
	mass_max = np.amax(data[:,4])+1                            # slightly larger bins to include both the max and the min
	mass_min = np.amin(data[:,4])-1
	bins = np.linspace(np.log10(mass_min), np.log10(mass_max), num_bins+1)
	bins = np.power(10, bins)
	return bins

def sort(data, col):                                           # return the sorted data along the specified column, from small to large 
	index = np.argsort(data[:,col], kind='mergesort')
	data_eff = data[index,:]                                   # advanced slicing with array, create new array
	return data_eff

def frac_statistic(data, hist):
	num_bins = hist.shape[0]
	mean = np.zeros(hist.shape)
	var  = np.zeros(hist.shape)
	median = np.zeros(hist.shape)
	j = 0
	for i in range(num_bins):
		mean[i] = np.mean(data[j:j+hist[i],14])
		var[i]  = np.std(data[j:j+hist[i],14], ddof=1)         # N-1
		median[i] = np.median(data[j:j+hist[i],14])
		j += hist[i]
	return  mean, var, median                              

def frac_mass_dep(data, mass_bins_num):
	data = sort(data, 4)                                       # sort data according to mass
	data[:,14] /= data[:,15]
	mass_bins = create_mass_bins(data, mass_bins_num)
	hist, bin_edge = np.histogram(data[:,4], mass_bins)
	mean, var, median = frac_statistic(data, hist)
	mass = np.log10(mass_bins)
	mass = mass[:-1] + (mass[1]-mass[0])/2.0
	mass = np.power(10, mass)
	cond = mean >= 0.0
	mean = mean[cond]
	var  = var[cond]
	median = median[cond]
	mass = mass[cond]
	return np.array((mass, mean, var, median)).T                 # return np array

def add_vk(data, vk):
	data_eff = np.zeros((data.shape[0], data.shape[1]+1))
	data_eff[:,:-1] = data
	data_eff[:,-1] = vk
	return data_eff	

def statistic_data(mass_bins_num):
	vals.total_mass_bin = mass_bins_num
	#get statistic data of dm fraction
	vals.stats_0050_50p = frac_mass_dep(vals.vk_0050_50p, mass_bins_num)
	vals.stats_0100_10p = frac_mass_dep(vals.vk_0100_10p, mass_bins_num)
	vals.stats_0100_30p = frac_mass_dep(vals.vk_0100_30p, mass_bins_num)
	vals.stats_0100_50p = frac_mass_dep(vals.vk_0100_50p, mass_bins_num)
	vals.stats_0200_10p = frac_mass_dep(vals.vk_0200_10p, mass_bins_num)
	vals.stats_0200_30p = frac_mass_dep(vals.vk_0200_30p, mass_bins_num)
	vals.stats_0200_50p = frac_mass_dep(vals.vk_0200_50p, mass_bins_num)
	vals.stats_0500_10p = frac_mass_dep(vals.vk_0500_10p, mass_bins_num)
	vals.stats_0500_30p = frac_mass_dep(vals.vk_0500_30p, mass_bins_num)
	vals.stats_0500_50p = frac_mass_dep(vals.vk_0500_50p, mass_bins_num)
	vals.stats_1000_10p = frac_mass_dep(vals.vk_1000_10p, mass_bins_num)
	vals.stats_1000_30p = frac_mass_dep(vals.vk_1000_30p, mass_bins_num)
	vals.stats_1000_50p = frac_mass_dep(vals.vk_1000_50p, mass_bins_num)
	#add vk to the last column
	vals.stats_0050_50p = add_vk(vals.stats_0050_50p,  50.0)
	vals.stats_0100_10p = add_vk(vals.stats_0100_10p, 100.0)
	vals.stats_0100_30p = add_vk(vals.stats_0100_30p, 100.0)
	vals.stats_0100_50p = add_vk(vals.stats_0100_50p, 100.0)
	vals.stats_0200_10p = add_vk(vals.stats_0200_10p, 200.0)
	vals.stats_0200_30p = add_vk(vals.stats_0200_30p, 200.0)
	vals.stats_0200_50p = add_vk(vals.stats_0200_50p, 200.0)
	vals.stats_0500_10p = add_vk(vals.stats_0500_10p, 500.0)
	vals.stats_0500_30p = add_vk(vals.stats_0500_30p, 500.0)
	vals.stats_0500_50p = add_vk(vals.stats_0500_50p, 500.0)
	vals.stats_1000_10p = add_vk(vals.stats_1000_10p,1000.0)
	vals.stats_1000_30p = add_vk(vals.stats_1000_30p,1000.0)
	vals.stats_1000_50p = add_vk(vals.stats_1000_50p,1000.0)

