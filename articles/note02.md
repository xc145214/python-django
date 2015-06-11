# 02 视图与URL配置

## 01 第一个视图
在mysite目录下创建 views.py 空文件文件
添加如下：
```
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world")
```

## 02 URL配置
修改urls.py 文件如下：
```
from django.conf.urls.defaults import *
from mysite.views import hello

urlpatterns = patterns('',
    ('^hello/$', hello),
)
```
所有执行 URL /hello/ 的请求都会由hello这个视图来处理。
>  如果我们用尾部不是$的模式’^hello/’，那么任何以/hello/开头的URL将会匹配，例如：/hello/foo 和/hello/bar，而不仅仅是/hello/。类似地，如果我们忽略了尖号(^)，即’hello/$’，那么任何以hello/结尾的URL将会匹配，例如：/foo/bar/hello/。如果我们简单使用hello/，即没有^开头和$结尾，那么任何包含hello/的URL将会匹配，如：/foo/hello/bar。因此，我们使用这两个符号以确保只有/hello/匹配，不多也不少。6

你大多数的URL模式会以^开始、以$结束，但是拥有复杂匹配的灵活性会更好。
> 你可能会问：如果有人申请访问/hello（尾部没有斜杠/）会怎样。 因为我们的URL模式要求尾部有一个斜杠(/)，那个申请URL将不匹配。 然而，默认地，任何不匹配或尾部没有斜杠(/)的申请URL，将被重定向至尾部包含斜杠的相同字眼的URL。 （这是受配置文件setting中APPEND_SLASH项控制的，参见附件D。）6

> 如果你是喜欢所有URL都以’/’结尾的人（Django开发者的偏爱），那么你只需要在每个URL后添加斜杠，并且设置”APPEND_SLASH”为”True”. 如果不喜欢URL以斜杠结尾或者根据每个URL来决定，那么需要设置”APPEND_SLASH”为”False”,并且根据你自己的意愿来添加结尾斜杠/在URL模式后.

+ 正则表达式

正则表达式 (或 regexes ) 是通用的文本模式匹配的方法。 Django URLconfs 允许你 使用任意的正则表达式来做强有力的URL映射，不过通常你实际上可能只需要使用很少的一 部分功能。
|符号 | 匹配|
|:--------|:---------------|
|. (dot) |  任意单一字符|
|\d     |任意一位数字|
|[A-Z]   |A 到 Z中任意一个字符（大写）|
|[a-z]  | a 到 z中任意一个字符（小写）|
|[A-Za-z]  |  a 到 z中任意一个字符（不区分大小写）|
|+   |匹配一个或更多 (例如, \d+ 匹配一个或 多个数字字符)|
|[^/]+   |一个或多个不为‘/’的字符|
|*   |零个或一个之前的表达式（例如：\d? 匹配零个或一个数字）|
|*   |匹配0个或更多 (例如, \d* 匹配0个 或更多数字字符)|
|{1,3}  | 介于一个和三个（包含）之前的表达式（例如，\d{1,3}匹配一个或两个或三个数字）|


## 03 页面跳转的顺序
1. 进来的请求转入/hello/.

2. Django通过在ROOT_URLCONF配置来决定根URLconf.

3. Django在URLconf中的所有URL模式中，查找第一个匹配/hello/的条目。

4. 如果找到匹配，将调用相应的视图函数

5. 视图函数返回一个HttpResponse

6. Django转换HttpResponse为一个适合的HTTP response， 以Web page显示出来


## 04 动态视图
添加views.py:
```
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
```
修改urls:
```
from django.conf.urls.defaults import *
from mysite.views import hello, current_datetime

urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^time/$', current_datetime),
)
```

## 05 URL配置和松耦合

current_datetime被两个URL使用
```
urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^time/$', current_datetime),
    ('^another-time-page/$', current_datetime),
)
``` 

## 06 另一个动态视图
views.py:
```
from django.http import Http404, HttpResponse
import datetime

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
```

urls.py:
```
from django.conf.urls.defaults import *
from mysite.views import hello, current_datetime, hours_ahead

urlpatterns = patterns('',
    (r'^hello/$', hello),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
)
```