from django.urls import include, path

from school.views import students_list
from website import settings as psettings

if psettings.DEBUG is True:
    import debug_toolbar

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('', students_list, name='students'),

]
