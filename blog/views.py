from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

    #post_list takes a request and returns a function 'render'
    #that renders our template blog/post_list.html
    