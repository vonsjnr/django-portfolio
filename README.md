# django-portfolio

# Basic django commands

# Create a venv 
python3 -m venv .env

# Activate the venv
source .env/bin/activate

# Create a Django project (in venv)
django-admin startproject portfolio .

# Active session available on
http://localhost:8000

# Create a Django app called 'projects'
python manage.py startapp projects

# Register your app in settings.py
INSTALLED_APPS = [
	# django apps
	# my apps
	"projects",
]

# Dug your way through different URL configurations

# Create a view function that returns a HttpResponse object
def project_list(request):
    return HttpResponse("<h1>Aye!</h1>")

# Change the view function to render a template instead
def project_list(request)
    return render(request, "projects/index.html")

# Create a Django template containing HTML code
<body>
    <h1>Hello template!</h1>
</body>

# Understand the nested folder structure of templates

# Register your new template folder in settings.py
TEMPLATES = [
    {
        "DIRS": [os.path.join(BASE_DIR, "projects/templates"),]
    }
]

# Add Bootstrap styling to your app
<head>
    <link rel="stylesheet" href="link.com">
</head>

# Related errors with above instructions:
- PageNotFound,
- ModuleNotFoundError,
- ImproperlyConfigured,
- AttributeError,
- ValueError,
- TemplateDoesNotExist
