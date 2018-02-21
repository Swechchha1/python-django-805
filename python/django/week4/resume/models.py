from django.db import models
# Create your models here.

class Resume(models.Model):
    first_name = models.CharField(max_length=64, null=False, blank=False)
    last_name = models.CharField(max_length=64, null=False, blank=False)

    def get_full_name(self):
        """
        returns full name in the form - firstname lastname
        """
        return "{} {}".format(self.first_name,self.last_name)

    def get_last_name_first_name(self):
        """
        returns full name in the form - lastname, firstname
        """
        return "{}, {}".format(self.last_name,self.first_name)

    def get_experience(self):
        """
        returns all the fields in the Experience model
        """
        return self.experience_set.all()

    def get_education(self):
        """
        returns all the fields in the Education model
        """
        return self.education_set.all()

class Experience(models.Model):
    """
    resume is the Foreign key
    """
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=64, null=False, blank=False)
    location = models.CharField(max_length=64, null=False, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=255, null=False, blank=True)

    def __str__(self):
        return self.title

class Education(models.Model):
    """
    resume is the Foreign key
    """
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, default=1)
    institution_name = models.CharField(max_length=64, null=False, blank=False)
    location = models.CharField(max_length=64, null=False, blank=False)
    degree = models.CharField(max_length=255, null=False, blank=False)
    major = models.CharField(max_length=255, null=False, blank=False)
    gpa = models.FloatField(null = False, blank = False)

    def __str__(self):
        return self.institution_name
