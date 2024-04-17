import web
import redis

urls = (
    '/', 'Index'
)

app = web.application(urls, globals())

# Configurar la conexión a Redis
redis_host = 'localhost'
redis_port = 6379
redis_db = 1
redis_connection = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

class Index:
    def GET(self):
        # Renderizar el formulario HTML
        return """
            <html>
            <head>
            <title>SUMA Redis</title>
            </head>
            <body>
            <h2>Insertar numeros en Redis</h2>
            <form action="/" method="post">
            Numero 1: <input type="text" name="numero1a"><br>
            Numero 2: <input type="text" name="numero2b"><br>
            <input type="submit" value="Sumar">
            </form>
            </body>
            </html>
        """

    def POST(self):

        datos = web.input(numero1=None, numero2=None)
        numero1a = int(datos.numero1a)
        numero2b = int(datos.numero2b)

        # Almacenar los números en claves separadas
        redis_connection.set('num1', numero1a)
        redis_connection.set('num2', numero2b)

        suma = numero1a + numero2b

        return "La suma de {} y {} es: {}".format(numero1a, numero2b, suma)

if __name__ == "__main__":
    app.run()