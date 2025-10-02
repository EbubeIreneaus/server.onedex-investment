from django.contrib.auth import authenticate
from .models import User
from account.models import Account
from uuid import uuid4
from django.core.mail import EmailMultiAlternatives
from utils.random import OTP
import datetime
from django.utils.timezone import make_aware
from django.db import transaction
from utils.mail import send_mail

# Create your views here.


def send_otp_code(id, label: str):
    otp_code = OTP(6)
    otp_valid_till = datetime.datetime.now() + datetime.timedelta(hours=24)

    try:
        user = User.objects.get(id=id)
        email = user.email
        user.OTP = otp_code
        user.OTP_VALID_TILL = otp_valid_till
        user.save()
        msg = (
            """
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html
        xmlns="http://www.w3.org/1999/xhtml"
        xmlns:v="urn:schemas-microsoft-com:vml"
        xmlns:o="urn:schemas-microsoft-com:office:office"
        lang="en"
        >
        <head>
            <title></title>
            <meta charset="UTF-8" />
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
            <!--[if !mso]>-->
            <meta http-equiv="X-UA-Compatible" content="IE=edge" />
            <!--<![endif]-->
            <meta name="x-apple-disable-message-reformatting" content="" />
            <meta content="target-densitydpi=device-dpi" name="viewport" />
            <meta content="true" name="HandheldFriendly" />
            <meta content="width=device-width" name="viewport" />
            <meta
            name="format-detection"
            content="telephone=no, date=no, address=no, email=no, url=no"
            />
            <style type="text/css">
            table {
                border-collapse: separate;
                table-layout: fixed;
                mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
            }
            table td {
                border-collapse: collapse;
            }
            .ExternalClass {
                width: 100%;
            }
            .ExternalClass,
            .ExternalClass p,
            .ExternalClass span,
            .ExternalClass font,
            .ExternalClass td,
            .ExternalClass div {
                line-height: 100%;
            }
            body,
            a,
            li,
            p,
            h1,
            h2,
            h3 {
                -ms-text-size-adjust: 100%;
                -webkit-text-size-adjust: 100%;
            }
            html {
                -webkit-text-size-adjust: none !important;
            }
            body,
            #innerTable {
                -webkit-font-smoothing: antialiased;
                -moz-osx-font-smoothing: grayscale;
            }
            #innerTable img + div {
                display: none;
                display: none !important;
            }
            img {
                margin: 0;
                padding: 0;
                -ms-interpolation-mode: bicubic;
            }
            h1,
            h2,
            h3,
            p,
            a {
                line-height: inherit;
                overflow-wrap: normal;
                white-space: normal;
                word-break: break-word;
            }
            a {
                text-decoration: none;
            }
            h1,
            h2,
            h3,
            p {
                min-width: 100% !important;
                width: 100% !important;
                max-width: 100% !important;
                display: inline-block !important;
                border: 0;
                padding: 0;
                margin: 0;
            }
            a[x-apple-data-detectors] {
                color: inherit !important;
                text-decoration: none !important;
                font-size: inherit !important;
                font-family: inherit !important;
                font-weight: inherit !important;
                line-height: inherit !important;
            }
            u + #body a {
                color: inherit;
                text-decoration: none;
                font-size: inherit;
                font-family: inherit;
                font-weight: inherit;
                line-height: inherit;
            }
            a[href^="mailto"],
            a[href^="tel"],
            a[href^="sms"] {
                color: inherit;
                text-decoration: none;
            }
            img,
            p {
                margin: 0;
                margin: 0;
                font-family: Lato, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial,
                sans-serif;
                line-height: 22px;
                font-weight: 400;
                font-style: normal;
                font-size: 16px;
                text-decoration: none;
                text-transform: none;
                letter-spacing: 0;
                direction: ltr;
                color: #333;
                text-align: left;
                mso-line-height-rule: exactly;
                mso-text-raise: 2px;
            }
            h1 {
                margin: 0;
                margin: 0;
                font-family: Roboto, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial,
                sans-serif;
                line-height: 34px;
                font-weight: 400;
                font-style: normal;
                font-size: 28px;
                text-decoration: none;
                text-transform: none;
                letter-spacing: 0;
                direction: ltr;
                color: #333;
                text-align: left;
                mso-line-height-rule: exactly;
                mso-text-raise: 2px;
            }
            h2 {
                margin: 0;
                margin: 0;
                font-family: Lato, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial,
                sans-serif;
                line-height: 30px;
                font-weight: 400;
                font-style: normal;
                font-size: 24px;
                text-decoration: none;
                text-transform: none;
                letter-spacing: 0;
                direction: ltr;
                color: #333;
                text-align: left;
                mso-line-height-rule: exactly;
                mso-text-raise: 2px;
            }
            h3 {
                margin: 0;
                margin: 0;
                font-family: Lato, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial,
                sans-serif;
                line-height: 26px;
                font-weight: 400;
                font-style: normal;
                font-size: 20px;
                text-decoration: none;
                text-transform: none;
                letter-spacing: 0;
                direction: ltr;
                color: #333;
                text-align: left;
                mso-line-height-rule: exactly;
                mso-text-raise: 2px;
            }
            </style>
            <style type="text/css">
            @media (min-width: 481px) {
                .hd {
                display: none !important;
                }
            }
            </style>
            <style type="text/css">
            @media (max-width: 480px) {
                .hm {
                display: none !important;
                }
            }
            </style>
            <style type="text/css">
            @media (min-width: 481px) {
                h1,
                img,
                p {
                margin: 0;
                margin: 0;
                }
                .t18,
                .t21,
                .t5,
                .t9 {
                width: 480px !important;
                }
                img,
                p {
                font-family: Lato, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial,
                    sans-serif;
                line-height: 22px;
                font-weight: 400;
                font-style: normal;
                font-size: 16px;
                text-decoration: none;
                text-transform: none;
                letter-spacing: 0;
                direction: ltr;
                color: #333;
                text-align: left;
                mso-line-height-rule: exactly;
                mso-text-raise: 2px;
                }
                h1 {
                font-family: Roboto, BlinkMacSystemFont, Segoe UI, Helvetica Neue,
                    Arial, sans-serif;
                line-height: 34px;
                font-weight: 400;
                font-style: normal;
                font-size: 28px;
                text-decoration: none;
                text-transform: none;
                letter-spacing: 0;
                direction: ltr;
                color: #333;
                text-align: left;
                mso-line-height-rule: exactly;
                mso-text-raise: 2px;
                }
                h2,
                h3 {
                margin: 0;
                margin: 0;
                font-family: Lato, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial,
                    sans-serif;
                font-weight: 400;
                font-style: normal;
                text-decoration: none;
                text-transform: none;
                letter-spacing: 0;
                direction: ltr;
                color: #333;
                text-align: left;
                mso-line-height-rule: exactly;
                mso-text-raise: 2px;
                }
                h2 {
                line-height: 30px;
                font-size: 24px;
                }
                h3 {
                line-height: 26px;
                font-size: 20px;
                }
                .t20,
                .t23 {
                mso-line-height-alt: 60px !important;
                line-height: 60px !important;
                display: block !important;
                }
                .t21 {
                padding: 60px !important;
                border-radius: 8px !important;
                overflow: hidden !important;
                }
            }
            </style>
            <style type="text/css">
            @media (min-width: 481px) {
                [class~="x_t20"] {
                mso-line-height-alt: 60px !important;
                line-height: 60px !important;
                display: block !important;
                }
                [class~="x_t23"] {
                mso-line-height-alt: 60px !important;
                line-height: 60px !important;
                display: block !important;
                }
                [class~="x_t21"] {
                padding-left: 60px !important;
                padding-top: 60px !important;
                padding-bottom: 60px !important;
                padding-right: 60px !important;
                border-top-left-radius: 8px !important;
                border-top-right-radius: 8px !important;
                border-bottom-right-radius: 8px !important;
                border-bottom-left-radius: 8px !important;
                overflow: hidden !important;
                width: 480px !important;
                }
                [class~="x_t5"] {
                width: 480px !important;
                }
                [class~="x_t9"] {
                width: 480px !important;
                }
                [class~="x_t18"] {
                width: 480px !important;
                }
            }
            </style>
            <style type="text/css" media="screen and (min-width:481px)">
            .moz-text-html img,
            .moz-text-html p {
                margin: 0;
                margin: 0;
                font-family: Lato, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial,
                sans-serif;
                line-height: 22px;
                font-weight: 400;
                font-style: normal;
                font-size: 16px;
                text-decoration: none;
                text-transform: none;
                letter-spacing: 0;
                direction: ltr;
                color: #333;
                text-align: left;
                mso-line-height-rule: exactly;
                mso-text-raise: 2px;
            }
            .moz-text-html h1 {
                margin: 0;
                margin: 0;
                font-family: Roboto, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial,
                sans-serif;
                line-height: 34px;
                font-weight: 400;
                font-style: normal;
                font-size: 28px;
                text-decoration: none;
                text-transform: none;
                letter-spacing: 0;
                direction: ltr;
                color: #333;
                text-align: left;
                mso-line-height-rule: exactly;
                mso-text-raise: 2px;
            }
            .moz-text-html h2 {
                margin: 0;
                margin: 0;
                font-family: Lato, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial,
                sans-serif;
                line-height: 30px;
                font-weight: 400;
                font-style: normal;
                font-size: 24px;
                text-decoration: none;
                text-transform: none;
                letter-spacing: 0;
                direction: ltr;
                color: #333;
                text-align: left;
                mso-line-height-rule: exactly;
                mso-text-raise: 2px;
            }
            .moz-text-html h3 {
                margin: 0;
                margin: 0;
                font-family: Lato, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial,
                sans-serif;
                line-height: 26px;
                font-weight: 400;
                font-style: normal;
                font-size: 20px;
                text-decoration: none;
                text-transform: none;
                letter-spacing: 0;
                direction: ltr;
                color: #333;
                text-align: left;
                mso-line-height-rule: exactly;
                mso-text-raise: 2px;
            }
            .moz-text-html .t20,
            .moz-text-html .t23 {
                mso-line-height-alt: 60px !important;
                line-height: 60px !important;
                display: block !important;
            }
            .moz-text-html .t21 {
                padding: 60px !important;
                border-radius: 8px !important;
                overflow: hidden !important;
                width: 480px !important;
            }
            .moz-text-html .t18,
            .moz-text-html .t5,
            .moz-text-html .t9 {
                width: 480px !important;
            }
            </style>
            <!--[if !mso]>-->
            <link
            href="https://fonts.googleapis.com/css2?family=Albert+Sans:wght@400;700;800&amp;family=Inter+Tight:wght@900&amp;display=swap"
            rel="stylesheet"
            type="text/css"
            />
            <!--<![endif]-->
            <!--[if mso]>
            <style type="text/css">
                img,
                p {
                margin: 0;
                margin: 0;
                font-family: Lato, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial,
                    sans-serif;
                line-height: 22px;
                font-weight: 400;
                font-style: normal;
                font-size: 16px;
                text-decoration: none;
                text-transform: none;
                letter-spacing: 0;
                direction: ltr;
                color: #333;
                text-align: left;
                mso-line-height-rule: exactly;
                mso-text-raise: 2px;
                }
                h1 {
                margin: 0;
                margin: 0;
                font-family: Roboto, BlinkMacSystemFont, Segoe UI, Helvetica Neue,
                    Arial, sans-serif;
                line-height: 34px;
                font-weight: 400;
                font-style: normal;
                font-size: 28px;
                text-decoration: none;
                text-transform: none;
                letter-spacing: 0;
                direction: ltr;
                color: #333;
                text-align: left;
                mso-line-height-rule: exactly;
                mso-text-raise: 2px;
                }
                h2 {
                margin: 0;
                margin: 0;
                font-family: Lato, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial,
                    sans-serif;
                line-height: 30px;
                font-weight: 400;
                font-style: normal;
                font-size: 24px;
                text-decoration: none;
                text-transform: none;
                letter-spacing: 0;
                direction: ltr;
                color: #333;
                text-align: left;
                mso-line-height-rule: exactly;
                mso-text-raise: 2px;
                }
                h3 {
                margin: 0;
                margin: 0;
                font-family: Lato, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial,
                    sans-serif;
                line-height: 26px;
                font-weight: 400;
                font-style: normal;
                font-size: 20px;
                text-decoration: none;
                text-transform: none;
                letter-spacing: 0;
                direction: ltr;
                color: #333;
                text-align: left;
                mso-line-height-rule: exactly;
                mso-text-raise: 2px;
                }
                div.t20,
                div.t23 {
                mso-line-height-alt: 60px !important;
                line-height: 60px !important;
                display: block !important;
                }
                td.t21 {
                padding: 60px !important;
                border-radius: 8px !important;
                overflow: hidden !important;
                }
            </style>
            <![endif]-->
            <!--[if mso]>
            <xml>
                <o:OfficeDocumentSettings>
                <o:AllowPNG />
                <o:PixelsPerInch>96</o:PixelsPerInch>
                </o:OfficeDocumentSettings>
            </xml>
            <![endif]-->
        </head>
        <body
            id="body"
            class="t26"
            style="
            min-width: 100%;
            margin: 0px;
            padding: 0px;
            background-color: #f4f4f4;
            "
        >
            <div class="t25" style="background-color: #f4f4f4">
            <table
                role="presentation"
                width="100%"
                cellpadding="0"
                cellspacing="0"
                border="0"
                align="center"
            >
                <tr>
                <td
                    class="t24"
                    style="
                    font-size: 0;
                    line-height: 0;
                    mso-line-height-rule: exactly;
                    background-color: #f4f4f4;
                    "
                    valign="top"
                    align="center"
                >
                    <!--[if mso]>
                    <v:background
                        xmlns:v="urn:schemas-microsoft-com:vml"
                        fill="true"
                        stroke="false"
                    >
                        <v:fill color="#F4F4F4" />
                    </v:background>
                    <![endif]-->
                    <table
                    role="presentation"
                    width="100%"
                    cellpadding="0"
                    cellspacing="0"
                    border="0"
                    align="center"
                    id="innerTable"
                    >
                    <tr>
                        <td>
                        <div
                            class="t20"
                            style="
                            mso-line-height-rule: exactly;
                            font-size: 1px;
                            display: none;
                            "
                        >
                            &nbsp;&nbsp;
                        </div>
                        </td>
                    </tr>
                    <tr>
                        <td align="center">
                        <table
                            class="t22"
                            role="presentation"
                            cellpadding="0"
                            cellspacing="0"
                            style="margin-left: auto; margin-right: auto"
                        >
                            <tr>
                            <!--[if mso]>
        <td width="600" class="t21" style="background-color:#FFFFFF;padding:40px 40px 40px 40px;">
        <![endif]-->
                            <!--[if !mso]>-->
                            <td
                                class="t21"
                                style="
                                background-color: #ffffff;
                                width: 400px;
                                padding: 40px 40px 40px 40px;
                                "
                            >
                                <!--<![endif]-->
                                <table
                                role="presentation"
                                width="100%"
                                cellpadding="0"
                                cellspacing="0"
                                style="width: 100% !important"
                                >
                                <tr>
                                    <td align="left">
                                    <table
                                        class="t2"
                                        role="presentation"
                                        cellpadding="0"
                                        cellspacing="0"
                                        style="margin-right: auto"
                                    >
                                        <tr>
                                        <!--[if mso]>
        <td width="70" class="t1" style="padding:0 15px 0 0;">
        <![endif]-->
                                        <!--[if !mso]>-->
                                        <td
                                            class="t1"
                                            style="width: 55px; padding: 0 15px 0 0"
                                        >
                                            <!--<![endif]-->
                                            <div style="font-size: 0px">
                                            <img
                                                class="t0"
                                                style="
                                                display: block;
                                                border: 0;
                                                height: auto;
                                                width: 100%;
                                                margin: 0;
                                                max-width: 100%;
                                                "
                                                width="55"
                                                height="35.78125"
                                                alt=""
                                                src="https://873bf0ff-510b-4e56-add9-23f07643d9f2.b-cdn.net/e/7c1b81b5-3da9-4347-857b-565f01b7aac4/0536ec87-177c-481c-9603-eaad2866556b.png"
                                            />
                                            </div>
                                        </td>
                                        </tr>
                                    </table>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                    <div
                                        class="t3"
                                        style="
                                        mso-line-height-rule: exactly;
                                        mso-line-height-alt: 42px;
                                        line-height: 42px;
                                        font-size: 1px;
                                        display: block;
                                        "
                                    >
                                        &nbsp;&nbsp;
                                    </div>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="center">
                                    <table
                                        class="t6"
                                        role="presentation"
                                        cellpadding="0"
                                        cellspacing="0"
                                        style="margin-left: auto; margin-right: auto"
                                    >
                                        <tr>
                                        <!--[if mso]>

                                        <!--[if !mso]>-->
                                        <td class="t5" style="width: 400px">
                                            <!--<![endif]-->
                                            <h1
                                            class="t4"
                                            style="
                                                margin: 0;
                                                margin: 0;
                                                font-family: Albert Sans,
                                                BlinkMacSystemFont, Segoe UI,
                                                Helvetica Neue, Arial, sans-serif;
                                                line-height: 41px;
                                                font-weight: 800;
                                                font-style: normal;
                                                font-size: 39px;
                                                text-decoration: none;
                                                text-transform: none;
                                                letter-spacing: -1.56px;
                                                direction: ltr;
                                                color: #333333;
                                                text-align: left;
                                                mso-line-height-rule: exactly;
                                                mso-text-raise: 1px;
                                            "
                                            >
                                            Confirm your account
                                            </h1>
                                        </td>
                                        </tr>
                                    </table>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                    <div
                                        class="t7"
                                        style="
                                        mso-line-height-rule: exactly;
                                        mso-line-height-alt: 16px;
                                        line-height: 16px;
                                        font-size: 1px;
                                        display: block;
                                        "
                                    >
                                        &nbsp;&nbsp;
                                    </div>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="center">
                                    <table
                                        class="t10"
                                        role="presentation"
                                        cellpadding="0"
                                        cellspacing="0"
                                        style="margin-left: auto; margin-right: auto"
                                    >
                                        <tr>
                                        <!--[if mso]>

                                        <!--[if !mso]>-->
                                        <td class="t9" style="width: 400px">
                                            <!--<![endif]-->
                                            <p
                                            class="t8"
                                            style="
                                                margin: 0;
                                                margin: 0;
                                                font-family: Albert Sans,
                                                BlinkMacSystemFont, Segoe UI,
                                                Helvetica Neue, Arial, sans-serif;
                                                line-height: 21px;
                                                font-weight: 400;
                                                font-style: normal;
                                                font-size: 16px;
                                                text-decoration: none;
                                                text-transform: none;
                                                letter-spacing: -0.64px;
                                                direction: ltr;
                                                color: #333333;
                                                text-align: left;
                                                mso-line-height-rule: exactly;
                                                mso-text-raise: 2px;
                                            "
                                            >
                                            Please copy your six(6) digit code below to confirm
                                            your email address and finish setting up
                                            your account. This code is valid for 24
                                            hours.
                                            </p>
                                        </td>
                                        </tr>
                                    </table>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                    <div
                                        class="t12"
                                        style="
                                        mso-line-height-rule: exactly;
                                        mso-line-height-alt: 35px;
                                        line-height: 35px;
                                        font-size: 1px;
                                        display: block;
                                        "
                                    >
                                        &nbsp;&nbsp;
                                    </div>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="left">
                                    <table
                                        class="t14"
                                        role="presentation"
                                        cellpadding="0"
                                        cellspacing="0"
                                        style="margin-right: auto"
                                    >
                                        <tr>
                                        <!--[if !mso]>-->
                                        <td
                                            class="t13"
                                            style="
                                            overflow: hidden;
                                            text-align: center;
                                            line-height: 34px;
                                            mso-line-height-rule: exactly;
                                            mso-text-raise: 6px;
                                            "
                                        >
                                            <!--<![endif]-->
                                            """
            f"""
                                            <h2
                                            class="t11"
                                            style="
                                                display: block;
                                                margin: 0;
                                                margin: 0;
                                                font-family: Inter Tight,
                                                BlinkMacSystemFont, Segoe UI,
                                                Helvetica Neue, Arial, sans-serif;
                                                line-height: 34px;
                                                font-weight: 900;
                                                font-style: normal;
                                                text-decoration: none;
                                                text-transform: uppercase;
                                                direction: ltr;
                                                color: #000000;
                                                text-align: center;
                                                mso-line-height-rule: exactly;
                                                mso-text-raise: 6px;
                                            "
                                            >{otp_code}</h2
                                            >
                                        </td>
                                        </tr>
                                    </table>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                    <div
                                        class="t17"
                                        style="
                                        mso-line-height-rule: exactly;
                                        mso-line-height-alt: 35px;
                                        line-height: 35px;
                                        font-size: 1px;
                                        display: block;
                                        "
                                    >
                                        &nbsp;&nbsp;
                                    </div>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="center">
                                    <table
                                        class="t19"
                                        role="presentation"
                                        cellpadding="0"
                                        cellspacing="0"
                                        style="margin-left: auto; margin-right: auto"
                                    >
                                        <tr>
                                        <!--[if mso]>

                                        <!--[if !mso]>-->
                                        <td class="t18" style="width: 400px">
                                            <!--<![endif]-->
                                            <p
                                            class="t16"
                                            style="
                                                margin: 0;
                                                margin: 0;
                                                font-family: Albert Sans,
                                                BlinkMacSystemFont, Segoe UI,
                                                Helvetica Neue, Arial, sans-serif;
                                                line-height: 21px;
                                                font-weight: 400;
                                                font-style: normal;
                                                font-size: 16px;
                                                text-decoration: none;
                                                text-transform: none;
                                                letter-spacing: -0.64px;
                                                direction: ltr;
                                                color: #333333;
                                                text-align: left;
                                                mso-line-height-rule: exactly;
                                                mso-text-raise: 2px;
                                            "
                                            >
                                            Didn&#39;t register on OneDex-Investment?
                                            <a
                                                class="t15"
                                                href="#"
                                                style="
                                                margin: 0;
                                                margin: 0;
                                                font-weight: 700;
                                                font-style: normal;
                                                text-decoration: none;
                                                direction: ltr;
                                                color: #2f353d;
                                                mso-line-height-rule: exactly;
                                                "
                                                target="_blank"
                                                >Please, do not confirm this email.</a
                                            >
                                            </p>
                                        </td>
                                        </tr>
                                    </table>
                                    </td>
                                </tr>
                                </table>
                            </td>
                            </tr>
                        </table>
                        </td>
                    </tr>
                    <tr>
                        <td>
                        <div
                            class="t23"
                            style="
                            mso-line-height-rule: exactly;
                            font-size: 1px;
                            display: none;
                            "
                        >
                            &nbsp;&nbsp;
                        </div>
                        </td>
                    </tr>
                    </table>
                </td>
                </tr>
            </table>
            </div>
        </body>
        </html>
    """
        )

        mail = EmailMultiAlternatives()
        mail.to = [email]
        mail.from_email = "ONEDEX INVESTMENT<service@onedex-lnvestment.com>"
        mail.subject = label
        mail.body = f"kindly copy your one time verification cold below \n {otp_code}"
        mail.attach_alternative(msg, "text/html")
        mail.send(fail_silently=False)
        print("mail success")
        return "200"
    except User.DoesNotExist:
        return "404"
    except Exception as e:
        print("mail error", str(e))
        return "500"


@transaction.atomic
def Register(**data):
    try:
        email = data["email"]
        user = User.objects.get(email=email)
        return {"status": "failed", "code": "Email Already Exist"}

    except User.DoesNotExist:
        user = User(**data)
        user.id = uuid4()
        user.set_password(data["password"])
        user.is_verified = True
        user.save()
        Account.objects.create(user=user)
        try:
            send_mail(
                user.email,
                "welcome Onboard",
                "We’re excited to have you join us. Your registration was successful, and you’re now part of a growing community of investors building a secure financial future.",
                user.fullname,
            )
            send_mail(
                "service@onedex-lnvestment.com",
                "New Member Onboard",
                f"{user.fullname} just joined the team",
                "Admin",
            )
        except Exception as e:
            pass
        return {"status": "success", "userId": user.id}

    except Exception as e:
        print(f"Error Msg {e}")
        return {"status": "failed", "code": "Unknown Server Error"}


def Login(**data):
    email = data["email"]
    try:
        user = authenticate(email=email, password=data["password"])

        if user is None:
            return {"status": "failed", "code": "No user found or Incorrect details"}

        if not user.is_verified:
            send_verify_otp = send_otp_code(
                id=user.id, label="ONEDEX Account Verification"
            )
            return {"status": "unverified", "userId": user.id}

        if user.isSuspended:
            return {"status": "suspended", "userId": user.id}

        return {"status": "success", "userId": user.id}
    except Exception as e:

        print(f"Error Msg {e}")
        return {"status": "failed", "code": "Unknown Server Error"}


def verifyOTPCode(id, otp):
    try:
        user = User.objects.get(id=id)
        otp_code = user.OTP
        otp_date = user.OTP_VALID_TILL
        today = make_aware(datetime.datetime.now())
        if otp_code != otp:
            return {"status": "failed", "code": "Invalid OTP code"}
        if today >= otp_date:
            return {
                "status": "failed",
                "code": "Elapsed time please request a new code",
            }
        user.OTP = None
        user.OTP_VALID_TILL = None
        user.is_verified = True
        user.save()
        return {"status": "success", "code": "account verified"}
    except User.DoesNotExist:
        return {"status": "failed", "code": "No such user found"}
    except Exception as e:
        return {"status": "failed", "code": str(e)}


def updateFullname(id, name):
    try:
        user = User.objects.get(id=id)
        user.fullname = name
        user.save()
        return {"status": "success", "name": user.fullname}
    except User.DoesNotExist:
        return {"status": "failed", "code": "user not found"}
    except Exception as e:
        return {"status": "failed", "code": str(e)}
