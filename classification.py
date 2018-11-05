'''
Created on 3 Nov. 2018

@author: Michael
'''
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt


import math

def mean(vals):
    m = []
    length = len(vals)
    for band in vals:
        sum = 0
        for val in band:
            sum = sum + val
        sum = float(sum) / length
        m.append(sum)
    return m

def dist(arr1, arr2):
    diff = []
    for i in range(len(arr1)):
        diff.append(abs(arr1[i]-arr2[i]))
    diffsq = []
    for i in diff:
        diffsq.append(i*i)
    diffsqsum = 0
    for i in diffsq:
        diffsqsum = diffsqsum + i
    
    return math.sqrt(diffsqsum)

def nDimProb(point, classesMeanStd):
    probabilities = []
    dims = len(point)
    for mean, std in classesMeanStd:
        prob = []
        for i in range(dims):
            expon = (-1.0/2.0)*((point[i]-mean[i])/std[i])*((point[i]-mean[i])/std[i])
            calc = (1.0/(std[i]*math.sqrt(2.0*math.pi)))*math.exp(expon)
            prob.append(calc)
        m = prob[0]
        for i in range(1,len(prob)):
            m = m*prob[i]
        probabilities.append(m)
    return probabilities

    
def getMinClass(vals):
    gmin = 999999999999
    classification = 0
    for i in range(len(vals)):
        if vals[i] < gmin:
            gmin = vals[i]
            classification = i
    return classification

def getMaxClass(vals):
    gmax = 0
    classification = 0
    for i in range(len(vals)):
        if vals[i] > gmax:
            gmax = vals[i]
            classification = i
    return classification
    
classA  = [
    [20,19,21,23,17,25,19,20],
    [10,11,8,14,12,8,13,7],
    [40,49,35,36,50,33,46,37],
    [101,89,100,90,82,93,80,96],
    ]

classB = [
    [50,49,45,51,43,46,57,55,48],
    [81,76,80,84,90,85,88,79,70],
    [101,111,90,86,130,100,99,124,131],
    [30,31,27,38,33,30,39,32,33],
    ]

pixel1 = [28,10,52,146]
pixel2 = [50,70,97,20]

if __name__ == '__main__':
    print("Starting Classification")
    
    plt.scatter(classA[2],classA[3],label="ClassA", color="r")
    plt.scatter(classB[2],classB[3],label="ClassB", color="b")
    plt.scatter([pixel1[2]],[pixel1[3]],label="Pixel1", color="y")
    plt.scatter([pixel2[2]],[pixel2[3]],label="Pixel2", color="g")
    plt.title("Classification of Stuff")
    plt.xlabel("Band 3")
    plt.ylabel("Band 4")
    plt.savefig("Band3-Band4.png")
    print("Saving Figure Band3-Band4.png")
    plt.close()
    
    plt.scatter(classA[0],classA[1],label="ClassA", color="r")
    plt.scatter(classB[0],classB[1],label="ClassB", color="b")
    plt.scatter([pixel1[0]],[pixel1[1]],label="Pixel1", color="y")
    plt.scatter([pixel2[0]],[pixel2[1]],label="Pixel2", color="g")
    plt.title("Classification of Stuff")
    plt.xlabel("Band 1")
    plt.ylabel("Band 2")
    plt.savefig("Band1-Band2.png")
    print("Saving Figure Band1-Band2.png")
    plt.close()
    
    meanA = mean(classA)
    meanB = mean(classB)
    
    print("Starting Minimum distance classification: \n")
    
    print("Means ClassA: "+str(meanA))
    print("Means ClassB: "+str(meanB))
    
    distPixel1 = [dist(pixel1,meanA), dist(pixel1,meanB)]
    distPixel2 = [dist(pixel2,meanA), dist(pixel2,meanB)]
    
    print("Distance Pixel1: "+str(distPixel1))
    print("Distance Pixel2: "+str(distPixel2))
    
    minClass = getMinClass(distPixel1)
    if(minClass==0):
        print("Pixel 1 is ClassA")
    elif(minClass==1):
        print("Pixel 1 is ClassB")
    else:
        print("WTF Pixel1")
    
    minClass = getMinClass(distPixel2)
    if(minClass==0):
        print("Pixel 2 is ClassA")
    elif(minClass==1):
        print("Pixel 2 is ClassB")
    else:
        print("WTF Pixel2")
            
    print("\n\n")
    print("Starting Maximum Likelihood classification: \n")
    
    stdevA = []
    for band in classA:
        stdevA.append(np.std(band))
        
    print("Means  ClassA:  "+str(meanA))
    print("Stdevs ClassA: "+str(stdevA))
    
    stdevB = []
    for band in classB:
        stdevB.append(np.std(band))
        
    print("Means  ClassB:  "+str(meanB))
    print("Stdevs ClassB: "+str(stdevB))
    
    classesMeanStd = [(meanA,stdevA),(meanB,stdevB)]
    print("\n")
    
    pixel1classdensity = nDimProb(pixel1, classesMeanStd)
    pixel2classdensity = nDimProb(pixel2, classesMeanStd)
    
    maxClass = getMaxClass(pixel1classdensity)
    if(maxClass==0):
        print("Pixel 1 is ClassA")
    elif(maxClass==1):
        print("Pixel 1 is ClassB")
    else:
        print("WTF Pixel1")
    
    maxClass = getMaxClass(pixel2classdensity)
    if(maxClass==0):
        print("Pixel 2 is ClassA")
    elif(maxClass==1):
        print("Pixel 2 is ClassB")
    else:
        print("WTF Pixel2")
    
    print("\n\nFinished Process")
    
    