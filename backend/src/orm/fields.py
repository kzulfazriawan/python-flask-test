"""
This file contains fields class for column in ORM
"""
from abc import ABCMeta

from sqlalchemy import Integer, String, Column, Text, DateTime, func, ForeignKey


class BaseFields(metaclass=ABCMeta):
    __datatype__ = String(191)
    __options__ = {
        "nullable": False
    }

    __field = None

    def set_field(self, **kwargs):
        """
        Set field for common column

        :param kwargs:
        """
        self.__field = Column(self.__datatype__, **kwargs) if kwargs else Column(self.__datatype__, **self.__options__)

    def set_field_with_name(self, name: str, **kwargs):
        """
        Set field with name for common version

        :param name:
        :param kwargs:
        """
        self.__field = Column(
            name, self.__datatype__, **kwargs
        ) if kwargs else Column(
            name, self.__datatype__, **self.__options__
        )

    def set_field_foreign_key(self, key, **kwargs):
        """
        Set field for foreign key relationship

        :param key:
        :param kwargs:
        """
        self.__field = Column(
            self.__datatype__, ForeignKey(key, **kwargs)
        ) if kwargs else Column(
            self.__datatype__, ForeignKey(key, **self.__options__)
        )

    def set_field_foreign_key_with_name(self, name: str, key, **kwargs):
        """
        Set field for foreign key relationship version

        :param name:
        :param key:
        :param kwargs:
        """
        self.__field = Column(
            name, self.__datatype__, ForeignKey(key, **kwargs)
        ) if kwargs else Column(
            name, self.__datatype__, ForeignKey(key, **self.__options__)
        )

    @property
    def field(self):
        """
        Declare the field

        :return: attribute field
        """
        return self.__field


class Character(BaseFields):
    def __init__(self, name: str = None, **kwargs):
        """
        Class field for common character datatype

        :param name:
        :param kwargs:
        """
        if name:
            self.set_field_with_name(name, **kwargs)
        else:
            self.set_field(**kwargs)


class RichText(BaseFields):
    __datatype__ = Text

    def __init__(self, name: str = None, **kwargs):
        """
        Class field for rich text datatype

        :param name:
        :param kwargs:
        """
        if name:
            self.set_field_with_name(name, **kwargs)
        else:
            self.set_field(**kwargs)


class Numeric(BaseFields):
    __datatype__ = Integer

    def __init__(self, name: str = None, **kwargs):
        """
        Class field for integer numeric datatype

        :param name:
        :param kwargs:
        """
        if name:
            self.set_field_with_name(name, **kwargs)
        else:
            self.set_field(**kwargs)


class AutoIncrementId(BaseFields):
    __datatype__ = Integer
    __options__ = {
        "primary_key": True,
        "nullable": False,
        "autoincrement": True
    }

    def __init__(self, name: str = None):
        """
        Class field for auto-increment primary key id

        :param name:
        """
        if name:
            self.set_field_with_name(name)
        else:
            self.set_field()


class Timestamp(BaseFields):
    __datatype__ = DateTime

    def __init__(self, name: str = None, **kwargs):
        """
        Class field for timestamp datatype

        :param name:
        :param kwargs:
        """
        if name:
            self.set_field_with_name(name, **kwargs)
        else:
            self.set_field(**kwargs)


class CreatedAt(Timestamp):
    __options__ = {
        "default": func.now(),
        "nullable": False
    }

    def __init__(self, name: str = None, **kwargs):
        """
        Helper class field for "created_at"

        :param name:
        :param kwargs:
        """
        super(CreatedAt, self).__init__(name, **kwargs)


class UpdatedAt(Timestamp):
    __options__ = {
        "default": func.now(),
        "onupdate": func.now(),
        "nullable": False
    }

    def __init__(self, name: str = None, **kwargs):
        """
        Helper class field for "updated_at"

        :param name:
        :param kwargs:
        """
        super(UpdatedAt, self).__init__(name, **kwargs)


class RelationshipKey(BaseFields):
    __datatype__ = Integer,
    __options__ = {
        "ondelete": "CASCADE",
    }

    def __init__(self, key, name: str = None, **kwargs):
        """
        Class field for foreign key relationship

        :param name:
        :param kwargs:
        """
        if name:
            self.set_field_foreign_key_with_name(name, key, **kwargs)
        else:
            self.set_field_foreign_key(key, **kwargs)
