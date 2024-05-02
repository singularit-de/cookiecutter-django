from collections import OrderedDict

from django.db import models


class CompareModelObjectsMixin:
    def assertModelObjectsListEqual(self, expected: list[dict | object], result: list[dict | object]) -> None:
        """
        Compares a list of objects with another list of objects. If the objects are not of type `dict` or `OrderedDict`
        type, `dict(instance)` is used. If it is a model instance, `.__dict__` is used. If a key is not present in an
        object of the expected list, it is ignored. For example this is good for excluding created_at and updated_at
        fields in comparison.
        :param expected: The expected list of objects. Keys that are not present in the objects of this list are
            ignored.
        :param result: The actual result list of objects.

        **Examples**:
            >>> self.assertModelObjectsListEqual([{"a":1}, {"a":2}], [{"a":1}, {"a":3}]) # Fails
            Traceback (most recent call last):
            ...
            AssertionError:
            >>> self.assertModelObjectsListEqual([{"a":1}, {"a":2}], [{"a":1}, {"a":2}])
            None
            >>> self.assertModelObjectsListEqual([{"a":1}, {"a":2}], [{"a":1}, {"b":1}])
            None
        """
        self.assertEqual(len(expected), len(result))
        for n1, n2 in zip(expected, result):
            self.assertModelObjectEquals(n1, n2)

    def assertModelObjectEquals(
        self,
        expected: dict | object,
        result: dict | object,
    ) -> None:
        """
        Compares an object with another object. If the objects are not of type `dict` or `OrderedDict`
        type, `dict(instance)` is used. If it is a model instance, `.__dict__` is used. If a key is not present in the
        expected object, it is ignored. For example this is good for excluding created_at and updated_at fields in
        comparison.
        :param expected: The expected object. Keys that are not present in this object are ignored.
        :param result: The actual result object.
        **Examples**:
            >>> self.assertModelObjectEquals({"a":1, "b":2}, {"a":1, "b":3}) # Fails
            Traceback (most recent call last):
            ...
            AssertionError:
            >>> self.assertModelObjectEquals({"a":1}, {"a":1, "b":2}) # Succeeds because b is ignored
            None
            >>> self.assertModelObjectEquals({"a":1, "b":2}, {"a":1, "b":2})
            None
            >>> self.assertModelObjectEquals({"a":1, "b":2}, {"a":1, "c":1})
            None
        """

        d1, d2 = self.__compare(expected, result)
        self.assertEqual(len(d1), 0, f"\nExpected: {d1}\nActual result: {d2}")
        self.assertEqual(len(d2), 0, f"\nExpected: {d1}\nActual result: {d2}")

    def __to_dict(self, obj: dict | list | object | None) -> dict:
        try:
            return obj if type(obj) in (dict, OrderedDict) else dict(obj)
        except TypeError:  # Model instances
            return obj.__dict__
        except ValueError:
            raise AssertionError(f"Could not convert '{obj}' to dict.")

    def __is_assert_equal(self, obj_1, obj_2):
        return (
            (
                type(obj_1) not in [dict, OrderedDict, list]
                and type(obj_2) not in [dict, OrderedDict, list]
                and not issubclass(type(obj_1), models.Model)
                and not issubclass(type(obj_2), models.Model)
            )
            or obj_1 is None
            or obj_2 is None
        )

    def __is_list_equal(self, obj_1, obj_2):
        return type(obj_1) is list and type(obj_2) is list

    def __compare(self, obj_1: dict | list | object | None, obj_2: dict | list | object | None) -> tuple[
        dict, dict]:

        old = {}
        new = {}

        if self.__is_assert_equal(obj_1, obj_2):
            self.assertEqual(obj_1, obj_2)
            return old, new

        if self.__is_list_equal(obj_1, obj_2):
            self.assertModelObjectsListEqual(obj_1, obj_2)

        d1 = self.__to_dict(obj_1)
        d2 = self.__to_dict(obj_2)

        for k, v in d1.items():
            if type(v) is dict:
                try:
                    self.assertModelObjectEquals(v, d2[k])
                except AssertionError as e:
                    raise AssertionError(f"Dictionary comparison failed for key {k}:\n\t{e}")
                except KeyError:
                    old.update({k: v})
            elif type(v) is list:
                try:
                    self.assertModelObjectsListEqual(v, d2[k])
                except AssertionError as e:
                    raise AssertionError(f"List comparison failed for key {k}:\n\t{e}")
                except KeyError:
                    old.update({k: v})
            else:
                try:
                    if v != d2[k]:
                        old.update({k: v})
                        new.update({k: d2[k]})
                except KeyError:
                    old.update({k: v})

        return old, new
