import json, logging

from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Product, Category
from config.settings import BASE_DIR

DATA_FILE = BASE_DIR.joinpath('catalog', 'data', 'catalog_data.json')
PATH_TO_LOG = BASE_DIR.joinpath('catalog', 'data', 'load_data.log')

logging.basicConfig(level=logging.ERROR,
                    filename=PATH_TO_LOG,
                    filemode='w',
                    format='%(asctime)s -%(name)s - %(levelname)s - %(message)s')
class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        cursor = connection.cursor()
        cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1;")
        cursor.execute("ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1;")

        try:
            with open(DATA_FILE) as f:
                data = json.load(f)

                categories = []
                products = []
                is_category_recorded = False

                for count, item in enumerate(data):
                    item_model = item['model']

                    if item_model == 'catalog.product':
                        if not is_category_recorded:
                            Category.objects.bulk_create(categories)
                            is_category_recorded = True
                        product = item['fields']
                        product['category'] = Category.objects.get(pk=product['category'])
                        products.append(Product(**product))
                    elif item_model == 'catalog.category':
                        categories.append(Category(**item['fields']))

            Product.objects.bulk_create(products)
        except FileNotFoundError as e:
            logging.error(f'Проверьте наличие файла {DATA_FILE}')
        except KeyError as e:
            logging.error(f'Проблема с ключом {e} транзакция {count+1}')
        else:
            print('Данные загружены в базу данных')
