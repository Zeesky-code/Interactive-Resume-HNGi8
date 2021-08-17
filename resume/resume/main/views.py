from django.shortcuts import render



def item_list(request):
    return render(request, 'home-page.html', context)
