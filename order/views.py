from authentication.models import User
from utils.mail import send_mail
from .models import Order, Investment
import string
import random
import datetime
from django.utils import timezone
from account.models import Account
from django.db import transaction
from decimal import Decimal


# Create your views here.
def generateOrderId(length=7):
    id = "".join(random.choice(string.digits) for _ in range(length))
    try:
        order = Order.objects.get(orderId=id)
        return generateOrderId()
    except Order.DoesNotExist:
        return id
    except Exception as e:
        return Exception(message=e)


def generateInvestmentId(length=7):
    id = "".join(random.choice(string.digits) for _ in range(length))
    try:
        order = Investment.objects.get(orderId=id)
        return generateInvestmentId()
    except Investment.DoesNotExist:
        return id
    except Exception as e:
        return Exception(message=e)


@transaction.atomic
def update_all_investment(userId):
    plans = {
        "bronze": {"duration": 24, "min": 50, 'roi': 0.2},
        "silver": {"duration": 48, "min": 350, 'roi': 0.4},
        "gold": {"duration": 72, "min": 900, 'roi': 0.6},
        "vip": {"duration": 24 * 5, "min": 5000, 'roi': 0.8},
    }

    now = timezone.now()
    try:
        account = Account.objects.select_for_update().get(user__id=userId)

        investments = Investment.objects.filter(
            user__id=userId,
            user__isSuspended=False,
            status="ongoing",
            end_date__lte=now
        )

        for inv in investments:
            amount = inv.amount
            plan = inv.plan
            roi_rate = Decimal(str(plans[plan]["roi"]))
            duration = plans[plan]["duration"]

            loop_count = 0
            while inv.end_date <= now and loop_count < 5:
                # Calculate ROI for one cycle
                roi = roi_rate * amount

                # Extend end_date by plan duration
                inv.end_date = inv.end_date + timezone.timedelta(hours=duration)

                # Update account balances
                account.balance += roi + amount
                account.total_earnings += roi

                loop_count += 1

            inv.save(update_fields=["end_date"])

        account.save(update_fields=["balance", "total_earnings"])
        return True
    except Exception as e:
        print(f"error updating transaction: {e}")


def createDepositFun(**data):
    orderId = generateOrderId()
    try:
        user = User.objects.get(id=data["id"])
        del data["id"]
        order = Order.objects.create(orderId=orderId, user=user, type="deposit", **data)
        try:
            message = f"""
We have received your deposit and it is currently being processed.

Deposit Details:

Amount: ${order.amount:.2f}

Date: {order.date}

Transaction ID: #{order.orderId}

Please note that processing may take some time depending on your payment method. You will receive another notification once the deposit is fully confirmed and available in your account.

Thank you for choosing Onedex Investment."""
            send_mail(
                order.user.email,
                "Deposit Received – Processing in Progress | Onedex Investment",
                message,
                order.user.fullname,
            )
        except Exception as e:
            pass
        return order.orderId
    except User.DoesNotExist:
        return "user does not exist"
    except Exception as e:
        return str(e)


@transaction.atomic
def createInvestFun(**data):
    orderId = generateInvestmentId()
    userId = data["id"]
    del data["id"]
    plans = {
        "bronze": {"duration": 24, "min": 50},
        "silver": {"duration": 48, "min": 350},
        "gold": {"duration": 72, "min": 900},
        "vip": {"duration": 24 * 5, "min": 5000},
    }
    if data["amount"] < plans[data["plan"]].get("min"):
        return {"status": "failed", "code": "please enter a valid amount"}
    try:
        user = User.objects.get(id=userId)
        end_date = datetime.datetime.now() + datetime.timedelta(
            hours=plans[data["plan"]]["duration"]
        )
        account = Account.objects.get(user__id=userId)
        if account.balance < data["amount"]:
            return {
                "status": "failed",
                "code": "insufficient balance, please fund your wallet",
            }
        account.balance -= data["amount"]
        account.active_investment += data["amount"]
        account.save()
        order = Investment.objects.create(
            orderId=orderId, user=user, end_date=end_date, **data
        )
        return {"status": "success", "orderId": order.orderId}
    except User.DoesNotExist:
        return {"status": "failed", "code": "user does not exist"}
    except Exception as e:
        return {"status": "failed", "code": str(e)}


@transaction.atomic
def createWithdrawFun(**data):
    orderId = generateOrderId()
    userId = data["id"]
    del data["id"]
    try:
        user = User.objects.get(id=userId)
        account = Account.objects.get(user__id=userId)
        if account.total_earnings < data["amount"]:
            return {"status": "failed", "code": "insufficient wallet earnings!!"}
        account.pending_withdraw += data["amount"]
        account.save()
        order = Order.objects.create(
            orderId=orderId, user=user, type="withdraw", **data
        )
        try:
            message = f"""
We have received your withdrawal request and it is currently being processed.

Deposit Details:

Amount: ${order.amount:.2f}

Date: {order.date}

Transaction ID: #{order.orderId}

Please note that processing times may vary depending on your bank or payment provider. You will receive a confirmation email once the withdrawal has been successfully completed.

Thank you for choosing Onedex Investment."""
            send_mail(
                user.email,
                "Withdrawal Request Received – Processing | Onedex Investment",
                message,
                user.fullname,
            )
        except Exception as e:
            pass

        return order.orderId
    except User.DoesNotExist:
        return {"status": "failed", "code": "user does not exist"}
    except Exception as e:
        return str(e)
