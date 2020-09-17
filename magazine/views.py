from django.shortcuts import render

# Create your views here.
def post_list(request):
 name = '공유'
 response = render(request, 'magazine/post_list.html', {'name': name})
 return response