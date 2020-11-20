from rest_framework.routers import DefaultRouter
from . import views

app_name = "boards"

router = DefaultRouter()
router.register("", views.BoardsViewSet)

urlpatterns = router.urls
