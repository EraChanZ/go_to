from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from .models import *

zabit = 0
sdelal = 0
# Create your views here.
def my(request):
    global zabit,sdelal
    azaz = request.POST.get('key')
    clear = request.POST.get('clear')
    do = request.POST.get('do')
    noto = request.POST.get('not')
    if noto:
        zabit += 1
        objects = Dann.objects.all()
        objects[int(noto) - 1].delete()
    if do:
        sdelal += 1
        objects = Dann.objects.all()
        objects[int(do)-1].delete()
    if clear:
        objects = Dann.objects.all()
        objects.delete()
    if azaz:

        # data = request.objects.all()
        D = Dann(kek=azaz)

        D.save()

    dannie = Dann.objects.all()

    return render(request, "index.html", context={"list": dannie,"zabil":zabit,"sdelano":sdelal})


def test(request):
    key = request.POST.get("key")
    if key:
        p = Person(first_name=key)
        p.save()
    return HttpResponse("LOL")
