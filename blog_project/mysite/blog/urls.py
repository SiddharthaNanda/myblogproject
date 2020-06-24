from django.urls import path,re_path
from blog import views


urlpatterns=[
    path('about/',views.AboutView.as_view(),name='about'),
    path('tryme/',views.TrymeView.as_view(),name='tryme'),
    re_path(r'^post/(?P<pk>\d+)/detail/$',views.PostDetailView.as_view(),name='post_detail'),
    path('',views.PostListView.as_view(),name='post_list'),
    re_path(r'^post/create/$',views.PostCreateView.as_view(),name='post_create'),
    re_path(r'^post/(?P<pk>\d+)/update/$',views.PostUpdateView.as_view(),name='post_update'),
    re_path(r'^post/(?P<pk>\d+)/delete/$',views.PostDeleteView.as_view(),name='post_delete'),
    path('drafts/',views.DraftListView.as_view(),name='post_draft_list'),
    re_path(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'),
    re_path(r'^post/(?P<pk>\d+)/approve/$',views.approve_comment,name='approve_comment'),
    re_path(r'^post/(?P<pk>\d+)/remove/$',views.remove_comment,name='remove_comment'),
    re_path(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish')
]
