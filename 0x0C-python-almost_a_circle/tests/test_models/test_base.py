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


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for the Base class from_json_string method"""

    def test_from_json_string_type_returned_test(self):
        list_input = [{"id": 1, "width": 8, "height": 12}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle_instance(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangle_instances(self):
        list_input = [
            {"id": 10, "width": 12, "height": 8, "x": 2, "y": 4},
            {"id": 20, "width": 6, "height": 4, "x": 3, "y": 6},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square_instance(self):
        list_input = [{"id": 10, "size": 10}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares_instances(self):
        list_input = [{"id": 10, "size": 10}, {"id": 20, "size": 5}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_with_None_input(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_with_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_with_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_with_more_than_allowed_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1, 4, 3)


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
            self.assertTrue(len(f.read()) == 39)

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


class TestBase_create(unittest.TestCase):
    """Unittests for the Base class create method"""

    def test_create_square_simple(self):
        s1 = Square(3, 2, 4, 1)
        self.assertEqual("[Square] (1) 2/4 - 3", str(s1))

    def test_create_rectangle_first_instance(self):
        r1 = Rectangle(1, 2, 1, 2, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual("[Rectangle] (1) 1/2 - 1/2", str(r1))

    def test_create_rectangle_clone_instance(self):
        r1 = Rectangle(8, 8, 4, 6, 9)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual("[Rectangle] (9) 4/6 - 8/8", str(r2))

    def test_create_rectangle_is_operator(self):
        r1 = Rectangle(2, 2, 4, 4, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals_operator(self):
        r1 = Rectangle(2, 2, 4, 4, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing load_from_file_method of Base class."""

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

    def test_load_from_file_first_rectangle(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_third_rectangle(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        r3 = Rectangle(11, 12, 13, 14, 15)
        Rectangle.save_to_file([r1, r2, r3])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r3), str(list_rectangles_output[2]))

    def test_load_from_file_rectangle_data_type(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(rect) == Rectangle for rect in output))

    def test_load_from_file_first_square(self):
        s1 = Square(5, 10, 3, 3)
        s2 = Square(15, 20, 2, 2)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        s1 = Square(5, 10, 3, 3)
        s2 = Square(15, 20, 2, 2)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_third_square(self):
        s1 = Square(5, 10, 3, 3)
        s2 = Square(15, 20, 2, 2)
        s3 = Square(25, 30, 4, 4)
        Square.save_to_file([s1, s2, s3])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s3), str(list_squares_output[2]))

    def test_load_from_file_square_types(self):
        s1 = Square(46, 8, 3, 3)
        s2 = Square(13, 15, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(sq) == Square for sq in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_with_more_than_allowed_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1, 2, 3)


if __name__ == "__main__":
    unittest.main()
