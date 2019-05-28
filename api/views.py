from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import base64
import random
import string
from .models import *
from django.http import JsonResponse
@csrf_exempt
def index(request):
    if request.method == "POST":
        data = request.body
        data = json.loads(data[0:len(data)])
        c = Category.objects.get(pk=1)
        temp = len('data:image/jpeg;base64,')
        for d in data:
            d = d[temp:len(d)]
            imgdata = base64.b64decode(d)
            filename = randomString()+'.jpg'  # I assume you have a way of picking unique filenames
            with open('media/'+filename, 'wb') as f:
                f.write(imgdata)
            i = Images.objects.create(category=c, file=filename)
            i.save()
        return JsonResponse({'data': 'Success'})
    return render(request, 'index.html')

def randomString(stringLength=5):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
