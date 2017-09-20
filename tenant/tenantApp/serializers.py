from rest_framework import serializers

from tenantApp.models import Question, Answer

class AnswerSerializer(serializers.ModelSerializer):

	user = serializers.SerializerMethodField()

	def get_user(self, obj):
		return obj.user.username

	class Meta:
		model = Answer
		fields = ('body', 'user')

class QuestionSerializer(serializers.ModelSerializer):

    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'title', 'answers')