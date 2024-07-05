from rest_framework import serializers


class RentalizerEstimateRequestSerializer(serializers.Serializer):
    accommodates = serializers.IntegerField()
    bathrooms = serializers.IntegerField()
    bedrooms = serializers.IntegerField()
    lat = serializers.CharField()
    lng = serializers.CharField()


class LocationSerializer(serializers.Serializer):
    lat = serializers.DecimalField(max_digits=12, decimal_places=8)
    lng = serializers.DecimalField(max_digits=12, decimal_places=8)


class DetailsSerializer(serializers.Serializer):
    address = serializers.CharField(allow_null=True)
    address_lookup = serializers.CharField(allow_null=True)
    zipcode = serializers.CharField(allow_null=True)
    accommodates = serializers.IntegerField(allow_null=True)
    bedrooms = serializers.IntegerField(allow_null=True)
    bathrooms = serializers.IntegerField(allow_null=True)


class MetricsSerializer(serializers.Serializer):
    adr = serializers.DecimalField(decimal_places=2, max_digits=17)
    date = serializers.CharField()
    occupancy = serializers.DecimalField(decimal_places=2, max_digits=3)
    revenue = serializers.IntegerField()
    revenue_lower = serializers.IntegerField()
    revenue_upper = serializers.IntegerField()


class SummarySerializer(serializers.Serializer):
    adr = serializers.DecimalField(max_digits=15, decimal_places=2)
    occupancy = serializers.DecimalField(max_digits=15, decimal_places=2)
    revenue = serializers.DecimalField(max_digits=15, decimal_places=2)


class FutureSerializer(serializers.Serializer):
    metrics = MetricsSerializer()
    summary = SummarySerializer()


class StatsSerializer(serializers.Serializer):
    future = FutureSerializer(source="*")
    property_value = serializers.DecimalField(
        max_digits=15, decimal_places=2, required=False, allow_null=True
    )


class PayloadSerializer(serializers.Serializer):
    details = DetailsSerializer()
    location = LocationSerializer()
    stats = StatsSerializer()


class RentalizerEstimateResponseSerializer(serializers.Serializer):
    payload = PayloadSerializer(source="*")
