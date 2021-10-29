from __future__ import absolute_import
import unittest

from priority_queuer import sort_priority_queue

class TestPriorityQueueFunctions(unittest.TestCase):
    def test_invalid_priority_types(self):
        mock_command_stream = [{"batch_process": 0},
                               {"maya_batch": 3},
                               {"setup_cmd": 'foo'},
                               {"postProcess": 2},
                               {"mov_review": 8},
                               {"katana_render": 4}]
        with self.assertRaises(ValueError):
            sort_priority_queue(mock_command_stream)

    def test_format_invalid_priorities(self):
        mock_command_stream = [{"batch_process": 0},
                               {"katana_render": -10},
                               {"maya_batch": 3},
                               {"mov_review": 8},
                               {"postProcess": 12},
                               {"test_exe": 0}]

        expected_stream = [{"batch_process": 0},
                           {"katana_render": 0},
                           {"test_exe": 0},
                           {"maya_batch": 3},
                           {"mov_review": 8},
                           {"postProcess": 10}]

        mock_sorted_stream = sort_priority_queue(mock_command_stream)
        assert expected_stream == mock_sorted_stream


    def test_correct_sorting(self):
        mock_command_stream = [{"batch_process": 0},
                               {"katana_render": 10},
                               {"maya_batch": 3},
                               {"mov_review": 8},
                               {"postProcess": 1},
                               {"test_exe": 0}]

        expected_stream = [{"batch_process": 0},
                           {"test_exe": 0},
                           {"postProcess": 1},
                           {"maya_batch": 3},
                           {"mov_review": 8},
                           {"katana_render": 10}
                           ]

        mock_sorted_stream = sort_priority_queue(mock_command_stream)
        assert expected_stream == mock_sorted_stream

if __name__ == "__main__":
    unittest.main()