# Que son las expresiones regulares en Python?
""" Son esencialmente en un lenguaje de programación diminuto y altamente especializado incrustado dentro de Python y disponible a través del módulo re. Usando este pequeño lenguaje, especificas las reglas para el conjunto de cadenas de caracteres posibles que deseas hacer coincidir; este conjunto puede contener frases en inglés, o direcciones de correo electrónico, o comandos TeX, o cualquier cosa que desee. """


# Quizás el metacarácter más importante es la barra invertida, \. Al igual que en los literales de cadena de Python, la barra invertida puede ir seguida de varios caracteres para señalar varias secuencias especiales. 
# Tomemos un ejemplo: \w coincide con cualquier carácter alfanumérico. Si el patrón de expresiones regulares se expresa en bytes, esto es equivalente a la clase [a-zA-Z0-9_]. Si el patrón de expresiones regulares es una cadena de caracteres, \w coincidirá con todos los caracteres marcados como letras en la base de datos Unicode proporcionada por el módulo unicodedata.
""" fuente: https://docs.python.org/es/3/howto/regex.html """

#Metacarácteres
meta = ". ^ $ * + ? { } [ ] \ | ( )"