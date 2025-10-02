from django.core.mail import EmailMultiAlternatives

def send_mail(to, subject, message, recipient=""):
    template= f"""
    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Email Template</title>
</head>
<body style="margin:0; padding:0; font-family: Arial, sans-serif; background-color:#f5f5f5;">

  <!-- Wrapper -->
  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background-color:#f5f5f5; padding:20px 0;">
    <tr>
      <td align="center">
        <table role="presentation" width="600" cellspacing="0" cellpadding="0" border="0" style="background:#ffffff; border-radius:8px; overflow:hidden;">

          <!-- Header -->
          <tr>
            <td align="center" style="background:#002147; padding:20px;">
              <img src="https://via.placeholder.com/100x50?text=Logo" alt="Onedex Investment" style="display:block; margin-bottom:10px;">
              <h1 style="color:#ffffff; margin:0; font-size:20px;">Onedex Investment</h1>
            </td>
          </tr>

          <!-- Content -->
          <tr>
            <td style="padding:30px; color:#333333; font-size:15px; line-height:1.6;">
              <!-- Replace this with your email content -->
              <p>Hello {recipient},</p>
              <p>{message}</p>
              <p>Best regards,<br>Onedex Investment Team</p>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td align="center" style="background:#f0f0f0; padding:20px; font-size:12px; color:#777777;">
              © 2025 Onedex Investment. All rights reserved.<br>
              <a href="#" style="color:#002147; text-decoration:none;">Unsubscribe</a>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>

</body>
</html>

"""
    mail = EmailMultiAlternatives()
    mail.to = [to]
    mail.subject = subject
    mail.body = message
    mail.attach_alternative(template, 'text/html')
    mail.from_email="ONEDEX INVESTMENT<service@onedex-lnvestment.com>"
    mail.send(fail_silently=False)