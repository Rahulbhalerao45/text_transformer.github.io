from os import remove
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
        return render(request,'index.html')
def analyze(request):
    
    djtext=request.POST.get('cool','default')
    removepunc=request.POST.get('removepunc','off')
    capitalized=request.POST.get('capitalized','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    charcount=request.POST.get('charcount','off')
    if removepunc == "on":
        analyzed=" "
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char  not in punctuations:
                analyzed+=char
               
        parameters={'purpose':'Remove punctions','analyzed_text':analyzed} 
        djtext=analyzed 
    if capitalized=="on":
        analyzed=" "
        for char in djtext:
            analyzed+=char.upper()
              
        
        parameters={'purpose':'Capitalize sentence','analyzed_text':analyzed}
        djtext=analyzed
     
    if newlineremover=="on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
                 
                
        parameters={'purpose':'Removing new lines','analyzed_text':analyzed}
        djtext=analyzed         
    if spaceremover=="on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
                
                
        parameters={'purpose':'Spaces removed','analyzed_text':analyzed}
        djtext=analyzed  
    if charcount=="on":
        count=0
        for char in djtext:
            if char!="":
                count+=1
          
        parameters={'purpose':'character count','analyzed_text':count} 
        analyzed=count
        djtext=analyzed     
    
    if(removepunc!="on"and charcount!="on"and newlineremover!="on"and spaceremover!="on" and capitalized!="on"  ):
        return HttpResponse("Eror: Please select atleast one object")   
        
        

    return render(request,'analyze.html',parameters)  
        
def aboutus(request):
    return render(request,'about.html')
def contactus(request):
    return render(request,'contact.html')
                    
            
    
    

   

    