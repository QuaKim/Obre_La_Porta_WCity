import logging
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_USERNAME, CONF_PASSWORD
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

class ObreLaPortaConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            email = user_input[CONF_USERNAME].strip()
            password = user_input[CONF_PASSWORD].strip()

            return self.async_create_entry(
                title=f"Basura ({email})",
                data={
                    CONF_USERNAME: email,
                    CONF_PASSWORD: password,
                },
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_USERNAME): str,
                vol.Required(CONF_PASSWORD): str,
            }),
        )