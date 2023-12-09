#!/usr/bin/python3
"""
Unittest module for the BaseModel class
"""
import unittest
import datetime
from models.base_model import BaseModel


class TestInstantiation(unittest.TestCase):
    """
    Instantiation tests for BaseModel class.
    -> 5 tests
    """

    def setUp(self):
        """
        This method will be called before each test method
        """
        self.a = BaseModel()

    def test_init(self):
        """Tests instance creation"""
        self.assertIsNotNone(self.a)

    def test_instance_attributes(self):
        """Test instance attributes"""
        self.assertEqual(type(self.a.id), str)
        self.assertEqual(type(self.a.created_at), datetime.datetime)
        self.assertEqual(type(self.a.updated_at), datetime.datetime)

    def test_more_variables(self):
        """Tests new instance variables"""
        self.a.my_number = 15
        self.a.name = "Another day"
        self.assertEqual(self.a.my_number, 15)
        self.assertEqual(self.a.name, "Another day")

    def test_id_uniqueness(self):
        """Tests the uniqueness of IDs"""
        self.b = BaseModel()
        self.assertNotEqual(self.a.id, self.b.id)

    def test_timestamp_order(self):
        """Tests the created_at and updated_at Timing"""
        self.a.save()
        self.assertLess(self.a.created_at, self.a.updated_at)
        self.b = BaseModel()
        self.assertLess(self.a.created_at, self.b.created_at)


class TestInitArguments(unittest.TestCase):
    """
    Argument instatiation tests
    -> 6 tests
    """
    def setUp(self):
        """
        This method will be called before each test method
        """
        self.my_model = BaseModel()
        self.my_model.name = "Hard-Work"
        self.my_model.number = 77
        self.my_json = self.my_model.to_dict()
        self.new_model= BaseModel(**self.my_json)

    def test_new_instance(self):
        """Tests new instance instantiation"""
        self.assertEqual(self.my_model.id, self.new_model.id)
        self.assertEqual(self.my_model.created_at, self.new_model.created_at)
        self.assertEqual(self.my_model.updated_at, self.new_model.updated_at)
    
    def test_creation(self):
        """Tests the correct creation of a new instance"""
        self.assertIsNot(self.my_model, self.new_model)

    def test_init_with_args(self):
        """Test instantiation with positional arguments"""
        another_model = BaseModel("123", "2022-01-01T12:00:00", "2022-01-01T13:00:00")
        self.assertNotEqual(another_model.id, "123")
        self.assertNotEqual(another_model.created_at, datetime.datetime(2022, 1, 1, 12, 0, 0))
        self.assertNotEqual(another_model.updated_at, datetime.datetime(2022, 1, 1, 13, 0, 0))

    def test_init_with_kwargs(self):
        """Test instantiation with keyword arguments"""
        additional_model = BaseModel(id="456", created_at="2022-02-01T10:00:00", updated_at="2022-02-01T11:00:00")
        self.assertEqual(additional_model.id, "456")
        self.assertEqual(additional_model.created_at, datetime.datetime(2022, 2, 1, 10, 0, 0))
        self.assertEqual(additional_model.updated_at, datetime.datetime(2022, 2, 1, 11, 0, 0))

    def test_init_with_mixed_args_kwargs(self):
        """Test instantiation with mixed positional and keyword arguments"""
        mixed_model = BaseModel("789", created_at="2022-03-01T08:00:00", updated_at="2022-03-01T09:00:00")
        self.assertFalse(hasattr(mixed_model, "id"))
        self.assertEqual(mixed_model.created_at, datetime.datetime(2022, 3, 1, 8, 0, 0))
        self.assertEqual(mixed_model.updated_at, datetime.datetime(2022, 3, 1, 9, 0, 0))

    def test_init_with_invalid_datetime(self):
        """Test instantiation with invalid datetime format"""
        with self.assertRaises(ValueError):
            invalid_model = BaseModel(created_at="2022-04-01Tinvalid", updated_at="2022-04-01T12:00:00")


class TestMethods(unittest.TestCase):
    """
    Methods test for the BaseModel class.
    Methods:
        - save()
        - to_dict()
        - __str__()
    -> 3 tests
    """
    def setUp(self):
        """
        This method will be called before each test method
        """
        self.a = BaseModel()

    def test_save_method(self):
        """Test the save() method"""
        initial_update_at = self.a.updated_at
        self.a.save()
        self.assertNotEqual(self.a.updated_at, initial_update_at)

    def test_to_dict_method(self):
        """Test the to_dict() method"""
        obj_dict = self.a.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['__class__'], self.a.__class__.__name__)
        self.assertEqual(obj_dict['created_at'], self.a.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.a.updated_at.isoformat())

    def test_str_method(self):
        """Test the __str__() method"""
        str_representation = str(self.a.to_dict())
        self.assertIn(self.a.id, str_representation)
        self.assertIn(self.a.__class__.__name__, str_representation)
        self.assertIn(self.a.created_at.isoformat(), str_representation)
        self.assertIn(self.a.updated_at.isoformat(), str_representation)


if __name__ == '__main__':
    unittest.main()
