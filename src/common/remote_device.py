import logging
from pydantic import BaseModel

logger = logging.getLogger(__name__)


class RPIDevice(BaseModel):

    # MAC ID of the primary NIC on the RPI, b8:27:eb:1f:8a:63
    device_id: str
