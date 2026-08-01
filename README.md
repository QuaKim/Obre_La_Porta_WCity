# 🗑️ Obre la Porta W-City (Mancomunitat Penedès-Garraf) — Home Assistant

Integración personalizada (*custom component*) para Home Assistant diseñada para consultar automáticamente el calendario de recogida de residuos puerta a puerta gestionado por la **Mancomunitat Penedès-Garraf** a través de la plataforma W-City.

### 📍 Ámbito de aplicación
Diseñado específicamente para los municipios adheridos al sistema de recogida puerta a puerta de la **Mancomunitat Penedès-Garraf** (Olèrdola, El Pla del Penedès, La Granada, Sant Pere de Riudebitlles, Sant Quintí de Mediona, Sant Sadurní d'Anoia, Torrelavit) que utilizan el portal web W-City.


### ✨ Características principales (v0.1.0)
* **Scraping directo:** Obtención del estado directamente desde la plataforma W-City de la Mancomunitat.
* **Sensor de estado:** Genera la entidad `sensor.basura_hoy` con la fracción del día (ej. *PAPEL*, *RESTO*, *ORGANICA*).
* **Frecuencia de actualización:** Consulta automática cada 30 minutos.
* **Configuración sencilla:** Introducción de credenciales desde el propio menú de Home Assistant (*Config Flow*).
* **Soporte HACS:** Preparado para instalar como repositorio personalizado.
