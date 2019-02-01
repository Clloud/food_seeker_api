# Food Advisor API v1
---

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
  - [1.6 更新用户信息](#16更新用户信息)
  - [1.7 删除用户](#17删除用户)
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
https://api.foodadvisor.top/v1/restraunt/1/comments?page=2&per_page=50
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
    "request_url": "POST /v1/client/register"
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
    "auth": 1,
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
    "avatar": null,
    "email": "example@gmail.com",
    "id": 16,
    "mobile": "17716805432",
    "nickname": "Ann"
}
```

### 1.6更新用户信息
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

### 1.7删除用户
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
        "comment_amount": 0,
        "grade": 0,
        "id": 1,
        "introduction": "没有介绍",
        "location": "东校区浴室旁边",
        "name": "第五食堂"
    },
    {
        "campus_id": 1,
        "comment_amount": 0,
        "grade": 0,
        "id": 2,
        "introduction": "没有介绍",
        "location": "东校区浴室旁边",
        "name": "第六食堂"
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
    "comment_amount": 0,
    "grade": 0,
    "id": 1,
    "introduction": "没有介绍",
    "location": "东校区浴室旁边",
    "name": "第五食堂"
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
|token    |string | **必填。** 管理员令牌    |

#### 示例
```json
{
	"name": "第四食堂",
	"introduction": "没有介绍",
	"location": "东区教超旁边",
	"campus_id": 1
}
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
|comment_amount    |integer| **选填。** 食堂评论数量|
|status    |integer| **选填。** 食堂状态|
|grade    |float| **选填。** 食堂评分|
|token    |string | **选填。** 管理员令牌    |
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
GET /canteen/:canteen_id/restraunts
```

#### 响应
```json
Status: 200 OK

[
    {
        "canteen_id": 1,
        "comment_amount": 0,
        "grade": 0,
        "id": 1,
        "introduction": "很好",
        "name": "汤哥特色风味"
    },
    {
        "canteen_id": 1,
        "comment_amount": 0,
        "grade": 0,
        "id": 2,
        "introduction": "很好",
        "name": "汤哥特色风味"
    }
]
```

### 3.2获取餐厅信息
```
GET /restraunt/:restraunt_id
```

#### 响应
```json
Status: 200 OK

{   
    "canteen_id": 1,
    "comment_amount": 0,
    "grade": 0,
    "id": 1,
    "introduction": "很好",
    "name": "汤哥特色风味"
}
```
### 3.3新增餐厅
```
POST /restaurant
```
#### 参数

|名称       |类型    |描述                   |
|:---------:|:------|:----------------------|
|canteen_id   |integer | **必填。** 餐厅所在食堂编号  |
|introduction     |string | **必填。** 餐厅介绍|
|name      |string | **必填。** 餐厅名称  |
|token    |string | **必填。** 管理员令牌    |

#### 示例
```json
{
    "canteen_id": 1,
    "introduction": "",
    "name": "汤哥特色风味"
}
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
```
PUT /restaurant/:restaurant_id
```
#### 参数

|名称         |类型    |描述                   |
|:-----------:|:------|:----------------------|
|name         |string | **选填。** 餐厅名称    |
|introduction |string | **选填。** 餐厅介绍    |
|canteen_id    |integer| **选填。** 餐厅所在食堂编号|
|comment_amount    |integer| **选填。** 餐厅评论数量|
|status    |integer| **选填。** 餐厅状态|
|grade    |float| **选填。** 餐厅评分|
|token    |string | **选填。** 管理员令牌    |
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
        "comment_amount": 0,
        "grade": 0,
        "id": 1,
        "introduction": "",
        "name": "椒盐排条",
        "price": 15,
        "restaurant_id": 1
    },
    {
        "comment_amount": 0,
        "grade": 0,
        "id": 2,
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
    "comment_amount": 0,
    "grade": 0,
    "id": 1,
    "introduction": "",
    "name": "椒盐排条",
    "price": 15,
    "restaurant_id": 1
}
```
### 4.3新增食品
```
POST /food
```
#### 参数

|名称       |类型    |描述                   |
|:---------:|:------|:----------------------|
|restaurant_id   |integer | **必填。** 食品所在餐厅编号  |
|introduction     |string | **必填。** 食品介绍|
|price    |float | **必填。** 食品价格|
|name      |string | **必填。** 食品名称  |
|token    |string | **必填。** 管理员令牌    |

#### 示例
```json
{
    "restaurant_id": 1,
    "introduction": "",
    "price": 15.0,
    "name": "椒盐排条"
}
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
```
PUT /food/:food_id
```
#### 参数

|名称         |类型    |描述                   |
|:-----------:|:------|:----------------------|
|name         |string | **选填。** 食品名称    |
|introduction |string | **选填。** 食品介绍    |
|canteen_id    |integer| **选填。** 食品所在餐厅编号|
|price    |integer| **选填。** 食品价格|
|comment_amount    |integer| **选填。** 食品评论数量|
|status    |integer| **选填。** 食品状态|
|grade    |float| **选填。** 食品评分|
|token    |string | **必填。** 管理员令牌    |
#### 示例
```json
{
    "price":15
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
GET /restraunt/:restraunt_id/comments
```

#### 响应
```json
Status: 200 OK

[
    {
        "content": "我吃到了虫子！",
        "grade": 1,
        "id": 1,
        "restaurant_id": 1,
        "user_id": 1
    },
    {
        "content": "我吃到了虫子！",
        "grade": 1,
        "id": 2,
        "restaurant_id": 1,
        "user_id": 1
    }
]
```

### 5.2列出单个用户的评论
```
GET /user/:user_id/comments
```

#### 响应
```json
Status: 200 OK

[
    {
        "content": "我吃到了虫子！",
        "grade": 1,
        "id": 1,
        "restaurant_id": 1,
        "user_id": 1
    },
    {
        "content": "我吃到了虫子！",
        "grade": 1,
        "id": 2,
        "restaurant_id": 1,
        "user_id": 1
    }
]
```
### 5.3获取评论信息
```
GET /comment/:comment_id
```

#### 响应
```json
Status: 201 Created

{
    "content": "我吃到了虫子！",
    "grade": 1,
    "id": 1,
    "restaurant_id": 1,
    "user_id": 1
}
```
### 5.4新增评论
**注意**：仅对通过身份认证的`用户`有效
```
POST /comment
```
#### 参数

|名称       |类型    |描述                   |
|:---------:|:------|:----------------------|
|restaurant_id   |integer | **必填。** 评论针对餐厅编号  |
|user_id   |integer | **必填。** 评论者编号  |
|content     |string | **必填。** 评论内容|
|grade    |float | **必填。** 评分|

#### 示例
```json
{
    "restaurant_id": 1,
    "user_id": 1,
    "grade": 1,
    "content": "我吃到了虫子！"
}
```
#### 响应
```json
Status: 201 Created

{
    "error_code": 0,
    "message": "Created",
    "request_url": "POST /v1/comment"
}
```

### 5.5更新评论
**注意**：仅对通过身份认证的`用户`有效
```
PUT /comment/:comment_id
```
#### 参数

|名称       |类型    |描述                   |
|:---------:|:------|:----------------------|
|restaurant_id   |integer | **必填。** 评论针对餐厅编号  |
|user_id   |integer | **必填。** 评论者编号  |
|content     |string | **必填。** 评论内容|
|grade    |float | **必填。** 评分|

#### 示例
```json
{
    "content": "hhh",
    "user_id": 1,
    "restaurant_id":1,
    "grade":5
}
```
#### 响应
```json
Status: 201 Created

{
    "error_code": 0,
    "message": "Updated",
    "request_url": "PUT /v1/comment/1"
}
```

### 5.6删除评论
**注意**：仅对通过身份认证的`用户`有效,可删除对象仅为自己的评论
```
DELETE /comment/:comment
```

#### 响应
```json
Status: 202 Accepted

{  
    "error_code": 0,
    "message": "Deleted",
    "request_url": "DELETE /v1/comment/1"
}
```