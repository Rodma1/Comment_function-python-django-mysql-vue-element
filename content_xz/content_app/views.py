from django.shortcuts import render

# Create your views here.
from content_app.models import Content
from django.http import JsonResponse
import json
"""
获取数据库的信息
"""
def get_contents(request):
    """获取所有评论信息"""
    try:
        #使用ORM获取所有评论信息
        obj_content=Content.objects.all().values()#{}{}
        print(obj_content[0])
        #把结果转为list格式
        contents=list(obj_content)
        return JsonResponse({'code':1,'data':contents})
    except Exception as e:
        return JsonResponse({'code':0,'msg':"获取评论信息异常"+str(e)})

"""
获取前端的传递的数据，读入数据库，然后显示
"""

def add_content(request):
    """接收前端传递过来的值"""
    data=json.loads(request.body.decode("utf-8"))
    #添加到数据库
    try:
        obj_content=Content(content=data['content'],name=data['name'])
        #执行添加
        obj_content.save()
        #使用ORM获取所有评论信息，并且吧对象转为字典格式
        obj_content=Content.objects.all().values()#{}{}
        #把结果转为list
        contents=list(obj_content)#[{},{}]
        #返回给前端
        return JsonResponse({'code':1,'data':contents})
    except Exception as e:
        return JsonResponse({'code':0,'msg':"添加到数据库异常:"+str(e)})