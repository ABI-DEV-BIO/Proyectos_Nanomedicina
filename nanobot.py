hallazgo = input("¿Qué detectó el nanobot? (bacteria/inflamacion/virus): ")

if hallazgo == "bacteria":
    print("Acción: Liberar antibiótico.")

elif hallazgo == "inflamacion":
    print("Acción: Liberar corticoide.")

elif hallazgo == "virus":
    print("Acción: Activar respuesta inmune.")

else:
    print("Estado normal: No se requiere acción.")
