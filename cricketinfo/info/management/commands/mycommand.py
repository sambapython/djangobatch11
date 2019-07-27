from django.core.management.base import BaseCommand, CommandError
class Command(BaseCommand):
	def handle(self,*k,**kw):
		print("this is my own command")