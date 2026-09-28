## =========================================================
## CALCULADORA CLINICA ONCOLOGICA: FASE AC (ESQUEMA ROJO)
## =========================================================

print("=" * 55)
print("     CALCULADORA DE DOSIFICACIÓN FASE AC (ROJA)")
print("=" * 55)

# Captura de datos antropométricos del paciente
peso = float(input("Ingresa el peso del paciente (kg): "))
talla = float(input("Ingresa la talla del paciente (cm): "))

# Cálculo de Superficie Corporal mediante la fórmula DuBois & DuBois
sc = 0.007184 * (peso ** 0.425) * (talla ** 0.725)

# Dosificación
doxorrubicina_dosis = sc * 60
ciclofosfamida_dosis = sc * 600

print(f"\n" + "=" * 50)
print(f"PRESCRIPCIÓN FASE AC (Doxorrubicina / Ciclofosfamida)")
print(f"Superficie Corporal (SC): {sc:.2f} m²")
print("=" * 50)

print("\nPREMEDICACIÓN Y ANTIEMESIS:")
print("1. Akynzeo (Netupitant 300 mg / Palonosetrón 0.5 mg) 1 cap VO 1 hr antes de quimioterapia.")
print("2. Dexametasona 8 mg en 100 cc SS 0.9% pp IV en 10 minutos.")
print("3. Cloropiramina 20 mg en 100 cc SS 0.9% pp IV en 10 minutos.")

print("\nQUIMIOTERAPIA CITOSTÁTICA (ESQUEMA ROJO):")
print(f"1. Doxorrubicina: {doxorrubicina_dosis:.2f} mg en 100 cc SS 0.9% pp IV en 20 minutos.")
print(f"2. Ciclofosfamida: {ciclofosfamida_dosis:.2f} mg en 500 cc SS 0.9% pp IV en 60 minutos.")

print("\nSOPORTE HEMATOPOYÉTICO:")
print("1. Filgrastim 300 mcg SC c/24 hrs por 5 días (Días 2, 3, 4, 5 y 6 posterior a quimioterapia).")
