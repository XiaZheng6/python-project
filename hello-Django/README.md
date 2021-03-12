# Hello Django
```
├── helloproject
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   └── settings.cpython-36.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
```
说明：init代表一个包，没有的话只是一个文件夹；settinngs为全局设置；url为路由器；wsgi为web service gateway interface，网管服务接口
```
python3.6 manage.py startapp App
```
开启应用、工程
```
├── App
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
```
说明：migrations为迁移文件；tests为测试；views为视图函数
```
python3.6 manage.py runserver
```
说明：runserver为开发者服务器，项目上线不可用此命令
###### 注意：pycharm打开文件的正确路径是manage.py文件的上一级，否则提示容易出错
