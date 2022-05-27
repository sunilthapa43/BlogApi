
from django.urls import path

#from .views import PostList ,  PostDetails, UserDetails, UserList


#better way is using routers
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, UserViewSet

#urlpatterns = [
   # path('', PostList.as_view()),
   # path('<int:pk>', PostDetails.as_view()),



    #path('user/', UserList.as_view()),
   # path('user/<int:pk>', UserDetails.as_view()),
#]
#


#contd..
router = SimpleRouter()
router.register('users', UserViewSet, basename= 'users')
router.register('posts', PostViewSet, basename = 'posts')
urlpatterns = router.urls