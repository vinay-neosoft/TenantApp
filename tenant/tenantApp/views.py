# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User

from tenantApp.models import Question, Answer, Tenant

class DashboardView(View):

	def get(self, request):
		tenants = Tenant.objects.all()
		total_users_count = User.objects.all().count()
		total_answers_count = Answer.objects.all().count()
		total_questions_count = Question.objects.all().count()
		return render(request, "dashboard.html", {'total_users_count': total_users_count,
												  'total_answers_count': total_answers_count,
												  'total_questions_count': total_questions_count,
												  'tenants': tenants})
