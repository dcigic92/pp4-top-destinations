from django.test import TestCase
from website.forms import CommentForm, PostForm, EditPostForm
from website.models import Comment, Post

class CommentFormTest(TestCase):
    def test_form_fields(self):
        form = CommentForm()
        self.assertEqual(form.Meta.model, Comment)
        self.assertEqual(form.Meta.fields, ('body',))

class PostFormTest(TestCase):
    def test_form_fields(self):
        form = PostForm()
        self.assertEqual(form.Meta.model, Post)
        self.assertEqual(form.Meta.fields, ('destination_name', 'country_of_destination', 'featured_image', 'content',))

class EditPostFormTest(TestCase):
    def test_form_fields(self):
        form = EditPostForm()
        self.assertEqual(form.Meta.model, Post)
        self.assertEqual(form.Meta.fields, ('featured_image', 'content',))