class TokenExpireCheck:
	def __init__(self, view):
		self.view = view
	def __call__(self,request):
	
		resp = self.view(request)
		return resp