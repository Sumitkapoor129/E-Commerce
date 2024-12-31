from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib import messages
from customer.models import Cart, Customer, Orders, Product
# Create your views here.
def home(request):
    products=Product.objects.all()
    context={"product":products}
    if request.user.is_authenticated:
        
        return render(request,'customers/loginhome.html',context)
    else:
        return render(request,'customers/home.html',context)


def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user:
            # Log the user in and redirect to the home page
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('customer:Home')  # Replace 'home' with the name of your home page route
        else:
            messages.error(request, "Invalid username or password")
    return render(request,'customers/login.html')
    
    
def register(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('password2')
        profile = request.FILES.get('profile_pic')
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('customer:register')
        
        if Customer.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('customer:register')
        
        if Customer.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('customer:register')
        
        
        user=Customer.objects.create(username=username,email=email,password=password,profile_pic=profile)
        login(request,user)
        return redirect('customer:Home')
    return render(request,'customers/register.html')

def profile(request):
    print(request.path)
    orders=Orders.objects.filter(user_id = request.user.id)
    total=0
    for order in orders:
        total += order.product.price
    return render(request,'customers/profile.html',{'orders':orders,'total':total})

def add_product(request):
    if request.method == 'POST':
        try:
            Product.objects.create(
                owner=request.user,
                name=request.POST.get("name"),
                price=request.POST.get("price"),
                quantity=request.POST.get("stock"),
                image=request.FILES.get("productImage"),
                description=request.POST.get("description")
            )
            return redirect("customer:Home")
        except Exception as e:
            print(e)
            return render(request,'customers/product.html')     
    return render(request,'customers/product.html')

def addtocart(request):
    if request.method=="POST":
        p_id=request.POST.get("addtocart")
        product=Product.objects.get(id=p_id)
        Cart.objects.create(user_id=request.user.id,product=product,quantity=1)
        print(request.user.id,request.user.username)
        return redirect("customer:Home")
    
def cart(request):
    orders=Cart.objects.filter(user_id = request.user.id)
    total=0
    for order in orders:
        total += order.product.price
    return render(request,"customers/cart.html",{"orders":orders,"total":total,"tax":total/10})    