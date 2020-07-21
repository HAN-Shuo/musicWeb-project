from django.shortcuts import render,HttpResponse
from .models import *


def indexView(request):
    songDynamic = Dynamic.objects.select_related('song')
    # 热搜歌曲
    searchs = songDynamic.order_by('-search').all()[:8]
    # 音乐分类
    labels = Label.objects.all()
    # 热门歌曲
    popular = songDynamic.order_by('-plays').all()[:10]
    # 新歌推荐
    recommend = Song.objects.order_by('-release').all()[:3]
    # 热门搜索、热门下载
    downloads = songDynamic.order_by('-download').all()[:6]
    tabs = [searchs[:6], downloads]
    return render(request, 'index.html', locals())


# 自定义404和500的视图函数
def page_not_found(request, exception):
    return render(request, '404.html', status=404)


def page_error(request):
    return render(request, '404.html', status=500)


def down(request):
    if request.method == 'GET':
        return render(request,'down.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        singer = request.POST.get('singer')
        time = request.POST.get('time')
        album = request.POST.get('album')
        languages = request.POST.get('languages')
        type = request.POST.get('type')
        release = request.POST.get('release')
        img = request.FILES.get('img')
        lyrics = request.FILES.get('lyrics')
        file = request.FILES.get('file')
        label_id = int(request.POST.get('label'))
        song = Song(name = name, singer = singer, time = time, album = album,languages = languages,type = type,release = release,img = img, lyrics = lyrics,file = file,label_id = label_id)
        song.save()
        return HttpResponse('OK')