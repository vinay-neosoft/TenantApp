# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Question, Answer, Tenant, Request


class TestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(username="simran",
        						password="password_simran")
        self.ques = Question.objects.create(question_title="How to create super user in django ?",
        						is_private=1,
      							user_id=self.user)
        self.ans = Answer.objects.create(answer_body='python manage.py createsuperuser',
								question_id=self.ques,
								user_id=self.user)

	def test_question(self):
		self.assertEqual(self.ques.question_title, "How to create super user in django ?")
		self.assertEqual(self.ques.is_private, 1)
		self.assertEqual(self.ques.user_id, self.user)

	def test_answer(self):
		self.assertEqual(self.ans.answer_body, "python manage.py createsuperuser")
		self.assertEqual(self.ans.question_id, self.ques)
		self.assertEqual(self.ans.user_id, self.user)
