from django.shortcuts import render,get_object_or_404
from blog.models import Post
from blog.forms import EmailSendForm,CommentForm
from django.core.mail import send_mail
#from django.views.generic import ListView
#from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

#Function based pagination
'''def post_list_view(request):
    post_list = Post.objects.filter(status='published')
    paginator = Paginator(post_list,2)
    page_number = request.GET.get('page')
    try:
        post_list = paginator.page(page_number)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request,'blog/post_list.html',{'post_list':post_list})'''

#Class based pegination
'''class PostListView(ListView):
    model = Post
    paginate_by = 2
    #queryset = Post.objects.filter(status = 'published')
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()      
        return queryset.filter(status = 'published')'''
    
    

def post_detail_view(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    comments=post.comments.filter(active=True)
    print('before')
    print(comments)
    csubmit=False
    if request.method=='POST':
        form=CommentForm(data=request.POST)
        print('middle')
        print(comments)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()            
            print('end')
            print(comments)
            csubmit=True
    else:
        form=CommentForm()
    return render(request,'blog/post_detail.html',{'post':post,'form':form,'comments':comments,'csubmit':csubmit})
def send_mail_view(request,id):
    post = get_object_or_404(Post,id=id,status = 'published')
    sent=False
    if request.method=='POST':
        form=EmailSendForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            post_url=request.build_absolute_uri(post.get_absolute_url())
            subject='{}({}) recommends you to read "{}"'.format(cd['name'],cd['email'], post.title)
            message='Read Post At: \n {}\n\n{}\' Comments:\n{}'.format(post_url,cd ['name'],cd['comments'])
            send_mail(subject,message,'sapan@blog.com',[cd['to']])
            sent=True
    else:
        form=EmailSendForm()
    return render(request,'blog/sharebymail.html',{'post':post,'form':form,'sent':sent})