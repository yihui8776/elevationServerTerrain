栅格数据存放路径

可以通过download-srtm-data.sh下载

也可以自己下载tif栅格文件 

这里取用网上12.5米的福建高程数据，经过分割成多个块，

坡度和坡向使用arcgis或Google earth进行转换，

栅格文件可以通过create-tiles.sh分割为多个小文件

如 ../create-tiles.sh   fujian125.tif 10 10
