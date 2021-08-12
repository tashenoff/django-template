from django.shortcuts import render


def index(request):
    # bbs = Bb.objects.all()
    # rubrics = Rubric.objects.all()
    # context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'main/index.html')
