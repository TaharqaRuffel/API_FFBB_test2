from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ffbbapi import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'members', views.MemberViewSet)
router.register(r'clubs', views.ClubViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'places', views.PlaceViewSet)
router.register(r'organizers', views.OrganizerViewSet)
router.register(r'championships', views.ChampionshipViewSet)
router.register(r'pools', views.PoolViewSet)
router.register(r'days', views.DayViewSet)
router.register(r'matches', views.MatchViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
