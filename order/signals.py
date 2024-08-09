
import logging
from account.models import Account

def handle_order_signal(old_data, new_data):
    old_status, new_status = (old_data['status'], new_data['status'] )
    userId = new_data['user']
    amount = new_data['amount']
    type = new_data['type']

    try:
        account = Account.objects.get(user__id = userId)

        if old_status == new_status:
            print('status did not change')
            return True
        
        if new_status == 'approved':
            # if type is deposit
            if type == "deposit":
                account.balance += amount
                account.last_deposit = amount
                account.save()
            
            #if type is withdraw
            if type == "withdraw":
                account.balance -= amount
                account.pending_withdraw -= amount
                account.save()

        if new_status == "declined":
            # remove from pending withdraw if type if withdraw
            if type == 'withdraw':
                account.pending_withdraw -= amount
                account.save()

    except Exception as e:
        print(f'error signaling order presave: {str(e)}')

