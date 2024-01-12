from django.test import TestCase
from website.models import Country, Post, Comment
from django.contrib.auth.models import User


class CountryModelTest(TestCase):
    def test_str_representation(self):
        country = Country(name="Test Country")
        self.assertEqual(str(country), "Test Country")


class PostModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        country = Country.objects.create(name="Test Country")
        self.post = Post.objects.create(
            destination_name="Test Post",
            slug="test-post",
            country_of_destination=country,
            author=user,
            content="Test content",
        )

    def test_str_representation(self):
        self.assertEqual(str(self.post), "Test Post")


class CommentModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        country = Country.objects.create(name="Test Country")
        post = Post.objects.create(
            destination_name="Test Post",
            slug="test-post",
            country_of_destination=country,
            author=user,
            content="Test content",
        )
        self.comment = Comment.objects.create(
            post=post, author=user, body="Test comment"
        )

    def test_str_representation(self):
        self.assertEqual(str(self.comment), "Comment Test comment by testuser")