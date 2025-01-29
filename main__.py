from PIL import Image

# Lista de imágenes (asegúrate de que sean del mismo tamaño)
imagenes = [
    "img/img-1.png",
    "img/img-2.png",
    "img/img-3.png",
    "img/img-4.png",
]

# Abrir las imágenes
frames = [Image.open(imagen) for imagen in imagenes]

# Crear el GIF
frames[0].save(
    "theme-search-client-admin.gif",
    save_all=True,
    append_images=frames[1:],
    duration=2000,  # Duración de cada cuadro en milisegundos
    loop=0,  # Número de loops (0 significa infinito)
)
