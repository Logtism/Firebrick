# Commands

These are all the commands that can be used with Firebrick.

## Running commands

To run any of these commands simply do `python manage.py command_name` some commands may need you to supply args but this will be mentioned in the commands description

## startaccountsapp

This command generates a `accounts` app in your project to handle authnetication, new user creation and add new commands to the `User` model.

You will need to add the follow to your `settings.py` file

##### In `INSTALLED_APPS` add:
- `'crispy_forms',`
- `'accounts.apps.AccountsConfig',`

##### At the bottom add
- `CRISPY_TEMPLATE_PACK = 'bootstrap4'`
- `USERNAME_LENGTH_MIN = 3`
- `USERNAME_LENGTH_MAX = 16`
- `USERNAME_VALID_CHARS = '^[0-9a-zA-Z_]*$'`


##### You will also need to add the following imports to your projects main `urls.py` file:
- `from django.contrib.auth import views as auth_views`
- `from accounts import views as accounts_views`


##### And the following to the `urlpatterns`:
- `path('register/', accounts_views.register, name='register'),`
- `path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),`
- `path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),`



## LoadFixtures

This command loads all fixtures in apps `fixtures/{app name}`.


## DumpFixtrues

This command dumps data from all models (except for django models) and puts them in the `fixtures/{app name}` inside that app.
