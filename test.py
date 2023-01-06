from osgeo import gdal
import sys
import richdem as rd

def Read_img2array(img_file_path):
    
    dataset = gdal.Open(img_file_path)  
    print('all raster count', dataset.RasterCount)
     
    if dataset is None:
        print('Unable to open *.tif')
        sys.exit(1)  
    projection = dataset.GetProjection()   
    geotrans = dataset.GetGeoTransform()   
    im_width = dataset.RasterXSize  
    im_height = dataset.RasterYSize  
    im_bands = dataset.RasterCount  
    
    img_array = dataset.ReadAsArray()
    return im_width,im_height,im_bands,projection, geotrans, img_array 
    
file_path = "data/fujian125/fujian125_0_0.tif"

im_width,im_height,im_bands,projection, geotrans, img_array  =  Read_img2array(file_path)

print('width,height:',im_width,im_height)
print('bands:',im_bands)
print('projection:',projection)
print('geotrans:',geotrans)

dem = rd.LoadGDAL(file_path)
aspect = rd.TerrainAttribute(dem, attrib='aspect')
slope = rd.TerrainAttribute(dem, attrib='slope_riserun')
print('aspect:',aspect)
print('slope:',slope)

