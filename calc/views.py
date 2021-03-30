from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html',{'name':'Arpit Khare'});

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    sol=val1+val2
    return render(request, 'result.html',{'res':sol})
def convert(s):
  
    # initialization of string to ""
    new = ""
  
    # traverse in the string 
    for x in s:
        new += x 
  
    # return string 
    return new
   
def encrypt(request):
    plainText=request.POST['plainText']
    name=request.POST['name']
    key=request.POST['password']
    m=len(key)
    plainText=plainText.replace(" ","")
    plainText=plainText.lower()


    textList=[]
    i=0
    while i<len(plainText):
        textList.append(plainText[i:m])
        i=i+len(key)
        m=m+len(key)

    # print(textList)

    codeList=[]
    for item in textList:
        codeWord=[]
        for i in range(0,len(item)):
            code=(ord(item[i])-97+ord(key[i])-65)%26
            codeWord.append(chr(code+65))
        # print(codeWord)
        str=convert(codeWord)
        codeList.append(str)
    codeList=convert(codeList)
    # return codeList


    return render(request, 'result.html',{'res':codeList});


def decrypt(request):
    cipherText=request.POST['cipherText']
    
    key=request.POST['password']
    key=key.lower()
    codeList=[]
    cipherList=[]
    i=0
    m=len(key)
    while i<len(cipherText):
        cipherList.append(cipherText[i:m])
        i=i+len(key)
        m=m+len(key)
    for item in cipherList:
        codeWord=[]
        for i in range(0,len(item)):
            code=(ord(item[i])-65-ord(key[i])-65)%26
            codeWord.append(chr(code+97))
        # print(codeWord)
        str=convert(codeWord)
        codeList.append(str)
    codeList=convert(codeList)
    return render(request, 'result.html',{'res':codeList});
