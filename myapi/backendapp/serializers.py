from .models import Farm, AreaFarmsRelation, Order, OrderProduct


def serialize_farm(farm: Farm):
    return {'id': farm.id, 'name': farm.name, 'delivery_days': farm.delivery_days, 'delivery_time': farm.delivery_time,
             'location': {"city": AreaFarmsRelation.objects.filter(farms_id=farm)[0].area_id.city_id.name, "areas": [
                 area_relation.area_id.name for area_relation in AreaFarmsRelation.objects.filter(farms_id=farm)]}}


def serialize_order(order: Order):
    return {
        'id': order.id,
        'user': {'id': order.user_id.id, 'role': order.user_id.role_id.name},
        'farm': serialize_farm(order.farm_id),
        'products': [
            {'id': product.id, 'product': product.product_id.name, 'price_per_unit': product.price, 'quantity': product.quantity, 'total_price': product.price * product.quantity, 'per_kg': product.per_kg} for product in OrderProduct.objects.filter(order_id=order)
        ]
    }