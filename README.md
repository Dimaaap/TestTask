# My Test Task 

## Installation

You need to create a python virtual env 
```bash
python -m venv /path/to/new/virtual/environment
cd /path/to/new/virtual/environment/Scripts
./activate
cd ../../
```

Next you need to install dependencies

```bash
pip install -r requirements.txt
```
In project you have **projects** directive with code for all test tasks
and tests for it

To run tests use 
```bash
 pytest projects
```
## Theory
#### 3.1 Using descriptors in practice
# Використання дескрипторів в Python

Дескриптори в Python — це спеціальні методи для управління доступом до атрибутів об'єктів. Вони дозволяють створювати складні механізми доступу та взаємодії з атрибутами класів. Ось кілька прикладів реальних проектів і бібліотек, де дескриптори активно використовуються.

## 1. **Django ORM (Object-Relational Mapping)**

Django використовує дескриптори для реалізації моделей, що відображають таблиці в базі даних. Поля моделей, такі як `CharField`, `IntegerField`, `DateField` тощо, використовують дескриптори для контролю доступу до значень цих полів у базі даних.

### Приклад:
```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
```
## 2. **  SQLAlchemy (ORM для бази даних)
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
```
