from django.test import TestCase
from django.urls import reverse
from website.models import Country, Post
from django.contrib.auth.models import User


class PostListViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'website/index.html')


class PostDetailViewTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        country = Country.objects.create(name='Test Country')
        self.post = Post.objects.create(
            destination_name='Test Post',
            slug='test-post',
            country_of_destination=country,
            author=user,
            content='Test content'
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/post/Test%20Country/test-post/')
        self.assertEqual(response.status_code, 404)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('post_detail', args=['Test Country', 'test-post']))
        self.assertTemplateUsed(response, 'website/post_detail.html')