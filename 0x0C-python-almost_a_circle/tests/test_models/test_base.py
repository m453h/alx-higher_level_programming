#!/usr/bin/python3
"""Defines unittest classes for Base class in models.base"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase__init__(unittest.TestCase):
    """Unittests for the Base class __init__ method"""

    def test_init_with_no_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, (b2.id - 1))

    def test_init_multiple_bases_with_no_args(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        b5 = Base()
        self.assertEqual(b1.id, b5.id - 4)

    def test_init_with_none_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_init_multiple_bases_with_none_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        b5 = Base()
        self.assertEqual(b1.id, b5.id - 4)

    def test_init_with_proper_id(self):
        self.assertEqual(1, Base(1).id)

    def test_init_after_init_with_proper_id(self):
        b1 = Base()
        b2 = Base(5)
        b3 = Base()
        b4 = Base()
        b5 = Base()
        self.assertEqual(b1.id, b5.id - 3)

    def test_change_id_after_init(self):
        b = Base(3)
        b.id = 9
        self.assertEqual(9, b.id)

    def test_init_with_str_type_id(self):
        self.assertEqual("abc", Base("abc").id)

    def test_init_with_float_type_id(self):
        self.assertEqual(3.14, Base(3.14).id)

    def test_init_with_inf_type_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_init_with_nan_type_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_init_with_complex_no_type_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_init_with_bool_type_id(self):
        self.assertEqual(True, Base(True).id)

    def test_init_with_dict_type_id(self):
        self.assertEqual({"x": 101, "y": 102}, Base({"x": 101, "y": 102}).id)

    def test_init_with_list_type_id(self):
        self.assertEqual([2, 4, 6], Base([2, 4, 6]).id)

    def test_init_with_tuple_type_id(self):
        self.assertEqual((1, 2, 3), Base((1, 2, 3)).id)

    def test_init_with_set_type_id(self):
        self.assertEqual({1, 2, 'a'}, Base({1, 2, 'a'}).id)

    def test_init_with_byte_type_id(self):
        self.assertEqual(b'ALX', Base(b'ALX').id)

    def test_init_with_bytearray_type_id(self):
        self.assertEqual(bytearray(b'School'), Base(bytearray(b'School')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(88, 99)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(1).__nb_instances)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for the Base class to_json_string method"""

    def test_to_json_string_rectangle_instance(self):
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(str, type(Base.to_json_string([r1.to_dictionary()])))

    def test_to_json_string_length_one_rectangle_instance(self):
        r1 = Rectangle(10, 2, 10, 10, 12)
        self.assertTrue(len(Base.to_json_string([r1.to_dictionary()])) == 56)

    def test_to_json_string_length_two_rectangle_instances(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 6, 7, 8, 9)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 104)

    def test_to_json_string_square_instance(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_length_one_square_instance(self):
        s = Square(1, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 38)

    def test_to_json_string_length_two_square_instances(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(6, 7, 8, 9)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 76)

    def test_to_json_string_empty_list_of_objects(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none_list_of_objects(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_with_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_with_more_than_allowed_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1, 3)


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for the Base class to_json_string method"""

    @classmethod
    def tearDown(self):
        """Delete created files during testing phase"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_with_one_rectangle_instance(self):
        r = Rectangle(11, 5, 9, 4, 3)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_with_two_rectangle_instances(self):
        r1 = Rectangle(11, 5, 9, 4, 3)
        r2 = Rectangle(11, 12, 13, 14, 15)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 110)

    def test_save_to_file_with_one_square_instance(self):
        s = Square(10, 20, 30, 40)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 42)

    def test_save_to_file_with_two_square_instances(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(1, 2, 3, 4)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 76)

    def test_save_to_file_filename(self):
        s = Square(1, 2, 3, 4)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 38)

    def test_save_to_file_overwrite_same_file(self):
        s = Square(2, 4, 6, 8)
        Square.save_to_file([s])
        s = Square(10, 8, 6, 4)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 38)

    def test_save_to_file_with_None_list_of_objects(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_with_empty_list_of_objects(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_with_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_with_more_than_allowed_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1, 4, 6)
