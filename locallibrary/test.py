import string
import secrets
# SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag')
# SECRET_KEY = os.environ['SECRET_KEY']

size = 64*10

SECRET_KEY1 = secrets.token_bytes(size)
print('bytes: ')
print(SECRET_KEY1)
print(len(SECRET_KEY1))
SECRET_KEY2 = secrets.token_hex(size)
print('hex: ')
print(SECRET_KEY2)
print(len(SECRET_KEY2))
SECRET_KEY3 = secrets.token_urlsafe(size)
print('urlsafe: ')
print(SECRET_KEY3)
print(len(SECRET_KEY3))
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(size))
print('password: ')
print(password)
print(len(password))
