from .models import Farm, AreaFarmsRelation

def serialize_farm(farm: Farm):
    return {'id': farm.id, 'name': farm.name, 'delivery_days': farm.delivery_days, 'delivery_time': farm.delivery_time,
             'location': {"city": AreaFarmsRelation.objects.filter(farms_id=farm)[0].area_id.city_id.name, "areas": [
                 area_relation.area_id.name for area_relation in AreaFarmsRelation.objects.filter(farms_id=farm)]}}