"""Prompts del asistente y construcción de la lista de mensajes.

Los prompts son parte del diseño de la aplicación: se versionan y se revisan
como cualquier otro código.
"""

from llm_client import Message

# TODO 4: diseña el prompt de sistema del asistente. Como mínimo debe:
#   - definir el rol (asistente del curso de IA) y el idioma de respuesta;
#   - indicar el nivel de los estudiantes (ya conocen Transformers);
#   - prohibir inventar información específica del curso (fechas, notas, programa).

SYSTEM_PROMPT = """
Eres un asistente académico para estudiantes de un curso universitario de
Inteligencia Artificial. Responde siempre en español, de manera clara,
precisa y pedagógica.

Los estudiantes ya conocen los fundamentos de los Transformers, incluyendo
tokens, embeddings y mecanismos de atención. Adapta tus explicaciones a ese
nivel y evita repetir conceptos básicos, salvo que el estudiante lo solicite.

Puedes responder preguntas de conocimiento general sobre inteligencia
artificial. Sin embargo, no debes inventar información específica del curso,
como fechas, calificaciones, plazos, programa, políticas, actividades o
materiales internos.

Cuando una pregunta dependa de información específica del curso que no se
encuentre en la conversación, indica claramente que no tienes esa información
y recomienda consultar el programa, la plataforma del curso o al docente.
"""


ANALYSIS_PROMPT = """Analiza la pregunta de un estudiante del curso de IA.
Responde ÚNICAMENTE con un objeto JSON con exactamente estas claves:
- "tema": tema principal de la pregunta, en pocas palabras.
- "dificultad": uno de "basica", "intermedia" o "avanzada".
- "requiere_documentos_del_curso": true si la respuesta depende de información específica \
del curso (fechas, notas, programa, material propio) que no es conocimiento general; false en otro caso.
- "respuesta_corta": respuesta en máximo dos frases; si requiere documentos del curso, \
escribe "No tengo esa información"."""


def build_messages(history: list[Message], user_input: str) -> list[Message]:
    """Construye lo que realmente recibe el LLM: system + historial + pregunta actual."""
    # TODO 3: devuelve una lista con, en este orden:
    #   1. el mensaje de rol "system" con SYSTEM_PROMPT;
    #   2. todos los mensajes de history;
    #   3. el mensaje de rol "user" con user_input.
    return [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        *history,
        {
            "role": "user",
            "content": user_input,
        },
    ]
