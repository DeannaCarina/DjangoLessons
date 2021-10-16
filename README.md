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
Period at the end to signify we want project in current directory
May need to reorder files/folders

To run locally:
> python3 manage.py runserver