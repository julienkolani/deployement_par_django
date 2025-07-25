from django.shortcuts import render

def base(request):
    return render(request, 'base.html')

def sum_numbers10(request):
    # Calcul de la somme des nombres de 1 à 50
    total = sum(range(1, 10))
    
    # Renvoyer le résultat dans un template
    return render(request, 'sum_template.html', {'total': total})

def sum_numbers100(request):
    # Calcul de la somme des nombres de 1 à 50
    total = sum(range(1, 100))
    
    # Renvoyer le résultat dans un template
    return render(request, 'sum_template.html', {'total': total})

def sum_numbers1000(request):
    # Calcul de la somme des nombres de 1 à 50
    total = sum(range(1, 1000))
    
    # Renvoyer le résultat dans un template
    return render(request, 'sum_template.html', {'total': total})

def sum_numbers10000(request):
    # Calcul de la somme des nombres de 1 à 50
    total = sum(range(1, 10000))
    
    # Renvoyer le résultat dans un template
    return render(request, 'sum_template.html', {'total': total})
