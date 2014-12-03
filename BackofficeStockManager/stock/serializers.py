from .models import Stock

from rest_framework import serializers

class Stockserializer(serializers.ModelSerializer):
	class Meta:
		model = Stock
		fields = (
			'id',
			'name',
			'ref',
			'brand',
			'desc',
			'price',
			'stock',
			)