from django.core.management import BaseCommand
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.core.management import CommandError
from django.core.exceptions import ValidationError
from django.conf import settings
from typing import List


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("receiver", nargs="+", type=str, help="이메일 수신자 주소")

    def handle(self, *args, **options):
        subject = "django를 활용한 이메일 발송"
        content = "메시지 내용"
        sender_email = settings.DEFAULT_FROM_EMAIL
        receiver_email_list: List[str] = options["receiver"]

        try:
            for email in receiver_email_list:
                validate_email(email)
        except ValidationError as e:
            raise CommandError(e.message)

        send_mail(
            subject, content, sender_email, receiver_email_list, fail_silently=False,
        )
