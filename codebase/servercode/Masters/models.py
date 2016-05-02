from django.db import models
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.forms import ModelForm

class City_reference(models.Model):
    city_name = models.CharField(max_length=20)
    city_code = models.CharField(max_length=20)
    district_name = models.CharField(max_length=20)
    district_code = models.CharField(max_length=20)
    state_name = models.CharField(max_length=20)
    state_code = models.CharField(max_length=20)
    def __unicode__(self):
    	return str(self.city_name)
    	return str(self.city_code)
    	return str(self.district_name)
    	return str(self.district_code)
    	return str(self.state_name)
    	return str(self.state_Code)


class City(models.Model):
	name = models.ForeignKey(City_reference)
	city_code = models.CharField(max_length=5)
	state_name = models.CharField(max_length=5)
	state_code = models.CharField(max_length=20)
	district_name = models.CharField(max_length=20)
	district_code = models.CharField(max_length=5)
	shape = models.CharField(max_length=2000)
	created_by =  models.ForeignKey(User)
	created_on = models.DateTimeField( default= datetime.datetime.now())
	
	def __unicode__(self):
		return str(self.name)
    
	class Meta: 
	 	verbose_name = 'City'
	 	verbose_name_plural = 'Cities'  



SURVEYTYPE_CHOICES = (('Slum Level', 'Slum Level'),
					  ('Household Level', 'Household Level'),
					  ('Household Member Level', 'Household Member Level'))


class Survey(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	city = models.ForeignKey(City)
	survey_type = models.CharField(max_length=50, choices=SURVEYTYPE_CHOICES)
	analysis_threshold = models.IntegerField()
	kobotool_survey_id = models.CharField(max_length=50)
	kobotool_survey_url = models.CharField(max_length=512)
	
	def __unicode__(self):
		return self.name
	
	class Meta: 
	 	verbose_name = 'Survey'
	 	verbose_name_plural = 'Surveys'  

class AdministrativeWard(models.Model):
	city	= models.ForeignKey(City)
	name = models.CharField(max_length=512)
	shape = models.CharField(max_length=2048)
	ward_no =models.CharField(max_length=10)
	description = models.CharField(max_length=2048)
	office_address = models.CharField(max_length=2048)
	
	def __unicode__(self):
		return self.name    

	class Meta: 
	 	verbose_name = 'Administrative Ward'
	 	verbose_name_plural = 'Administrative Wards'  

class ElectoralWard(models.Model):
	administrative_ward = models.ForeignKey(AdministrativeWard)
	name = models.CharField(max_length=512)
	shape = models.CharField(max_length=2048)
	ward_no = models.CharField(max_length=10)
	ward_code = models.CharField(max_length=10)
	extra_info = models.CharField(max_length=4096)
	
	def __unicode__(self):
		return self.name

	class Meta: 
	 	verbose_name = 'Electoral Ward'
	 	verbose_name_plural = 'Electoral Wards'  

class Slum(models.Model):
	electoral_ward = models.ForeignKey(ElectoralWard)
	name = models.CharField(max_length=100)
	shape = models.CharField(max_length=2048)
	description = models.CharField(max_length=100)
	shelter_slum_code = models.CharField(max_length=512)
    
	def __unicode__(self):
		return str(self.name)

	class Meta: 
	 	verbose_name = 'Slum'
	 	verbose_name_plural = 'Slums'  


class WardOfficeContact(models.Model):
	administrative_ward = models.ForeignKey(AdministrativeWard)
	title = models.CharField(max_length=25)
	name  = models.CharField(max_length=200)
	telephone = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.name  

	class Meta: 
	 	verbose_name = 'Ward Officer Contact'
	 	verbose_name_plural = 'Ward Officer Contacts'  

class ElectedRepresentative(models.Model):
	electoral_ward = models.ForeignKey(ElectoralWard)
	name = models.CharField(max_length=200) 
	tel_nos = models.CharField(max_length=50)
	address = models.CharField(max_length=512)
	post_code = models.CharField(max_length=20)
	additional_info = models.CharField(max_length=2048)
	elected_rep_Party = models.CharField(max_length=50)
	

	def __unicode__(self):
		return self.name

	class Meta: 
	 	verbose_name = 'Elected Representative'
	 	verbose_name_plural = 'Elected Representatives'  

class ShapeCode(models.Model):
	code = models.CharField(max_length=25)
	description = models.CharField(max_length=100)

	class Meta: 
	 	verbose_name = 'Shape Code'
	 	verbose_name_plural = 'Shape Codes'  

class DrawableComponent(models.Model):
	name  = models.CharField(max_length=100)
	color = models.CharField(max_length=100)
	extra = models.CharField(max_length=4096)
	maker_icon = models.CharField(max_length=500)
	shape_code = models.ForeignKey(ShapeCode)
	
	def __unicode__(self):
		return self.name
	
	class Meta: 
	 	verbose_name = 'Drawable Component'
	 	verbose_name_plural = 'Drawable Components'  

class PlottedShape(models.Model):
	slum = models.CharField(max_length=100)
	name = models.CharField(max_length=512)
	lat_long = models.CharField(max_length=2000)
	drawable_component = models.ForeignKey(DrawableComponent)
	created_by =  models.ForeignKey(User)
	created_on= models.DateTimeField(default= datetime.datetime.now())
	
	def __unicode__(self):
		return self.name

	class Meta: 
		verbose_name = 'Plotted Shape'
	 	verbose_name_plural = 'Plotted Shapes'  

CHOICES_ALL = (('0', 'None'),
					  ('1', 'All'),
					  ('2', 'Allow Selection'))

class RoleMaster(models.Model):
	name = models.CharField(max_length=100)
	city = models.IntegerField(choices=CHOICES_ALL)
	slum = models.IntegerField(choices=CHOICES_ALL)
	kml =  models.BooleanField(blank=False)
	dynamic_query = models.BooleanField(blank=False)
	predefined_query = models.BooleanField(blank=False)
	can_request = models.BooleanField(blank=False)
	users = models.BooleanField(blank=False)
	create_save_query = models.BooleanField(blank=False)
	deploy_survey = models.BooleanField(blank=False)
	upload_images = models.BooleanField(blank=False)
	prepare_reports = models.BooleanField(blank=False)

	class Meta: 
	 	verbose_name = 'Role Master'
	 	verbose_name_plural = 'Role Masters'  

	
class UserRoleMaster(models.Model):
	user = models.ForeignKey(User)
	role_master = models.ForeignKey(RoleMaster)
	city = models.ForeignKey(City)
	slum = models.ForeignKey(Slum)

	class Meta: 
	 	verbose_name = 'User Role Master'
	 	verbose_name_plural = 'User Role Masters'  


class ProjectMaster(models.Model):
	created_user = models.CharField(max_length=100) 
	created_date = models.DateTimeField(default= datetime.datetime.now())

	class Meta: 
	 	verbose_name = 'Project Master'
	 	verbose_name_plural = 'Project Masters'  


"""
@receiver(post_save,sender=Slum)
def Slum_Created_Trigger(sender,instance,**kwargs):
	#Database connection with Kobocat Postgres

    conn = psycopg2.connect(database=settings.KOBOCAT_DATABASES['DBNAME'], 
							user=settings.KOBOCAT_DATABASES['USER'], 
							password=settings.KOBOCAT_DATABASES['PASSWORD'], 
							host=settings.KOBOCAT_DATABASES['HOST'], 
							port=settings.KOBOCAT_DATABASES['PORT'] )
   

    objSurveys=Survey.objects.filter(City_id=instance.ElectoralWard_id.AdministrativeWard_id.City_id)
    for objSurvey in objSurveys:
    	#Split Kobocat URL to get Form_ID
    	arrlist = objSurvey.kobotoolSurvey_url.split('/')
    	koboformId = arrlist[len(arrlist)-1].split('?')[0]
    	
    	#Get JSON data from Kobocat
    	cursor = conn.cursor()
        cursor.execute('select json from logger_xform where id='+koboformId)
        jsonCursor = cursor.fetchall()
        koboJson = None
        for jsonValue in jsonCursor[0]: 
            koboJson=json.loads(jsonValue)
        koboJson["children"][0]["children"].append({'name':instance.Name,'label':instance.Name})   
        koboformJson = json.dumps(koboJson)
        
        #Get XML data from Kobocat
        cursor = conn.cursor()
        cursor.execute('select xml from logger_xform where id='+koboformId)
        xmlCursor = cursor.fetchall()
        koboXml = []
        for xmlValue in xmlCursor[0]:           
            koboXml=xmlValue
            
        soup = Soup(koboXml,"html.parser")    
        
        #Append New City In XML
        soup.select1.append(Soup('<item>\n<label>'+instance.Name+'</label>\n<value>'+instance.Name+'</value>\n</item>\n','html.parser'))
        koboformXml= unicode(soup.prettify())
        
        #Update Kobocat database JSON and XML fields 
        cursor.execute('BEGIN')
        cursor.execute('update logger_xform set json=%s, xml=%s where id='+koboformId,[(koboformJson,),(koboformXml,)])
        cursor.execute('COMMIT')

"""
