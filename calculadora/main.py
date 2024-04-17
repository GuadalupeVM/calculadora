import web
import redis

urls = (
    '/', 'index',
)

app = web.application(urls, globals())

redis_host = 'localhost'
redis_port = 6379
redis_db = 1
redis_connection = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)


class index:
    def GET(self):
        return render('index.html')

    def POST(self):
        numero1 = int(web.input().numero1)
        numero2 = int(web.input().numero2)
        resultado = numero1 + numero2

        # Usar Redis para almacenar el resultado
        # redis_client = redis.Redis()
        redis_client.get('numero1')
        redis_client.get('numero2')
        # redis_client.set('resultado', resultado)

        return render('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run()
