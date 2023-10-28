from .models import Farm, AreaFarmsRelation, Order, OrderInfo


def serialize_farm(farm: Farm):
    return {'id': farm.id, 'name': farm.name, 'delivery_days': farm.delivery_days, 'delivery_time': farm.delivery_time,
             'location': {"city": AreaFarmsRelation.objects.filter(farms_id=farm)[0].area_id.city_id.name, "areas": [
                 area_relation.area_id.name for area_relation in AreaFarmsRelation.objects.filter(farms_id=farm)]}}


def serialize_order(order: Order):
    return {
        'id': order.id,
        'user': {'id': order.user_id.id, 'role': order.user_id.role_id.name},
        'farm': serialize_farm(order.farm_id),
        'product': order.order_info_id.product_id.name,
        'total_price': order.order_info_id.total_price,
        'quantity': order.order_info_id.quantity,
        'per_kg': order.order_info_id.per_kg
    }