from pydantic import BaseModel, field_validator


class TronInfo(BaseModel):
    address: str
    trx_balance: float
    energy: int
    bandwidth: int

    @field_validator('address')
    def validate_tron_address(self, value):
        # Проверяем, что адрес начинается с 'T' и имеет длину 34 символа
        if not value.startswith('T'):
            raise ValueError('Address must start with "T"')
        if len(value) != 34:
            raise ValueError('Address must be 34 characters long')
        # Проверяем, что остальные символы являются допустимыми (буквы и цифры)
        if not all(c.isalnum() for c in value[1:]):
            raise ValueError('Address must contain only alphanumeric characters after the initial "T"')
        return value
