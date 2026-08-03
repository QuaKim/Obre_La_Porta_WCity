# W-City - Recogida Porta a Porta (Home Assistant Integration)

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)
[![GitHub Release](https://img.shields.io/github/v/release/QuaKim/Obre_La_Porta_WCity)](https://github.com/TU-USUARIO/TU-REPOSITORIO/releases)
[![License](https://img.shields.io/github/license/QuaKim/Obre_La_Porta_WCity)](LICENSE)

Integración personalizada para **Home Assistant** que conecta con la plataforma **W-City** para la gestión del servicio de recogida de residuos **Porta a Porta (PaP)**.

> 📍 **Soporte actual:** Inicialmente compatible con la **Mancomunitat Penedès Garraf** (servicio *"Obre la Porta"* - `obrelaporta.wcity.app`). Pensado para ir añadiendo soporte a otros municipios o mancomunidades que utilicen la plataforma W-City.

---

## 📊 Entidades Generadas

La integración proporciona las siguientes entidades principales:

* **Sensor de Recogida del Día:** Indica la fracción de residuo que corresponde sacar en el día de hoy (ej. *Orgànica*, *Envasos*, *Paper i Cartró*, *Resto*, etc.).
* **Calendario del Mes en Curso (`calendar`):** Muestra la planificación y el desglose completo de todas las recogidas programadas para el **mes en curso**, permitiendo consultar cualquier día del mes actual en tu interfaz o mediante automatizaciones.

---

## 🛠️ Instalación mediante HACS

### Paso 1: Añadir como Repositorio Personalizado

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=QuaKim&repository=Obre_La_Porta_WCity&category=integration)

1. Abre **Home Assistant** y ve a **HACS** > **Integraciones**.
2. Haz clic en los tres puntos de la esquina superior derecha `⋮` y selecciona **Repositorios personalizados** (*Custom repositories*).
3. Añade la URL de este repositorio: https://github.com/QuaKim/Obre_La_Porta_WCity
4. Instalar Obre_La_Porta_WCity
5. Reinciar Home Assitant

### Paso 2: Añadir como Integración

1. Añadir Obre_La_Porta_WCity desde Configuración > Dispositivos y Servicios
2. Introducir tus credenciales de acceso. 

