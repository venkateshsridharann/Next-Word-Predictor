from django.shortcuts import render

def textbox_page(request):
    return render(request, 'textboxapp/textbox.html')