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

def connection_user():
    g=set()
    write = write_to_file()
    next(write)
    while True:
        a=yield
        a=a.split()

        if a[0]=='auth':
            g.add(a[1])
        if a[0] == 'disconnect':
            g.remove(a[1])
        if a[0]!='auth' and a[0] != 'disconnect' and a[0] in g:
            try:
                write.send(a[0]+' '+a[1])
            except StopIteration:
                write.close()

def write_to_file():
    s=yield
    with open('C:\\Users\\Евгений\\PycharmProjects\\pycharmrepository\\repositoriy\\lesson9 iters and proc\\for №5\\text.txt','a') as file:
        file.write(s+'\n')

con=connection_user()
next(con)
for i in connection():
    con.send(i)