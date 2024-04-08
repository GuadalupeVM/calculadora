import web

urls = (
    '/', 'index',
)

app = web.app(urls)

class index:
    def GET(self):
        return render('index.html')

    def POST(self):
        numero1 = int(web.input().numero1)
        numero2 = int(web.input().numero2)
        resultado = numero1 + numero2

        # Usar Redis para almacenar el resultado
        redis_client = redis.Redis()
        redis_client.set('resultado', resultado)

        return render('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run()
