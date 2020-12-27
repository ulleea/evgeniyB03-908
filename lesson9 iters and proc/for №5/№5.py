def user_connection(username):
    import random
    for i in range(random.randint(10, 20)):
        yield f"{username} message{i}"

def establish_connection(auth=True):
    import random
    id = f"{random.randint(0,100000000):010}"
    if auth:
        yield f"auth {id}"
    yield from user_connection(id)
    if auth:
        yield f"disconnect {id}"

def connection():
    import random
    connections = [establish_connection(True) for i in range(10)]
    connections.append(establish_connection(False))
    connections.append(establish_connection(False))
    while len(connections):
        conn = random.choice(connections)
        try:
            yield next(conn)
        except StopIteration:
            del connections[connections.index(conn)]

def write_to_file(f_obj):
    while True:
        x = yield
        f_obj.write(x + '\n')

def connect_user(name):
    with open(name + '.txt', 'w+') as file:
        yield from write_to_file(file)

def task_planner(message, logins):
    if 'auth' in message:
        writer = connect_user(message[5:])
        next(writer)
        logins[message[5:]] = writer
    elif 'disconnect' in message:
        logins[message[11:]].close()
    elif message[:10] in logins:
        logins[message[:10]].send(message[11:])

import os
os.chdir('C:\\Users\\Евгений\\PycharmProjects\\pycharmrepository\\repositoriy\\lesson9 iters and proc\\for №5')
logins = dict()
for i in connection():
    task_planner(i, logins)