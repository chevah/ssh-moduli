ssh-moduli
==========

Helper to generate the prime numbers used in the SSH Diffie-Hellman Group Exchange key exchange

The resulting files in OpenSSH format are stored as artifacts.

Needs latest OpenSSH::

    ssh-keygen -M generate -O bits=2048 moduli-2048.candidates
    ssh-keygen -M screen -f moduli-2048.candidates moduli-2048

Limits for GitHub Hosted VM [1]:
* 6 hours per job
* 72 hours per workflow
* 20 concurrent jobs

Generating the candidates is fast. About 15 minutes for 8k.

Validating is slow:
* 4096 - 1 hour
* 6144 - 10 hours
* 7680 - 30 hours
* 8192


[1] https://docs.github.com/en/actions/reference/usage-limits-billing-and-administration#usage-limits
