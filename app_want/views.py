from django.shortcuts import render, redirect
from .models import wanted, bando, texto, usuario
from .forms import escreverForm, CadastrarForm
from django.http import HttpResponse
from django.contrib.auth.forms import User
from django.contrib.auth.hashers import make_password

def inicial(request):
    wanteds=list(wanted.objects.all())
    lista=[]
    listinha=[]
    for i in wanteds:
        if len(listinha) == 5:
            lista.append(listinha)
            listinha=[]
        elif i == wanteds[-1]:
            lista.append(listinha)
        listinha.append(i)

    for i in lista:
        for x in i:
            if x.Nome == "Stefan":
                i.remove(x)

    bandos=bando.objects.all()
    
    return render(request, 'app_want/inicial.html', {'todos':lista})

def Cartaz(request,id):
    perso=wanted.objects.get(pk=id)
    if texto.objects.filter(personagem=perso):
        text=texto.objects.get(personagem=perso)
    else:
        text='vazio'
    print(perso,text)
    return render(request, 'app_want/cartaz.html', {'perso':perso,'texto':text})

def Sobre(request):
    criador=wanted.objects.get(Nome='Stefan')
    return render(request, 'app_want/sobre.html', {'criador':criador})

def pesquisar(request):
    if request.method=='POST':
        pesquisa=request.POST['entrada']
        if len(pesquisa) != 0:
            if wanted.objects.filter(Nome=pesquisa):
                personagem=wanted.objects.get(Nome=pesquisa)
                msg=None
            elif wanted.objects.filter(Nome=pesquisa[0].upper()+pesquisa[1:]):
                funciona=pesquisa[0].upper()+pesquisa[1:]
                personagem=wanted.objects.get(Nome=funciona)
                msg=None
            else:
                personagem='n encontrado'
                msg='PERSONAGEM NÃO ENCONTRADO!'
            
            
        else:
            pesquisa=True 
            personagem='n encontrado'
            msg='DIGITE ALGO PARA PESQUISAR'
            print('msg: ',msg,'personagem',personagem,'pesquisa',pesquisa)
    
    return render(request, 'app_want/inicial.html', {'perso':personagem,'pesquisa':pesquisa,'msg':msg})       

def escrever(request,id):
    if request.method=='GET':
        form=escreverForm()
        perso=wanted.objects.get(pk=id)
        return render(request,'app_want/escrever.html',{'form':form,'perso':perso})
    elif request.method == 'POST':
        text=texto()
        perso=wanted.objects.get(pk=id)
        text.titulo=request.POST['titulo']
        text.corpo=request.POST['corpo']
        text.personagem=perso
        text.autor=usuario.objects.get(user=request.user)
        text.save()
        usu=usuario.objects.get(user=request.user)
        usu.pontos+=10
        usu.save()

        return Cartaz(request,id)

def publicar(request,id):
    text=texto.objects.get(pk=id)
    if text.status == 'publicado':
        text.status='analise'
        text.save()
    else:
        text.status='publicado'
        text.save()

    return gerencia(request)

def top8(lista):
    pontos=[]
    for i in lista:
        pontos.append(i.pontos)
    crescente=sorted(pontos)
    rank=[]
    for i in crescente:
        for x in lista:
            if i == x.pontos and x not in rank:
                rank.insert(0,x)
    top=[]
    listinha=[]
    for i in rank[:9]:
        if len(listinha) == 4:
            top.append(listinha)
            listinha=[]
        elif i == rank[-1]:
            top.append(listinha)
        listinha.append(i)

    return top

def topusu(request):
    usu=usuario.objects.get(user=request.user)
    usuarios=usuario.objects.all()
    top=top8(usuarios)
    return render(request,'app_want/topusuarios.html',{'usuarios':top,'usu':usu})

def cadastrar(request):
    if request.method=="GET":
        form=CadastrarForm()
        return render(request, 'app_want/cadastrar.html',{'form':form})
    elif request.method == "POST":
        nome=request.POST['nome']
        user=User()
        user.username=nome
        user.password=make_password(request.POST['senha'])
        user.save()
        usu=usuario()
        usu.nome=nome
        usu.user=user
        usu.pontos=0
        usu.save()
        return redirect('login')

def gerencia(request):
    textos=texto.objects.all()
    analise=texto.objects.filter(status='analise')
    usuarios=usuario.objects.all()
    return render(request, 'app_want/gerencia.html',{'todos':textos,'analise':analise,'usuarios':usuarios})

def addPontos(request,id):
    if request.method=='POST':
        usu=usuario.objects.get(pk=id)
        add=int(request.POST['addPontos'])
        usu.pontos+=add
        usu.save()

        return gerencia(request)