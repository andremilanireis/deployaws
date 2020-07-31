from django.shortcuts import render, redirect
from crud.models import Loja, Instrumento
from crud.forms import InstrumentoCreationForm

def loja(request):

    loja_atual = Loja.objects.get(nome='Guitar Center')

    context = {'loja': loja_atual}

    return render(request, 'loja.html', context)

def instrumento_detail(request, pk):

    instrumento_atual = Instrumento.objects.get(id=pk)

    context = {'instrumento': instrumento_atual}

    return render(request, 'instrumento_detail.html', context)


def create_instrumento(request, pk):

    loja_atual = Loja.objects.get(id=pk)                        #armazenar a loja do novo instrumento

    instrumento_form = InstrumentoCreationForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':                          #checa se o formulário foi enviado
        if instrumento_form.is_valid():                   #checa se os valores do formulario sao validos
           novo_instrumento = instrumento_form.save()     #salva o novo objeto na variável novo_instrumento
           novo_instrumento.loja = loja_atual             #define a loja do novo_instrumento como a loja atual
           novo_instrumento.save()                        #cria de fato o novo instrumento no banco de dados
           return redirect('loja')                        #leva de volta pra página da loja


            

    context = {'instrumento_form': instrumento_form, 'loja': loja_atual}

    return render(request, 'create_instrumento.html', context)
    

def edit_instrumento(request, pk):

    instrumento_atual = Instrumento.objects.get(id=pk)

    instrumento_form = InstrumentoCreationForm(instance=instrumento_atual) 

    # Ao passar o objeto no atributo instance, o forms fica com os valores do objeto

    if request.method == 'POST':
        instrumento_form = InstrumentoCreationForm(request.POST, request.FILES, instance=instrumento_atual)
        if instrumento_form.is_valid():                      #checa se os valores do formulario são validos
            instrumento_form.save()                          #atualiza as informações do objeto pelos valores do forms
            return redirect('/loja/instrumentos/' + str(pk)) #leva de volta pra página do instrumento (agora atualizado)


    context = {'instrumento_form': instrumento_form, 'instrumento': instrumento_atual}

    return render(request, 'edit_instrumento.html', context)

def delete_instrumento(request, pk):
    instrumento = Instrumento.objects.get(id=pk)
    instrumento.delete()
    return redirect('loja') 




