# Food Advisor API v1

- [概述](#概述)
  - [架构](#架构)
  - [身份认证](#身份认证)
  - [HTTP动词](#HTTP动词)
  - [参数](#参数)
  - [分页](#分页)
- [1.用户](#1用户)
  - [1.1 用户注册](#11用户注册)
  - [1.2 用户登录](#12用户登录)
  - [1.3 校验令牌](#13校验令牌)
  - [1.4 获取用户信息](#14获取用户信息)
  - [1.5 获取经过身份验证用户的信息](#15获取经过身份验证用户的信息)
  - [1.6 获取用户收藏餐厅](#16获取用户收藏餐厅)
  - [1.7 更新用户信息](#17更新用户信息)
  - [1.8 删除用户](#18删除用户)
- [2.食堂](#2食堂)
  - [2.1 列出单个校区的食堂](#21列出单个校区的食堂)
  - [2.2 获取食堂信息](#22获取食堂信息)
  - [2.3 新增食堂](#23新增食堂)
  - [2.4 更新食堂信息](#24更新食堂信息)
  - [2.5 删除食堂](#25删除食堂)
- [3.餐厅](#3餐厅)
  - [3.1 列出单个食堂的餐厅](#31列出单个食堂的餐厅)
  - [3.2 获取餐厅信息](#32获取餐厅信息)
  - [3.3 新增餐厅](#33新增餐厅)
  - [3.4 更新餐厅信息](#34更新餐厅信息)
  - [3.5 删除餐厅](#35删除餐厅)
- [4.食品](#4食品)
  - [4.1 列出单个餐厅的食品](#41列出单个餐厅的食品)
  - [4.2 获取食品信息](#42获取食品信息)
  - [4.3 新增食品](#43新增食品)
  - [4.4 更新食品信息](#44更新食品信息)
  - [4.5 删除食品](#45删除食品)
- [5.评论](#5评论)
  - [5.1 列出单个餐厅的评论](#51列出单个餐厅的评论)
  - [5.2 列出单个用户的评论](#52列出单个用户的评论)
  - [5.3 获取评论信息](#53获取评论信息)
  - [5.4 新增评论](#54新增评论)
  - [5.5 更新评论](#55更新评论)
  - [5.6 删除评论](#56删除评论)
- [6.查询](#6查询)
  - [6.1 查询餐厅](#61查询餐厅)
  - [6.2 查询食品](#62查询食品)
  - [6.3 查询评论](#63查询评论)
  - [6.4 查询用户](#64查询用户)

## 概述
### 架构
所有API访问均通过HTTPS进行访问。所有数据都以JSON的形式发送和接收。

所有API均以`api.foodadvisor.top/v1`开头：
```
api.foodadvisor.top/v1
```

### 身份认证
Food Advisor API采用`HTTP Basic Authentication`进行身份认证，请在`HTTP Header`中设置：
```http
Authentication: Basic base64Encoded(username:password)
```
其中，`username`为用户的身份令牌token，`password`留空。

### HTTP动词
请为每个请求选取恰当的HTTP动词。

|动词      |描述                 |
|:-------:|:--------------------|
|`GET`    |用于获取资源          |
|`POST`   |用于新增资源          |
|`PUT`    |用于更新或替换资源     |
|`PATCH`  |用于更新资源的部分信息 |
|`DELETE` |用于删除资源          |

### 参数

不包含在URL中的参数应当被编码为`JSON`格式,并在`HTTP Header`中设置：
```http
Content-Type: application/json
```

### 分页
对于返回多条结果的请求，默认返回第一页的20个结果。可以通过`page`指定页数，`per_page`指定页面大小，例如:
```
http://api.foodadvisor.top/v1/restraunt/1/reviews?page=2&per_page=50
```
请注意，页码编号是从1开始的。

## 1. 用户
### 1.1用户注册
 
```
POST /user
```

#### 参数

|名称|类型|描述|
|:-----:|:-----|:-----|
|account   |string  |**必填。** 账号名称|
|secret    |string  |**必填。** 注册密码|
|type      |integer |**必填。** <br> `100` 邮箱注册 <br> `101`手机号注册|
|nickname  |string  |**邮箱注册时必填。** |

#### 示例
```json
{
  "account": "example@gmail.com",
  "secret": "QOA12D2X3",
  "type": 100,
  "nickname": "Ann"
}
```

#### 响应
```json
Status: 200 OK

{
    "error_code": 0,
    "message": "OK",
    "request_url": "POST /v1/user"
}
```

### 1.2用户登录
成功登录后可获取唯一的身份标识。

```
POST /token/auth
```

#### 参数

|名称|类型|描述|
|:-----:|:-----|:-----|
|account   |string  |**必填。** 账号|
|secret    |string  |**必填。** 密码|
|type      |integer |**必填。** <br> `100` 邮箱登录 <br> `101`手机号登录|

#### 示例
```json
{
  "account": "123456@qq.com",
  "secret": "123456",
  "type": 100
}
```

#### 响应
```json
Status: 201 Created

{
    "token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU0Nzk4NTkxNSwiZXhwIjoxNTQ3OTkzMTE1fQ.eyJ1aWQiOjksInR5cGUiOjEwMCwic2NvcGUiOjF9.crX5pEtGWhj2SH73qhgLeV3rnY-QWbv6qJzqS82rsqPuw0W09m8TNkAsQZ_mTmu5ylwbPSd0xLEOhyRTKqdH_w"
}
```

### 1.3校验令牌
 
```
POST /token/secret
```

#### 参数

|名称|类型|描述|
|:-----:|:-----|:-----|
|token     |string  |**必填。** 用户的令牌|


#### 示例
```json
{
    "token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU0Nzk4NTkxNSwiZXhwIjoxNTQ3OTkzMTE1fQ.eyJ1aWQiOjksInR5cGUiOjEwMCwic2NvcGUiOjF9.crX5pEtGWhj2SH73qhgLeV3rnY-QWbv6qJzqS82rsqPuw0W09m8TNkAsQZ_mTmu5ylwbPSd0xLEOhyRTKqdH_w"
}
```

#### 响应
```json
Status: 200 OK

{
    "create_at": 1547985915,
    "expire_in": 1547993115,
    "scope": 1,
    "uid": 9
}
```

### 1.4获取用户信息
获取用户的公开信息
```
GET /uesr/:user_id
```

#### 响应
```json
Status: 200 OK

{
    "avatar": null,
    "email": "example@gmail.com",
    "id": 16,
    "mobile": "17716805432",
    "nickname": "Ann"
}
```

### 1.5获取经过身份验证用户的信息
获取用户的公开信息和私人信息
**注意**：仅对通过身份认证的`用户`有效
```
GET /uesr
```

#### 响应
```json
Status: 200 OK

{   
    "auth": 1,
    "avatar_url": null,
    "email": "example@gmail.com",
    "id": 16,
    "mobile": "17716805432",
    "nickname": "Ann"
}
```

### 1.6获取用户收藏餐厅
**注意**：仅对通过身份认证的`用户`有效
```
GET /uesr/restaurant
```

#### 响应
```json
Status: 200 OK

[
    {
        "canteen_id": 1,
        "create_time": 1551430660,
        "grade": 5,
        "id": 1,
        "images": [],
        "introduction": "sdfsfsf",
        "name": "sefsafsf",
        "review_amount": 434
    },
    {
        "canteen_id": 1,
        "create_time": 1551430660,
        "grade": 5,
        "id": 2,
        "images": [],
        "introduction": "sdfsfsf",
        "name": "sefsafsf",
        "review_amount": 434
    }
]
```

### 1.7更新用户信息
**注意**：仅对通过身份认证的`用户`有效
```
PUT /uesr
```
#### 参数

|名称       |类型    |描述                   |
|:---------:|:------|:----------------------|
|nickname   |string | **选填。** 用户的昵称  |
|mobile     |string | **选填。** 用户的手机号|
|email      |string | **选填。** 用户的邮箱  |

#### 示例
```json
{
    "nickname":"中道",
    "mobile":"15967542312",
    "email":"12345678@163.com"
}
```

#### 响应
```json
Status: 202 Accepted

{  
    "error_code": 0,
    "message": "Updated",
    "request_url": "PUT /v1/uesr"
}
```

### 1.8删除用户
**注意**：仅对通过身份认证的`用户`有效
```
DELETE /uesr
```

#### 响应
```json
Status: 202 Accepted

{  
    "error_code": 0,
    "message": "Deleted",
    "request_url": "DELETE /v1/uesr"
}
```

## 2. 食堂
### 2.1列出单个校区的食堂
```
GET /campus/:campus_id/canteens
```

#### 响应
```json
Status: 200 OK

[
    {
        "campus_id": 1,
        "review_amount": 0,
        "create_time": 1549957033,
        "grade": 0,
        "id": 1,
        "images": [
            {
                "id": 1,
                "url": "http://api.foodadvisor.top/food_seeker/images/20190212/2f46051c2e9811e9aaf754ee75dc7dce.jpg"
            }
        ],
        "introduction": "没有介绍",
        "location": "东区教超旁边",
        "name": "第四食堂"
    },
    {
        "campus_id": 1,
        "review_amount": 0,
        "create_time": 1549957033,
        "grade": 0,
        "id": 1,
        "images": [
            {
                "id": 1,
                "url": "http://api.foodadvisor.top/food_seeker/images/20190212/2f46051c2e9811e9aaf754ee75dc7dce.jpg"
            }
        ],
        "introduction": "没有介绍",
        "location": "东区教超旁边",
        "name": "第五食堂"
    }
]
```

### 2.2获取食堂信息
```
GET /canteen/:canteen_id
```

#### 响应
```json
Status: 200 OK

{
    "campus_id": 1,
    "review_amount": 0,
    "create_time": 1549957033,
    "grade": 0,
    "id": 1,
    "images": [
        {
            "id": 1,
            "url": "http://api.foodadvisor.top/food_seeker/images/20190212/2f46051c2e9811e9aaf754ee75dc7dce.jpg"
        }
    ],
    "introduction": "没有介绍",
    "location": "东区教超旁边",
    "name": "第四食堂"
}
```

### 2.3新增食堂

**注意**：仅对通过身份认证的`管理员`有效

```
POST /canteen
```

#### 参数

|名称         |类型    |描述                   |
|:-----------:|:------|:----------------------|
|name         |string | **必填。** 食堂名称    |
|introduction |string | **选填。** 食堂介绍    |
|location     |string | **必填。** 食堂位置    |
|campus_id    |integer| **必填。** 食堂所在校区编号|
|image_amount |integer| **必填。** 上传图片总数    |
|image        |file   | **必填。** 食堂图片    |

#### 示例
```http
POST /v1/canteen HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: multipart/form-data; boundary=7MA4YWxkTrZu0gW
Authorization: Basic ZXlKaGJHY2lPaUpJVXpVeE1pSXNJbWxoZENJNk1UVTBPRFkxTkRneE15d2laWGh3SWpveE5UVXhNalEyT0RFemZRLmV5SjFhV1FpT2pFMkxDSjBlWEJsSWpveE1EQXNJbk5qYjNCbElqb3lmUS5HOU14c2QtSm43cTFRTWY0eUx1a1B0elY0eUJmV2RKUURmSWRId2NraUJJa1BnN0lXRHVZWUtIOU55ZFMzeDZtMnp4cWEzaWpBYThaRzJPSFdGVWtuUTo=
cache-control: no-cache

--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="name"

第四食堂

--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="introduction"

这是食堂介绍

--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="location"

东校区教超旁边

--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="campus_id"

1

--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="image_amount"

2

--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="image-1"; filename="C:\Users\lenovo\Desktop\github_release.png


--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="image-2"; filename="C:\Users\lenovo\Desktop\github_release.png


--7MA4YWxkTrZu0gW--
```

#### 响应
```json
Status: 201 Created

{
    "error_code": 0,
    "message": "Created",
    "request_url": "POST /v1/canteen"
}
```
### 2.4更新食堂信息

**注意**：仅对通过身份认证的`管理员`有效

```
PUT /canteen/:canteen_id
```
#### 参数

|名称         |类型    |描述                   |
|:-----------:|:------|:----------------------|
|name         |string | **选填。** 食堂名称    |
|introduction |string | **选填。** 食堂介绍    |
|location     |string | **选填。** 食堂位置    |
|campus_id    |integer| **选填。** 食堂所在校区编号|

#### 示例
```json
{
    "name": "第5食堂"
}
```
#### 响应
```json
Status: 202 Accepted

{
    "error_code": 0,
    "message": "Updated",
    "request_url": "PUT /v1/canteen/1"
}
```
### 2.5删除食堂
```
DELETE /canteen/:canteen_id
```

#### 响应
```json
Status: 202 Accepted

{
    "error_code": 0,
    "message": "Deleted",
    "request_url": "DELETE /v1/canteen/1"
}
```

## 3. 餐厅
### 3.1列出单个食堂的餐厅
```
GET /canteen/:canteen_id/restaurants
```

#### 响应
```json
Status: 200 OK

[
    {
        "canteen_id": 1,
        "review_amount": 0,
        "create_time": 1549957256,
        "grade": 0,
        "id": 1,
        "images": [
            {
                "id": 1,
                "url": "http://api.foodadvisor.top/food_seeker/images/20190212/2f46051c2e9811e9aaf754ee75dc7dce.jpg"
            }
        ],
        "introduction": "很好",
        "name": "汤哥特色风味"
    },
    {
        "canteen_id": 1,
        "review_amount": 0,
        "create_time": 1549957256,
        "grade": 0,
        "id": 2,
        "images": [
            {
                "id": 1,
                "url": "http://api.foodadvisor.top/images/20190212/2f46051c2e9811e9aaf754ee75dc7dce.jpg"
            }
        ],
        "introduction": "很好",
        "name": "汤哥特色风味"
    }
]
```

### 3.2获取餐厅信息
```
GET /restaurant/:restaurant_id
```

#### 响应
```json
Status: 200 OK

{   
    "canteen_id": 1,
    "review_amount": 0,
    "create_time": 1549957256,
    "grade": 0,
    "id": 1,
    "images": [
        {
            "id": 1,
            "url": "E:/food_seeker/images/20190212/2f46051c2e9811e9aaf754ee75dc7dce.jpg"
        }
    ],
    "introduction": "很好",
    "name": "汤哥特色风味"
}
```
### 3.3新增餐厅

**注意**：仅对通过身份认证的`管理员`有效

```
POST /restaurant
```

#### 参数

|名称         |类型    |描述                   |
|:-----------:|:------|:----------------------|
|name         |string | **必填。** 餐厅名称    |
|introduction |string | **必填。** 餐厅介绍    |
|canteen_id   |integer| **必填。** 餐厅所在食堂编号 |
|image_amount |string | **必填。** 餐厅图片总数|
|image        |file   | **必填。** 餐厅图片    |

#### 示例
```http
POST /v1/restaurant HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: multipart/form-data; boundary=7MA4YWxkTrZu0gW
Authorization: Basic ZXlKaGJHY2lPaUpJVXpVeE1pSXNJbWxoZENJNk1UVTBPRFkxTkRneE15d2laWGh3SWpveE5UVXhNalEyT0RFemZRLmV5SjFhV1FpT2pFMkxDSjBlWEJsSWpveE1EQXNJbk5qYjNCbElqb3lmUS5HOU14c2QtSm43cTFRTWY0eUx1a1B0elY0eUJmV2RKUURmSWRId2NraUJJa1BnN0lXRHVZWUtIOU55ZFMzeDZtMnp4cWEzaWpBYThaRzJPSFdGVWtuUTo=
cache-control: no-cache

--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="name"

汤哥特色风味

--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="introduction"

这是食堂窗口的介绍

--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="location"

第四食堂

--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="canteen_id"

1

--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="image_amount"

2

--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="image-1"; filename="C:\Users\lenovo\Desktop\github_release.png


--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="image-2"; filename="C:\Users\lenovo\Desktop\github_release.png


--7MA4YWxkTrZu0gW--
```

#### 响应
```json
Status: 201 Created

{
    "error_code": 0,
    "message": "Created",
    "request_url": "POST /v1/restaurant"
}
```

### 3.4更新餐厅信息

**注意**：仅对通过身份认证的`管理员`有效

```
PUT /restaurant/:restaurant_id
```
#### 参数

|名称         |类型    |描述                   |
|:-----------:|:------|:----------------------|
|name         |string | **选填。** 餐厅名称    |
|introduction |string | **选填。** 餐厅介绍    |
|canteen_id   |integer| **选填。** 餐厅所在食堂编号|

#### 示例
```json
{
    "name": "汤哥特色风味"
}
```

#### 响应
```json
Status: 202 Accepted

{
    "error_code": 0,
    "message": "Updated",
    "request_url": "PUT /v1/restaurant/1"
}
```
### 3.5删除餐厅

**注意**：仅对通过身份认证的`管理员`有效

```
DELETE /restaurant/:restaurant_id
```

#### 响应
```json
Status: 202 Accepted

{
    "error_code": 0,
    "message": "Deleted",
    "request_url": "DELETE /v1/restaurant/1"
}
```

## 4. 食品
### 4.1列出单个餐厅的食品
```
GET /restraunt/:restraunt_id/foods
```

#### 响应
```json
Status: 200 OK

[
    {
        "review_amount": 0,
        "create_time": 1549957632,
        "grade": 0,
        "id": 1,
        "images": [
            {
                "id": 1,
                "url": "http://foodadvisor.top/food_seeker/images/20190212/2f46051c2e9811e9aaf754ee75dc7dce.jpg"
            }
        ],
        "introduction": "",
        "name": "椒盐排条",
        "price": 15,
        "restaurant_id": 1
    },
    {
        "review_amount": 0,
        "create_time": 1549957632,
        "grade": 0,
        "id": 2,
        "images": [
            {
                "id": 1,
                "url": "http://foodadvisor.top/food_seeker/images/20190212/2f46051c2e9811e9aaf754ee75dc7dce.jpg"
            }
        ],
        "introduction": "",
        "name": "椒盐排条",
        "price": 15,
        "restaurant_id": 1
    }
]
```

### 4.2获取食品信息
```
GET /food/:food_id
```

#### 响应
```json
Status: 200 OK

{
    "review_amount": 0,
    "create_time": 1549957632,
    "grade": 0,
    "id": 1,
    "images": [
        {
            "id": 1,
            "url": "http://foodadvisor.top/food_seeker/images/20190212/2f46051c2e9811e9aaf754ee75dc7dce.jpg"
        }
    ],
    "introduction": "",
    "name": "椒盐排条",
    "price": 15,
    "restaurant_id": 1
}
```
### 4.3新增食品

**注意**：仅对通过身份认证的`管理员`有效

```
POST /food
```
#### 参数

|名称           |类型    |描述                   |
|:------------:|:-------|:----------------------|
|restaurant_id |integer | **必填。** 食品所在餐厅编号  |
|name          |string  | **必填。** 食品名称    |
|introduction  |string  | **必填。** 食品介绍    |
|price         |float   | **必填。** 食品价格    |
|image_amount  |integer | **必填。** 食品图片总数|
|image         |file    | **必填。** 食品图片    |

#### 示例

```http
POST /v1/food HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: multipart/form-data; boundary=7MA4YWxkTrZu0gW
Authorization: Basic ZXlKaGJHY2lPaUpJVXpVeE1pSXNJbWxoZENJNk1UVTBPRFkxTkRneE15d2laWGh3SWpveE5UVXhNalEyT0RFemZRLmV5SjFhV1FpT2pFMkxDSjBlWEJsSWpveE1EQXNJbk5qYjNCbElqb3lmUS5HOU14c2QtSm43cTFRTWY0eUx1a1B0elY0eUJmV2RKUURmSWRId2NraUJJa1BnN0lXRHVZWUtIOU55ZFMzeDZtMnp4cWEzaWpBYThaRzJPSFdGVWtuUTo=
cache-control: no-cache

--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="name"

椒盐排条

--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="introduction"

这是介绍

--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="restaurant_id"

1

--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="image_amount"

2

--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="image-1"; filename="C:\Users\lenovo\Desktop\github_release.png


--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="image-2"; filename="C:\Users\lenovo\Desktop\github_release.png


--7MA4YWxkTrZu0gW--
```

#### 响应
```json
Status: 201 Created

{
    "error_code": 0,
    "message": "Created",
    "request_url": "POST /v1/food"
}
```
### 4.4更新食品信息

**注意**：仅对通过身份认证的`管理员`有效

```
PUT /food/:food_id
```
#### 参数

|名称         |类型    |描述                   |
|:-----------:|:------|:----------------------|
|name         |string | **选填。** 食品名称    |
|introduction |string | **选填。** 食品介绍    |
|canteen_id   |integer| **选填。** 食品所在餐厅编号|
|price        |integer| **选填。** 食品价格    |

#### 示例
```json
{
    "price": 15
}
```

#### 响应

```json
Status: 202 Accepted

{
    "error_code": 0,
    "message": "Updated",
    "request_url": "PUT /v1/food/1"
}
```

### 4.5删除食品

**注意**：仅对通过身份认证的`管理员`有效

```
DELETE /food/:food_id
```

#### 响应
```json
Status: 202 Accepted

{
    "error_code": 0,
    "message": "Deleted",
    "request_url": "DELETE /v1/food/1"
}
```

## 5. 评论
### 5.1列出单个餐厅的评论
```
GET /restraunt/:restraunt_id/reviews
```

#### 响应
```json
Status: 200 OK

[
    {
        "content": "我吃到了虫子！",
        "create_time": 1549967536,
        "grade": 1,
        "id": 1,
        "images": [
            {
                "id": 1,
                "url": "http://api.foodadvisor.top/food_seeker/images/20190212/2f46051c2e9811e9aaf754ee75dc7dce.jpg"
            },
            {
                "id": 8,
                "url": "http://api.foodadvisor.top/food_seeker/images/20190212/d6a31b622ea211e9be1654ee75dc7dce.jpg"
            }
        ]
        
    },
    {
        
        "content": "我吃到了虫子！",
        "create_time": 1549967536,
        "grade": 1,
        "id": 1,
        "images": [
            {
                "id": 1,
                "url": "http://api.foodadvisor.top/food_seeker/images/20190212/2f46051c2e9811e9aaf754ee75dc7dce.jpg"
            },
            {
                "id": 8,
                "url": "http://api.foodadvisor.top/food_seeker/images/20190212/d6a31b622ea211e9be1654ee75dc7dce.jpg"
            }
        ]
        
    }
]
```

### 5.2列出单个用户的评论
```
GET /user/:user_id/reviews
```

#### 响应
```json
Status: 200 OK

[
    {
        "content": "我吃到了虫子！",
        "create_time": 1549967736,
        "grade": 1,
        "id": 1,
        "images": [
            {
                "id": 1,
                "url": "http://api.foodadvisor.top/food_seeker/images/20190212/2f46051c2e9811e9aaf754ee75dc7dce.jpg"
            },
            {
                "id": 8,
                "url": "http://api.foodadvisor.top/food_seeker/images/20190212/d6a31b622ea211e9be1654ee75dc7dce.jpg"
            }
        ]
    },
    {
        "content": "我吃到了虫子！",
        "create_time": 1549967736,
        "grade": 1,
        "id": 1,
        "images": [
            {
                "id": 1,
                "url": "http://api.foodadvisor.top/food_seeker/images/20190212/2f46051c2e9811e9aaf754ee75dc7dce.jpg"
            },
            {
                "id": 8,
                "url": "http://api.foodadvisor.top/food_seeker/images/20190212/d6a31b622ea211e9be1654ee75dc7dce.jpg"
            }
        ]
    }
]
```

### 5.3获取评论信息
```
GET /review/:review_id
```

#### 响应
```json
Status: 201 Created

{
    "content": "我吃到了虫子！",
    "create_time": 1549967782,
    "grade": 1,
    "id": 1,
    "images": [
        {
            "id": 1,
            "url": "http://api.foodadvisor.top/food_seeker/images/20190212/2f46051c2e9811e9aaf754ee75dc7dce.jpg"
        },
        {
            "id": 8,
            "url": "http://api.foodadvisor.top/food_seeker/images/20190212/d6a31b622ea211e9be1654ee75dc7dce.jpg"
        }
    ],
    "restaurant": {
        "canteen_id": 1,
        "review_amount": 0,
        "create_time": 1549967782,
        "grade": 0,
        "id": 1,
        "images": [
            {
                "id": 1,
                "url": "http://api.foodadvisor.top/food_seeker/images/20190212/2f46051c2e9811e9aaf754ee75dc7dce.jpg"
            },
            {
                "id": 6,
                "url": "http://api.foodadvisor.top/food_seeker/images/20190212/21f712a82ea111e98abc54ee75dc7dce.jpg"
            }
        ],
        "introduction": "很好",
        "name": "汤哥特色风味"
    },
    "user": {
        "avatar_url": null,
        "email": "12345678@163.com",
        "id": 1,
        "mobile": "15967542312",
        "nickname": "中道"
    }
}
```

### 5.4新增评论
**注意**：仅对通过身份认证的`用户`有效
```
POST /review
```
#### 参数

|名称            |类型    |描述                   |
|:-------------:|:-------|:----------------------|
|restaurant_id  |integer | **必填。** 评论针对餐厅编号  |
|content        |string  | **必填。** 评论内容    |
|grade          |float   | **必填。** 评分        |
|image_amount   |integer | **必填。** 评论图片总数 |
|image          |file    | **必填。** 评论图片    |

#### 示例
```http
POST /v1/review HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: multipart/form-data; boundary=7MA4YWxkTrZu0gW
Authorization: Basic ZXlKaGJHY2lPaUpJVXpVeE1pSXNJbWxoZENJNk1UVTBPRFkxTkRneE15d2laWGh3SWpveE5UVXhNalEyT0RFemZRLmV5SjFhV1FpT2pFMkxDSjBlWEJsSWpveE1EQXNJbk5qYjNCbElqb3lmUS5HOU14c2QtSm43cTFRTWY0eUx1a1B0elY0eUJmV2RKUURmSWRId2NraUJJa1BnN0lXRHVZWUtIOU55ZFMzeDZtMnp4cWEzaWpBYThaRzJPSFdGVWtuUTo=
cache-control: no-cache

--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="content"

这是一条评论

--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="restaurant_id"

1

--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="grade"

5

--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="image_amount"

2

--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="image-1"; filename="C:\Users\lenovo\Desktop\github_release.png


--7MA4YWxkTrZu0gW--
Content-Disposition: form-data; name="image-2"; filename="C:\Users\lenovo\Desktop\github_release.png


--7MA4YWxkTrZu0gW--
```

#### 响应
```json
Status: 201 Created

{
    "error_code": 0,
    "message": "Created",
    "request_url": "POST /v1/review"
}
```

### 5.5更新评论

**注意**：仅对通过身份认证的`用户`有效
```
PUT /review/:review_id
```

#### 参数

|名称            |类型    |描述                   |
|:-------------:|:-------|:----------------------|
|restaurant_id  |integer | **选填。** 评论针对餐厅编号  |
|content        |string  | **选填。** 评论内容    |
|grade          |float   | **选填。** 评分        |

#### 示例
```json
{
    "content": "hhh",
    "grade": 5
}
```

#### 响应
```json
Status: 202 Accepted

{
    "error_code": 0,
    "message": "Updated",
    "request_url": "PUT /v1/review/1"
}
```

### 5.6删除评论
**注意**：仅对通过身份认证的`用户`有效
```
DELETE /review/:review_id
```

#### 响应
```json
Status: 202 Accepted

{
    "error_code": 0,
    "message": "Deleted",
    "request_url": "DELETE /v1/review/1"
}
```

## 6. 查询

### 6.1查询餐厅
```
GET /search/restaurants
```

#### 参数

|名称    |类型  |描述                    |
|:-----:|:------|:----------------------|
|q      |string | **必填。** 查询关键字  |
|sort   |string | **选填。** 根据评分(`grade`)或者热度(`hot`)，对查询结果进行排序。默认：`grade`   |
|order  |string | **选填。** 确定返回的搜索结果是降序(`desc`)还是升序(`asc`)。默认：`desc`|

#### 示例
```
http://api.foodadvisor.top/search/restaurants?q=第四食堂&sort=grade&order=desc
```

#### 响应
```json
Status: 200 OK

{
    "items": [
        {
            "canteen_id": 1,
            "create_time": 1551871049,
            "grade": 0,
            "id": 1,
            "images": [],
            "introduction": "暂无",
            "name": "家之味",
            "review_amount": 0
        }
    ],
    "total_count": 1
}
```

### 6.2查询食品
```
GET /search/foods
```
#### 参数

|名称    |类型  |描述                    |
|:-----:|:------|:----------------------|
|q      |string | **必填。** 查询关键字  |
|sort   |string | **选填。** 根据评分(`grade`)或者热度(`hot`)，对查询结果进行排序。默认：`grade`   |
|order  |string | **选填。** 确定返回的搜索结果是降序(`desc`)还是升序(`asc`)。默认：`desc`|

#### 示例
```
http://api.foodadvisor.top/search/foods?q=椒盐排条&sort=grade&order=desc
```

#### 响应
```json
Status: 200 OK

{
    "items": [
        {
            "create_time": 1551884675,
            "grade": 0,
            "id": 2,
            "images": [],
            "introduction": "暂无",
            "name": "招牌香辣花溪牛肉粉",
            "price": 12,
            "restaurant_id": 1,
            "review_amount": 0
        },
        {
            "create_time": 1551871255,
            "grade": 0,
            "id": 1,
            "images": [],
            "introduction": "暂无",
            "name": "招牌原味花溪牛肉粉",
            "price": 12,
            "restaurant_id": 1,
            "review_amount": 0
        }
    ],
    "total_count": 2
}
```

### 6.3查询评论
```
GET /search/reviews
```
#### 参数

|名称    |类型  |描述                    |
|:-----:|:------|:----------------------|
|q      |string | **必填。** 查询关键字  |
|sort   |string | **选填。** 根据评分(`grade`)或者热度(`hot`)，对查询结果进行排序。默认：`grade`   |
|order  |string | **选填。** 确定返回的搜索结果是降序(`desc`)还是升序(`asc`)。默认：`desc`|

#### 示例
```
http://api.foodadvisor.top/search/reviews?q=没有&sort=grade&order=desc
```

#### 响应
```json
Status: 200 OK

{
    "items": [
        {
            "content": "很好吃",
            "create_time": 1551969464,
            "grade": 5,
            "id": 1,
            "images": [],
            "user": {
                "auth": 2,
                "avatar_url": null,
                "create_time": 1551870546,
                "email": "example@gmail.com",
                "id": 1,
                "mobile": null,
                "nickname": "Ann"
            }
        }
    ],
    "total_count": 1
}
```

### 6.4查询用户
```
GET /search/users
```
#### 参数

|名称    |类型  |描述                    |
|:-----:|:------|:----------------------|
|q      |string | **必填。** 查询关键字，可选用户的邮箱(email)和用户的手机号(mobile)  |
|sort   |string | **选填。** 根据认证时间(`new`)，对查询结果进行排序。默认：`new`   |
|order  |string | **选填。** 确定返回的搜索结果是降序(`desc`)还是升序(`asc`)。默认：`desc`|

#### 示例
```
http://api.foodadvisor.top/search/reviews?q=email:1111,mobile:1312&sort=new&order=desc
```

#### 响应
```json
Status: 200 OK

{
    "items": [
        {
            "avatar_url": null,
            "create_time": 1551870546,
            "email": "example@gmail.com",
            "id": 1,
            "mobile": null,
            "nickname": "Ann"
        }
    ],
    "total_count": 1
}
```