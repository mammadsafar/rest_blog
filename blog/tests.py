from django.test import TestCase
from django.shortcuts import reverse
from .models import Post
from django.contrib.auth.models import User
import os
import io

from PIL import Image


class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username="Test")
        cls.post1 = Post.objects.create(
            title='mohammad',
            text='Sample Text.',
            thumbnail='/home/mammadsafar/Pictures/Screenshot from 2022-05-08 18-04-28.png',
            author=cls.user,
            status=Post.STATUS_CHOICES[0][0]  # Published
        )
        cls.post2 = Post.objects.create(
            title='Post 2',
            text='Sample Text.',
            thumbnail='/home/mammadsafar/Pictures/Screenshot from 2022-05-08 18-04-28.png',
            author=cls.user,
            status=Post.STATUS_CHOICES[1][0]  # Draft
        )

    def test_post_model_str(self):
        post = self.post1
        self.assertEqual(str(post), post.title)

    def test_post_detail(self):
        self.assertEqual(self.post1.title, 'mohammad')
        self.assertEqual(self.post1.text, 'Sample Text.')
        self.assertEqual(self.post1.author, self.user)
        self.assertEqual(self.post1.status, 'pub')

    # ! check post list

    def test_posts_list_view_url(self):
        response = self.client.get('/blog', {}, True)
        self.assertEqual(response.status_code, 200)

    def test_posts_list_view_url_by_name(self):
        response = self.client.get(reverse('post_list'), {}, True)
        self.assertEqual(response.status_code, 200)

    def test_posts_list_page(self):
        response = self.client.get(reverse('post_list'), {}, True)
        self.assertContains(response, self.post1.title)

    # ! check post Details

    def test_posts_detail_view_url(self):
        post_id = int(self.post1.id)
        response = self.client.get(f'/blog/{post_id}', {}, True)
        self.assertEqual(response.status_code, 200)

    def test_posts_detail_page(self):
        post_id = int(self.post1.id)
        response = self.client.get(reverse('post_detail', args=[post_id]), {}, True)
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_posts_detail_page_does_not_exist_404_status(self):
        response = self.client.get(reverse('post_detail', args=[777]), {}, True)

        self.assertEqual(response.status_code, 404)

    def test_draft_post_not_show_in_posts_list(self):  # TDD : Test Driven Development
        response = self.client.get(reverse('post_list'), {}, True)
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    # ! check post Create

    def test_post_create_view(self):
        with open('/home/mammadsafar/Pictures/ee.png', 'rb') as fp:
            response = self.client.post(reverse('post_create'), {
                'title': 'Some Title',
                'text': 'This is some text!',
                'status': Post.STATUS_CHOICES[0][0],
                'author': self.user.id,
                'thumbnail': fp,
            })
        print('--> ==========1========= <--')

        print('--> ==========2========= <--')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'Some Title')
        self.assertEqual(Post.objects.last().text, 'This is some text!')
        self.assertEqual(Post.objects.last().status, 'pub')
        self.assertEqual(Post.objects.last().author, self.user)

    # ! check post Update

    def test_post_update_view(self):
        response = self.client.post(reverse('post_update', args=[self.post2.id]), {
            'title': 'Post2 Updated',
            'text': 'This text is Updated!',
            'author': self.user.id,
            'status': Post.STATUS_CHOICES[0][0],

        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'Post2 Updated')
        self.assertEqual(Post.objects.last().text, 'This text is Updated!')

    # ! check post Delete

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args=[self.post2.id]), )
        self.assertEqual(response.status_code, 302)
