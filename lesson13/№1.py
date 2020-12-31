import pickle

# Коллекция сериализуемых объектов
data = {
    'a': [1, 2.0, 3, 4+6j, float("nan")],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

# Сериализация словаря data с использованием
# версии протокола по умолчанию.

with open('data.pickle', 'wb') as f:
    # Сериализация словаря data с использованием
    # последней доступной версии протокола.
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
with open('data.pickle', 'rb') as f:
        # Версия протокола определяется автоматически,
        # нет необходимости явно указывать его.
    data = pickle.load(f)
print(data)

print('___________________')
print(pickle.dumps(data))
n=123
a=print
a(n)
a=pickle.dumps(a)
print(a)
a=pickle.loads(a)
print(a)
a(n)