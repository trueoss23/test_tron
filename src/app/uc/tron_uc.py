import logging

from ..client.tron_client import TronClient
from ..models.dto import TronInfo
from ..repo import TronRequest


class TronUC:
    def __init__(self, repo: TronRequest, client: TronClient):
        self.repo = repo
        self.client = client

    async def get_address_info(self, address: str) -> TronInfo:
        res = await self.client.get_address_info(address=address)

        try:
            # TODO: реализовать метод
            await self.repo.save_address_info()
        except Exception as e:
            logging.error(f"Данные о запросе не записались в бд. {e}")
        return res
