from django.contrib.auth.models import BaseUserManager
##########################################################################################################
# User Mananager
##########################################################################################################
class CareersBucketBaseUserManager(BaseUserManager):

    def create_user(self, email, password):
        if not email:
            raise ValueError('Users must have an Email Address')

        user = self.model(
            email=self.normalize_email(email),
            is_active=False,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.model(email=email)
        user.set_password(password)
        user.is_superuser = True
        if user.is_superuser:
            user.first_name = "Developer"
            user.user_type = "Dev"
        
        user.is_active = True
        user.save(using=self._db)
        return user
    
    
    # class HospitalBaseUserManager(BaseUserManager):
    #     def create_user(self, email, mobile_number, password=None, **extra_fields):
    #         if not email:
    #             raise ValueError('Users must have an Email Address')

    #         user = self.model(
    #             email=self.normalize_email(email),
    #             mobile_number=mobile_number,
    #             is_active=False,
    #             **extra_fields,
    #         )
    #         user.set_password(password)
    #         user.save(using=self._db)
    #         return user

    #     def create_superuser(self, email, mobile_number, password=None, **extra_fields):
    #         extra_fields.setdefault('is_staff', True)
    #         extra_fields.setdefault('is_superuser', True)

    #         user = self.create_user(email, mobile_number, password, **extra_fields)
    #         user.is_superuser = True
    #         if user.is_superuser:
    #             user.first_name = "Developer"
    #             user.user_type = "Dev"
            
    #         user.is_active = True
    #         user.save(using=self._db)
    #         return user
