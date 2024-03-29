from django.db import models
from django.utils import timezone

class Doctors(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=200)
    last_name = models.CharField(verbose_name='Фамилие', max_length=200)
    position = models.CharField(verbose_name='Должность', max_length=200)
    info = models.CharField(verbose_name='Информация о пользователе', max_length=1000)

    def __str__(self):
        return '' + self.name + ' ' + self.last_name

    class Meta:
        verbose_name_plural = "Врачи"
        verbose_name = "Врач"

class TimesOfWork(models.Model):
    start_time = models.TimeField(verbose_name='время начала приема')
    end_time = models.TimeField(verbose_name='время конца приема')

    def __str__(self):
        return '' + self.start_time.strftime("%H:%M") + ' - ' + self.end_time.strftime("%H:%M")

    class Meta:
        verbose_name_plural = "Время работы"
        verbose_name = "Время работы"

class Reception(models.Model):
    date = models.DateField(verbose_name='дата приема')
    time = models.ForeignKey(TimesOfWork, verbose_name='время приема', on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    patient_info = models.CharField(verbose_name='Информация о поциенте', max_length=1000)
    doctor = models.ForeignKey( Doctors, verbose_name='Доктор', on_delete=models.CASCADE)

    def __str__(self):
        return 'Прием № %s' % self.id

    class Meta:
        verbose_name_plural = "Приемы"
        verbose_name = "Прием"

