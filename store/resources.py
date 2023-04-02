from import_export import resource
from store.models.product import Product
from store.models.customer import Customer
class ProductResource(resource.modelResource):
    class Meta:
        model = Product

class CustomerResource(resource.modelResource):
    class Meta:
        model = Customer
