import vals
import fit
import frac_dis

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def plot_fit(ax, M, vk, params, style):
	a = params[0]
	b = params[1]
	c = params[2]
	y = np.zeros(M.shape)
	index = M >= np.power(10, c)*np.power(vk, b)
	temp = np.log10(M[index]) - b*np.log10(vk) - c
	y[index] = 1.0 - np.exp(-a*temp*temp)
	ax.plot(M, y, style, alpha=0.7)

def M_star(vk, params):
	a = params[0]
	b = params[1]
	c = params[2]
	return np.power(10, c)*np.power(vk, b)

def step_function(M, vk):
	suntokg = 1.9891e30
	mpctom  = 3.08567758e22
	g0 = 6.67384e-11
	v = vk/100.0          # the velocity unit here is 100km/s
	g1 = g0/1e10/mpctom*suntokg
	Delta = 200           # the boudary of host is define by 200 *rho_crit
	Mstep = v * v * v / 2.0 / g1 / np.sqrt(Delta) # we work with z=0 
	y = np.zeros(M.shape)
	index = M > Mstep
	y[index] = 1
	return y


def plot_mass_relation():
	fig1 = plt.figure(figsize=(10, 5))
	ax1 = fig1.add_subplot(1,2,1)
	ax1.set_xscale('log')
	ax1.set_xlabel(r"$M[M_{\odot}/h]$")
	ax1.set_xlim(2e8, 1e16)
	ax1.set_ylim(-0.05, 0.55)
	ax1.set_ylabel(r"$f_{host}$")
	ax1.set_yticks(np.arange(0, 0.6, 0.1))
	ax1.plot(vals.stats_0100_10p[:,0], vals.stats_0100_10p[:,1]*0.1, "kd--", alpha=0.7)
	ax1.plot(vals.stats_0100_30p[:,0], vals.stats_0100_30p[:,1]*0.3, "ks--", alpha=0.7)
	ax1.plot(vals.stats_0100_50p[:,0], vals.stats_0100_50p[:,1]*0.5, "ko--", alpha=0.7)
	ax1.plot(vals.stats_0200_10p[:,0], vals.stats_0200_10p[:,1]*0.1, "rd--", alpha=0.7)
	ax1.plot(vals.stats_0200_30p[:,0], vals.stats_0200_30p[:,1]*0.3, "rs--", alpha=0.7)
	ax1.plot(vals.stats_0200_50p[:,0], vals.stats_0200_50p[:,1]*0.5, "ro--", alpha=0.7)
	ax1.plot(vals.stats_0500_10p[:,0], vals.stats_0500_10p[:,1]*0.1, "gd--", alpha=0.7)
	ax1.plot(vals.stats_0500_30p[:,0], vals.stats_0500_30p[:,1]*0.3, "gs--", alpha=0.7)
	ax1.plot(vals.stats_0500_50p[:,0], vals.stats_0500_50p[:,1]*0.5, "go--", alpha=0.7)	
	ax1.plot(vals.stats_1000_10p[:,0], vals.stats_1000_10p[:,1]*0.1, "bd--", alpha=0.7)
	ax1.plot(vals.stats_1000_30p[:,0], vals.stats_1000_30p[:,1]*0.3, "bs--", alpha=0.7)
	ax1.plot(vals.stats_1000_50p[:,0], vals.stats_1000_50p[:,1]*0.5, "bo--", alpha=0.7)
	ax2 = fig1.add_subplot(1,2,2)
	ax2.set_xscale('log')
	ax2.set_xlabel(r"$M[M_{\odot}/h]$")
	ax2.set_ylabel(r"$f_{host}/f_{global}$")
	ax2.set_ylim(-0.05, 1.05)
	ax2.set_yticks(np.linspace(0,1,6))
	ax2.set_xlim(2e8, 1e16)
	M = np.linspace(8, 16, 100)
	M = np.power(10, M)
	plot_fit(ax2, M, 100,  vals.best_params, "k-")
	plot_fit(ax2, M, 200,  vals.best_params, "r-")
	plot_fit(ax2, M, 500,  vals.best_params, "g-")
	plot_fit(ax2, M, 1000, vals.best_params, "b-")
	ax2.plot(M, step_function(M, 100),  "k--")          # plot the step function
	ax2.plot(M, step_function(M, 200),  "r--")
	ax2.plot(M, step_function(M, 500),  "g--")
	ax2.plot(M, step_function(M, 1000), "b--")         
	#thesis_params = np.array([0.31409, 3.35710, 2.44739])
	#plot_fit(ax2, M, 100,  thesis_params, "k--")
	#plot_fit(ax2, M, 200,  thesis_params, "r--")
	#plot_fit(ax2, M, 500,  thesis_params, "g--")
	#plot_fit(ax2, M, 1000, thesis_params, "b--")	
	ax2.plot(vals.stats_0100_10p[:,0], vals.stats_0100_10p[:,1], "kd", alpha=0.7)
	ax2.plot(vals.stats_0100_30p[:,0], vals.stats_0100_30p[:,1], "ks", alpha=0.7)
	ax2.plot(vals.stats_0100_50p[:,0], vals.stats_0100_50p[:,1], "ko", alpha=0.7)
	ax2.plot(vals.stats_0200_10p[:,0], vals.stats_0200_10p[:,1], "rd", alpha=0.7)
	ax2.plot(vals.stats_0200_30p[:,0], vals.stats_0200_30p[:,1], "rs", alpha=0.7)
	ax2.plot(vals.stats_0200_50p[:,0], vals.stats_0200_50p[:,1], "ro", alpha=0.7)
	ax2.plot(vals.stats_0500_10p[:,0], vals.stats_0500_10p[:,1], "gd", alpha=0.7)
	ax2.plot(vals.stats_0500_30p[:,0], vals.stats_0500_30p[:,1], "gs", alpha=0.7)
	ax2.plot(vals.stats_0500_50p[:,0], vals.stats_0500_50p[:,1], "go", alpha=0.7)	
	ax2.plot(vals.stats_1000_10p[:,0], vals.stats_1000_10p[:,1], "bd", alpha=0.7)
	ax2.plot(vals.stats_1000_30p[:,0], vals.stats_1000_30p[:,1], "bs", alpha=0.7)
	ax2.plot(vals.stats_1000_50p[:,0], vals.stats_1000_50p[:,1], "bo", alpha=0.7)
	fig1.set_tight_layout(True)
	fig1.savefig("host-mean.pdf")	

def plot_mass_relation_solo():
	fig1 = plt.figure(figsize=(4.5, 4))
	ax2 = fig1.add_subplot(1,1,1)
	ax2.set_xscale('log')
	ax2.set_xlabel(r"$M[M_{\odot}/h]$")
	ax2.set_ylabel(r"$\tilde{f}_h$")
	ax2.set_ylim(-0.05, 1.05)
	ax2.set_yticks(np.linspace(0,1,6))
	ax2.set_xlim(2e8, 1e16)
	M = np.linspace(8, 16, 100)
	M = np.power(10, M)
	plot_fit(ax2, M, 100,  vals.best_params, "k-")
	plot_fit(ax2, M, 200,  vals.best_params, "r-")
	plot_fit(ax2, M, 500,  vals.best_params, "g-")
	plot_fit(ax2, M, 1000, vals.best_params, "b-")
	ax2.plot(M, step_function(M, 100),  "k--")          # plot the step function
	ax2.plot(M, step_function(M, 200),  "r--")
	ax2.plot(M, step_function(M, 500),  "g--")
	ax2.plot(M, step_function(M, 1000), "b--")         
	#thesis_params = np.array([0.31409, 3.35710, 2.44739])
	#plot_fit(ax2, M, 100,  thesis_params, "k--")
	#plot_fit(ax2, M, 200,  thesis_params, "r--")
	#plot_fit(ax2, M, 500,  thesis_params, "g--")
	#plot_fit(ax2, M, 1000, thesis_params, "b--")	
	ax2.plot(vals.stats_0100_10p[:,0], vals.stats_0100_10p[:,1], "kd", alpha=0.7)
	ax2.plot(vals.stats_0100_30p[:,0], vals.stats_0100_30p[:,1], "ks", alpha=0.7)
	ax2.plot(vals.stats_0100_50p[:,0], vals.stats_0100_50p[:,1], "ko", alpha=0.7)
	ax2.plot(vals.stats_0200_10p[:,0], vals.stats_0200_10p[:,1], "rd", alpha=0.7)
	ax2.plot(vals.stats_0200_30p[:,0], vals.stats_0200_30p[:,1], "rs", alpha=0.7)
	ax2.plot(vals.stats_0200_50p[:,0], vals.stats_0200_50p[:,1], "ro", alpha=0.7)
	ax2.plot(vals.stats_0500_10p[:,0], vals.stats_0500_10p[:,1], "gd", alpha=0.7)
	ax2.plot(vals.stats_0500_30p[:,0], vals.stats_0500_30p[:,1], "gs", alpha=0.7)
	ax2.plot(vals.stats_0500_50p[:,0], vals.stats_0500_50p[:,1], "go", alpha=0.7)	
	ax2.plot(vals.stats_1000_10p[:,0], vals.stats_1000_10p[:,1], "bd", alpha=0.7)
	ax2.plot(vals.stats_1000_30p[:,0], vals.stats_1000_30p[:,1], "bs", alpha=0.7)
	ax2.plot(vals.stats_1000_50p[:,0], vals.stats_1000_50p[:,1], "bo", alpha=0.7)
	fig1.set_tight_layout(True)
	fig1.savefig("host-mean-solo.pdf")	

def plot_var_mass_relation():
	fig1 = plt.figure(figsize=(10, 5))
	ax1 = fig1.add_subplot(1,2,1)
	ax1.set_xscale('log')
	ax1.set_xlabel(r"$M[M_{\odot}/h]$")
	ax1.set_xlim(2e8, 1e16)
	#ax1.set_ylim(-0.05, 0.55)
	ax1.set_ylabel(r"$\sigma$")
	#ax1.set_yticks(np.arange(0, 0.6, 0.1))
	ax1.plot(vals.stats_0100_10p[:,0], vals.stats_0100_10p[:,2], "kd--", alpha=0.7)
	ax1.plot(vals.stats_0100_30p[:,0], vals.stats_0100_30p[:,2], "ks--", alpha=0.7)
	ax1.plot(vals.stats_0100_50p[:,0], vals.stats_0100_50p[:,2], "ko--", alpha=0.7)
	ax1.plot(vals.stats_0200_10p[:,0], vals.stats_0200_10p[:,2], "rd--", alpha=0.7)
	ax1.plot(vals.stats_0200_30p[:,0], vals.stats_0200_30p[:,2], "rs--", alpha=0.7)
	ax1.plot(vals.stats_0200_50p[:,0], vals.stats_0200_50p[:,2], "ro--", alpha=0.7)
	ax1.plot(vals.stats_0500_10p[:,0], vals.stats_0500_10p[:,2], "gd--", alpha=0.7)
	ax1.plot(vals.stats_0500_30p[:,0], vals.stats_0500_30p[:,2], "gs--", alpha=0.7)
	ax1.plot(vals.stats_0500_50p[:,0], vals.stats_0500_50p[:,2], "go--", alpha=0.7)	
	ax1.plot(vals.stats_1000_10p[:,0], vals.stats_1000_10p[:,2], "bd--", alpha=0.7)
	ax1.plot(vals.stats_1000_30p[:,0], vals.stats_1000_30p[:,2], "bs--", alpha=0.7)
	ax1.plot(vals.stats_1000_50p[:,0], vals.stats_1000_50p[:,2], "bo--", alpha=0.7)
	ax2 = fig1.add_subplot(1,2,2)
	ax2.set_xscale('log')
	ax2.set_xlabel(r"$M/M_{\bigstar}$")
	#ax2.set_xlim(2e8, 1e16)
	#ax2.set_ylim(-0.05, 0.55)
	ax2.set_ylabel(r"$\sigma$")
	#ax2.set_yticks(np.arange(0, 0.6, 0.1))
	ax2.plot(vals.stats_0100_10p[:,0]/M_star( 100, vals.best_params), vals.stats_0100_10p[:,2], "kd", alpha=0.7)
	ax2.plot(vals.stats_0100_30p[:,0]/M_star( 100, vals.best_params), vals.stats_0100_30p[:,2], "ks", alpha=0.7)
	ax2.plot(vals.stats_0100_50p[:,0]/M_star( 100, vals.best_params), vals.stats_0100_50p[:,2], "ko", alpha=0.7)
	ax2.plot(vals.stats_0200_10p[:,0]/M_star( 200, vals.best_params), vals.stats_0200_10p[:,2], "rd", alpha=0.7)
	ax2.plot(vals.stats_0200_30p[:,0]/M_star( 200, vals.best_params), vals.stats_0200_30p[:,2], "rs", alpha=0.7)
	ax2.plot(vals.stats_0200_50p[:,0]/M_star( 200, vals.best_params), vals.stats_0200_50p[:,2], "ro", alpha=0.7)
	ax2.plot(vals.stats_0500_10p[:,0]/M_star( 500, vals.best_params), vals.stats_0500_10p[:,2], "gd", alpha=0.7)
	ax2.plot(vals.stats_0500_30p[:,0]/M_star( 500, vals.best_params), vals.stats_0500_30p[:,2], "gs", alpha=0.7)
	ax2.plot(vals.stats_0500_50p[:,0]/M_star( 500, vals.best_params), vals.stats_0500_50p[:,2], "go", alpha=0.7)	
	ax2.plot(vals.stats_1000_10p[:,0]/M_star(1000, vals.best_params), vals.stats_1000_10p[:,2], "bd", alpha=0.7)
	ax2.plot(vals.stats_1000_30p[:,0]/M_star(1000, vals.best_params), vals.stats_1000_30p[:,2], "bs", alpha=0.7)
	ax2.plot(vals.stats_1000_50p[:,0]/M_star(1000, vals.best_params), vals.stats_1000_50p[:,2], "bo", alpha=0.7)
	x = np.linspace(-1, 5, 500)
	y = fit.fit_function_var(x, vals.best_params_var[0], vals.best_params_var[1], vals.best_params_var[2])
	#ax2.set_ylim(0, 0.12)
	ax2.plot(np.power(10, x), y, "m-", linewidth=3)
	fig1.set_tight_layout(True)
	fig1.savefig("host-var.pdf")

def plot_one_distribution(ax, data, bin_num, hist_color, line_style, fg, label_seq, plot_seq):
	frac_max = np.amax(data[:,14]) * 1.01
	frac_min = np.amin(data[:,14]) * 0.99
	frac_mean = np.mean(data[:,14])
	frac_median = np.median(data[:,14])
	frac_var = np.std(data[:,14], ddof = 1)
	bins = np.linspace(frac_min, frac_max, bin_num)
	x = np.linspace(frac_min*0.8, frac_max*1.2, 200)
	y = norm.pdf(x, loc=frac_mean, scale=frac_var)
	ax.set_xlim(0, 0.5)
	ax.set_ylim(0, 70)
	if(plot_seq == 1):
		ax.set_yticks(np.arange(10, 80, 10))
	if(plot_seq == 3):
		ax.set_yticks(np.arange(0, 70, 10))
		ax.set_xticks(np.arange(0., 0.5, 0.1))
	if(plot_seq == 4):
		ax.set_xticks(np.arange(0.1, 0.6, 0.1))
	ax.hist(data[:,14], bins, normed=1, color = hist_color, alpha=0.6)# plot the histgram
	ax.plot(x, y, line_style, linewidth=2)
	if(label_seq != 0):
		ax.text(0.85, 0.4-0.1*label_seq, r"$%.0f$%%"%(fg*100), horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, color=hist_color, fontsize=15)
	

def make_multi_plot():
	fig = plt.figure(figsize=(12, 5))
	rec1 = [0.1, 0.5, 0.4, 0.4]
	rec2 = [0.5, 0.5, 0.4, 0.4]
	rec3 = [0.1, 0.1, 0.4, 0.4]
	rec4 = [0.5, 0.1, 0.4, 0.4]
	ax1 = fig.add_axes(rec1)
	ax2 = fig.add_axes(rec2)
	ax3 = fig.add_axes(rec3)
	ax4 = fig.add_axes(rec4)
	ax1.set_xticklabels([])
	ax2.set_xticklabels([])
	ax2.set_yticklabels([])
	ax4.set_yticklabels([])
	reduce_tick_size(ax1)
	reduce_tick_size(ax2)
	reduce_tick_size(ax3)
	reduce_tick_size(ax4)
	return fig, ax1, ax2, ax3, ax4

def reduce_tick_size(ax):
	ax.xaxis.set_tick_params(length=4)
	ax.yaxis.set_tick_params(length=4)


def add_text_for_plot(ax, bin_num):
	mass_left = vals.dis_mass_bin_vk_200[bin_num-1]
	mass_right = vals.dis_mass_bin_vk_200[bin_num]
	mass_left = np.log10(mass_left)
	mass_right = np.log10(mass_right)
	text = r"$%.2f%s%.2f$"%(mass_left, "<log_{10}M<", mass_right)
	ax.text(0.5, 0.9, text, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, color='black', fontsize=15)


def plot_frac_distribution(bin1):  # the bin starts from 1
	fig, ax1, ax2, ax3, ax4 = make_multi_plot()
	dis_0200_10p, dis_0200_30p, dis_0200_50p = frac_dis.prepare_data(bin1)
	plot_one_distribution(ax1, dis_0200_10p, 10, "green", "g--", 0.1, label_seq=1, plot_seq=1)
	plot_one_distribution(ax1, dis_0200_30p, 10, "blue",  "b--", 0.3, label_seq=2, plot_seq=1)
	plot_one_distribution(ax1, dis_0200_50p, 10, "red",   "r--", 0.5, label_seq=3, plot_seq=1)
	dis_0200_10p, dis_0200_30p, dis_0200_50p = frac_dis.prepare_data(bin1+1)	
	plot_one_distribution(ax2, dis_0200_10p, 10, "green", "g--", 0.1, label_seq=0, plot_seq=2)
	plot_one_distribution(ax2, dis_0200_30p, 10, "blue",  "b--", 0.3, label_seq=0, plot_seq=2)
	plot_one_distribution(ax2, dis_0200_50p, 10, "red",   "r--", 0.5, label_seq=0, plot_seq=2)
	dis_0200_10p, dis_0200_30p, dis_0200_50p = frac_dis.prepare_data(bin1+2)	
	plot_one_distribution(ax3, dis_0200_10p, 10, "green", "g--", 0.1, label_seq=0, plot_seq=3)
	plot_one_distribution(ax3, dis_0200_30p, 10, "blue",  "b--", 0.3, label_seq=0, plot_seq=3)
	plot_one_distribution(ax3, dis_0200_50p, 10, "red",   "r--", 0.5, label_seq=0, plot_seq=3)
	dis_0200_10p, dis_0200_30p, dis_0200_50p = frac_dis.prepare_data(bin1+3)	
	plot_one_distribution(ax4, dis_0200_10p, 10, "green", "g--", 0.1, label_seq=0, plot_seq=4)
	plot_one_distribution(ax4, dis_0200_30p, 10, "blue",  "b--", 0.3, label_seq=0, plot_seq=4)
	plot_one_distribution(ax4, dis_0200_50p, 10, "red",   "r--", 0.5, label_seq=0, plot_seq=4)
	add_text_for_plot(ax1, bin1)
	add_text_for_plot(ax2, bin1+1)
	add_text_for_plot(ax3, bin1+2)
	add_text_for_plot(ax4, bin1+3)
	fig.text(0.5, 0.05, "Fraction", ha='center', va='center', fontsize=18)
	fig.text(0.05, 0.5, "Probobility", rotation='vertical', ha='center', va='center', fontsize=18)
	plt.show()
	fig.savefig("host-distribution.pdf")
