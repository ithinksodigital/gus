
from django.db import models


class Divorces2018(models.Model):
    # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    divorces_2018 = models.FloatField(db_column='Divorces_2018', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'divorces_2018'


class MortalityBeforeSixty2018(models.Model):
    # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    mortality_before_sixty_2018 = models.FloatField(db_column='Mortality_before_sixty_2018', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mortality_before_sixty_2018'


class Salaries2018(models.Model):
    # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    salary_2018 = models.FloatField(db_column='Salary_2018', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'salaries_2018'


class UnemploymentRate2018(models.Model):
    # id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    unemployment_rate_2018 = models.FloatField(db_column='Unemployment_rate_2018', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'unemployment_rate_2018'
