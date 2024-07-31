from typing import List
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, Schema
from account.models import Account
from authentication.views import Register, Login, updateFullname, verifyOTPCode, send_otp_code
from order.models import Order
from order.views import createDepositFun, createInvestFun, createWithdrawFun
from utils.classes import (
    CreateInvestScheme,
    LoginUserIntake,
    OrderOut,
    UserInfo,
    NotFoundError,
    AccountInfo,
    CreateDepositScheme,
    CreateWithdrawScheme,
)
from authentication.models import User

api = NinjaAPI()


# Shemas
class UserIntake(Schema):
    fullname: str
    email: str
    password: str


@api.post("/auth/signup")
def newUser(request, payload: UserIntake):
    user = Register(**payload.dict())
    return user


@api.post("/auth/signin")
def authUser(request, payload: LoginUserIntake):
    user = Login(**payload.dict())
    return user


@api.get("/requestOTP")
def sendOTP(request, id: str, label: str):
    """REQUEST OTP CODE"""
    requestOTP = send_otp_code(id=id, label=label)
    return {"status": "reached", "code": requestOTP}


@api.get("/verifyOTP")
def verifyOTP(request, id: str, otp: int):
    """verify User OTP code"""
    res = verifyOTPCode(id=id, otp=otp)
    return res


@api.get("/userInfo", response={200: UserInfo})
def userInfo(request, id: str):
    user = get_object_or_404(User, id=id)
    return user


@api.get("/accountInfo", response={200: AccountInfo})
def accountInfo(request, id: str):
    """Get Account Details"""
    account = get_object_or_404(Account, user__id=id)
    return account


@api.post("/order/deposit")
def createDeposit(request, payload: CreateDepositScheme):
    req = createDepositFun(**payload.dict())
    return req


@api.post("/order/withdraw")
def createWithdraw(request, payload: CreateWithdrawScheme):
    req = createWithdrawFun(**payload.dict())
    return req

@api.post("/order/invest")
def createInvest(request, payload: CreateInvestScheme):
    req = createInvestFun(**payload.dict())
    return req

@api.get("/order", response=List[OrderOut])
def getOrders(request, id: str):
    req = Order.objects.filter(user__id = id)
    return req

@api.get("/update/fullname")
def getOrders(request, id: str, name: str):
    req = updateFullname(id, name)
    return req