- [1.用户](#1用户)
  - [1.1 用户注册](#11用户注册)
  - [1.2 用户登录](#12用户登录)
  - [1.3 校验令牌](#13校验令牌)


## 1. 用户
### 1.1用户注册
 
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
    "message": "OK",
    "request_url": "POST /v1/client/register"
}
```

### 1.2用户登录
成功登录后可获取唯一的身份标识
 
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
