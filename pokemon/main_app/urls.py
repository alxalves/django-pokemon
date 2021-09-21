from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pokemon/', views.pokemon_index, name='index'),
    path('pokemon/<int:pokemon_id>/', views.pokemon_detail, name='detail'),
    path('pokemon/create/', views.PokemonCreate.as_view(), name="pokemon_create"),
    path('pokemon/<int:pk>/update/', views.PokemonUpdate.as_view(), name='pokemon_update'),
    path('pokemon/<int:pk>/delete/', views.PokemonDelete.as_view(), name='pokemon_delete'),
    path('pokemon/<int:pokemon_id>/add_move', views.add_move, name='add_move'),
    path('ribbons/', views.RibbonList.as_view(), name='ribbons_list'),
    path('ribbons/create/', views.RibbonCreate.as_view(), name='ribbons_create'),
    path('ribbons/<int:pk>/', views.RibbonDetail.as_view(), name='ribbons_detail'),
    path('ribbons/<int:pk>/update/', views.RibbonUpdate.as_view(), name='ribbons_update'),
    path('ribbons/<int:pk>/delete/', views.RibbonDelete.as_view(), name='ribbons_delete'),
    path('pokemon/<int:pokemon_id>/assoc_ribbon/<int:ribbon_id>/',
         views.assoc_ribbon, name="assoc_ribbon"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup')
]

