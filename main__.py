from PIL import Image

# Lista de imágenes (asegúrate de que sean del mismo tamaño)
imagenes = ["frame1.png", "frame2.png", "frame3.png"]

# Abrir las imágenes
frames = [Image.open(imagen) for imagen in imagenes]

# Crear el GIF
frames[0].save(
    "mi_animacion.gif",
    save_all=True,
    append_images=frames[1:],
    duration=200,  # Duración de cada cuadro en milisegundos
    loop=0,  # Número de loops (0 significa infinito)
)