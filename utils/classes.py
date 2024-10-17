from ninja import Schema

class NotFoundError(Schema):
    message: str
    
class LoginUserIntake(Schema):
    email: str
    password: str

class UserInfo(Schema):
    fullname: str
    email: str
    id: None | str
    isSuspended: bool | None

class AccountInfo(Schema):
    user: UserInfo
    balance: float
    active_investment: float
    pending_withdraw: float
    total_earnings: float

class CreateDepositScheme(Schema):
    id: str
    amount: int
    channel: str

class CreateWithdrawScheme(Schema):
    id: str
    amount: int
    channel: str
    wallet: str

class CreateInvestScheme(Schema):
    id: str
    amount: int
    plan: str


class OrderOut(Schema):
    orderId: str
    type: str
    status: str
    amount: int
    channel: str | None

class InvestmentOut(Schema):
    orderId: str
    plan: str
    status: str
    amount: int