from django.core.management.base import BaseCommand
from DjOpsCenter.models import Clients, Commands
import os

class Command(BaseCommand):
    help = 'Scans the first level directories and lists all clients.'

    START_PATH = '/Users/yuri/Work/ansible-infrastructure/inventories'  

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
                  client_name = entry.name.capitalize()  # Получаем название клиента
                  clients.add(client_name)
  
                  # Создаем запись в базе данных и проверяем, был ли клиент только что создан
                  client, created = Clients.objects.get_or_create(name=client_name)
                  if created:
                      self.stdout.write(f"New client added: {client_name}")

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
    
