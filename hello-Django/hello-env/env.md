# 虚拟环境
```
➜  hello-env git:(main) ✗ virtualenv --no-site-packages hello_env -p /usr/local/bin/python3.6
Running virtualenv with interpreter /usr/local/bin/python3.6
Using base prefix '/Library/Frameworks/Python.framework/Versions/3.6'
New python executable in /Users/xiazheng/python-project/hello-Django/hello-env/hello_env/bin/python3.6
Also creating executable in /Users/xiazheng/python-project/hello-Django/hello-env/hello_env/bin/python
Installing setuptools, pip, wheel...done.

➜  bin git:(main) ✗ . ./activate
(hello_env) ➜  bin git:(main) ✗ python
Python 3.6.4 (v3.6.4:d48ecebad5, Dec 18 2017, 21:07:28)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> ^D
(hello_env) ➜  bin git:(main) ✗ pip freeze
```