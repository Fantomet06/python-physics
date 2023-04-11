import numpy as np

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
#%matplotlib inline

from astropy.io import fits
from astropy.utils.data import download_file

image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True)

#print("\n")

image_data = fits.getdata(image_file)
print(image_data.shape)

plt.imshow(image_data, cmap='gray', norm=LogNorm())
plt.colorbar()
plt.show()