from rest_framework.test import APITestCase
from info.models import UserProfile,Country
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
class CountryTesCases(APITestCase):

	@classmethod
	def tearDownClass(cls):
		cls.client.credentials(HTTP_AUTHORIZATION=None)

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
		#cls.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

	def test_country_post(self):
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
		resp = self.client.post("/api/country/",
			{"name":"Australia","shortname":"aus","description":"AUST"})
		self.assertTrue(resp.status_code==200,"test_country_post failed.%s"%resp.content)





