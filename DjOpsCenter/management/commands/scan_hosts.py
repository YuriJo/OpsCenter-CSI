from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Scans the first level directories and lists all clients.'

    START_PATH = '/Users/yuri/Work/ansible-infrastructure/inventories'  # Измените на ваш фактический путь

    def add_arguments(self, parser):
        parser.add_argument('action', type=str, help='Action to perform: list or product')

    def handle(self, *args, **options):
        action = options['action']

        if action == 'list':
            self.list_clients()
        elif action == 'product':
            self.list_products()
        else:
            self.stdout.write("Invalid action. Please use 'list' or 'product'.")



    def list_clients(self):
        self.stdout.write("Listing all clients...")

        clients = set()  # Используем множество для хранения уникальных клиентов

        # Получаем все элементы в стартовом каталоге
        with os.scandir(self.START_PATH) as entries:
            for entry in entries:
                if entry.is_dir():
                    clients.add(entry.name.capitalize())  # Добавляем название клиента с большой буквы

        # Выводим список клиентов
        for index, client in enumerate(sorted(clients), start=1 ):  # Сортируем для удобства чтения
            self.stdout.write(f"Client {index}: {client}")

        self.stdout.write("Scanning complete.")



    def list_products(self):
            self.stdout.write("Listing products for each client...")
    
            # Словарь для хранения продуктов клиентов
            client_products = {}
    
            # Сканирование каталогов
            for client_entry in os.scandir(self.START_PATH):
                if client_entry.is_dir():
                    client = client_entry.name.capitalize()
                    client_products[client] = self.find_products_for_client(client_entry.path)
    
            # Вывод продуктов для каждого клиента
            for client, products in client_products.items():
                self.stdout.write(f"Client: {client}")
                for product in sorted(products):
                    self.stdout.write(f"  Product: {product}")
    
    def find_products_for_client(self, client_path):
        products = set()
        for root, dirs, files in os.walk(client_path):
            if 'hosts' in files:
                product = os.path.basename(root)
                products.add(product)
        return products
    
        # Дополнительные функции для сканирования и обработки данных
        # ...
