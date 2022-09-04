from django.urls import path

from app.views import RecordsApiView, RecordsDetailApiView

urlpatterns = [
    path('records/', RecordsApiView.as_view()),
    path('records/<int:records_id>/', RecordsDetailApiView.as_view()),
]
