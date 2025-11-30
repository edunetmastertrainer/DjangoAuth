# DjangoAuth
Create project - myauth
Create App - userauth
open view.py
        **from django.shortcuts import render,redirect
        from django.contrib.auth.forms import UserCreationForm
        def register(request):
            if request.method == 'POST':
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('login')
            else:
                form = UserCreationForm()
            return render(request,'register.html',{'form':form})
        
        def dashboard(request):
            return render(request,'dashboard.html')**
Open urls.py 
         path('admin/', admin.site.urls),
          path('register/',views.register,name='register'),
          path("accounts/", include("django.contrib.auth.urls")),
          path('dashboard/',views.dashboard,name='dashboard')

Run command for makemigration and migrate

