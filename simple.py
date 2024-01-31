# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 17:39:24 2024

@author: David
"""

from astropy.io import fits
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit
from scipy.interpolate import CubicSpline
from scipy.interpolate import lagrange
from scipy import ndimage
from scipy.optimize import minimize
from scipy.ndimage import median_filter
import random

def gaussian(x, μ, σ, A):
   return (A / (σ * np.sqrt(2 * np.pi))) * np.exp(-((x - μ) ** 2) / (2 * σ** 2))

ZPinst = 2.530e+01
# hdulist = fits.open("Fits_Data\mosaic.fits")
# data = hdulist[0].data
# header = hdulist[0].header
# data_trans = np.transpose(data)
# data_minus_background = data

# cropped_value = 120
# cropped_image = data[cropped_value:4611-cropped_value,cropped_value:2570-cropped_value]

# height = len(cropped_image)
# width = len(cropped_image[0])

# binary_check = np.zeros((height,width))
# for i in range(height):
#     for j in range(width):
#         if data[i][j] > 3425:
#             binary_check[i][j] = 1            

# s = [[0,1,0],
#       [1,1,1],
#       [0,1,0]]

# labeled_data, num_features = ndimage.label(binary_check,s)
# print(num_features)
# labeled_areas = np.array(ndimage.sum(binary_check, labeled_data, np.arange(labeled_data.max()+1)))
# mask1 = labeled_areas > 50
# remove_small_area = mask1[labeled_data.ravel()].reshape(labeled_data.shape)

# final_labeled_data, num_features = ndimage.label(remove_small_area,s)
# print(num_features)
# labeled_areas = np.array(ndimage.sum(binary_check, final_labeled_data, np.arange(final_labeled_data.max()+1)))

# '''Replace this with a lower value at some point.'''
# mask2 = labeled_areas < 1000
# remove_large_area = mask2[big_labeled_data.ravel()].reshape(big_labeled_data.shape)

# final_labeled_data, num_features = ndimage.label(remove_large_area,s)
# print(num_features)

# background = np.zeros((height,width))
# for i in range(height):
#     xp =  np.array([])
#     fp = np.array([])
#     for j in range(width):
#         if binary_check[i][j] == 0:
#             background[i][j] = data[i][j]
#             xp = np.append(xp,j)
#             fp= np.append(fp,background[i][j])
#     for j in range(width):
#         if binary_check[i][j] != 0:
#             background[i][j] = np.interp(j,xp,fp)

# blurred = ndimage.median_filter(background, size=20)

# hdubackground = fits.open("Fits_Data\\background.fits", mode='update')

# plt.imshow(blurred)
# plt.show()

# hdubackground[0].data = blurred
# hdubackground.close()

# plt.hist(blurred.flatten())
# plt.title("Histogram of fits background values")
# plt.xlabel("Fits value")
# plt.ylabel("Count")
# plt.show()

# image = cropped_image - blurred
# plt.imshow(image)
# plt.show()

# plt.hist(image.flatten(),bins=50)
# plt.title("Histogram of fits background values")
# plt.xlabel("Fits value")
# plt.ylabel("Count")
# plt.show()

# fig, axes = plt.subplots(figsize=(10,6))
# hist_zoom, bins_zoom = np.histogram(image.flatten(),150, range=(-200,200))
# width_zoom = 0.7 * (bins_zoom[1] - bins_zoom[0])
# center_zoom = (bins_zoom[:-1] + bins_zoom[1:]) / 2
# plt.bar(center_zoom, hist_zoom, align='center', width=width_zoom, label = 'Histogram')

# x_data = center_zoom
# y_data = hist_zoom
# popt, pcov = curve_fit(gaussian, x_data, y_data, p0=(0,20,1e6))
# mu_fit, sd_fit, A_fit = popt
# y_fit = gaussian(x_data, mu_fit, sd_fit, A_fit)
# plt.plot(x_data, y_fit, 'r', label='Gaussian Fit')
# plt.xlabel('Count (Fits Value)',size=20)
# plt.ylabel('Frequency',size=20)
# plt.title('Histogram of pixel brightness count', size=24)
# plt.legend(loc='upper right',fancybox=True, shadow=True, prop={'size': 18})
# plt.xticks(size=18,color='#4f4e4e')
# plt.yticks(size=18,color='#4f4e4e')
# # sns.set(style='whitegrid')
# plt.show()

# print(*popt)

# binary_check_2 = np.zeros((height,width))
# for i in range(height):
#     for j in range(width):
#         if image[i][j] > 3*popt[1]:
#             binary_check[i][j] = 1            

# s = [[0,1,0],
#       [1,1,1],
#       [0,1,0]]

# labeled_data, num_features = ndimage.label(binary_check,s)
# print(num_features)
# labeled_areas = np.array(ndimage.sum(binary_check, labeled_data, np.arange(labeled_data.max()+1)))
# mask1 = labeled_areas > 122
# remove_small_area = mask1[labeled_data.ravel()].reshape(labeled_data.shape)

# final_labeled_data, num_features = ndimage.label(remove_small_area,s)
# print(num_features)

'''NEED TO FIND A WAY TO REMOVE STARS HERE'''

# counts = np.zeros(num_features+1)
# counts[0] = 1
# for i in range(height):
#     for j in range(width):
#         feature = final_labeled_data[i][j]
#         if feature==0:
#             pass
#         else:
#             counts[feature] = counts[feature] + image[i][j]

print(counts)

mag_i = -2.5*np.log10(counts/720)
print(mag_i)

m = mag_i + ZPinst
print(m)

plt.hist(m)
plt.show()

m_hist, bins= np.histogram(m,100,range=(0,35))
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2

N_m = np.cumsum(m_hist)

plt.plot(center,np.log10(N_m),)
plt.plot(center,0.6*center-6)
plt.show()