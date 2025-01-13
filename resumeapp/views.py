from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Resume
from .forms import ResumeForm, UserRegisterForm


from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect unauthenticated users to the login page
    resumes = Resume.objects.filter(user=request.user)
    return render(request, 'home.html', {'resumes': resumes})






def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})



    

from django.shortcuts import render, redirect
from .models import Resume
from .forms import ResumeForm
from django.contrib.auth.decorators import login_required

@login_required
def create_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            # Save the form, creating a new resume
            new_resume = form.save(commit=False)
            new_resume.user = request.user  # Set the current user
            new_resume.save()
            
            # After saving the new resume, redirect to the view_resume page
            return redirect('view_resume', resume_id=new_resume.id)  # Pass the new resume's ID to the URL

    else:
        form = ResumeForm()

    return render(request, 'create_resume.html', {'form': form})


from django.shortcuts import render
from .models import Resume
from django.contrib.auth.decorators import login_required

@login_required
def view_resume(request, resume_id):  # Accept the resume_id from the URL
    try:
        # Get the specific resume for the logged-in user and the provided resume_id
        resume = Resume.objects.get(user=request.user, id=resume_id)
    except Resume.DoesNotExist:
        # If the resume doesn't exist, you can return a message or redirect as needed
        msg = "Resume not found."
        return render(request, 'view_resume.html', {'msg': msg})
    
    return render(request, 'view_resume.html', {'resume': resume})



from django.shortcuts import render, redirect
from .models import Resume
from .forms import ResumeForm
from django.contrib.auth.decorators import login_required

@login_required
def update_resume(request, resume_id):
    resume = Resume.objects.get(id=resume_id, user=request.user)
    
    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            # After successful update, redirect to the view_resume page with the updated resume_id
            return redirect('view_resume', resume_id=resume.id)  # Pass the resume_id to the URL
    else:
        form = ResumeForm(instance=resume)
    
    return render(request, 'update_resume.html', {'form': form})





@login_required
def delete_resume(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)  # Get resume by ID for the logged-in user
    if request.method == 'POST':
        resume.delete()  # Delete the resume
        return redirect('home')
    
    return render(request, 'delete_resume.html', {'resume': resume})



from django.contrib.auth.models import User  # Ensure User model is imported
from django.shortcuts import render, redirect

def forgot_password(request):
    return render(request, 'password_reset.html')


def resetpassword(request):
    uname = request.POST.get('uname')  # Use .get() to avoid KeyError if fields are missing
    newpwd = request.POST.get('password')
    try:
        user = User.objects.get(username=uname)  # Query the User model
        if user:
            user.set_password(newpwd)  # Use User's set_password method
            user.save()  # Save the updated password
            return redirect('login')  # Redirect to login page
    except User.DoesNotExist:  # Handle case where username doesn't exist
        return render(request, 'password_reset.html', {'msg': 'Username not found.'})
    except Exception as e:
        print(e)
        return render(request, 'password_reset.html', {'msg': 'Password not reset'})



# resumeapp/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from xhtml2pdf import pisa
from .models import Resume
from django.template.loader import render_to_string


def download_resume_pdf(request, resume_id):
    # Get the resume by ID
    resume = get_object_or_404(Resume, id=resume_id)
    
    # Create HTML content for the PDF
    html_content = render_to_string('view_resume.html', {'resume': resume})

    # Create a response with PDF content
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="resume_{resume.full_name}.pdf"'

    # Convert the HTML content to PDF
    pisa_status = pisa.CreatePDF(html_content, dest=response)

    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)

    return response
