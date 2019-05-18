
from rest_framework import serializers
from .models import User

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		#fields = '__all__'
		fields = ('first_name','last_name','phone_number','email','store_name','address_line1','address_line2','pin_code','district','state','pan_number','gst_number')