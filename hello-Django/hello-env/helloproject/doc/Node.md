# Django

## 快捷键
- 万能键
    - command + enter
- 参数提示
    - command + p
    
## 实现一个请求
- 注册一个路由
    - urls中
        - url
            - 参数 匹配规则 正则
        - 视图函数
            - 对应的是views中的一个函数
                - 没有括号
- 去views实现对应的视图函数
    - 第一个参数是request
    - 永远记得返回response
    
## html
- ul>li
- ul*5
- ul>li*5

## 模板配置
- 两种
    - 在App中进行模板配置
        - 只需在APP的根目录创建templates文件夹j即可
        - 如果想让代码自动提示，我们应该标记文件夹为模板文件夹
    - 在项目目录中进行模板配置
        - 需要在项目目录中创建templates文件夹并标记
        - 需要在settings中进行注册
    - 在开发中使用第二种
        - 模板是可以继承和复用的

## 路由优化配置
- 项目中如果逻辑过于复杂，可以进行拆分
- 拆分为多个APP
- 继续拆分路由器urls
    - 在APP中创建自己的urls
        - urlpatterns 路由规则列表
        - 在根urls中进行子路由的包含
    - 子路由使用
        - 根路由规则 + 子路由规则

## 迁移数据
- pycharm连接数据库
    - 生成迁移
        - python3.6 manage.py makemigrations
    - 执行迁移
        - python3.6 manage.py migrate
        
## models 使用了ORM技术
- Object Relational Mapping 对象关系映射
- 将业务逻辑进行了一个解耦合
    - object.save()
    - object.delete()
- 关系型数据库
    - DDL 定义数据库
    - 通过models定义实现 数据库表的定义 
- 数据操作
    - 增删改查
    - 存储
        - save()
    - 查询
        - 查所有 objects.all()
        - 查单个 objects.get(pk=xx)
    - 更新
        - 基于查询的
        - 查好的对象，修改属性，然后save()
    - 删除
        - 基于查询的
        - 调用delete()
        
## 连接MySQL驱动
- mysqlclient
    - python2,3都能直接使用
    - 致命缺点
        - 对MySQL安装有要求，必须指定位置存在配置文件
- python-mysql
    - python2 支持很好
    - python3 不支持
- pymysql
    - python2,python3都支持
    - 他还可以伪装成前面的库
    
## 如何看待bug
- 看日志
    - 先看第一条
    - 再看最后一条
- 梳理思路
    - 程序在哪一个位置和预期出现偏差
    
## 表关系
- 1对1    1:1
- 1对多   1:M
- 多对多   M:M
       