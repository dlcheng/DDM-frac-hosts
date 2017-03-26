#
#  This python routine is designed to extract the fraction of dm particles within halos, fit them
#  with the empirical function of my thesis. Improved from previous study, the data of different simulations
#  is combined together before binned according to the mass. Also we study the fraction distribution within
#  the mass bins characterized by the turn-over mass of the fraction-mass relation.
#                                                                          -Dalong Cheng, 2015/12/28
import vals
import load_data
import filters
import mass_dep
import fit
import frac_dis
import plot

#reload incase there is any change
reload(vals)
reload(load_data)
reload(filters)
reload(mass_dep)
reload(fit)
reload(frac_dis)
reload(plot)

import numpy as np
import matplotlib.pyplot as plt

load_data.load_data()
filters.select_hosts()

mass_dep.statistic_data(10)

fit.make_fit_data_mean()
fit.do_fit_mean()

fit.make_fit_data_var()
fit.do_fit_var()

#plot.plot_mass_relation()
plot.plot_mass_relation_solo()
#plot.plot_var_mass_relation()
#plot.plot_frac_distribution(2)  # 4 bins start from bin 2

#np.savetxt("host-mean-params.txt", vals.best_params)
#np.savetxt("host-var-params.txt", vals.best_params_var)


