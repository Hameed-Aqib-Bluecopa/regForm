def remote_ip(request):
  return {'remote_ip': request.META['REMOTE_ADDR']}
