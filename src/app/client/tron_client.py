from tronpy import Tron


from ..models.dto import TronInfo
# Создаем объект Tron
tron = Tron()

# Укажите адрес, для которого хотите получить информацию
address = 'ВАШ_АДРЕС_TRON'

# Получаем информацию о аккаунте
account_info = tron.get_account(address)

# Получаем баланс TRX
balance_trx = account_info['balance'] / 1_000_000  # Баланс в TRX (значение в SUN, 1 TRX = 1_000_000 SUN)

# Получаем информацию о bandwidth и energy
bandwidth = account_info['bandwidth']
energy = account_info['energy']

# Выводим информацию
print(f"Баланс TRX: {balance_trx} TRX")
print(f"Доступная пропускная способность (bandwidth): {bandwidth}")
print(f"Доступная энергия (energy): {energy}")


class TronClient:
    def __init__(self, tron):
        self.tron = tron

    async def get_address_info(self, address: str):
        info = tron.get_account(address)
        return TronInfo(address=address, trx_balance=info['balance'], bandwidth=info['bandwidth'], energy=info['energy'])
