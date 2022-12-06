"""
This file is contains the queries pre-built and base model
"""
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base

from src.orm import session

Model = declarative_base()


class Queries:
    _s = session()
    _q = None

    def commit(self, query=None):
        """
        This method will commit the session query and return it if query run outside the Q property

        :param query:
        :return: queryset
        """
        try:
            self._s.commit()
        except SQLAlchemyError as err:
            self._s.rollback()
            raise err
        else:
            if query is not None:
                self._s.refresh(query)
                return query

    def select(self, *args):
        """
        Basic select method to get the documents from table

        :param args:
        :return: self class
        """
        self._q = self._s.query(*[getattr(self.__class__, i) for i in args]) if bool(args) else self._s.query(self.__class__)
        return self

    def filter(self, **kwargs):
        """
        Basic method to filter the specified documents from table

        :param kwargs:
        :return: self class
        """
        if self._q:
            for k, v in kwargs.items():
                self._q = self._q.filter(getattr(self.__class__, k) == v)
            return self

    def all(self):
        """
        Show all from the selected documents

        :return: queryset all
        """
        if self._q:
            self.commit()
            return self._q.all()

    def first(self):
        """
        Show only first from the selected document

        :return: queryset first
        """
        if self._q:
            self.commit()
            return self._q.first()

    def create(self, **kwargs):
        """
        Method to create a object row in table query

        :param kwargs:
        :return: queryset object
        """
        if kwargs is not None:
            _q = self.__class__(**kwargs)
            self._s.add(_q)
            self.commit(_q)
            return _q
        raise SQLAlchemyError("Keyword arguments are not supplied")

    def edit(self, update):
        """
        Method to directly edit the selected document

        :param update:
        :return: queryset first
        """
        if isinstance(update, dict) and self._q:
            self._q.update(update, synchronize_session="fetch")
            self.commit()
            return self._q.first()

    def delete(self):
        if self._q:
            self._q.delete()
            self.commit()
            return True


def to_dict(query_result):
    """
    Utility method to convert the query result to dictionary

    :param query_result:
    :return: dictionary
    """
    try:
        data = dict()

        for k, v in query_result.__dict__.items():
            if "_sa_instance_state" != k:
                data[k] = v

        return data
    except AttributeError as err:
        raise err


def to_list(query_result):
    data = list()

    for item in query_result:
        data.append(to_dict(item))

    return data
