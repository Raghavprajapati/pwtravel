from django.shortcuts import render

def homepage(request):
    return render(request,'index.htm')
def header(request):
    return render(request,'header.htm')
def footer(request):
    return render(request,'footer.htm')