from django.shortcuts import render
from django.http import HttpResponse
from stegano import lsb

def encode_text(request):
    if request.method == 'POST':
        text = request.POST['text']
        image = request.FILES['image']
        secret_image = lsb.hide(image, text)
        
        response = HttpResponse(content_type='image/png')
        response['Content-Disposition'] = 'attachment; filename="encoded_image.png"'
        secret_image.save(response, format='PNG')
        return response
    
    return render(request, 'steganoApp/encode.html')

def decode_text(request):
    if request.method == 'POST':
        image = request.FILES['image']
        decoded_text = lsb.reveal(image)
        return render(request, 'steganoApp/result.html', {'result': decoded_text})
    
    return render(request, 'steganoApp/decode.html')
