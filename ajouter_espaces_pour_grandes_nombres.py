def ajouter_espaces_pour_grandes_nombres(nombre):
  """
  Ajoute des espaces à un nombre pour l'afficher de manière plus lisible,
  en tenant compte de nombres potentiellement grands (1000, 1000000, etc.).

  Args:
    nombre: Le nombre entier à formater.

  Returns:
    Une chaîne de caractères représentant le nombre avec des espaces ajoutés
    pour faciliter la lecture.
  """
  nombre_str = str(nombre)
  decimal_point_index = nombre_str.find('.')
  if decimal_point_index != -1:
    nombre_str = nombre_str[:decimal_point_index]  # Ne considérent que la partie entière

  espace_total = 0
  for i in range(len(nombre_str) - 1, -1, -1):
    if nombre_str[i] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
      if espace_total < 3:
        espace_total = 3
      else:
        espace_total = 0

      if espace_total > 0:
        print(" ", end="")
        espace_total -= 1
    else:
      print(nombre_str[i], end="")
      espace_total = 0

  return ""  # Retourne une chaine vide car la fonction  affiche directement