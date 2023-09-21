from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

# Uma especie de database se fosse um model seria tipo month.name
monthly_challenges = {
    "january":"january",
    "february":"february",
    "march":"march",
    "april":"april",
    "may":"may",
    "june":"june",
    "july":"july",
    "august":"august",
    "september":"september",
    "october":"october",
    "november":"november",
    "december":"december",
}

# Create your views here.

# View que renderiza a pagina inicial onde e mostrada os links para todas as tarefas de todos os meses
def index(request):

    # De acordo com o dict nois estamos pegando todos os months e os colocando em uma lista
    months = list(monthly_challenges.keys())

    return render(request, 'challenges/index.html', {'months':months})

# View que que relaciona um numero de 1 a 12 com os meses do ano
def monthly_challenge_by_number(request, month):
    # De acordo com o dict nois estamos pegando todos os months e os colocando em uma lista
    months = list(monthly_challenges.keys())
    # Tranforma o valor em valor positivo 
    month = abs(month)

    # Verifica se os o numero e maior que 12 nesse caso se for retorna uma mensagem de erro
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    # Relaciona o numero com os nomes dos meses para ser passado na url
    redirect_moth = months[month-1] #Menos 1 pois uma lista começa no indice [0]   
    # Define a rota para a view de monthly_challenge
    redirect_path = reverse("month-challenge", args=[redirect_moth])
    # Redireciona para monthly_challenge
    return HttpResponseRedirect(redirect_path)

# View para rederizaçao de uma tarefa de acordo com um mes
def monthly_challenge(request, month):
    # Tenta pegar a informaçao do mes 
    try:
        # Pega o value do dict pela chave passada pelo month
        challenge_text = monthly_challenges[month]
        # Retorna o valor em formato "HTML"
        # responce_data = f'<h1>{challenge_text}</h1>'
        return render(request, 'challenges/challenge.html', {'text':challenge_text,
                                                             'month_name':month})
    # Se der algum erro ele faz isso
    except:
        # responce_data =  render_to_string("404.html")
        # return HttpResponseNotFound(responce_data)
        raise Http404()