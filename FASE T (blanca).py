## =========================================================
## CALCULADORA CLINICA ONCOLOGICA: FASE T (ESQUEMA BLANCO)
## =========================================================

print("=" * 55)
print("     CALCULADORA DE DOSIFICACIÓN FASE T (BLANCA)")
print("=" * 55)

# Captura de datos antropométricos del paciente
peso = float(input("Ingresa el peso del paciente (kg): "))
talla = float(input("Ingresa la talla del paciente (cm): "))

# Cálculo de Superficie Corporal mediante la fórmula DuBois & DuBois
sc = 0.007184 * (peso ** 0.425) * (talla ** 0.725)

print("\n--- SELECCIÓN DE TAXANO ---")
print("1. Paclitaxel Semanal (80 mg/m²)")
print("2. Docetaxel Trisemanal (75 mg/m²)")
opcion = input("Elige la opción de esquema (1 ó 2): ")

if opcion == "1":
    paclitaxel_dosis = sc * 80
    print(f"\n" + "=" * 50)
    print(f"PRESCRIPCIÓN FASE T: PACLITAXEL SEMANAL (BLANCO)")
    print(f"Superficie Corporal (SC): {sc:.2f} m²")
    print("=" * 50)

    print("\nPREMEDICACIÓN:")
    print("1. Dexametasona 8 mg en 100 cc SS 0.9% pp IV en 10 minutos.")
    print("2. Ondansetron 8 mg en 100 cc SS 0.9% pp IV en 10 minutos.")
    print("3. Cloropiramina 20 mg en 100 cc SS 0.9% pp IV en 10 minutos.")

    print("\nQUIMIOTERAPIA CITOSTÁTICA:")
    print(f"1. Paclitaxel: {paclitaxel_dosis:.2f} mg en 250 cc SS 0.9% pp IV en 120 minutos (requiere filtro de 0.22 micras).")

elif opcion == "2":
    docetaxel_dosis = sc * 75
    print(f"\n" + "=" * 50)
    print(f"PRESCRIPCIÓN FASE T: DOCETAXEL TRISEMANAL (BLANCO)")
    print(f"Superficie Corporal (SC): {sc:.2f} m²")
    print("=" * 50)

    print("\nPREMEDICACIÓN:")
    print("1. Akynzeo (Netupitant 300 mg / Palonosetrón 0.5 mg) 1 cap VO previo a quimioterapia.")
    print("2. Dexametasona 8 mg en 100 cc SS 0.9% pp IV en 10 minutos.")
    print("3. Cloropiramina 20 mg en 100 cc SS 0.9% pp IV en 10 minutos.")

    print("\nQUIMIOTERAPIA CITOSTÁTICA:")
    print(f"1. Docetaxel: {docetaxel_dosis:.2f} mg en 500 cc SS 0.9% pp IV en 120 minutos.")

else:
    print("\n[ERROR] Opción inválida. Debes ingresar 1 o 2.")

print("\nSOPORTE HEMATOPOYÉTICO:")
print("No requiere Filgrastim profiláctico de rutina (evaluar solo si hay neutropenia previa o riesgo elevado).")
