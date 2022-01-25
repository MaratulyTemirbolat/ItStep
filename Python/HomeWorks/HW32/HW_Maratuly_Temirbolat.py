CREATE_NEW_ORDER_OPTION = 1
SHOW_GOODS_LIST_OPTION = 2
CREATE_CUSTOMER_OPTION = 3
SHOW_CUSTOMER_LIST_OPTION = 4
MAKE_NEW_ORDER_OPTION = 5
ADD_PRODUCTS_TO_ORDER_OPTION = 6
SHOW_CUSTOMER_ORDER_INFO_OPTION = 7
EXIT_OPTION = 8

NON_EXIT_ORDERS_CASE = None
EXISTED_PRODUCT_CASE = 1
NON_EXISTED_ORDER_PRODUCT_CASE = 0
WRONG_QUANTITY_PRODUCT_CASE = -1

ONE_STEP = 1

WRONG_QUANTITY_CASE = -1
CORRECT_QUANTITY_CASE = 1

class Product:
    def __init__(self,name,price, description=''):
        self.__name = name
        self.__price = price
        self.__description = description

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price

    def get_description(self):
        return self.__description

class Order:
    __order_id = '' 
    __order_goods = dict()

    def __init__(self,order_id):
        self.__order_id = order_id

    def __is_quantity_valid(self,product_quantity):
        if(product_quantity > 0):
            return True
        return False

    def get_order_id(self):
        return self.__order_id

    def __is_product_exist(self,product):
        if(product in self.__order_goods):
            return True
        return False

    def add_product(self,product,quantity):
        if(self.__is_quantity_valid(quantity) == True):
            if(self.__is_product_exist(product) == True):
                self.__order_goods[product] += quantity
                return EXISTED_PRODUCT_CASE
            else:
                self.set_good_quantity(product,quantity)
                return NON_EXISTED_ORDER_PRODUCT_CASE
        else:
            return WRONG_QUANTITY_PRODUCT_CASE

    def get_good_quantity(self,good):
        if(good in self.__order_goods):
            return self.__order_goods[good]
        else:
            return WRONG_QUANTITY_CASE

    def set_good_quantity(self,good,good_quantity):
        if(self.__is_quantity_valid(good_quantity) == True):
            self.__order_goods[good] = good_quantity
            return CORRECT_QUANTITY_CASE
        else:
            return WRONG_QUANTITY_CASE

    def set_order_id(self,order_id):
        self.__order_id = order_id
    
    def get_order_goods(self):
        return self.__order_goods

class Customer:
    def __balance_validation(self, balance):
        if balance < 0:
            self.__balance = 0
        else:
            self.__balance = balance
            
    def __init__(self,id,name,balance):
        self.__id = id
        self.__name = name
        self.__balance_validation(balance)
        self.__orders = []

    def add_product_to_order(self,product,quantity):
        product_status = None
        if(len(self.__orders) > 0):
            product_status = self.__orders[len(self.__orders) - ONE_STEP].add_product(product,quantity)
        return product_status

    def set_balance(self,balance):
        self.__balance_validation(balance)

    def get_balance(self):
        return self.__balance

    def get_id(self):
        return self.__id

    def set_id(self,id):
        self.__id = id

    def get_name(self):
        return self.__name
    
    def get_orders(self):
        return self.__orders
        
class View:
    def input_name(self):
        return input('Введите наименование: ')
    
    def input_price(self):
        return int(input('Введите цену товара: '))

    def input_description(self):
        return(input('Введите описание товара: '))

    def input_balance(self):
        return int(input('Введите баланс: '))

    def input_customer_id(self):
        return input('Введите Id Покупателя: ')
    
    def input_order_id(self):
        return input('Введите Id заказа: ')
    
    def input_good_quantity(self):
        return int(input('Введите количество товара к заказу: '))

    def show_line(self):
        print('------------------------------------------------------------')

    def show_customer_orders(self,customer):
        self.show_line()
        print('Все заказы клиента "{}":'.format(customer.get_name())) 
        for order in customer.get_orders():
            print('Заказ №' + str(order.get_order_id()) + ": ")
            order_goods = order.get_order_goods()
            for product in order_goods:
                good_name = product.get_name()
                good_price = product.get_price()
                good_description = product.get_description()
                good_quantity = order_goods[product]
                goor_total_price = order_goods[product] *product.get_price()
                print('\t\tНаименование: {} , Цена за 1 товар: {}, Описание товара: {}, Количество: {}, Стоимость: {}\
'.format(good_name,good_price,good_description,good_quantity,goor_total_price))

    def show_items(self,items):
        self.show_line()
        item_number = 1
        for item in items:
            print(item_number,item)
            item_number += ONE_STEP
        self.show_line()

    def show_product_list(self, products):
        product_number = 1
        self.show_line()
        print('Список товаров:\n')
        for product in products:
            print('Наименование: ',product.get_name())
            print('Цена:', product.get_price())
            print('Описание', product.get_description())
            self.show_line()
    
    def show_customers_list(self,customers):
        customer_number = 1
        self.show_line()
        print('Список покупателей:\n')
        for customer in customers:
            print(customer_number,'Имя: ',customer.get_name())
            print('  Доступный баланс: ', customer.get_balance())
            customer_number += ONE_STEP
            self.show_line()

    def show_customer_not_found_error(self):
        print('Извините, но такого клиента нет. Повторите попытку')
    
    def show_successful_order_creation_message(self):
        print('Новый заказ клиента успешно создан!')
    
    def show_product_not_found_error(self):
        print('Извините, но такого товара нет. Повтороите попытку!')

    def show_order_non_exist_error(self):
        print('Извините, но у вас нет ни одного заказа!')
    
    def show_successfully_added_good_to_order_message(self):
        print('Товар Успешно добавлен к текущему заказу!')
    
    def show_product_quantity_error(self):
        print('Извините, но вы ввели недопустимое количество для товара!')

    def input_user_choice(self):
        return int(input('Ваш выбор: '))
    
    def show_wrong_user_input_error(self):
        print('Извините, но вы ввели недопустимый символ!')
    
    def show_good_buy_message(self):
        print('Спасибо за использование программы! До свидания!')

class Controller:
    menu_items = ['Принять товара на склад',
                  'Показать список товаров на складе',
                  'Добавить нового покупателя',
                  'Показать список текущих покупателей',
                  'Сделать новый заказ Покупателю',
                  'Добавить продукты к заказу',
                  'Показать список всех Заказов с их продуктами Покупателя',
                  'Выход']
    
    view = View()
    products = []
    customers = []

    def __is_customer_exist(self,customer_id):
        for customer in self.customers:
            if(customer.get_id() == customer_id):
                return True
        return False

    def __get_customer_by_id(self,customer_id):
        for customer in self.customers:
            if(customer.get_id() == customer_id):
                return customer

    def find_customer(self):
        customer_id = self.view.input_customer_id()
        while(self.__is_customer_exist(customer_id) == False):
            self.view.show_customer_not_found_error()
            customer_id = self.view.input_customer_id()
        
        found_customer = self.__get_customer_by_id(customer_id)
        return found_customer

    def make_new_customer_order(self):
        found_customer = self.find_customer()
        order_id = self.view.input_order_id()
        found_customer.get_orders().append(Order(order_id))
        self.view.show_successful_order_creation_message()

    def create_product(self):
        product_name = self.view.input_name()
        product_price = self.view.input_price()
        product_description = self.view.input_description()
        return Product(product_name, product_price,product_description)
        
    def filling_store(self):
        self.products.append(self.create_product())

    def add_customer(self):
        customer_id = self.view.input_customer_id()
        customer_name = self.view.input_name()
        customer_balance = self.view.input_balance()
        self.customers.append(Customer(customer_id,customer_name,customer_balance))

    def show_products(self):
        self.view.show_product_list(self.products)

    def show_customers(self):
        self.view.show_customers_list(self.customers)
    
    def __is_product_exist(self,product_name):
        for product in self.products:
            if(product.get_name() == product_name):
                return True
        return False
    
    def __get_product(self,product_name):
        for product in self.products:
            if(product.get_name() == product_name):
                return product

    def find_product(self):
        product_name = self.view.input_name()
        while(self.__is_product_exist(product_name) == False):
            self.view.show_product_not_found_error()
            product_name = self.view.input_name()
        found_product = self.__get_product(product_name)
        return found_product

    def add_product_to_order(self):
        found_customer = self.find_customer()
        found_product = self.find_product()
        product_quantity = self.view.input_good_quantity()
        product_order_status = found_customer.add_product_to_order(found_product,product_quantity)
        if(product_order_status == NON_EXIT_ORDERS_CASE):
            self.view.show_order_non_exist_error()
        elif(product_order_status == EXISTED_PRODUCT_CASE or product_order_status == NON_EXISTED_ORDER_PRODUCT_CASE):
            self.view.show_successfully_added_good_to_order_message()
        elif(product_order_status == WRONG_QUANTITY_PRODUCT_CASE):
            self.view.show_product_quantity_error()
    
    def show_customer_orders_with_goods(self):
        found_customer = self.find_customer()
        self.view.show_customer_orders(found_customer)

        
    def main_menu(self):
        while True:
            self.view.show_items(self.menu_items)
            user_choice = self.view.input_user_choice()
            if user_choice == CREATE_NEW_ORDER_OPTION:
                self.filling_store()
            elif user_choice == SHOW_GOODS_LIST_OPTION:
                self.show_products()
            elif user_choice == CREATE_CUSTOMER_OPTION:
                self.add_customer()
            elif user_choice == SHOW_CUSTOMER_LIST_OPTION:
                self.show_customers()
            elif user_choice == MAKE_NEW_ORDER_OPTION:
                self.make_new_customer_order()
            elif user_choice == ADD_PRODUCTS_TO_ORDER_OPTION:
                self.add_product_to_order()
            elif user_choice == SHOW_CUSTOMER_ORDER_INFO_OPTION:
                self.show_customer_orders_with_goods()
            elif user_choice == EXIT_OPTION:
                self.view.show_good_buy_message()
                break
            else:
                self.view.show_wrong_user_input_error()

conroller = Controller()
conroller.main_menu()