ssh-moduli
==========

Helper to generate the prime numbers used in the SSH Diffie-Hellman Group Exchange key exchange

The resulting files in OpenSSH format are stored as artifacts.

Needs latest OpenSSH::

    ssh-keygen -M generate -O bits=2048 moduli-2048.candidates
    ssh-keygen -M screen -f moduli-2048.candidates moduli-2048
