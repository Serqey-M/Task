import pprint
import requests

# Задача 1. Выведите в консоль категории товаров, представленных на https://fakestoreapi.com. Запросите у пользователя, товары какой категории он желает просмотреть.
# Выведите информацию о соответствующих товарах в отформатированном для чтения виде в консоль. Используйте API https://fakestoreapi.com/docs.

all_categories = requests.get('https://fakestoreapi.com/products/categories')
print('Категории товаров:', *all_categories.json(), sep='\n- ')
print()
request = input('Какую категорию желаете просмотреть?\n')
products_in_a_specific_category = requests.get(f"https://fakestoreapi.com/products/category/{request}").json()
pprint.pprint(products_in_a_specific_category)

# Задача 2. Выведите информацию о всех корзинах пользователей (Cart), представленных на https://fakestoreapi.com.
# Проанализируйте данные и устно ответьте на вопрос, что из себя представляют эти корзины и какая информация в них находится - что означает каждое поле в полученном json.
# * По желанию доработайте программу: запросите у пользователя его имя (или идентификатор), в соответствии с этим выведите содержание всех корзин этого
# пользователя в отформатированном для чтения виде в консоль. Используйте API https://fakestoreapi.com/docs.

all_carts = requests.get("https://fakestoreapi.com/carts").json()
pprint.pprint(all_carts)
all_users = requests.get("https://fakestoreapi.com/users").json()
user = input('Введите имя пользователя или идентификатор: ')
try:
    id_user = int(user)
except:
    for i in all_users:
        if i['name']['firstname'] == user:
            id_user = i['id']
cart_user = requests.get(f"https://fakestoreapi.com/carts/user/{id_user}").json()
pprint.pprint(cart_user)

# Задача 3. Запросите у пользователя идентификатор аккаунта VK, у которого он желает просмотреть список друзей.
# Выведите только общее количество друзей пользователя в консоль. Для этого Вам необходимо, как и при работе с любым API,
# найти необходимый метод и изучить его описание, параметры и их значения, которыми можно варьировать.
# Также для работы с API VK Вам потребуется access token, процедуру получения которого мы разбирали на практике. Используйте API VK https://dev.vk.com/ru/method
# * По желанию доработайте программу: выведите основную информацию о каждом друге и дополнительно информацию о последнем его заходе в сеть.
# В полученном json друзья сразу должны быть отсортированы по имени.

token = ''
user_id = input("Введите идентификатор аккаунта VK: ")
friends = requests.get(
    f"https://api.vk.com/method/friends.get?user_id={user_id}&order=name&access_token={token}&fields=last_seen&v=5.199 HTTP/1.1"
).json()
print(f"Общее количество друзей: {friends['response']['count']}")
pprint.pprint(friends)
