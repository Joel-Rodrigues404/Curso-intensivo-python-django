# # Em seguida percorremos essa lista com 12 meses

# for month in months:
#     # pegamos cada mes e passamos na funçao capitalize() que faz com que a string tenha a primeira letra maiuscula
#     capitalized_month = month.capitalize()
#     # Criamos uma rota de acordo com o padrado de rotas da funçao monthly_challenge()
#     """ 
#         path('<str:month>', monthly_challenge, name='month-challenge'),
#             challenges/nome_do_mes/
#     """
#     month_path = reverse("month-challenge", args=[month])
#     # Cria a lista de items com links html que sera imcrementada na list_items
#     list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

# # Cria uma lista ordenada com a list_items
# responce_data = f'<ul>{list_items}</ul>'
# # Retorna uma pagina "HTML" com a responce_data
# return HttpResponse(responce_data)