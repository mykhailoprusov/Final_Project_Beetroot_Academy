from . import views
from django.urls import path


urlpatterns = [
    path('', views.start, name = 'start-page'),
    path('articles/breakfasts/',views.BreakfastPageView.as_view(), name= 'article-breakfasts'),
    path('articles/lunches/', views.LunchPageView.as_view(), name='article-lunches'),
    path('articles/dinners/', views.DinnerPageView.as_view(), name='article-dinners'),
    path('articles/supplements/', views.SupplementPageView.as_view(), name='article-supplements'),
    path('articles/protein/', views.ProteinPageView.as_view(), name='article-protein'),
    path('blog/',views.BlogPostsView.as_view(), name = 'blog-page'),
    path('blog/post/<int:pk>/',views.BlogPostsDetailsView.as_view(),name='post-details' ),
    path('blog/create/',views.CreateBlogPost.as_view(),name='blog-create'),
    path('blog/post/<int:pk>/update/',views.UpdateBlogPost.as_view(),name='post-update'),
    path('blog/post/<int:pk>/delete/',views.DeleteBlogPost.as_view(),name='post-delete'),
    path('blog/post/profile/<int:pk>',views.PostProfileDetailsView.as_view(),name='post-profile'),
    path('contacts/',views.ContactsPageView.as_view(),name='contact-page')

]

