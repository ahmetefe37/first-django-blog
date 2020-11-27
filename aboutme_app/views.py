from django.shortcuts import render


def aboutme_view(request):
    context = {

    }
    return render(request, "aboutme.html", context)
