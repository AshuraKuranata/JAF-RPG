from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

class TimeStampMixin(models.Model): # Unique Time Stamp that can be re-used
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UserManager(BaseUserManager): # Custom User Manager to help create custom users instead of Django default
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(username=username, email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin, TimeStampMixin): # Custom User Model
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True, null=False, blank=False)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    @property
    def id(self):
        return self.user_id

    def __str__(self):
        return self.username

class RoleClass(models.Model):
    role_class_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_magical = models.BooleanField(default=False)
    is_physical = models.BooleanField(default=False)
    level_requirement = models.IntegerField(default=1)

class Skill(models.Model):
    skill_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    role_class = models.ForeignKey(RoleClass, on_delete=models.CASCADE)
    cooldown = models.IntegerField(default=0)
    stamina_cost = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Magic(models.Model):
    magic_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    role_class = models.CharField(max_length=100)
    mp_cost = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Item(models.Model):
    item_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField(default=1)
    is_equipped = models.BooleanField(default=False)
    is_equippable = models.BooleanField(default=False)
    is_consumable = models.BooleanField(default=False)
    is_usable = models.BooleanField(default=False)
    is_sellable = models.BooleanField(default=False)
    is_buyable = models.BooleanField(default=False)
    is_tradeable = models.BooleanField(default=False)
    is_droppable = models.BooleanField(default=False)
    is_stackable = models.BooleanField(default=False)

class Shop(models.Model):
    shop_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    items = models.ManyToManyField(Item)

class Enemy(models.Model):
    enemy_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=1)
    max_hp = models.IntegerField(default=10)
    current_hp = models.IntegerField(default=10)
    max_mp = models.IntegerField(default=0)
    current_mp = models.IntegerField(default=0)
    role_class = models.CharField(max_length=10)
    strength = models.IntegerField(default=10)
    vitality = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)
    description = models.TextField()

class Location(models.Model):
    location_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    condition = models.CharField(max_length=100)
    enemies = models.ManyToManyField(Enemy)
    items = models.ManyToManyField(Item)

class Character(models.Model):
    character_id = models.BigAutoField(primary_key=True)
    character_name = models.CharField(max_length=100)
    level = models.IntegerField(default=1)
    max_hp = models.IntegerField(default=10)
    current_hp = models.IntegerField(default=10)
    max_mp = models.IntegerField(default=0)
    current_mp = models.IntegerField(default=0)
    max_stamina = models.IntegerField(default=10)
    current_stamina = models.IntegerField(default=10)
    role_class = models.ForeignKey(RoleClass, on_delete=models.CASCADE)
    strength = models.IntegerField(default=10)
    vitality = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Inventory(models.Model):
    inventory_id = models.BigAutoField(primary_key=True)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)