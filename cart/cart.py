from webapp.models import Product


class Cart():

    def __init__(self,request):
        self.session= request.session
        cart=self.session.get('session_key')
        if 'session_key' not in request.session:
            cart=self.session['session_key']={}
        self.cart=cart  #make sure cart is available on all pages
    def add(self,product,quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        #logic
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price':str(product.price)} #{'101':{'price':'25.99'}}
            self.cart[product_id]=int(product_qty)
        self.session.modified = True #save changes
    
    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        product_ids=self.cart.keys()
        products=Product.objects.filter(id__in=product_ids)
        return products
    def get_quants(self):
        quantities = self.cart
        return quantities
    def update(self, product, quantity): #coming from the views post
        product_id = str(product)  #{'4':3}
        product_qty = int(quantity)
        # Get cart
        ourcart = self.cart
        # Update Dictionary/cart
        ourcart[product_id] = product_qty #call ourcart and pass what we want to update in[]
        self.session.modified = True
        thing = self.cart
        return thing
    
    def delete(self,product):
        product_id=str(product)
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified=True

    def cart_total(self):
        # Get product IDS
        product_ids = self.cart.keys()
        # lookup those keys in our products database model
        products = Product.objects.filter(id__in=product_ids)
        # Get quantities, {'4':3}
        quantities = self.cart
        # Start counting at 0
        total = 0
       
        for key, value in quantities.items():
            # Convert key string into int so we can do math
            key = int(key) #convert string to a int
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)






        return total