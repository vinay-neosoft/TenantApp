from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from tenantApp.models import Question
from tenantApp.serializers import QuestionSerializer
from tenantApp.api.permissions import IsApiKeyProvided
from tenantApp.api.throttling import TenantRateThrottle

class QuestionViewSet(viewsets.ReadOnlyModelViewSet):

    permission_classes = (IsAuthenticated, IsApiKeyProvided,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    throttle_classes = (TenantRateThrottle,)

    def get_queryset(self):
		query_params = self.request.GET.get('q')
		if query_params:
			queryset = self.request.user.questions.filter(is_private=False,
														  title__contains=query_params)
		else:
			queryset = self.request.user.questions.filter(is_private=False)
		return queryset