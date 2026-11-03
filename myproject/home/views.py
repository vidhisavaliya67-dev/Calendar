from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import calendar

def home(request):
    yy=2026
    mm=4

    cal=calendar.month(yy,mm)
    return render(request,'Home.html',{'cal':cal})

# def Home(request):
#     values={'name':'amit','age':25,'city':'pune'}
#     return render(request,'Home.html',values)
# def home(request):
#     return HttpResponse("Hello!, welcome to the home page!")

# def about(request):
#     return HttpResponse("THis is the about page")

# def contact(request):
#     return HttpResponse("This is the contact page")

# def services(request):
#     return HttpResponse("This is our good services.")

# def index(request):
#     return HttpResponse("""
#     <h1>Welcome to my project</h1>
#     <a href="https://www.google.com/?zx=1793341527121">Open Google</a><br><br>
#     <a href="https://www.facebook.com/">Open Facebook</a><br><br>
#     <a href="https://mail.google.com/mail/u/0/">Open Gmail</a><br><br>
#      <a href=https://in.search.yahoo.com/?fr2=inr">Open Yahoo</a><br><br>
# """) 

# def index(request):
#     return HttpResponse("""
#     <nav style="background-color: black; padding:15px;">
#     <a href="/" style="color:white; margin:20px;">Home</a>
#     <a href="/about/" style="color:white; margin:20px;">About</a>
#     <a href="/contact/" style="color:white; margin:20px;">Contact<a/>
#     <a href="/service/" style="color:white;margin:20px;">Services</a>
#     </nav>
#     <h1>Home Page</h1>""")

# def about(request):
#     return HttpResponse("""
#     <nav style="background-color: black; padding:15px;">
#     <a href="/" style="color:white; margin:20px;">Home</a>
#     <a href="/about/" style="color:white; margin:20px;">About</a>
#     <a href="/contact/" style="color:white; margin:20px;">Contact<a/>
#     <a href="/service/" style="color:white;margin:20px;">Services</a>
#     </nav>
#     <h1>about Page</h1>""")

# def contact(request):
#     return HttpResponse("""
#     <nav style="background-color: black; padding:15px;">
#     <a href="/" style="color:white; margin:20px;">Home</a>
#     <a href="/about/" style="color:white; margin:20px;">About</a>
#     <a href="/contact/" style="color:white; margin:20px;">Contact<a/>
#     <a href="/service/" style="color:white;margin:20px;">Services</a>
#     </nav>
#     <h1>contact Page</h1>""")

# def service(request):
#     return HttpResponse("""
#     <nav style="background-color: black; padding:15px;">
#     <a href="/" style="color:white; margin:20px;">Home</a>
#     <a href="/about/" style="color:white; margin:20px;">About</a>
#     <a href="/contact/" style="color:white; margin:20px;">Contact<a/>
#     <a href="/service/" style="color:white;margin:20px;">Services</a>
#     </nav>
#     <h1>service Page</h1>""")


# def index(request):
    # return HttpResponse("""
#     <style>
#     body{
#     margin:0;
#     font-family:Arial,sans-serif;
#     background-color: white;
#     text-align:center;
#     }
#     nav{
#     background-color: #222;
#     padding:20px;
#     }
#     nav a{
#     color:white;
#     text-decoration:none;
#     margin:0 20px
#     font.size:18px;
#     }
#     nav a:hover{
#     color: #00c6ff;
#     }
#     .hero{
#     padding:40px;
#     }
#     .hero img{
#     width:100%;
#     height:500px;
#     object-fit:cover;
#     border-radius:20px;
#     }
#     h1{
#     color: #222
#     font-size:40px;
#     }
#     p{
#     color: #666;
#     font-size:18px;
#     }
#     .btn{
#     display:inline-block;
#     background-color: #007bff;
#     color:black;
#     padding:12px 25px;
#     margin-top:15px;
#     border-radius:8px;
#     text-decoration:none;
#     }
#     btn.hover{
#     background-color: #0056b3;
#     }
#     </style>
# <nav>
# <a href="/"Home</a>
# <a href="/about">About</a>
# <a href="/contact">Contact</a>
# </nav>
# <div class="hero">
# <img src="https://images.unsplash.com/photo-1497366811353-6870744d04b2?q=80&w=1169&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D"
# alt="Beautiful office">
# <h1>Welcome to My Website</h1>
# <p> Learn Django and build amazing websites</p>
# <a class="btn" href="/about/">Explore More</a></div>""")

