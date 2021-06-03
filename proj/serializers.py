import serpy



class resSerializer(serpy.DictSerializer):
    """The serializer schema definition."""
    # Use a Field subclass like IntField if you need more validation.
    
    ifsc = serpy.Field()
    bank_id = serpy.IntField()
    branch = serpy.Field()
    address=serpy.Field()
    city=serpy.Field()
    district=serpy.Field()
    state=serpy.Field()
    bank_name=serpy.Field()
