from django.shortcuts import render


def moscow_map(request):
    return render(request, "index.html")
