import perc_model as p_m
import perc_ext as p_e
import perc_plot as p_p
import numpy as n

def floating(radius,dimension):
    floating = False
    i = 1
    max_n = ()
    while floating == False:
        clusters = p_m.cluster_finder(p_m.disk_gen(i,dimension),radius,dimension)
        rho = 2.65*n.exp((-p_e.nc_calc(i,radius)))
        if rho < 1:
            max_n = (i,clusters)
            break
        i += 1
    return max_n

dim = 3
for i in n.linspace(0.05,0.2,16):
    x = floating(i,dim)[0]
    print(x,p_e.nc_calc(x,i))
