from django.shortcuts import render
#sometimes we might want to store some data on persite-visitor basis 

def index(request):

    context={
         
    } 
    return render(request,"cookiestest/index.html",context)

#Setting cookie is done by the set_cookie method called on Response Not request :
def set_cookies(request): #To save values inside cookies is called set:
    response=render(request,"cookiestest/page1.html")
    response.set_cookie(key='name',value='Max',max_age=60) # To save Time of  cookie,max_age:keeps our data till 60 Sec 
    response.set_cookie(key='family',value='jokar',max_age=60)  #To set a cookie we use response Class 
    response.set_cookie(key='age',value='42',max_age=60)
    return response

# 1 .To return datas from our cookie we need the following function 
# def get_cookies(request):
#     name=request.COOKIES['name']
#     family=request.COOKIES['family']
#     age=request.COOKIES['age']
#     context={
#         'name':name,
#         'family':family,
#         'age':age,
#     }
#     return render(request, "cookiestest/page2.html",context)

# 1 .To return datas from our cookie we need the following function 
def get_cookies(request):
    context={}
    if request.COOKIES.get('name'): #if you found fill them all with name , family age otherwise ,get the empty context :
        name=request.COOKIES['name']#ask(request) the browser to get cookies [name,family,age]
        family=request.COOKIES['family']
        age=request.COOKIES['age']
        context={
            'name':name,
            'family':family,
            'age':age,
        }
        return render(request, "cookiestest/page2.html",context)














