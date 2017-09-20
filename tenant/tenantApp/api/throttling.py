import datetime
from rest_framework.throttling import BaseThrottle
from tenantApp.models import Tenant, Request

class TenantThrottleRate(BaseThrottle):

	def allow_request(self, request, view):

		today = datetime.datetime.now()
		api_key = request.META.get('HTTP_API_KEY')
		tenant = Tenant.objects.get(api_key=api_key)
		todays_requests = Request.objects.filter(tenant=tenant, requested_on__date=datetime.datetime.today())
		is_allowed = True
		delta = today - datetime.timedelta(seconds=10)

		if len(todays_requests) > 100 and todays_requests.filter(requested_on__gte=datetime.datetime.now() - datetime.timedelta(seconds=10)):
			is_allowed = False

		if is_allowed:
			Request.objects.create(tenant=tenant, requested_on=today,
								   requested_by=request.user, url=request.path)
		return is_allowed
