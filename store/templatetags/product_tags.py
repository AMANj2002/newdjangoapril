from django import template

register = template.Library()

@register.simple_tag
def call_sellprice(price,discount):
   if discount is None  or discount is 0:
      return price
   sellprice = (price * discount/100)
   sellprice = price - sellprice
   return sellprice