from django.shortcuts import render
from .forms import ImageForm
import openai

# Create your views here.
def generate_image(request):
    image_url = ''
    form = None
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            openai.api_key = "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"
            prompt = request.POST.get('prompt')
            response = openai.Image.create(prompt=prompt)
            image_url = response['data'][0]['url']
            return render(request, 'image/index.html', {'image_url': image_url})     
    else:
        form = ImageForm()
    return render(request, 'image/index.html', {'form': form})
