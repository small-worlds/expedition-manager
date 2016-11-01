# Small Worlds Expeditions Expedition-Manager

### Making managing expeditions easy since 3302.

ExMan is written using [Django Rest Framework](http://www.django-rest-framework.org/), on top of [Django](https://www.djangoproject.com/), with RESTful auth provided by [Djoser](https://github.com/sunscrapers/djoser). Documentation available at the respective projects' links.

## Requirements

* Python 2.7, 3.4, or 3.5. __NOTE__: ExMan was developed with 3.5 - backwards compatibility is untested!
* Python Pip
* (Optional:) virtualenv (and virtualenvwrapper)

Production database requirements are TBD, but will likely be PostgreSQL. Development currently uses sqlite3.

## Development

How to get started with the app!

1. Clone repository
2. Create a virtualenv, because virtualenvs are amazeballs.
3. `pip install -r requirements.txt`
4. Copy `exman/settings.py.example` to `exman/settings.py` and edit. It does provide some sane defaults, but you may want to look over things to be safe.
4. `python manage.py createsuperuser` and go through the prompts, to create a super user. This user will have full admin permissions to the app, and can access the backend Django admin view (located at `/admin`).
5. `python manage.py runserver` to run the server. It will run on `127.0.0.1:8000`.

## Caveats

* While the app is useable, we're still very actively developing it.
* This is only the backend API - a frontend is in development separately. Hooray separation of duty!
* The defaults in `exman/settings.py.example` are sane defaults __FOR DEVELOPMENT ONLY__ and should __NOT__ be used in production!
* The `auth` endpoint does not appear on the root view. This is a known issue and will require a decent amount of work to fix (as it involves writing a custom root view instead of relying on the `DefaultRouter` built-in view). Rest assured - it's there and useable!
* Auth relies on the built-in DRF token authentication. Request a login token by posting a username/password combo to the /auth/login/ route. See [Djoser](https://github.com/sunscrapers/djoser) for full documentation of the auth endpoint.
* The built-in development server does not support HTTPS. This is being handled by nginx on the production server.
* If you're feeling particularly adventurous, we are using gunicorn to run the production server as a service. Scripts will be added Eventually™ (once they're cleaned up of my system-specific configs)
