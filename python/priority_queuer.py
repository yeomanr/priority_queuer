from collections import OrderedDict
import logging
import operator

import six


logging.basicConfig(format='%(filename)s:%(message)s', level=logging.INFO)


def sort_priority_queue(command_stream):
    """ Given a stream of commands, each comprised of a {command:priority}
        key-value pair, return a sorted queue stream where commands of the
        same priority are processed in the order in which they were receieved.

    Args:
        command_stream (list): Incoming list of {command:priority} dicts

    Returns:
        (list): A stream of commands sorted by priority and the order in which
                they were received.
    """
    # Converting command_stream to a single dict will aid in the sort later.
    command_dict = dict()
    for command in command_stream:
        cmd, prio = list(command.items())[0]

        if not isinstance(prio, six.integer_types):
            raise ValueError("Priority assigned to command: '{}' is not that "
                             "of type 'integer'. Command stream will not be "
                             "processed.".format(cmd))

        # Update command priorities which fall outside priority range of 0-10
        if prio < 0:
            command_dict[cmd] = 0
            logging.info("Invalid priority of {prio} assigned to cmd: "
                         "'{cmd}'. Assigning priority of 0".format(prio=prio,
                                                                   cmd=cmd))
        elif prio > 10:
            command_dict[cmd] = 10
            logging.info("Invalid priority of {prio} assigned to cmdd: "
                         "'{cmd}'. Assigning priority of 10".format(prio=prio,
                                                                    cmd=cmd))
        else:
            command_dict[cmd] = prio

    # Sort the command stream by priorities while maintaining the key-order in
    # which the commands came in.
    prioritized_cmds = OrderedDict(sorted(list(command_dict.items()),
                                   key=operator.itemgetter(1)))

    # Convert the sorted command stream back to its original format/type
    sorted_command_stream = list()
    for executable, priority in list(prioritized_cmds.items()):
        sorted_command_stream.append({executable: priority})

    return sorted_command_stream
