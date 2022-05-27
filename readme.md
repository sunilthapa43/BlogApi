so there are many ways to authenticate:
1. basic
2. session/cookies:  user dont have to enter credentials after once logged in so it is secured as credentials dont have to be sent multiple times 
3. token auth: most popular, stateless, can be shared to multiple frontends
4. default auth




now lets add rest_framework.auth to installed apps and set authentication classes




for user registration we provide endpoint using allauth 
remember that auth token was used for login/logout/pwreset purpose

then add to settings:  django.contrib.sites , allauth, allauth.account, allauth.socialaccount, dj_rest_auth.registration

now add EMAIL_BACKEND and SITE_ID to settings



#final touch is schemas and documentations
 py manage.py generateschema > openapi-schema.yml