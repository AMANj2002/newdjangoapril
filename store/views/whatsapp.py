
'''from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from twilio.rest import Client
from store.models import SalesOrder, OrderItem  # add missing import



@receiver(post_save, sender=SalesOrder)
def send_order_via_whatsapp(sender, instance, created, **kwargs):
    
    if created:
        # Create the message body
        message = f"New order received:\n"
        message += f"Order #{instance.id}\n"
        message += f"Retail store: {instance.retail.name}\n"
        message += f"Date ordered: {instance.date_ordered}\n"
        message += f"Complete: {instance.complete}\n\n"
        message += "Order Items:\n"
        order_items = instance.order_items.all()
        for order_item in order_items:
            message += f"{order_item.product.name} - Quantity: {order_item.qty}\n"
    
        # Debugging: print the message to the console
        print("Message:", message)
        
        # Initialize the Twilio client
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        # Send the message via WhatsApp
        message = client.messages.create(
            body=message,
            from_=f'whatsapp:{settings.TWILIO_PHONE_NUMBER}',
            to=f'whatsapp:{settings.MY_PHONE_NUMBER}'
        )
        
        # Debugging: print the Twilio message to the console
        print("Twilio message:", message)
'''




from twilio.rest import Client
from django.conf import settings
from django.http import HttpResponse
from store.models.salesorder import SalesOrder

def send_order_via_whatsapp(request):
    # Get all SalesOrder objects
    orders = SalesOrder.objects.all()
    
    # Create the message body
    message = ''
    for order in orders:
        message += f"Order #{order.id}\n"
        message += f"Retail store: {order.retail.name}\n"
        message += f"Date ordered: {order.date_ordered}\n"
        message += f"Complete: {order.complete}\n"
        
        # Access the related OrderItem objects
        order_items = order.orderitem_set.all()
        for item in order_items:
            message += f"Item: {item.product.name}\n"
   #         message += f"Quantity: {item.quantity}\n"
            message += f"Price: {item.product.price}\n\n"
    
    # Initialize the Twilio client
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    
    # Send the message via WhatsApp
    message = client.messages.create(
        body=message,
        from_=f'whatsapp:{settings.TWILIO_PHONE_NUMBER}',
        to=f'whatsapp:{settings.MY_PHONE_NUMBER}'
    )
    orders.delete()
    # Return a response to the client
    return HttpResponse(f'Message sent to {message.to}: {message.body}')
