from rest_framework import serializers
from .models import Product,Catagory,CustomerProfile,Orders,OrderItems,News,SubCatagory
from django.shortcuts import get_object_or_404


class CatagorySerilizer(serializers.ModelSerializer):
    class Meta:
        model=Catagory
        fields=['id','name','date','images']
class SubCatagorySerilizer(serializers.ModelSerializer):
    class Meta:
        model=SubCatagory
        fields=['id','name','date','images','catagory']
class ProductSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model=Product
        fields=['id','name','images','description','price','cattagory','date','discount','subcatagory']
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomerProfile
        fields=['id','Phone_no','user']
class OrderItemSeializer(serializers.ModelSerializer):
   
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
  
    class Meta:
        model=OrderItems
        fields=['id','product','quantity']
class OrderSerilizer(serializers.ModelSerializer):
    customer= serializers.PrimaryKeyRelatedField(read_only=True)
    order_items = OrderItemSeializer(many=True)
    total = serializers.DecimalField(max_digits=8, decimal_places=2, read_only=True)

    

    class Meta:
        model=Orders
        fields=['orderuniqueId','customer','total','date_created','status','location','order_items']
    
    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')  
        order = Orders.objects.create(**validated_data)
        orderitemarray = []

        for order_item_data in order_items_data:
            product = order_item_data['product']
            quantity = order_item_data['quantity']
            data = OrderItems.objects.create(product=product, quantity=quantity)
            orderitemarray.append(data)
        order.order_items.set(orderitemarray)

        # Calculate and set the total field
        
        
        return order

       
    def save(self, **kwargs):
        if self.context['userid']:
            (customer,created)=CustomerProfile.objects.get_or_create(user_id=self.context['userid'])
            if customer:
                self.validated_data['customer'] = customer
        return super().save(**kwargs)

class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model=News
        fields=['id','Headline','description']


