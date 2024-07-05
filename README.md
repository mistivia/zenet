# ZeNET

A set of scripts to quickly build a Wireguard network for games like Touhou Hisoutensoku.

## How to Use

Clone this repo.

    git clone https://github.com/mistivia/zenet.git

Generate private key:

    wg genkey > ./privkey ; cat privkey

Generate public key:

    cat privkey | wg pubkey

Create config file and edit it:

    cp config_example.ini config.ini
    vim config.ini

Create some new users:

    ./new-user.sh alice
    ./new-user.sh bob

Deploy it:

    ./deploy.sh

Enable IP packet forwarding on server:

    ssh user@www.yourserver.com

Edit `/etc/sysctl.conf`:

    sudo nano /etc/sysctl.conf

Add this line:
    
    net.ipv4.ip_forward = 1

Apply settings:

    sudo bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'
    sudo sysctl -p

To add new users, create user and rerun `deploy.sh`.
    
    ./new-user.sh carol
    ./deploy.sh

Now you can distribute Wireguard profiles in `./cli-confs` to your friends.

