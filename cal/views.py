from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Calculation

def calculator_view(request):
    return render(request, 'calculator.html')

@csrf_exempt
def calculate_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        expression = data.get('expression')
        result = data.get('result')
        
        # Save to database
        Calculation.objects.create(
            expression=expression,
            result=result,
            user=request.user if request.user.is_authenticated else None
        )
        
        return JsonResponse({'status': 'success'})

def history_api(request):
    calculations = Calculation.objects.filter(
        user=request.user if request.user.is_authenticated else None
    ).order_by('-created_at')[:10]
    
    return JsonResponse({
        'history': [
            {'expression': calc.expression, 'result': calc.result}
            for calc in calculations
        ]
    })
