# Food Seeker API Documentation


<!-- ## Schema
All API access is over HTTPS, and accessed from `root endpoint`. All data is sent and received as JSON. -->

- [1.Canteen](#1Canteen)
  - [1.1 用户注册](#11用户注册)
  - [1.2 用户登录](#12用户登录)
  - [1.3 校验令牌](#13校验令牌)
##API List:
##1.食堂
###1.1获取所有食堂*
```
GET /v1/canteen/all
```
#### 参数

|名称|类型|描述|
|:-----:|:-----|:-----|
|无

#### 示例
```json
{}
```

#### 响应
```json
Status: 200 OK

[
    {
    "canteen_id":1,
    "name":"本部土豪食堂",
    "introduction":"贵，好，净，挤",
    "grade":4.9,
    "comment_amount":1230,
    "location":"本部某地",
    "images":[]
    },      
    {
    "canteen_id":2,
    "name":"本部方塔食堂",
    "introduction":"贵，好，净，挤",
    "grade":4.9,
    "comment_amount":1230,
    "location":"本部某地",
    "images":[]
    }
]
```
###1.2获取某个校区所有食堂*
```
GET /v1/canteen/campus_code/all
```
#### 参数

|名称|类型|描述|
|:-----:|:-----|:-----|
|campus_code      |integer |**必填。**校区编码 |

#### 示例
```json
{
  "campus_code": 1
}
```

#### 响应
```json
Status: 200 OK

[ 
    {
    "canteen_id":1,
    "name":"本部土豪食堂",
    "introduction":"贵，好，净，挤",
    "grade":4.9,
    "comment_amount":1230,
    "location":"本部某地",
    "images":[]
    } ,      
    {
    "canteen_id":2,
    "name":"本部土豪食堂",
    "introduction":"贵，好，净，挤",
    "grade":4.9,
    "comment_amount":1230,
    "location":"本部某地",
    "images":[]
    }
]
```
###1.3获取某个食堂*
```
GET /v1/canteen/canteen_id
```
#### 参数

|名称|类型|描述|
|:-----:|:-----|:-----|
|canteen_id      |integer | **必填。**食堂id号 |

#### 示例
```json
{
  "canteen_id": 1
}
```

#### 响应
```json
Status: 200 OK

[ 
    {
    "canteen_id":2,
    "name":"本部土豪食堂",
    "introduction":"贵，好，净，挤",
    "grade":4.9,
    "comment_amount":1230,
    "location":"本部某地",
    "images":[]
    }
]
```
##2.餐厅
###2.1获取某个食堂所有餐厅*
```
GET /v1/canteen/restaurant/all
```
#### 参数

|名称|类型|描述|
|:-----:|:-----|:-----|
|canteen_id      |integer | **必填。**食堂id号 |

#### 示例
```json
{
      "canteen_id": 1
}
```

#### 响应
```json
Status: 200 OK

[
    {
    "restaurant_id":1,
    "name":"汤哥特色风味",
    "introduction":"贵，好，净，挤",
    "grade":4.9,
    "canteen_id":7,
    "comment_amount":1230,
    "images":[]
    },
    {
    "restaurant_id":2,
    "name":"皇茶",
    "introduction":"贵，好，净，挤",
    "grade":4.9,
    "canteen_id":7,
    "comment_amount":1230,
    "images":[]
    }
]
```
###2.2获取某个食堂某个餐厅*
```
GET /v1/canteen/restaurant/restaurant_id
```
#### 参数

|名称|类型|描述|
|:-----:|:-----|:-----|
|canteen_id      |integer | **必填。**食堂id号 |

#### 示例
```json
{
      "canteen_id": 1
}
```

#### 响应
```json
Status: 200 OK

{
    "restaurant_id":1,
    "name":"汤哥特色风味",
    "introduction":"贵，好，净，挤",
    "grade":4.9,
    "canteen_id":1,
    "comment_amount":1230,
    "images":[]
}
```
##3.食品
###3.1获取某个食堂某个餐厅所有食品*
```
GET /v1/canteen/restaurant/food/all
```
#### 参数

|名称|类型|描述|
|:-----:|:-----|:-----|
|canteen_id      |integer | **必填。**食堂id号 |
|restaurant_id      |integer | **必填。**餐厅id号 |

#### 示例
```json
{
      "canteen_id": 1,
      "restaurant_id": 1
}
```

#### 响应
```json
Status: 200 OK

[
    {
    "food_id":1,
    "name":"包菜肉片",
    "introduction":"便宜好吃",
    "price":10,
    "grade":4.9,
    "restaurant_id":1,
    "comment_amount":1230,
    "images":[]
    },
    {
    "food_id":1,
    "name":"小炒牛肉",
    "introduction":"便宜好吃",
    "price":10,
    "grade":4.9,
    "restaurant_id":1,
    "comment_amount":1230,
    "images":[]
    }
]
```
###3.2获取某个食堂某个餐厅某个食品*
```
GET /v1/canteen/restaurant/food/food_id
```
#### 参数

|名称|类型|描述|
|:-----:|:-----|:-----|
|canteen_id      |integer | **必填。**食堂id号 |
|restaurant_id      |integer | **必填。**餐厅id号 |
|food_id      |integer | **必填。**食品id号 |

#### 示例
```json
{
      "canteen_id": 1,
      "restaurant_id": 1,
      "food_id": 1
}
```

#### 响应
```json
Status: 200 OK

{
    "food_id":1,
    "name":"包菜肉片",
    "introduction":"便宜好吃",
    "price":10,
    "grade":4.9,
    "restaurant_id":1,
    "comment_amount":1230,
    "images":[]
}
```
##4.评论
###4.1获取某个食堂某个餐厅某个食品全部评论*
```
GET /v1/comment/food_id/all
```
#### 参数

|名称|类型|描述|
|:-----:|:-----|:-----|
|food_id      |integer | **必填。**食品id号 |

#### 示例
```json
{
      "food_id": 1
}
```

#### 响应
```json
Status: 200 OK

[
    {
    "comment_id":1,
    "user_id":1,
    "nickname":"中道",
    "authentication_time":1543584026,
    "user_images":[],
    "food_id":2,
    "restaurant_id":1,
    "grade":4.9,
    "content":"难吃得一匹",
    "create_time":1543584026,
    "delete_time":1543584026,
    "images":[]
    },
    {
    "comment_id":2,
    "user_id":2,
    "nickname":"中道",
    "authentication_time":1543584026,
    "user_images":[],
    "food_id":2,
    "restaurant_id":1,
    "grade":4.9,
    "content":"难吃得一匹",
    "create_time":1543584026,
    "delete_time":1543584026,
    "images":[]
    }
]
```
###4.2获取某个食堂某个餐厅某个食品某个评论*
```
GET /v1/comment/food_id/comment_id
```
#### 参数

|名称|类型|描述|
|:-----:|:-----|:-----|
|food_id      |integer | **必填。**食品id号 |

#### 示例
```json
{
      "food_id": 1
}
```

#### 响应
```json
Status: 200 OK
{
    "comment_id":1,
    "user_id":1,
    "nickname":"中道",
    "authentication_time":1543584026,
    "user_images":[],
    "food_id":2,
    "restaurant_id":1,
    "grade":4.9,
    "content":"难吃得一匹",
    "create_time":1543584026,
    "delete_time":1543584026,
    "images":[]
}
```
###4.3提交评论*
```
POST /v1/write_comment
```
#### 参数

|名称|类型|描述|
|:-----:|:-----|:-----|
|token      |string | **必填。**用户的令牌 |
|food_id      |integer | **必填。**评论对象食品的id号 |
|restaurant_id      |integer | **必填。**评论对象餐厅的id号 |
|content      |string | **必填。**用户的评论内容 |
|picture      |string | **选填。**用户的评论图片 |

#### 示例
```json
{
      "token":"eyJhbGciOiJIUzUxMiIsImlhdCI6MTU0Nzk4NTkxNSwiZXhwIjoxNTQ3OTkzMTE1fQ.eyJ1aWQiOjksInR5cGUiOjEwMCwic2NvcGUiOjF9.crX5pEtGWhj2SH73qhgLeV3rnY-QWbv6qJzqS82rsqPuw0W09m8TNkAsQZ_mTmu5ylwbPSd0xLEOhyRTKqdH_w",
      "food_id":"1",
      "restaurant_id":"1",
      "content":"味道可以",
      "picture":"skflndskfnsfdsjavldfwafhieo"
}
```

#### 响应
```json
Status: 200 OK
{
    "error_code": 0,
    "message": "评论成功",
    "request_url": "POST /v1/write_comment"
}
```
###4.4修改评论*
```
POST /v1/rwrite_comment
```
#### 参数

|名称|类型|描述|
|:-----:|:-----|:-----|
|token      |string | **必填。**用户的令牌 |
|comment_id      |integer | **必填。**修改对象 |
|food_id      |integer | **必填。**评论对象食品的id号 |
|restaurant_id      |integer | **必填。**评论对象餐厅的id号 |
|content      |string | **选填。**用户的评论内容 |
|picture      |string | **选填。**用户的评论图片 |

#### 示例
```json
{
      "token":"eyJhbGciOiJIUzUxMiIsImlhdCI6MTU0Nzk4NTkxNSwiZXhwIjoxNTQ3OTkzMTE1fQ.eyJ1aWQiOjksInR5cGUiOjEwMCwic2NvcGUiOjF9.crX5pEtGWhj2SH73qhgLeV3rnY-QWbv6qJzqS82rsqPuw0W09m8TNkAsQZ_mTmu5ylwbPSd0xLEOhyRTKqdH_w",
      "food_id":"1",
      "restaurant_id":"1",
      "content":"味道8行",
      "picture":"skflndskfnsfdsjavldfwafhieo"
}
```

#### 响应
```json
Status: 200 OK
{
    "error_code": 0,
    "message": "修改评论成功",
    "request_url": "POST /v1/rwrite_comment"
}
```
###4.5删除评论*
```
DELETE /v1/delete_comment
```
#### 参数

|名称|类型|描述|
|:-----:|:-----|:-----|
|token      |string | **必填。**用户的令牌 |
|comment_id      |integer | **必填。**评论对象食品的id号 |

#### 示例
```json
{
      "token":"eyJhbGciOiJIUzUxMiIsImlhdCI6MTU0Nzk4NTkxNSwiZXhwIjoxNTQ3OTkzMTE1fQ.eyJ1aWQiOjksInR5cGUiOjEwMCwic2NvcGUiOjF9.crX5pEtGWhj2SH73qhgLeV3rnY-QWbv6qJzqS82rsqPuw0W09m8TNkAsQZ_mTmu5ylwbPSd0xLEOhyRTKqdH_w",
      "comment_id":"1",
}
```

#### 响应
```json
Status: 200 OK
{
    "error_code": 0,
    "message": "删除评论成功",
    "request_url": "POST /v1/delete_comment"
}
```
##5.用户
##5.1获取某个用户*
```
GET /v1/uesr/user_id
```
#### 参数

|名称|类型|描述|
|:-----:|:-----|:-----|
|token      |string | **必填。**用户的令牌 |

#### 示例
```json
{
      "token":"eyJhbGciOiJIUzUxMiIsImlhdCI6MTU0Nzk4NTkxNSwiZXhwIjoxNTQ3OTkzMTE1fQ.eyJ1aWQiOjksInR5cGUiOjEwMCwic2NvcGUiOjF9.crX5pEtGWhj2SH73qhgLeV3rnY-QWbv6qJzqS82rsqPuw0W09m8TNkAsQZ_mTmu5ylwbPSd0xLEOhyRTKqdH_w",
}
```

#### 响应
```json
Status: 200 OK
{
    "id":1,
    "authentication_time":2018-1-1,
    "comment_amount":234,
    "nickname":"中道",
    "images":[]
    }
```
##5.2注册
```
POST /client/register
```

#### 参数

|名称|类型|描述|
|:-----:|:-----|:-----|
|account   |string  |**必填。** 账号名称|
|secret    |string  |**必填。** 注册密码|
|type      |integer |**必填。** <br> `100` 邮箱注册 <br> `101`手机号注册|
|nickname  |string |**邮箱注册时必填。** |

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
    "message": "注册成功",
    "request_url": "POST /v1/client/register"
}
```
##5.3登录
```
POST /token
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
##5.4校验令牌
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
##5.5更新用户*
```
POST /v1/uesr/user_id/update
```
#### 参数

|名称|类型|描述|
|:-----:|:-----|:-----|
|token      |string | **必填。**用户的令牌 |
|nickname      |string | **选填。**用户的昵称 |
|image      |string | **选填。**用户的头像 |


#### 示例
```json
{
    "token":"eyJhbGciOiJIUzUxMiIsImlhdCI6MTU0Nzk4NTkxNSwiZXhwIjoxNTQ3OTkzMTE1fQ.eyJ1aWQiOjksInR5cGUiOjEwMCwic2NvcGUiOjF9.crX5pEtGWhj2SH73qhgLeV3rnY-QWbv6qJzqS82rsqPuw0W09m8TNkAsQZ_mTmu5ylwbPSd0xLEOhyRTKqdH_w",
    "nickname":"中道",
    "images":[]
}
```

#### 响应
```json
Status: 200 OK
{  
    "error_code": 0,
    "message": "用户信息更新成功",
    "request_url": "POST /v1/uesr/user_id/update"
    }
```
##5.5删除用户
```
DELETE /v1/uesr/user_id/delete
```
#### 参数

|名称|类型|描述|
|:-----:|:-----|:-----|
|token      |string | **必填。**用户的令牌 |
|user_id      |integer | **必填。**用户的id |


#### 示例
```json
{
    "token":"eyJhbGciOiJIUzUxMiIsImlhdCI6MTU0Nzk4NTkxNSwiZXhwIjoxNTQ3OTkzMTE1fQ.eyJ1aWQiOjksInR5cGUiOjEwMCwic2NvcGUiOjF9.crX5pEtGWhj2SH73qhgLeV3rnY-QWbv6qJzqS82rsqPuw0W09m8TNkAsQZ_mTmu5ylwbPSd0xLEOhyRTKqdH_w",
    "user_id":1
}
```

#### 响应
```json
Status: 200 OK
{  
    "error_code": 0,
    "message": "用户删除成功",
    "request_url": "DELETE /v1/uesr/user_id/delete"
    }
```