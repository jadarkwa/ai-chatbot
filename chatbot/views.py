from django.shortcuts import render
from django.http import JsonResponse
import openai

#test

openai.api_key = "sk-proj-BGkstxoJ10nEndYM6F8NT3BlbkFJAm67HqcZO6bk7iJT4efo"

def ask_openai(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    # Extract the response content
    answer = response.choices[0].message['content'].strip()
    return answer

# Create your views here.
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        try:
            response = ask_openai(message)
            return JsonResponse({'message': message, 'response': response})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return render(request, 'chatbot.html')
