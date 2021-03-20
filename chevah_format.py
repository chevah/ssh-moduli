"""
Combine the OpenSSH moduli and output in Chevah Python format.

The files should end with the file size.
"""
import os
import sys


def generate_ssh_moduli(source_start, output_path):
    """
    Generate the Python source file which stores the SSH moduli values.
    """

    # Lines for the Python module where to store the SSH moduli values.
    python_moduli = [
        '"""'
        'SSH Moduli files for this release.'
        ''
        'Generate the content of file using'
        '`$ paver test_remote gk-ssh-moduli`'
        'and then copy the output of the step below.'
        '"""',
        '',
        'STATIC_MODULI = {}'
        ]

    source_files = [n for n in os.listdir() if n.startswith(source_start)]

    for validated_file in sorted(source_files):

        size = int(validated_file[len(source_start):])

        python_moduli.append('')
        python_moduli.append('STATIC_MODULI[%s] = []' % (size,))

        with open(validated_file, 'rb') as stream:
            for line in stream.readlines():
                line = line.strip()
                if not line or line[0] == '#':
                    continue
                tim, typ, tst, tri, bits, gen, mod = line.split()
                if size != int(bits) + 1:
                    raise Exception('Mismatch in moduli size.')

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
        print('Usage: SOURCE_START_NAME OUTPUT_PATH')
        sys.exit(1)

    generate_ssh_moduli(sys.argv[1], sys.argv[1])
