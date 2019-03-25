
from django.test import TestCase
from .models import Business, Profile, Neighbourhood, News, Health, Authorities
from django.contrib.auth.models import User
import datetime as dt

# Create your tests here.

class neighbourhoodTestClass(TestCase):

    def setUp(self):
        self.new_neighbourhood = Neighbourhood(name = "runda", neighbourhood_count="13")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_neighbourhood, Neighbourhood))
     
    def tearDown(self):
        
        Neighbourhood.objects.all().delete()

    def test_save_neighbourhood(self):
       
        self.new_neighbourhood.save_neighbourhood()
        self.assertTrue(len(Neighbourhood.objects.all()) > 0)    

   
    def test_init(self):
        self.assertTrue(self.new_neighbourhood.name =='runda')

    def test_delete_neighbourhood(self):
        self.new_neighbourhood.save_neighbourhood()
        neighbourhoods = Neighbourhood.objects.all()
        neighbourhoods.Neighbourhood.filter(Neighbourhood=Neighbourhood).delete()
        self.assertTrue(len(neighbourhoods)==0)    
        