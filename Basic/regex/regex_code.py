import re

text = "@robot9 "

print(re.findall(r"\d", text))
print(re.findall(r"\w", text))
print(re.findall(r"\s", text))

angka = "1234"

text = "Budi suka makan buah apel"

print(re.findall(r"\d+", angka))
print(re.findall(r"\w+", text))

text = "Poseidon dan Zeus"

print(re.findall(r"[aiueo]", text))

text = "Air, api, tanah, udara"

print(re.findall(r"Air|Water", text))
