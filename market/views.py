from django.shortcuts import render


def index(request):
    return render(request, 'market/index.html')



def product2(request: str):
    context = {
        
    }
    return render(request, 'market/product.html', context)


def product(request: str, prod_id: str):
    context = {
        "prod_id":prod_id,
    }
    return render(request, 'market/product.html', context)




def products(request):
    return render(request, 'market/products.html')


