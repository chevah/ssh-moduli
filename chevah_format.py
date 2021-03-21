"""
Convert from OpenSSH moduli to Chevah Python format.
"""
import os
import sys


def generate_ssh_moduli(input_path, output_path):
    """
    Generate the Python source file which stores the SSH moduli values.
    """

    # Lines for the Python module where to store the SSH moduli values.
    python_moduli = [
        '"""',
        'SSH Moduli files for this release.',
        '',
        'Generate from GHA.',
        '"""',
        '',
        'STATIC_MODULI = {}',
        '',
        ]

    initialized_sizes = []

    with open(input_path, 'r') as stream:
        for line in stream.readlines():
            line = line.strip()
            if not line or line[0] == '#':
                continue

            tim, typ, tst, tri, bits, gen, mod = line.split()

            size = int(bits) + 1

            if size not in initialized_sizes:
                initialized_sizes.append(size)
                python_moduli.append('')
                python_moduli.append('STATIC_MODULI[%s] = []' % (size,))

            gen = int(gen)
            mod = int(mod, 16)
            python_moduli.append(
                'STATIC_MODULI[%s].append((%s, %s))' % (size, gen, mod))

    # Have empty line at the end.
    python_moduli.append('')

    with open(output_path, 'w') as stream:
        stream.write('\n'.join(python_moduli))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: INPUT_PATH OUTPUT_PATH')
        sys.exit(1)

    generate_ssh_moduli(sys.argv[1], sys.argv[2])
