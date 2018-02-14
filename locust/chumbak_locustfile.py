import os
from random import choice
from locust import HttpLocust, TaskSet, task


def get_category_api(catalog_response):
    """
    return random category api from catalog api response
    """
    categories = catalog_response["data"]["categories"]
    random_category = choice(categories)
    category_url = random_category.get("url")
    category_api = "v1{}".format(category_url)
    return category_api


def get_category_product_api(category_response):
    """
    return random category product api from category api response
    """
    category_hierarchy = category_response["hierarchy"]
    random_hierarchy = choice(category_hierarchy)
    hierarchy_id = random_hierarchy.get("id")
    category_product_api = "v1/category/{}/products".format(hierarchy_id)
    return category_product_api


def get_random_product(category_product_response):
    """
    return random product from categroy product api response
    """
    products = category_product_response.get("products")
    random_product = choice(products)
    return random_product


class MyTaskSet(TaskSet):
    def on_start(self):
        self.login()
        #self.remove_product_from_cart()

    def login(self):
        email = os.environ.get("CHUMBAK_EMAIL")
        password = os.environ.get("CHUMBAK_PASSWORD")
        response = self.client.post("v1/login/", {"email": email, "password": password, "email_login": 1}).json()
        print "LoginMessage: %s" % (response.get("message"))

    @task
    def add_product_to_cart(self):
        """
        Catalog --> Categories --> Subcategory --> Product --> Cart
        """
        catalog_api = "v1/catalog-update/?timestamp=0"
        catalog_api_response = self.client.get(catalog_api).json()

        category_api = get_category_api(catalog_api_response)
        category_api_response = self.client.get(category_api).json()

        category_product_api = get_category_product_api(category_api_response)
        category_product_api_response = self.client.get(category_product_api).json()

        random_product = get_random_product(category_product_api_response)

        if random_product["type_id"] == "simple":
            product_id = random_product.get("entity_id")
        else:
            url = random_product.get("url")
            api = "v1{}".format(url)
            api_response = self.client.get(api).json()
            product_keys = api_response.get('children_details').keys()
            product_id = choice(product_keys)
        cart_api = "v1/cart/add/{}/1".format(product_id)
        cart_api_response = self.client.get(cart_api).json()
        print "ProductId: %s CartApiResponse: %s" % (product_id, cart_api_response.get("status"))

        cart_view_api = "v1/cart/view"
        cart_view_api_response = self.client.get(cart_view_api)
        print "CartViewApi: %s" % (cart_view_api_response.status_code)

        address_api = "v1/checkout/address"
        address_api_response = self.client.get(address_api)
        print "CheckoutAddressApi: %s" % (address_api_response.status_code)

        checkout_details_api = "v1/checkout/details"
        checkout_details_api_response = self.client.get(checkout_details_api)
        print "CheckoutDetailsApi: %s" % (checkout_details_api_response.status_code)

    @task
    def common_details(self):
        common_details_api = "v1/common-details"
        response = self.client.get(common_details_api)
        print "CommonDetailsApi: %s" % (response.status_code)

    def remove_product_from_cart(self):
        api = "v1/cart/view"
        response = self.client.get(api).json()
        products = response.get("cart").get("items")
        for p in products:
            pid = p.get("product_id")
            remove_api = "v1/cart/remove/{}".format(pid)
            response = self.client.get(remove_api).json()
            print "Item %s is removed from cart" %(pid)

    # @task
    # def cart_view(self):
    #     cart_view_api = "v1/cart/view"
    #     response = self.client.get(cart_view_api)
    #     print "CartViewApi: %s" % (response.status_code)

    # @task
    # def checkout_address(self):
    #     address_api = "v1/checkout/address"
    #     response = self.client.get(address_api)
    #     print "CheckoutAddressApi: %s" % (response.status_code)

    # @task
    # def checkout_details(self):
    #     checkout_details_api = "v1/checkout/details"
    #     response = self.client.get(checkout_details_api)
    #     print "CheckoutDetailsApi: %s" % (response.status_code)


class WebsiteUser(HttpLocust):
    # host = "https://api.chumbak.com/"
    host = "http://127.0.0.1:9000/"
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 9000
