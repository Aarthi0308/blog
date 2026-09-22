from django.shortcuts import redirect, render,get_object_or_404
from .models import blog ,category 
from django.db.models import Q
from django.http import HttpResponse
def post_by_category(request,category_id):
    # fetch the post belongs to the category by using category_id
    posts=blog.objects.filter(status="published",category=category_id)
    # use try and expect block when  we wnt to some custom  action ig cateegory does not exists
    try:
     category1=category.objects.get(pk=category_id)
    except:
      # return redirect('home')
      #use redirect when we want to redirect to hoem but not showing error message
    # use get_object_or_404 when you want to show 404 error page if the category does not exists
     category1 = get_object_or_404(
    category,
    pk=category_id
)
  
    context={
          'posts':posts,
          'category':category1,
      }
    return render(request,'post_by_category.html',context)

def blogs(request,slug):
      single_blog=get_object_or_404(blog,slug=slug,status='published')
      context={
         'single_blog':single_blog,
      }
      return render(request,'blogs.html',context)

def search (request):
   keyword= request.GET.get('keyword')
   print('keyword==',keyword)
   blogs=blog.objects.filter(Q(title__icontains=keyword )| Q(short_description__icontains=keyword) | Q( blog_body__icontains=keyword ))
   print(blogs)
   context={
      'blogs':blogs,
      'keyword':keyword
   }
   return render(request,'search.html',context)

