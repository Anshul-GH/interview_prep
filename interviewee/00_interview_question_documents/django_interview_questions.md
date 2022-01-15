References: 
https://www.interviewbit.com/django-interview-questions/


1. Explain the Django Architecture?
- Django follows the MVT (Model View Template) pattern which is based on the Model View Controller architecture.
- MVT maintains its own convention so the controller is handled by the framework itself
- The template is the presentation layer - HTML file mixed with Django Template Language (DTL).
- The developer provides the model, the view and the template then maps it to a URL that is served to the end users.
***

2. Explain the Django project directory structure?
- manage.py: A command-line utility file that allows you to interact with your Django project
- __init__.py: An empty file that tells Python that the current directory should be considered as a Python package
- settings.py: Comparises the configurations of the current project like DB connections
- urls.py: All the urls of the project are present here
- wsgi.py: Entry point for the application which is used by the web servers to serve the project created
***

3. What are models in Django?
- A model in Django refers to a class that maps to a database table or database collection.
- Each attribute of the Django model class represents a database field.
- They are defined under <app_name>/models.py file
***

4. What are templates in Django or Django Template Language?
- Templates are integral part of Django MVT architecture
- They generally comparise of HTML, CSS and JavaScript in which dynamic variables and information are embedded with the help of views
***

5. Explain the functionality of various components of a Django project
- settings.py: Controls project settings
- urls.py: Tells Django which pages to build in response to a browser or URL request
- wsgi.py: Web Server Gateway Interface file helps Django serve our eventual web pages
- manage.py: Used for executing various 