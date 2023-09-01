# LIT-test-work

### Test work. Longevity InTime Test Tasks. Backend.
##### Stack
Django, Django REST Framework, drf-spectacular, gunicorn, redis, docker, docker-compose, postgresql, celery.
##### Install
To build the api open project folder in terminal and do the following (docker and docker-compose must be installed):
```sh
docker-compose up -d
```
Building will require some environment variables that listed in example.env file.

##### API endpoints
Default address is localhost:80 (80 omitted cause it is default http port).
```sh
GET http://localhost/api/v1/docs/ - Redoc documentation.
POST http://localhost/api/v1/users/ - register new user with email and password provided.
POST http://localhost/api/v1/users/login/ - provide email and password to receive OTP to provided email.
POST http://localhost/api/v1/users/login/confirm/ - provide email and OTP to reveice authentication Token.
GET http://localhost/api/v1/users/ - retrieve current user profile. Requires authorization.
PUT, PATCH http://localhost/api/v1/users/ - update user profile. Requires authorization.
DELETE http://localhost/api/v1/users/ - delete user profile. Requires authorization.
```
More info in Redoc documentation which was created automatically with drf-spectacular module.
