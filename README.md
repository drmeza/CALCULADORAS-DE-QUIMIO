# 🩺 Calculadoras Clínicas de Quimioterapia (Esquema AC-T)

Este repositorio contiene las herramientas de cálculo y dosificación automatizada para el esquema de quimioterapia **AC-T** (Doxorrubicina, Ciclofosfamida y Taxanos), utilizado  en el tratamiento neoadyuvante y adyuvante del cáncer de mama.

Desarrollado en **Python**, el código traduce de forma precisa guías de práctica clínica internacionales (NCCN / ASCO) para apoyar en la prescripción médica, minimizando el riesgo de errores de cálculo antropométrico y dosificación.

---

## 📌 Contenido del Repositorio

* **`fase_ac_roja.py`**: Calculadora de la Fase AC (Doxorrubicina + Ciclofosfamida). Incluye esquema de antiemesis y profilaxis hematopoyética con Filgrastim.
  
* **`fase_t_blanca.py`**: Calculadora de la Fase T (Paclitaxel Semanal / Docetaxel Trisemanal). Incluye premedicación contra reacciones de hipersensibilidad y especificaciones clínicas de infusión (uso de filtro de 0.22 micras).

---

## 📐 Parámetros Clínicos Integrados

1. **Superficie Corporal (SC):** Calculada mediante la ecuación validada de **DuBois & DuBois**:
   $$SC (m^2) = 0.007184 \times \text{Peso}^{0.425} \times \text{Talla}^{0.725}$$
   
3. **Esquemas de Dosificación Basales:**
   * **Doxorrubicina:** $60 \text{ mg/m}^2$
   * **Ciclofosfamida:** $600 \text{ mg/m}^2$
   * **Paclitaxel (Semanal):** $80 \text{ mg/m}^2$
   * **Docetaxel (Trisemanal):** $75 \text{ mg/m}^2$

---

## 🚀 Cómo Ejecutar los Scripts Localmente

Para ejecutar cualquiera de las calculadoras desde la terminal:

```bash
# Para la Fase AC
python fase_ac_roja.py

# Para la Fase T
python fase_t_blanca.py
