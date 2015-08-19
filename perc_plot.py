# Author: David Monk
# Project: Percolation modelling

import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3
import perc_model as p_m
import perc_ext as p_e
import numpy as n
import stat_analysis as st
import matplotlib.mlab as mlab
from itertools import combinations, product

def disks(clusters,dimension,N):
    if dimension == 2:
        fig = p.figure()
        fig.add_subplot(111,aspect='equal')
        p.title('N = %s r = %s'%(N,clusters[0].radius))
        for i in clusters:
            if i.connection == True:
                for j in i.disks:
                    fig.gca().add_artist(p.Circle((j[0],j[1]),i.radius,alpha=0.5,color='r'))
            elif i.connection == False:
                for j in i.disks:
                    fig.gca().add_artist(p.Circle((j[0],j[1]),i.radius,alpha=0.5,color='b'))
        p.show()
    elif dimension == 3:
        u = n.r_[0:2*n.pi:20j]
        v = n.r_[0:2*n.pi:20j]
        fig = p.figure()
        ax = fig.add_subplot(111,projection='3d')
        for i in clusters:
            if i.connection == True:
                for j in i.disks:
                    x=i.radius*n.outer(n.cos(u),n.sin(v))+j[0]
                    y=i.radius*n.outer(n.sin(u),n.sin(v))+j[1]
                    z=i.radius*n.outer(n.ones(n.size(u)),n.cos(v))+j[2]
                    ax.plot_wireframe(x,y,z,color='r')
            elif i.connection == False:
                for j in i.disks:
                    x=i.radius*n.outer(n.cos(u),n.sin(v))+j[0]
                    y=i.radius*n.outer(n.sin(u),n.sin(v))+j[1]
                    z=i.radius*n.outer(n.ones(n.size(u)),n.cos(v))+j[2]
                    ax.plot_wireframe(x,y,z,color='b')
        r = [0,1]
        for s,e in combinations(n.array(list(product(r,r,r))),2):
            if n.sum(n.abs(s-e)) == r[1]-r[0]:
                ax.plot_wireframe(*zip(s,e),color = 'black')
#        p3.set_xlim3d((0,1))
#        p3.set_ylim3d((0,1))
#        p3.set_zlim3d((0,1))
        p.title('N = %s r = %s'%(N,clusters[0].radius))
        p.show()                   
    else:
        return False

def nc_r(radius,dimension,repeats):
    n_c = []
    nc = []
    freq = []
    for i in range(repeats):
        n_c.append(p_e.min_disks(radius,dimension)[0])
    for i in range(min(n_c),max(n_c)+1):
        nc.append(i)
        freq.append(n_c.count(i)/repeats)
    mean = st.mean(n_c)
    sd = st.sd(n_c)
    fig,ax = p.subplots()
    bar = p.bar(nc,freq)
    x = n.linspace(min(n_c),max(n_c),1000)
    phi = p.plot(x,mlab.normpdf(x,mean+0.5,sd),color = 'r')
    p.title('Frequency density of n for radius = %s'%radius)
    p.xlabel('n')
    p.ylabel('Frequency density')
    p.show()
    return mean,sd

def nc_mean(start,finish,N,dimension):
    r = n.linspace(start,finish,N)
    n_c = []
    mean_n = []
    for i in range(len(r)):
        n_c.append(p_e.cr_density_calc(r[i],dimension))
        mean_n.append(sum(n_c)/(i+1))
    p.plot(r,mean_n)
    p.show()

def nc(start,finish,N,iterations,dimension):
    r = n.linspace(start,finish,N)
    t = lambda x:sum(x)/len(x)
    n_c = []
    for i in r:
        n_c.append(p_e.min_disks(i,dimension)[0])
#        n_c.append(p_e.mean_density_r(i,iterations,dimension))        
    p.plot(r,n_c)
    x = t(n_c)
    p.plot(r,[x for i in range(len(n_c))])
    p.xlabel('Radius')
    p.ylabel('nc')
    p.title('Critical density against radius')
    p.show()
    return t(n_c)

print(nc(0.05,0.1,10,1,3))
