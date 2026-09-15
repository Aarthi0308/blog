from django.shortcuts import redirect, render
from .models import blog ,category
from django.http import HttpResponse
def post_by_category(request,category_id):
    # fetch the post belongs to the category by using category_id
    posts=blog.objects.filter(status="published",category=category_id)
    # use try and expect block we wnt to some custom  action ig cateegory does not exists
    try:
     category1=category.objects.get(pk=category_id)
    except:
       return redirect('home')
    # use get_object_or_404 when you want to show 404 error page if the category does not exists
    #  category=get_object_or_404(category,pk=category_id)
    context={
          'posts':posts,
          'category':category1,
      }
    return render(request,'post_by_category.html',context)


