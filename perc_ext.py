# Author: David Monk
# Project: Percolation modelling

import numpy as n
import perc_model as p_m

def min_disks(radius,dimension):
    i = 1
    con = False
    while con == False:
        R = p_m.disk_gen(i,dimension)
        clusters = p_m.cluster_finder(R,radius,dimension)
        for j in clusters:
            if j.connection == True:
                con = True
                break
        i += 1
    return i,clusters

def max_disks(radius,dimension):
    i = 1
    con = False
    while con == False:
        R = p_m.disk_gen(i,dimension)
        clusters = p_m.cluster_finder(R,radius,dimension)
        for j in clusters:
            if j.contained == True:
                max_f = clusters
            elif j.contained == False:
                con = True
                break
        i += 1
    return i - 1,max_f

def nc_calc(N,radius):
    return N*n.pi*pow(radius,2)

def cr_density_calc(radius,dimension):
    return min_disks(radius,dimension)[0]*n.pi*pow(radius,2)

def density_m(maximum,minimum,iterations,dimension):
    dens = []
    mean = lambda x:sum(x)/len(x)
    for i in n.linspace(maximum,minimum,iterations):
        dens.append(cr_density_calc(i,dimension))
    return mean(dens)

def mean_density_r(radius,iterations,dimension):
    dens = []
    mean = lambda x:sum(x)/len(x)
    for i in range(iterations):
        dens.append(cr_density_calc(radius,dimension))
    return mean(dens)

def fraction_disks(n_c):
    return 1 - n.exp(-n_c)
