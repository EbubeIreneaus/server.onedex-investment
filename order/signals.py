import logging
from account.models import Account
from authentication.models import User
from order.models import Investment
from order.views import generateOrderId
from utils.mail import send_mail
import datetime


def handle_order_signal(old_data, new_data):
    old_status, new_status = (old_data["status"], new_data["status"])
    userId = new_data["user"]
    amount = new_data["amount"]
    type = new_data["type"]

    try:
        account = Account.objects.get(user__id=userId)
        user = User.objects.get(id=userId)

        if old_status == new_status:
            print("status did not change")
            return True

        if new_status == "approved":
            # if type is deposit
            if type == "deposit":
                account.last_deposit = amount
                # create investment
                arr = ["vip", "gold", "silver", "bronze"]
                plans = {
                    "bronze": {"duration": 24, "min": 50},
                    "silver": {"duration": 48, "min": 350},
                    "gold": {"duration": 72, "min": 900},
                    "vip": {"duration": 24 * 5, "min": 5000},
                }
                invest_plan = "bronze"
                for plan in arr:
                    if plans[plan]['min'] <= int(amount):
                        invest_plan = plan
                    break
                id = generateOrderId()
                end_date = datetime.datetime.now() + datetime.timedelta(
                    hours=plans[plan]["duration"]
                )
                Investment.objects.create(
                    user=user, amount=amount, plan=invest_plan, orderId=id, end_date=end_date
                )
                account.active_investment = account.active_investment + amount
                account.save()
                try:
                    message = f"""
We are pleased to inform you that we have successfully received your deposit.

Deposit Details:

Amount: ${amount:.2f}

Date: {datetime.datetime.now().strftime("%Y-%m-%d")}

Transaction ID: #{new_data['orderId']}

Your funds are now active on investement.

Thank you for choosing Onedex Investment."""
                    send_mail(user.email, "Deposit Approved", message, user.fullname)
                except Exception as e:
                    print("error",str(e))

            # if type is withdraw
            if type == "withdraw":
                account.total_earnings -= amount
                account.pending_withdraw -= amount
                account.save()
                try:
                    message = f"""
We are pleased to inform you that your withdrawal request has been successfully processed.

Withdrawal Details:

Amount: ${amount:.2f}

Date: {datetime.datetime.now().strftime("%Y-%m-%d")}

Transaction ID: #{new_data['orderId']}

The funds have been sent to your designated account. Please allow some time for your bank or payment provider to complete the transfer.

Thank you for choosing Onedex Investment."""
                    send_mail(
                        user.email,
                        "Withdrawal Request Confirmation",
                        message,
                        user.fullname,
                    )
                except Exception as e:
                    pass

        if new_status == "declined":
            # remove from pending withdraw if type if withdraw
            if type == "withdraw":
                account.pending_withdraw -= amount
                account.save()

    except Exception as e:
        print(f"error signaling order presave: {str(e)}")
