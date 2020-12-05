from django.shortcuts import render
from django.http import JsonResponse
from tools.send_code import GetCode
from topic.models import Topics
import json
# Create your views here.

def create_topic(request):
    '''
        {
            "title":"xxx",                  //文章标题
            "categroy":"技术类/非技术类",   //文章分类
            "content":"xxx"                 //文章内容
        }
    '''
    if request.method == "POST":
        data = request.body
        # 判断是否有数据
        if data:
            # 文章标题
            title = request.POST.get('title', '我是标题呀')
            # 文章分类
            categroy = request.POST.get('categroy', '技术类')
            # 文章内容
            content = request.POST.get('content', '第一条博客')
            try:
                # 增加数据
                Topics.objects.create(title=title, categroy=categroy, content=content)
            except Exception as e:
                return JsonResponse(GetCode(10002))

            return JsonResponse(GetCode(10001)) 
        else:
            return JsonResponse(GetCode(12003))
    else:
        return JsonResponse(GetCode(12001))

def delete_topic(request):
    if request.method == "POST":
        # 获取需要删除文章的id
        topic_id = request.POST.get('topic_id')
        try:
            # 查询出是否有这篇文章
            topic = Topics.objects.get(id=topic_id)
        except Exception as e:
            return JsonResponse(GetCode(10008))
        # 删除这篇文章
        topic.delete()
        return JsonResponse(GetCode(10007))
    else:
        return JsonResponse(GetCode(12001))

def update_topic(request):
    if request.method == "POST":
        # 获取需要修改文章的id
        topic_id = request.POST.get('topic_id')
        try:
            # 查询出是否有这篇文章
            topic = Topics.objects.get(id=topic_id)
        except Exception as e:
            return JsonResponse(GetCode(10006))
        # 文章标题
        title = request.POST.get('title', None)
        # 文章分类
        categroy = request.POST.get('categroy', None)
        # 文章内容
        content = request.POST.get('content', None)
        # 如果没有数据则不更新
        if title:
            topic.title = title
        if categroy:
            topic.categroy = categroy
        if content:
            topic.content = content
        # 保存
        topic.save()
        return JsonResponse(GetCode(10005))
    else:
        return JsonResponse(GetCode(12001))


def select_topics(request):
    if request.method == "GET":
        # 获取所有文章
        topics = Topics.objects.all().values('id', 'title', 'categroy', 'content')
        data = []
        # 循环遍历取值
        for i in topics:
            data.append({
                "id": i['id'],
                "title": i['title'],
                "categroy": i['categroy'],
                "content": i['content']
            })
        restul = GetCode(10003)
        restul['data'] = data
        return JsonResponse(restul)
    else:
        return JsonResponse(GetCode(12002))

