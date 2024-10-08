import cv2
import sys
import dlib

# Carrega o detector de rostos fora da função, para não inicializá-lo repetidamente
face_detector = dlib.get_frontal_face_detector()


def validar_argumentos():
    if len(sys.argv) != 2:
        print("Uso: python face_detection.py <caminho_da_imagem>")
        sys.exit()


def carregar_imagem(image_path):
    # Carrega a imagem diretamente em escala de cinza para economizar recursos
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print(f"Erro ao carregar a imagem: {image_path}")
        sys.exit()

    return image


def detectar_rostos(image_gray):
    # Detecta os rostos na imagem em escala de cinza
    return face_detector(image_gray)


def desenhar_retangulos(image, faces):
    # Desenha retângulos ao redor dos rostos detectados
    for face in faces:
        x, y, w, h = (face.left(), face.top(), face.width(), face.height())
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


def exibir_resultado(image, num_faces):
    # Exibe o número de rostos detectados
    print(f"Rostos detectados: {num_faces}")

    # Exibe a imagem com os rostos detectados
    cv2.imshow('Face Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    validar_argumentos()
    image_path = sys.argv[1]

    # Carrega a imagem original e em escala de cinza
    image = cv2.imread(image_path)
    image_gray = carregar_imagem(image_path)

    # Detecta os rostos
    faces = detectar_rostos(image_gray)

    # Desenha os retângulos nos rostos detectados
    desenhar_retangulos(image, faces)

    # Exibe o resultado
    exibir_resultado(image, len(faces))


if __name__ == "__main__":
    main()
