from django.shortcuts import render, redirect, get_object_or_404
from .forms import TopicForm, EntryForm
from .models import Topic, Entry
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm  # 添加这一行
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import TopicForm  # 确保导入你的 TopicForm
from django.http import Http404
from .forms import EntryForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib import messages
# Create your views here.

def home(request):
    topics = Topic.objects.prefetch_related('entries').all()
    return render(request, 'notes/home.html', {'topics': topics})  # 指定正确的模板路径

def about(request):
    return render(request, 'notes/about.html')


@login_required
def new_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.owner = request.user  # 设置主题的所有者为当前用户
            topic.save()
            return redirect('notes:home')  # 添加成功后重定向到主页
    else:
        form = TopicForm()
    return render(request, 'notes/new_topic.html', {'form': form})

@login_required
def topic_update(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    if topic.owner != request.user:
        raise Http404  # 用户不是主题的所有者
    # 处理表单数据
    if request.method == 'POST':
        topic.title = request.POST.get('title')
        topic.save()
        return redirect('home')
    return render(request, 'notes/topic_update.html', {'topic': topic})


@login_required
def delete_entry(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    topic_id = entry.topic.id  # 获取条目所属主题的 ID
    entry.delete()
    messages.success(request, '条目删除成功！')
    return redirect('notes:topic_detail', topic_id=topic_id)  # 重定向到主题详情页

@login_required
def delete_topic(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    topic.delete()
    messages.success(request, '主题删除成功！')
    return redirect('notes:home')  # 重定向到主页

#提交条目和添加条目按钮处理
@login_required
def add_entry(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.topic = topic
            entry.owner = request.user
            entry.save()
            messages.success(request, '条目添加成功！')
            return redirect('notes:home')  # 修改为重定向到主页
        else:
            messages.error(request, '表单数据有误，请检查！')
    else:
        form = EntryForm()
    
    return render(request, 'notes/add_entry.html', {'form': form, 'topic': topic})

def topic_list(request):
    topics = Topic.objects.filter(owner=request.user)  # 仅获取当前用户的主题
    return render(request, 'notes/topic_list.html', {'topics': topics})

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    return render(request, 'notes/topic_detail.html', {'topic': topic})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('notes:home')  # 登录成功后重定向到主页
    else:
        form = AuthenticationForm()
    return render(request, 'notes/login.html', {'form': form})

def custom_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 注册成功后立即登录
            return redirect('notes:login')  # 注册并登录后重定向到登录界面
    else:
        form = UserCreationForm()
    return render(request, 'notes/register.html', {'form': form})