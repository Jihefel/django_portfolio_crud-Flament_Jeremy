import django
django.setup()

from portfolio.seed import run

if __name__== '__main__':
    run()
