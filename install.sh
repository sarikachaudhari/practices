!/bin/zsh

virtualenv ~/environment/PracticesWebEnv 

source ~/environment/PracticesWebEnv/bin/activate


pip install django

django-admin.py startproject Practices

