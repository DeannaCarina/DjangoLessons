# Django Lessons

### Lesson 1 - Getting set up
1. Install Django using CLI
> pip3 install django

To check version of python:
> python[tab]

To check installed packages:
> 1. cd /workspace/.pip-modules/lib/python3.8/site-packages/
> 2. ls -la

To get back to previous directory:
> cd -

To start a project:
> django-admin startproject {project_name} .

Period at the end to signify we want project in current directory<br>
May need to reorder files/folders

To run locally:
> python3 manage.py runserver


### Lesson 2 - URLs

Creating an app:
> python3 manage.py startapp {app_name}

In views.py add in a test function:
> def say_hello(request):<br>
>    return HttpResponse("Hello!")

In urls.py:
1.  import the test function with other imports:
    > from to_do.views import say_hello

2. add a new path function in url patterns:
    > path('hello/', say_hello, name='hello')

3. To test it's working, navigate to the locally hosted server, and add /hello to the end of the url


### Lesson 3 - Templates

1. In the app folder which we created in Lesson 2, create a new folder called 'templates'
2. Inside of the 'templates' folder, create another folder called '{app_name}' from Lesson 2 (in this case 'to_do')
3. Inside that folder, create a file called '{app_name}_list.html' (in this case to_do_list.html)
4. Add boilerplate to this HTML file (type '!' and press enter)
5. Test file by adding some valid HTML within the body

In views.py:
1. Remove the return statement from the say_hello function
2. Replace with:
> return render(request, 'to_do/to_do_list.html')
3. Rename function to something more applicable if necessary
4. Remove unused HttpResponse import

In urls.py:
1. Remore the 'hello/' url path and replace with an empty string
2. Update function name and name parameter
3. Update imports to match function name

In settings.py:
1. In the INSTALLED_APPS section, add the new app 'to_do' under the other pre-installed apps

Test the locally hosted server to see if template has rendered.
