from django.shortcuts import render
from translate import Translator
from django.contrib import messages

def home(request):
    translation = None
    if request.method == 'POST':
        text = request.POST.get('translate')
        language = request.POST.get('language')

        translator = Translator(to_lang=language)
        translation = translator.translate(text)

        messages.add_message(request, messages.INFO, 'Translating...')
        return render(request, 'main/home.html', {'translation': translation})

    # Clear any messages that might have been set during the last translation request
    if request.method == 'GET':
        messages.get_messages(request).used = True
    
    return render(request, 'main/home.html', {'translation': translation})
