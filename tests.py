import unittest
import tempfile
import os
import common_ip


class TestIPAddressComparisonScript(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create temporary CSV and TXT files
        cls.temp_csv1 = tempfile.NamedTemporaryFile(
            mode='w', delete=False, suffix='.csv')
        cls.temp_csv1.write("192.168.1.1\n"
                            "10.0.0.1\n"
                            "192.168.1.2\n")
        cls.temp_csv1.close()

        cls.temp_txt1 = tempfile.NamedTemporaryFile(
            mode='w', delete=False, suffix='.txt')
        cls.temp_txt1.write("192.168.1.1\n"
                            "10.0.0.1\n"
                            "192.168.1.3\n")
        cls.temp_txt1.close()

        cls.temp_csv2 = tempfile.NamedTemporaryFile(
            mode='w', delete=False, suffix='.csv')
        cls.temp_csv2.write("192.168.1.1\n"
                            "10.0.0.1\n"
                            "192.168.1.4\n")
        cls.temp_csv2.close()

        cls.temp_txt2 = tempfile.NamedTemporaryFile(
            mode='w', delete=False, suffix='.txt')
        cls.temp_txt2.write("192.168.1.1\n"
                            "10.0.0.2\n"
                            "192.168.1.3\n")
        cls.temp_txt2.close()

    @classmethod
    def tearDownClass(cls):
        # Remove temporary files
        os.remove(cls.temp_csv1.name)
        os.remove(cls.temp_txt1.name)
        os.remove(cls.temp_csv2.name)
        os.remove(cls.temp_txt2.name)

    def test_csv_to_list(self):
        # Execute the function "csv_to_list"
        ip_list = common_ip.csv_to_list(self.temp_csv1.name)
        # Test if ip_list is a good list
        self.assertEqual(ip_list, {"192.168.1.1", "10.0.0.1", "192.168.1.2"})

    def test_txt_to_list(self):
        # Execute the function "txt_to_list"
        ip_list = common_ip.txt_to_list(self.temp_txt1.name)
        # Test if ip_list is a good list
        self.assertEqual(ip_list, {"192.168.1.1", "10.0.0.1", "192.168.1.3"})

    def test_load_ip_addresses_from_file(self):
        # Execute the function "load_ip_addresses_from_file"
        ip_list = common_ip.load_ip_addresses_from_file(self.temp_csv1.name)
        # Test if ip_list is a good list
        self.assertEqual(ip_list, {"192.168.1.1", "10.0.0.1", "192.168.1.2"})

        ip_list = common_ip.load_ip_addresses_from_file(self.temp_txt1.name)
        self.assertEqual(ip_list, {"192.168.1.1", "10.0.0.1", "192.168.1.3"})

        # Test unsupported file format
        with self.assertRaises(ValueError):
            common_ip.load_ip_addresses_from_file(self.temp_csv1.name + '.xyz')

    def test_compare_all_files(self):
        # Compare files
        common_ips = common_ip.compare_all_files(
            self.temp_csv1.name, self.temp_txt1.name, self.temp_csv2.name, self.temp_txt2.name)
        self.assertEqual(common_ips, {"192.168.1.1"})

    def test_compare_common_ips_across_files(self):
        # Compare files
        common_ips = common_ip.compare_common_ips_across_files(
            self.temp_csv1.name, self.temp_txt1.name, self.temp_csv2.name, self.temp_txt2.name)
        self.assertEqual(common_ips, {'192.168.1.1': {self.temp_csv1.name, self.temp_txt1.name, self.temp_csv2.name, self.temp_txt2.name}, '10.0.0.1': {
                         self.temp_csv1.name, self.temp_txt1.name, self.temp_csv2.name}, '192.168.1.3': {self.temp_txt1.name, self.temp_txt2.name}})


if __name__ == '__main__':
    unittest.main()
