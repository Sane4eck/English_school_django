from django.db.models.signals import post_save
from django.dispatch import receiver

from english_school.settings import EMAIL_HOST_USER
from teacher.models import LanguageInform
from utils.email_sender.teacher_approval import TeacherRequestApprovalSender


@receiver(post_save, sender=LanguageInform)
def send_approval_teacher(sender, instance, created, **kwargs):
    if created:
        TeacherRequestApprovalSender(to_email=EMAIL_HOST_USER).send_email(
            language_inform=instance
        )
