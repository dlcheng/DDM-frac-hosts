import vals
import plot

import numpy as np
from scipy.optimize import curve_fit

def make_fit_data_mean():
	vals.fit_data = np.concatenate((vals.stats_0100_10p, vals.stats_0100_30p), axis=0)
	vals.fit_data = np.concatenate((vals.fit_data, vals.stats_0100_50p),       axis=0)
	vals.fit_data = np.concatenate((vals.fit_data, vals.stats_0200_10p),       axis=0)
	vals.fit_data = np.concatenate((vals.fit_data, vals.stats_0200_30p),       axis=0)
	vals.fit_data = np.concatenate((vals.fit_data, vals.stats_0200_50p),       axis=0)
	vals.fit_data = np.concatenate((vals.fit_data, vals.stats_0500_10p),       axis=0)
	vals.fit_data = np.concatenate((vals.fit_data, vals.stats_0500_30p),       axis=0)
	vals.fit_data = np.concatenate((vals.fit_data, vals.stats_0500_50p),       axis=0)
	vals.fit_data = np.concatenate((vals.fit_data, vals.stats_1000_10p),       axis=0)
	vals.fit_data = np.concatenate((vals.fit_data, vals.stats_1000_30p),       axis=0)
	vals.fit_data = np.concatenate((vals.fit_data, vals.stats_1000_50p),       axis=0)

def fit_function_mean(x, a, b, c):                       # x[:,0] = M, x[:,1] = vk
	y = np.zeros((x.shape[0],))
	index = x[:,0] >= np.power(10, c)*np.power(x[:,1], b)
	temp = np.log10(x[index,0]) - b*np.log10(x[index, 1]) - c
	y[index] = 1.0 - np.exp(-a*temp*temp)
	return y

def do_fit_mean():
	vals.best_params, vals.cov_matrix = curve_fit(fit_function_mean, vals.fit_data[:,0::4], vals.fit_data[:,1], p0=(0.31409, 3.35710, 2.44739))

def make_fit_data_var():
	vals.fit_data_var = np.concatenate((vals.stats_0100_10p, vals.stats_0100_30p),       axis=0)
	vals.fit_data_var = np.concatenate((vals.fit_data_var, vals.stats_0100_50p),         axis=0)
	vals.fit_data_var = np.concatenate((vals.fit_data_var, vals.stats_0200_10p),         axis=0)
	vals.fit_data_var = np.concatenate((vals.fit_data_var, vals.stats_0200_30p),         axis=0)
	vals.fit_data_var = np.concatenate((vals.fit_data_var, vals.stats_0200_50p),         axis=0)
	vals.fit_data_var[:,0] = vals.fit_data_var[:,0] / plot.M_star(vals.fit_data_var[:,-1], vals.best_params)
	index = vals.fit_data_var[:,2] < 100
	vals.fit_data_var = vals.fit_data_var[index, :]
	vals.fit_data_var[:,0] = np.log10(vals.fit_data_var[:,0])

def fit_function_var(x, a, b, c):
	y = np.zeros((x.shape[0],))
	index = x >= 0.0
	y[index] = c*np.exp(-np.power(x[index]-a, 2)/b)
	return y

def do_fit_var():
	vals.best_params_var, vals.cov_matrix_var = curve_fit(fit_function_var, vals.fit_data_var[:,0], vals.fit_data_var[:,2], p0=(1.2, 1.1, 1.0))
