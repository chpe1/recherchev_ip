import unittest
import tempfile
import os
import common_ip


class TestIPAddressComparisonScript(unittest.TestCase):
    def test_csv_to_list(self):
        # Create a temporary CSV file
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_csv:
            temp_csv.write("192.168.1.1\n"
                           "10.0.0.1\n"
                           "192.168.1.2\n")
        # Execute the function "csv_to_list"
        ip_list = common_ip.csv_to_list(temp_csv.name)
        # Test if ip_list is a good list
        self.assertEqual(ip_list, {"192.168.1.1", "10.0.0.1", "192.168.1.2"})
        # Delete the temp csv file
        os.remove(temp_csv.name)

    def test_txt_to_list(self):
        # Create a temporary TXT file
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_txt:
            temp_txt.write("192.168.1.1\n"
                           "10.0.0.1\n"
                           "192.168.1.2\n")
        # Execute the function "txt_to_list"
        ip_list = common_ip.txt_to_list(temp_txt.name)
        # Test if ip_list is a good list
        self.assertEqual(ip_list, {"192.168.1.1", "10.0.0.1", "192.168.1.2"})
        # Delete the temp txt file
        os.remove(temp_txt.name)

    def test_load_ip_addresses_from_file(self):
        # Create a temporary CSV file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as temp_csv:
            temp_csv.write("192.168.1.1\n"
                           "10.0.0.1\n"
                           "192.168.1.2\n")
        # Execute the function "load_ip_addresses_from_file"
        ip_list = common_ip.load_ip_addresses_from_file(temp_csv.name)
        # Test if ip_list is a good list
        self.assertEqual(ip_list, {"192.168.1.1", "10.0.0.1", "192.168.1.2"})
        # Delete the temp csv file
        os.remove(temp_csv.name)

        # Create a temporary TXT file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_txt:
            temp_txt.write("192.168.1.1\n"
                           "10.0.0.1\n"
                           "192.168.1.2\n")
        ip_list = common_ip.load_ip_addresses_from_file(temp_txt.name)
        self.assertEqual(ip_list, {"192.168.1.1", "10.0.0.1", "192.168.1.2"})
        os.remove(temp_txt.name)

        # Test unsupported file format
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.xyz') as temp_xyz:
            with self.assertRaises(ValueError):
                common_ip.load_ip_addresses_from_file(temp_xyz.name)
        os.remove(temp_xyz.name)

    def test_compare_all_files(self):
        # Create temporary CSV and TXT files
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as temp_csv1:
            temp_csv1.write("192.168.1.1\n"
                            "10.0.0.1\n"
                            "192.168.1.2\n")
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_txt1:
            temp_txt1.write("192.168.1.1\n"
                            "10.0.0.1\n"
                            "192.168.1.3\n")

        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as temp_csv2:
            temp_csv2.write("192.168.1.1\n"
                            "10.0.0.1\n"
                            "192.168.1.4\n")
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_txt2:
            temp_txt2.write("192.168.1.1\n"
                            "10.0.0.2\n"
                            "192.168.1.3\n")

        # Compare files
        common_ips = common_ip.compare_all_files(
            temp_csv1.name, temp_txt1.name, temp_csv2.name, temp_txt2.name)
        self.assertEqual(common_ips, {"192.168.1.1"})

        # Remove temporary files
        os.remove(temp_csv1.name)
        os.remove(temp_txt1.name)
        os.remove(temp_csv2.name)
        os.remove(temp_txt2.name)


if __name__ == '__main__':
    unittest.main()
