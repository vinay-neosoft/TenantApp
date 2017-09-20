# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Question, Answer, Tenant, Request
import json
from rest_framework.authtoken.models import Token


class TestCase(TestCase):

	def setUp(self):
		self.user = User.objects.create(username="simran",
								password="password_simran")
		self.user.set_password("password_simran")
		self.user.save()
		self.ques = Question.objects.create(question_title="How to create super user in django ?",
								is_private=1,
									user_id=self.user)
		self.ans = Answer.objects.create(answer_body='python manage.py createsuperuser',
								question_id=self.ques,
								user_id=self.user)
		self.tenant = Tenant.objects.create(tenant_name="new_neosoft", 
								api_key="6s21sdc231sd65csd561csd21dc32145")
		token = Token.objects.create(user=self.user)		
		self.access_token = 'Token ' + token.key

	def test_question(self):
		self.assertEqual(self.ques.question_title, "How to create super user in django ?")
		self.assertEqual(self.ques.is_private, 1)
		self.assertEqual(self.ques.user_id, self.user)

	def test_answer(self):
		self.assertEqual(self.ans.answer_body, "python manage.py createsuperuser")
		self.assertEqual(self.ans.question_id, self.ques)
		self.assertEqual(self.ans.user_id, self.user)
	
	def test_get_questions_without_login(self):
		response = self.client.get('/api/questions/')
		self.assertEqual(response.status_code, 401)

	def test_get_questions_with_login_tenant_key(self):
		response = self.client.get('/api/questions/',
								   HTTP_API_KEY=self.tenant.api_key,
								   HTTP_AUTHORIZATION=self.access_token)
		self.assertEqual(response.status_code, 200)

	def test_get_questions_without_tenant_key(self):
		response = self.client.get('/api/questions/',
								   HTTP_AUTHORIZATION=self.access_token)
		self.assertEqual(response.status_code, 403)

	def test_private_question(self):
		response = self.client.get('/api/questions/',
								   HTTP_API_KEY=self.tenant.api_key,
								   HTTP_AUTHORIZATION=self.access_token)
		self.assertEqual(response.status_code, 200)
		print (response.data)
		self.assertEqual(len(response.data), 1)

	def test_get_questions_with_query_string(self):
		response = self.client.get('/api/questions/?q=xyz',
								   HTTP_API_KEY=self.tenant.api_key,
								   HTTP_AUTHORIZATION=self.access_token)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.data), 0)

		response = self.client.get('/api/questions/?q=what',
								   HTTP_API_KEY=self.tenant.api_key,
								   HTTP_AUTHORIZATION=self.access_token)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.data), 1)

	def teardown(self):
		User.objects.all().delete()
		Question.objects.all().delete()
		