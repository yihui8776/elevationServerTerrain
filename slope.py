import os
import numpy as np
from osgeo import gdal

def make_slices(data,win_size):
    rows = data.shape[0] - win_size[0] +1
    cols = data.shape[1] - win_size[1]+1
    slices = []
    for i in range(win_size[0]):
        for j in range(win_size[1]):
            slices.append(data[i:rows+i,j:cols+j])
    return slices

def save_raster(input_data, out_file,output_data,data_type,nodata=None):
    driver = gdal.GetDriverByName('GTiff')
    dataset = driver.Create(out_file, input_data.RasterXSize, input_data.RasterYSize, 1, data_type)
    im_proj = input_data.GetProjection()
    im_geotrans = input_data.GetGeoTransform()
    dataset.SetGeoTransform(im_geotrans)
    dataset.SetProjection(im_proj) 
    dataset.GetRasterBand(1).WriteArray(output_data)
    return dataset
 
dem = "data/fujian125/fujian125_0_0.tif"
out_tif = "data/slope.tif"

dem_ds = gdal.Open(dem)
cell_width = dem_ds.GetGeoTransform()[1]
cell_height = dem_ds.GetGeoTransform()[5]
band = dem_ds.GetRasterBand(1)
in_data = band.ReadAsArray().astype(np.float)
out_data = np.ones((band.YSize, band.XSize)) * -99 

slices = make_slices(in_data,(3,3))
rise= ((slices[6] + (2 *slices[7]) + slices[8])- (slices[0]+(2*slices[1])+slices[2]))/(8*cell_height)
run = ((slices[2] + (2*slices[5])+slices[8])-(slices[0]+(2*slices[3])+slices[6]))/ (8*cell_width)
dist = np.sqrt(np.square(rise)+np.square(run))
out_data[1:-1,1:-1] = np.arctan(dist)*180/np.pi

save_raster(dem_ds,out_tif,out_data,gdal.GDT_Float32,-99)
del dem_ds