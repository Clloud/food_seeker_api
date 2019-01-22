# Food Seeker API Documentation


<!-- ## Schema
All API access is over HTTPS, and accessed from `root endpoint`. All data is sent and received as JSON. -->
##接口列表:
###获取评论
```
GET /v1/comment/single
```
#### 参数

|名称|类型|描述|
|:-----:|:-----|:-----|
|comment_id      |integer |**必填。** <br> 

#### 示例
```json
{
  "comment_id": 1,
}
```

#### 响应
```json
Status: 200 OK

{
    "comment_id": 1,
    "user_id": 1,
   "nickname":"中道",
    "authentication_time":1543584026,
    "user_images":[],
    "cuisine_id":2,
    "window_id":1,
    "grade":4.9,
    "content":"难吃得一匹",
    "like":2,
    "oppose":2,
    "create_time":1543584026,
    "delete_time":1543584026,
    "images":[]
}
```