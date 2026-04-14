from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, DriverViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'drivers', DriverViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = router.urls