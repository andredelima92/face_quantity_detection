import cv2
import sys
import dlib


def detect_faces(image_path):
    # Carrega a imagem
    image = cv2.imread(image_path)

    if image is None:
        print(f"Erro ao carregar a imagem: {image_path}")
        sys.exit()

    # Converte a imagem para escala de cinza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Carrega o detector de rostos pré-treinado do dlib
    face_detector = dlib.get_frontal_face_detector()

    # Detecta os rostos na imagem
    faces = face_detector(gray)

    # Desenha retângulos ao redor dos rostos detectados
    for face in faces:
        x, y, w, h = (face.left(), face.top(), face.width(), face.height())
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Exibe o número de rostos detectados
    print(f"Rostos detectados: {len(faces)}")

    # Exibe a imagem com os rostos detectados
    cv2.imshow('Face Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python face_detection.py <caminho_da_imagem>")
        sys.exit()

    image_path = sys.argv[1]
    detect_faces(image_path)
