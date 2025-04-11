# main/views.py
from django.shortcuts import render, redirect
from .models import Event
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """
    Handles user registration by displaying and processing the registration form.

    Purpose:
        Allows new users to create an account on the platform using Django's built-in 
        UserCreationForm. On successful registration, users are redirected to the login page.

    Impact:
        Saves a new user instance to the database, contributing to user authentication 
        and personalized access to other views.

    Interaction:
        - Uses Django's UserCreationForm for validation and saving the user.
        - Redirects to the 'login' view upon successful registration.
        - Renders the 'main/register.html' template with form context on GET or invalid POST.

    Args:
        request (HttpRequest): The HTTP request from the client.

    Returns:
        HttpResponse: The rendered registration page or a redirect to the login page.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})


def events(request):
    """
    Displays a list of upcoming events sorted by date.

    Purpose:
        Provides users with a view of all future events, helping them stay informed and engaged.

    Impact:
        Retrieves data from the Event model, improving user engagement and interaction 
        by presenting scheduled activities or programs.

    Interaction:
        - Queries the Event model to get all events ordered by their scheduled date.
        - Passes the result to the 'main/events.html' template for display.

    Args:
        request (HttpRequest): The HTTP request from the client.

    Returns:
        HttpResponse: The rendered events page with a list of upcoming events.
    """
    upcoming_events = Event.objects.order_by('date')
    return render(request, 'main/events.html', {'events': upcoming_events})


def home(request):
    """
    Renders the application's home page.

    Purpose:
        Serves as the landing page for the application, providing an introduction or
        overview for both new and returning users.

    Impact:
        Enhances user experience by offering a central starting point for navigating
        the website.

    Interaction:
        - Loads static content from 'main/home.html'.
        - May include navigation to other key views like events, about, or contact.

    Args:
        request (HttpRequest): The HTTP request from the client.

    Returns:
        HttpResponse: The rendered home page.
    """
    return render(request, 'main/home.html')


def about(request):
    """
    Renders the About page containing information about the organization or website.

    Purpose:
        Informs users about the mission, vision, or background of the entity 
        behind the application.

    Impact:
        Builds trust and transparency with users by offering context about the 
        application's purpose and creators.

    Interaction:
        - Displays content from 'main/about.html'.
        - Can include links to team members, history, or objectives.

    Args:
        request (HttpRequest): The HTTP request from the client.

    Returns:
        HttpResponse: The rendered about page.
    """
    return render(request, 'main/about.html')


def contact(request):
    """
    Renders the Contact page to allow users to reach out or find contact information.

    Purpose:
        Provides users with a channel to communicate, inquire, or request support.

    Impact:
        Encourages engagement and feedback from users, fostering trust and 
        responsiveness in the application's community.

    Interaction:
        - Displays static or interactive content from 'main/contact.html'.
        - May include a contact form or direct contact details like email and phone.

    Args:
        request (HttpRequest): The HTTP request from the client.

    Returns:
        HttpResponse: The rendered contact page.
    """
    return render(request, 'main/contact.html')
