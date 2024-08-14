from authentication.models import User
from .models import Order, Investment
import string
import random
import datetime
from django.utils import timezone
from account.models import Account
from django.db import transaction
from decimal import Decimal


# Create your views here.
def generateOrderId(length = 7):
    id = "".join(random.choice(string.digits) for _ in range(length))
    try:
        order = Order.objects.get(orderId = id)
        return generateOrderId()
    except Order.DoesNotExist:
        return id
    except Exception as e:
        return Exception(message=e)

def generateInvestmentId(length = 7):
    id = "".join(random.choice(string.digits) for _ in range(length))
    try:
        order = Investment.objects.get(orderId = id)
        return generateInvestmentId()
    except Investment.DoesNotExist:
        return id
    except Exception as e:
        return Exception(message=e)

@transaction.atomic
def update_all_investment(userId):
    invplan = {'bronze':0.2,'silver':0.4,'gold':0.6,'vip':0.8}
    now = timezone.now()
    try:
        account = Account.objects.get(user__id = userId)
        investment = Investment.objects.filter(user__id = userId, status = 'ongoing')

        #loop through all investments and get which date is due
        for inv in investment:
            if inv.end_date <= now:
                amount = inv.amount
                plan = inv.plan
                roi = Decimal(invplan[plan]) * amount
                inv.status = 'completed'
                account.balance += roi + amount
                account.active_investment -= amount
                account.total_earnings += roi
                inv.save()
                account.save()
    
        return True
    except Exception as e:
        print(f"error updating transaction: {e}")


def createDepositFun(**data):
    orderId = generateOrderId()
    try:
        user = User.objects.get(id=data['id'])
        del data['id']
        order = Order.objects.create(orderId=orderId, user=user, type="deposit", **data)
        return order.orderId
    except User.DoesNotExist:
        return "user does not exist"
    except Exception as e:
        return str(e)

@transaction.atomic
def createInvestFun(**data):
    orderId = generateInvestmentId()
    userId =  data['id']
    del data['id']
    plans = {
        'bronze': {'duration': 24, "min":50},
        'silver': {'duration': 48, "min":350},
        'gold': {'duration': 72, "min":900},
        'vip': {'duration': 24*5, "min":5000},
    }
    if data['amount'] < plans[data['plan']].get('min'):
        return {'status': 'failed', 'code': 'please enter a valid amount'}
    try:
        user = User.objects.get(id=userId)
        end_date = datetime.datetime.now() + datetime.timedelta(hours=plans[data['plan']]['duration'])
        account = Account.objects.get(user__id = userId)
        if account.balance < data['amount']:
            return {'status': 'failed', 'code': 'insufficient balance, please fund your wallet'}
        account.balance -= data['amount']
        account.active_investment += data['amount']
        account.save()
        order = Investment.objects.create(orderId=orderId, user=user, end_date=end_date, **data)
        return {"status":"success", "orderId": order.orderId}
    except User.DoesNotExist:
        return {'status': 'failed', 'code': 'user does not exist'}
    except Exception as e:
        return {'status': 'failed', 'code': str(e)}

@transaction.atomic
def createWithdrawFun(**data):
    orderId = generateOrderId()
    userId = data['id']
    del data['id']
    try:
        user = User.objects.get(id=userId)
        account = Account.objects.get(user__id=userId)
        if account.balance < data['amount']:
            return {'status': 'failed', 'code': "insufficient wallet balance"}
        account.pending_withdraw += data['amount']
        account.save()
        order = Order.objects.create(orderId=orderId, user=user, type="withdraw", **data)
        return order.orderId
    except User.DoesNotExist:
        return {'status':'failed', 'code':"user does not exist"}
    except Exception as e:
        return str(e)
