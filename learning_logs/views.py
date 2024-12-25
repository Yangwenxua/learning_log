from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """显示所有的主题"""
<<<<<<< HEAD
    topics = Topic.objects.order_by('date_added')
=======
    if request.user.is_authenticated:
        # 登录用户看到自己的所有主题
        topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    else:
        # 未登录用户只能看到公开的主题
        topics = Topic.objects.filter(public=True).order_by('date_added')
<<<<<<< HEAD
>>>>>>> temp-lzy
=======
>>>>>>> main
>>>>>>> 692d21f307d04745ca70f09977f7c5aaa7a6f475
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """显示单个主题及其所有的条目"""
<<<<<<< HEAD
    topic = Topic.objects.get(id=topic_id)
=======
    topic = get_object_or_404(Topic, id=topic_id)
    # 如果主题不是公开的，确保用户已登录并且是主题的所有者
    if not topic.public and (not request.user.is_authenticated or topic.owner != request.user):
        raise Http404
<<<<<<< HEAD
>>>>>>> temp-lzy
=======
>>>>>>> main
>>>>>>> 692d21f307d04745ca70f09977f7c5aaa7a6f475
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

<<<<<<< HEAD
def new_topic(request):
=======
@login_required
def new_topic(request):
    """允许用户添加新主题"""
<<<<<<< HEAD
>>>>>>> temp-lzy
=======
>>>>>>> main
>>>>>>> 692d21f307d04745ca70f09977f7c5aaa7a6f475
    if request.method != 'POST':
        # 未提交数据，创建一个新表单
        form = TopicForm()
    else:
        # POST 提交的数据，对数据进行处理
        form = TopicForm(data=request.POST)
        if form.is_valid():
<<<<<<< HEAD
            form.save()
=======
            new_topic = form.save(commit=False)
            new_topic.owner = request.user  # 确保新主题关联到当前用户
            new_topic.save()
<<<<<<< HEAD
>>>>>>> temp-lzy
=======
>>>>>>> main
>>>>>>> 692d21f307d04745ca70f09977f7c5aaa7a6f475
            return redirect('learning_logs:topics')

    # 显示空表单或指出表单数据无效
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

<<<<<<< HEAD
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
=======
@login_required
def new_entry(request, topic_id):
    """允许用户为特定主题添加新条目"""
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method != 'POST':
        # 未提交数据，创建一个新表单
        form = EntryForm()
    else:
        # POST 提交的数据，对数据进行处理
<<<<<<< HEAD
>>>>>>> temp-lzy
=======
>>>>>>> main
>>>>>>> 692d21f307d04745ca70f09977f7c5aaa7a6f475
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

<<<<<<< HEAD
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
=======
    # 显示空表单或指出表单数据无效
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic

    # 确保只有条目的所有者才能编辑它
    if entry.topic.owner != request.user:
        raise Http404

<<<<<<< HEAD
>>>>>>> temp-lzy
=======
>>>>>>> main
>>>>>>> 692d21f307d04745ca70f09977f7c5aaa7a6f475
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
<<<<<<< HEAD

@login_required
def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
    
@login_required
def new_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    else:
        form = TopicForm()
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
    
@login_required
def new_entry(request, topic_id):
    # 获取主题，确保它存在
    topic = get_object_or_404(Topic, id=topic_id)

    # 检查主题是否属于当前用户
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 没有提交数据：创建一个空表单
        form = EntryForm()
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # 显示空表单或指出表单数据无效
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
    
# @login_required
# def edit_entry(request, entry_id):
=======
<<<<<<< HEAD
>>>>>>> temp-lzy
=======
>>>>>>> main
>>>>>>> 692d21f307d04745ca70f09977f7c5aaa7a6f475
    