# import random
#
# from app_movement_goods.models import UserCart
# from app_products.models import Product, ExtraData, ValueData, TitleData
# from app_users.models import User

# user1 = User.objects.get(pk=9)
# user2 = User.objects.get(pk=12)
# prod1 = Product.objects.get(pk=10)
# prod2 = Product.objects.get(pk=15)
# prod3 = Product.objects.get(pk=23)
# cart1 = UserCart.objects.get_or_create(owner=user1)[0]
# cart2 = UserCart.objects.get_or_create(owner=user2)[0]

# all_prod = Product.objects.filter(id__gte=2)
# list_country = ValueData.objects.filter(id__in=[1, 4, 9, 10, 11, 12, 13])  # страны
# list_term = ValueData.objects.filter(id__in=[3, 6, 7, 8])  # сроки
# list_type = ValueData.objects.filter(id__in=[2, 5])  # тип
# list_title = TitleData.objects.all()
# for prod in all_prod:
#     country = random.choice(list_country)
#     term = random.choice(list_term)
#     types = random.choice(list_type)
#     ExtraData.objects.create(title=list_title[0], device=prod, value=country)
#     ExtraData.objects.create(title=list_title[1], device=prod, value=types)
#     ExtraData.objects.create(title=list_title[2], device=prod, value=term)

# from app_users.models import User
# for user in ['zea@crid.ru',
# 'peter@cho.za',
# 'chtoto@za.pochta',
# 'valid@me.co',
# 'sova@cho.za',
# 'ulyba@cho.za',
# '123@cho.za',
# 'kot@na.oborot']:
#     user = User.objects.get(email=user)
#     user.set_password('1234')
#     user.save()

# import random
# import lorem
# from app_comments.models import CommentProduct, ProxyProduct
# from app_users.models import User
# count = 1
# while count < 300:
#     count += 1
#     user = random.choice(User.objects.all())
#     prod = random.choice(ProxyProduct.objects.all())
#     text = result = lorem.get_paragraph()
#     CommentProduct.objects.create(author=user, product=prod, content=text)

# import random
# import lorem
# from app_movement_goods.models import Order, OrderContents
# from app_products.models import Product
# from app_users.models import User
# count = 1
# while count < 100:
#     count += 1
#     order = Order.objects.create(
#         owner=random.choice(User.objects.all()),
#         city=lorem.get_word(),
#         address=lorem.get_word(count=3),
#         paid=True,
#         card_number=random.randrange(1000000, 99999999, 2)
#     )
#     prod = random.choice(Product.objects.all())
#     OrderContents.objects.create(
#         order=order,
#         product=prod,
#         price=prod.price,
#         quantity=random.randint(1, 5)
#     )

# py -Xutf8 manage.py dumpdata --natural-foreign --natural-primary -a -e contenttypes -e sessions -e auth.permission -e thumbnail -e admin --indent 4 -o fixtures/data_fixture.json
# py manage.py loaddata fixtures/data_fixture.json

# import datetime
# import random
# from app_comments.models import CommentProduct
# for com in CommentProduct.objects.all():
#     if random.random() > 0.3:
#         year = 2022
#         month = random.randint(1, 12)
#         day = random.randint(1, 28)
#         hour = random.randint(0, 23)
#         minute = random.randint(0, 59)
#         pub = datetime.datetime(year, month, day, hour, minute)
#         com.pub_at = pub
#         com.save()

