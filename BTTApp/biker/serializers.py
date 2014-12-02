from .models import Biker

from rest_framework import serializers

class Bikerserializer(serializers.ModelSerializer):
	class Meta:
		model = Biker
		fields = (
			'id',
			'name',
			'phone',
			'start_time',
			'first_check',
			'second_check',
			'final_check',
			)