# Lock
Application for securely storing, sharing, and backing up sensitive information.

Data can be in any format.  Each item is a simple JSON object, with a structure based on its type.  Currently the only type is "credential".  Every value is associated with a key.  The key can contain slashes to denote hierarchy, but they are stored as flat key-value pairs.  

## Why another password manager?

There are two main ways to store passwords at the moment: in the cloud, or locally.  Cloud-based password storage has the advantage of being easy to share, but may not be suitable for all security requirements.  Locally stored password managers have the advantage in security, but make it difficult to share securely.  Even worse, they encourage sharing credentials in plain text over email, since that's the easiest way to do it.

Lock aims to be the best of both worlds.  The security of being stored on your local machine, but with the ease of sharing provided by online options.

## How

What is the solution to this problem?  Asymmetric encryption.  When lock is first run, it generates a private/public keypair, locked with a passphrase that you define.  The public key is used to encrypt your password database, while the private key is used to decrypt it.  The passwords are only ever decrypted in memory.

If you want to share passwords with someone else, you only need their public key.  Because it's a public key, they can send it by any means: keeping the public key safe is not necessary.  Once you have it, you can export a limited number of passwords into a new encrypted database using their key.  Because this file is encrypted, and only the intended recipient can depcrypt it, you can safely send it to them without worrying about it being shared with the wrong people.

## Commands

### `add`

Adds a new key pair.

    $ lock add projects/lock/github username=jonahbron password=abcdefg

The information will be stored under the key `projects/lock/github`, with the assigned values for `username` and `password`.

### `get`

Gets a stored key pair 

    $ lock add projects/lock/github

    username: jonahbron
    password: abcdefg

To access keys in a file received from someone else, specify the path to the file with `--file`.

### `update`

Updates an existing key pair.

    $ lock update projects/lock/github password=bcdefgh

To change the key itself, use the `--key` flag.

    $ lock update projects/lock/github --key projects/lock/heroku

### remove

Remove a keypair

    $ lock remove projects/lock/github

By default, `remove` will only mark it as deleted, but it won't actually be gone.  Use the `--permanent` flag to completely remove it.

### key

Outputs your public key so it can be shared.

    $ lock key

