import re
from rest_framework import serializers

from api.models import Package, Booking

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

# Create the Booking Serializer using Booking model
class BookingSerializer(serializers.ModelSerializer):
    # error message
    STREET_ADDRESS_ERROR = 'Street address must be in the format "11 Abc St."'

    class Meta:
        model = Booking
        fields = '__all__'

    # Validation for street address
    def validate_street_address(self, value):
        regexp = re.compile(r'\d+ \w+ \w+') # reg expression: a number or a digt followed by some text in 2 words ex: 12 Bukit Merah
        if regexp.search(value):
            return value # if reg exp matches we return the value
        raise serializers.ValidationError(
            self.STREET_ADDRESS_ERROR # else we raise a validation error with the above message declared
        )
