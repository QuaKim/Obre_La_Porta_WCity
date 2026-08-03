# Recollida Porta a Porta - WCity (Home Assistant Integration)

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)
[![GitHub Release](https://img.shields.io/github/v/release/QuaKim/Recollida-Porta-a-Porta-WCity)](https://github.com/QuaKim/Recollida-Porta-a-Porta-WCity/releases)
[![License](https://img.shields.io/github/license/QuaKim/Recollida-Porta-a-Porta-WCity)](LICENSE)

<details>
<summary><b><img src="https://upload.wikimedia.org/wikipedia/commons/c/ce/Flag_of_Catalonia.svg" width="20" height="14" alt="Català"> Clic per veure la versió en Català</b></summary>

### Versió en Català
Integració personalitzada per a **Home Assistant** que connecta amb la plataforma **W-City**...

Integració personalitzada per a **Home Assistant** que connecta amb la plataforma **W-City** per a la gestió del servei de recollida de residus **Porta a Porta (PaP)**.

> 📍 **Suport actual:** Inicialment compatible amb la **Mancomunitat Penedès Garraf** (servei *"Obre la Porta"* - `obrelaporta.wcity.app`). Pensat per anar afegint suport a altres municipis o mancomunitats que utilitzin la plataforma W-City.

---

## 📊 Entitats Generades

La integració proporciona les següents entitats principals:

* **Sensor de Recollida del Dia:** Indica la fracció de residu que correspon treure en el dia d'avui (ex. *Orgànica*, *Envasos*, *Paper i Cartró*, *Resta*, etc.).
* **Calendari del Mes en Curs (`calendar`):** Mostra la planificació i el desglossament complet de totes les recollides programades per al **mes en curs**, permetent consultar qualsevol dia del mes actual a la teva interfície o mitjançant automatitzacions.

---

## 🛠️ Instal·lació 

### Opció 1: HACS (Custom Repository) — *Recomanat*

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=jQuaKim&repository=Recollida-Porta-a-Porta-WCity&category=integration)

1. Obre **HACS** > **Integracions** > Tres punts (dalt a la dreta) > **Repositoris personalitzats**.
2. Afegeix la URL: `https://github.com/jQuaKim/Recollida-Porta-a-Porta-WCity` (Categoria: *Integració*).
3. Fes clic a **Descarregar** i reinicia Home Assistant.
4. Ves a **Ajustos > Dispositius i serveis > Afegir integració** i cerca **Recollida Porta a Porta WCity**.
5. **Autenticació:** Introdueix les teves credencials d'accés del portal WCity per finalitzar la configuració.

---

### Opció 2: Instal·lació Manual

1. Descarrega la darrera versió (*Release*) des de l'apartat de [Releases de GitHub](https://github.com/jQuaKim/Recollida-Porta-a-Porta-WCity/releases).
2. Descomprimeix el fitxer zip.
3. Copia la carpeta `wcity_pap` dins del directori `custom_components` de la teva instal·lació de Home Assistant:
   ```text
   config/
   └── custom_components/
       └── wcity_pap/
           ├── __init__.py
           ├── manifest.json
           ├── sensor.py
           └── ...
4. Ves a **Ajustos > Dispositius i serveis > Afegir integració** i cerca **Recollida Porta a Porta WCity**.
5. **Autenticació:** Introdueix les teves credencials d'accés del portal WCity per finalitzar la configuració.
6. 
</details>

Integración personalizada para **Home Assistant** que conecta con la plataforma **W-City** para la gestión del servicio de recogida de residuos **Porta a Porta (PaP)**.

> 📍 **Soporte actual:** Inicialmente compatible con la **Mancomunitat Penedès Garraf** (servicio *"Obre la Porta"* - `obrelaporta.wcity.app`). Pensado para ir añadiendo soporte a otros municipios o mancomunidades que utilicen la plataforma W-City.

---

## 📊 Entidades Generadas

La integración proporciona las siguientes entidades principales:

* **Sensor de Recogida del Día:** Indica la fracción de residuo que corresponde sacar en el día de hoy (ej. *Orgànica*, *Envasos*, *Paper i Cartró*, *Resta*, etc.).
* **Calendario del Mes en Curso (`calendar`):** Muestra la planificación y el desglose completo de todas las recogidas programadas para el **mes en curso**, permitiendo consultar cualquier día del mes actual en tu interfaz o mediante automatizaciones.

---

## 🛠️ Instalación 

### Opción 1: HACS (Custom Repository) — *Recomendado*

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=jQuaKim&repository=Recollida-Porta-a-Porta-WCity&category=integration)

1. Abre **HACS** > **Integraciones** > Tres puntos (arriba a la derecha) > **Repositorios personalizados**.
2. Añade la URL: `https://github.com/jQuaKim/Recollida-Porta-a-Porta-WCity` (Categoría: *Integración*).
3. Haz clic en **Descargar** y reinicia Home Assistant.
4. Ve a **Ajustes > Dispositivos y servicios > Añadir integración** y busca **Recollida Porta a Porta WCity**.
5. **Autenticación:** Introduce tus credenciales de acceso del portal WCity para finalizar la configuración.

---

### Opción 2: Instalación Manual

1. Descarga la última versión (*Release*) desde el apartado de [Releases de GitHub](https://github.com/jQuaKim/Recollida-Porta-a-Porta-WCity/releases).
2. Descomprime el archivo comprimido.
3. Copia la carpeta `wcity_pap` dentro del directorio `custom_components` de tu instalación de Home Assistant:
   ```text
   config/
   └── custom_components/
       └── wcity_pap/
           ├── __init__.py
           ├── manifest.json
           ├── sensor.py
           └── ...
4. Ve a **Ajustes > Dispositivos y servicios > Añadir integración** y busca **Recollida Porta a Porta WCity**.
5. **Autenticación:** Introduce tus credenciales de acceso del portal WCity para finalizar la configuración.

