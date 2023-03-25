from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'index.html')
def analyze(request):
    djtext=request.POST.get('text','default')
#Check checkboc values
    removepunc=request.POST.get('removepunc','off')
    uppercase=request.POST.get('uppercase','off')
    new_line_remover=request.POST.get('new_line_remover','off')
    analyzed=""
    purpose=""
#Check Which Checkbox
    if removepunc == "on":
        punctuations='''~!@#$%^&*()_+-=|\]}[{'";:/?.>,<}]'''
        for char in djtext:
            if char not in punctuations:
                analyzed =analyzed+char
        djtext=analyzed
        purpose=purpose+"Remove Punctution"
    if(uppercase=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        djtext=analyzed
        purpose=purpose+" Upper Case"
    if(new_line_remover=="on"):
        analyzed=""
        for char in djtext:
            if char !='\n' and char !='\r':
                analyzed=analyzed+char
        purpose=purpose+ " New Line Remover"        
    ajju={'purpose':purpose,'analyzed_text':analyzed}
        
    if(removepunc !="on" and uppercase !="on"   and new_line_remover !="on"):
        return HttpResponse("Please Select One")
        
    return render(request,'analyze.html',ajju)
def nav(request):
    return render(request,'nav.html')
def about_us(request):
    return render(request,'about_us.html')
def contact_us(request):
    return render(request,'contact_us.html')
