# Author: David Monk
# Project: Percolation modelling

import numpy as n
import math as m
from random import random as rand


class cluster:
    def __init__(self,disks,radius,dimension):
        self.radius = radius
        self.disks = n.array(disks)
        self.bounds = tuple([(n.amin(self.disks,axis=0)[i] - self.radius, n.amax(self.disks,axis=0)[i] + self.radius) for i in range(dimension)])
        self.connection = False
        self.contained = True
        for i in range(len(self.bounds)):
            if self.bounds[i][0] < 0 and self.bounds[i][1] > 1:
                self.connection = True
        for i in range(len(self.bounds)):
            if self.bounds[i][0] < 0 or self.bounds[i][1] > 1:
                self.contained = False
        
        
def cluster_check(disk,array,radius,dimension):
    c = []
    if disk in array:
        array.remove(disk)
    for i in array:
        if m.sqrt(sum([pow(i[j]-disk[j],2) for j in range(dimension)])) < 2*radius:
            c.append(i)
    if len(c) == 0:
        return [disk]
    else:
        c_t = c
        for i in c:
            c_n = cluster_check(i,array,radius,dimension)
            for j in c_n:
                if j not in c_t:
                    c_t.append(j)
        for i in c_t:
            if i not in c:
                c.append(i)
        c.append(disk)
        return c

def cluster_finder(array,radius,dimension):
    clusters=[]
    while len(array)>0:
        c = cluster_check(array[0],array,radius,dimension)
        for j in c:
            if j in array:
                array.remove(j)
        clusters.append(cluster(c,radius,dimension))
    return clusters

def disk_gen(N,dimension):
    R = [tuple([rand() for j in range(dimension)]) for i in range(N)] 
    return R
