import vals

import numpy as np

def load_data():
	decay_2 = np.loadtxt("../data-bin-10/Decay-2/z-0/halo_catalog.txt")
	decay_3 = np.loadtxt("../data-bin-10/Decay-3/z-0/halo_catalog.txt")
	decay_5 = np.loadtxt("../data-bin-10/Decay-5/z-0/halo_catalog.txt")
	decay_7 = np.loadtxt("../data-bin-10/Decay-7/z-0/halo_catalog.txt")
	decay_8 = np.loadtxt("../data-bin-10/Decay-8/z-0/halo_catalog.txt")
	decay_9 = np.loadtxt("../data-bin-10/Decay-9/z-0/halo_catalog.txt")
	decay_10= np.loadtxt("../data-bin-10/Decay-10/z-0/halo_catalog.txt")
	decay_11= np.loadtxt("../data-bin-10/Decay-11/z-0/halo_catalog.txt")
	decay_12= np.loadtxt("../data-bin-10/Decay-12/z-0/halo_catalog.txt")
	decay_13= np.loadtxt("../data-bin-10/Decay-13/z-0/halo_catalog.txt")
	decay_14= np.loadtxt("../data-bin-10/Decay-14/z-0/halo_catalog.txt")
	decay_15= np.loadtxt("../data-bin-10/Decay-15-altix/z-0/halo_catalog.txt")
	decay_16= np.loadtxt("../data-bin-10/Decay-16/z-0/halo_catalog.txt")
	decay_17= np.loadtxt("../data-bin-10/Decay-17/z-0/halo_catalog.txt")
	decay_18= np.loadtxt("../data-bin-10/Decay-18/z-0/halo_catalog.txt")
	decay_19= np.loadtxt("../data-bin-10/Decay-19/z-0/halo_catalog.txt")
	decay_20= np.loadtxt("../data-bin-10/Decay-20/z-0/halo_catalog.txt")
	decay_21= np.loadtxt("../data-bin-10/Decay-21/z-0/halo_catalog.txt")
	decay_22= np.loadtxt("../data-bin-10/Decay-22/z-0/halo_catalog.txt")
	decay_23= np.loadtxt("../data-bin-10/Decay-23/z-0/halo_catalog.txt")
	decay_24= np.loadtxt("../data-bin-10/Decay-24/z-0/halo_catalog.txt")
	decay_25= np.loadtxt("../data-bin-10/Decay-25/z-0/halo_catalog.txt")
	decay_26= np.loadtxt("../data-bin-10/Decay-26/z-0/halo_catalog.txt")
	decay_27= np.loadtxt("../data-bin-10/Decay-27/z-0/halo_catalog.txt")
	decay_28= np.loadtxt("../data-bin-10/Decay-28/z-0/halo_catalog.txt")
	decay_29= np.loadtxt("../data-bin-10/Decay-29/z-0/halo_catalog.txt")
	#combine together according to decay-dark-matter-1.pdf
	vals.vk_0050_50p = decay_29
	vals.vk_0100_10p = np.concatenate((decay_22, decay_23), axis=0)
	vals.vk_0100_30p = np.concatenate((decay_17, decay_19), axis=0)
	vals.vk_0100_50p = np.concatenate((decay_16, decay_18), axis=0)
	vals.vk_0200_10p = np.concatenate((decay_24, decay_25), axis=0)
	vals.vk_0200_30p = np.concatenate((decay_7, decay_8),   axis=0)
	vals.vk_0200_50p = np.concatenate((decay_2, decay_3),   axis=0)
	vals.vk_0500_10p = np.concatenate((decay_26, decay_27), axis=0)
	vals.vk_0500_30p = np.concatenate((decay_11, decay_12), axis=0)
	vals.vk_0500_50p = np.concatenate((decay_9, decay_10),  axis=0)
	vals.vk_1000_10p = decay_28
	vals.vk_1000_30p = decay_14
	vals.vk_1000_50p = decay_13

