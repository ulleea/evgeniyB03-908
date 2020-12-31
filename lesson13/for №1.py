import pickle

with open('data.pickle', 'rb') as f:
    # Версия протокола определяется автоматически,
    # нет необходимости явно указывать его.
    data = pickle.load(f)
print(data)