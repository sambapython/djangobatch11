from rest_framework.test import APITestCase
from info.models import UserProfile,Country
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
class CountryTesCases(APITestCase):

	@classmethod
	def setUpClass(cls):
		c=Country(name="INDIA",shortname="ind",description="eerew")
		c.save()
		user = UserProfile.objects.create_user(username="dummy",
			password="dummy",country=c)
		t=Token(user=user)
		t.save()
		token = t.key
		cls.token = token
		cls.client = APIClient()
		#cls.client.login(username="dummy",password="dummy")
		#cls.client.force_authenticate(user=user)
		cls.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

	def test_country_post(self):
		resp = self.client.post("/api/country/",
			{"name":"Australia","shortname":"aus","description":"AUST"},
			format="json")
		self.assertTrue(resp.status_code==200,"test_country_post failed.%s"%resp.content)








# sample
'''
def fun(x,y):
	"""
	10,20-->30
	str1,str2-->str1str2
	str1,20-->0
	10,str2-->0
	"""
	try:
		return x+y
	except:
		return 0
# Create your tests here.
class FunTestCases(TestCase):
	def test_fun_10_20(self):
		exp=30
		act=fun(10,20)
		self.assertTrue(exp==act,"test_fun_10_20 failed.")
	def test_fun_str1_str2(self):
		exp = "str1str2"
		act=fun("str1","str2")
		self.assertTrue(exp==act,"test_fun_str1_str2 failed.")
	def test_fun_str1_20(self):
		exp=0
		act=fun("str1",10)
		self.assertTrue(exp==act,"test_fun_str1_20 failed.")
'''

