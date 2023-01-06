# Public API Documentation

原始高程服务的 Open-Elevation's API 比较简单，基于python 的bottle框架，在config文件修改endpoint和data-folder即可
只用单个服务文件 server.py
返回的是高程
   
## `GET /api/v1/lookup`

返回 ("looks up")在一个或多个坐标点经纬度 `(latitude,longitude)` 的高程，即海拔高度；

GET API 参数限制 **1024** bytes. 如果请求量大可以使用 POST api.

### 参数:

* **`locations`**: 地点列表, 由`|` 分割 `latitude, longitude` 格式, 和 Google Elevation API 比较类似.

### 返回格式 

一个返回结果列表的json对象， `results` 里为结果，. 包括 `latitude`, `longitude` 和 `elevation`. 为经度，纬度和高程。 **高程单位是米**.

如果是海平面（海拔为0米）则没有返回记录。
 
```json
{
	"results":
	[
		{
			"latitude": ...,
			"longitude": ...,
			"elevation": ...
		},
		...
	]
}
```


### Example:

#### Request

```
curl 'https://api.open-elevation.com/api/v1/lookup?locations=10,10|20,20|41.161758,-8.583933'
```

#### Response

```json
{
   "results":
   [
      {
         "longitude":10.0,
         "elevation":515,
         "latitude":10.0
      },
      {
         "longitude":20.0,
         "elevation":545,
         "latitude":20.0
      },
      {
         "latitude":41.161758,
         "elevation":117,
         "longitude":-8.583933
      }
   ]
}
```


## `POST /api/v1/lookup`

返回一个或多个坐标点`(latitude,longitude)` 的 ("looks up") 高程    .

POST API  无限制

### Parameters:

*  JSON (and respective headers) 按以下格式:
```
{
    "locations":
    [
        {
            "latitude": ...,
            "longitude": ...
        },
        ...
}
```


### Response format

结果列表的JSON对象,   `results` 字段是返回结果. 每个包括 `latitude`, `longitude` 和 `elevation`. 为经度，纬度和高程。 **高程单位是米**
如果是海平面（海拔为0米）则没有返回记录。

```json
{
	"results":
	[
		{
			"latitude": ...,
			"longitude": ...,
			"elevation": ...
		},
		...
	]
}
```


### Example:

#### Request

```
curl -X POST \
  https://api.open-elevation.com/api/v1/lookup \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
	"locations":
	[
		{
			"latitude": 10,
			"longitude": 10
		},
		{
			"latitude":20,
			"longitude": 20
		},
		{
			"latitude":41.161758,
			"longitude":-8.583933
		}
	]

}'
```

#### Response

```json
{
   "results":
   [
      {
         "longitude":10.0,
         "elevation":515,
         "latitude":10.0
      },
      {
         "longitude":20.0,
         "elevation":545,
         "latitude":20.0
      },
      {
         "latitude":41.161758,
         "elevation":117,
         "longitude":-8.583933
      }
   ]
}
```

坡度API

使用类似高程API
## `GET /api/v1/getSlope`   
## `POST /api/v1/getSlope` 

例如 http://172.18.137.96:8282/api/v1/getSlope?locations=27.834,118.629

坡向API

## `GET /api/v1/getAspect`   
## `POST /api/v1/getAspect` 


例如 http://172.18.137.96:8282/api/v1/getAspect?locations=27.834,118.629