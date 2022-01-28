ssh-moduli
==========

Helper to generate the prime numbers used in the SSH Diffie-Hellman Group Exchange key exchange

The resulting files in OpenSSH format are stored as artifacts.

See the artifacts for each scheduled run:
https://github.com/chevah/ssh-moduli/actions

You can retrieve the links for the already generated artifacts
via the GitHub API using this long command::

    curl -s https://api.github.com/repos/chevah/ssh-moduli/actions/artifacts\?per_page\=9 | jq '[.artifacts[] | {name : .name, archive_download_url : .archive_download_url}]' | jq -r '.[] | select (.name == "etc_ssh_moduli") | .archive_download_url'
OpenSSH upstream generation script which generates the candidates twice:
https://cvsweb.openbsd.org/cgi-bin/cvsweb/src/usr.bin/ssh/moduli-gen/

You can see the OpenSSH portable moduli file here.
This is pulled by Debian and Ubuntu...and I guess other distributions.
Updated 2 or 3 times per year.
https://github.com/openssh/openssh-portable/commits/master/moduli

It needs latest OpenSSH::

    ssh-keygen -M generate -O bits=2048 moduli-2048.candidates
    ssh-keygen -M screen -f moduli-2048.candidates moduli-2048


Limits for GitHub Hosted VM [1]:
* 6 hours per job
* 72 hours per workflow
* 20 concurrent jobs

Generating the candidates is fast. About 15 minutes for 8k.

Validating is slow. Some rough estimates:
* 4096 - 1 hour
* 6144 - 8 hours
* 7680 - 20 hours
* 8192 - 24 hours


[1] https://docs.github.com/en/actions/reference/usage-limits-billing-and-administration#usage-limits
