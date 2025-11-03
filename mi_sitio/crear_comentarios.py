from email.mime import application
from faker import Faker

def main():
    fake = Faker('es_ES')  # Configurar Faker para español de España

    for _ in range(10):  # Crear 10 comentarios de ejemplo
        comentario = Comentario.objects.create(texto=fake.text(max_nb_chars=200))
        
    comentarios=Comentario.objects.all()
    print(f'Se han creado {comentarios.count()} comentarios de ejemplo.')
    
if __name__ == '__main__':
    import os 
    from django.core.wsgi import get_wsgi_application
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_sitio.settings')
    application = get_wsgi_application()

    from comments.models import Comentario  # Asegúrate de que 'mi_app' es el nombre correcto de tu aplicación

    main()  