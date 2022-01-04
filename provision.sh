# change shell

main () {
    homedir='/home/vagrant'
    # make zsh the default shell
    usermod --shell /bin/zsh vagrant

    # install most wanted packages and config
    upgrade
    add_configs
    add_zsh_theme
    install_fzf
    install_neovim
    install_rust
    install_bat
    install_lsd
    install_python_modules
    install_seclists
    install_openvpn
    user_accessible
    cleanup
}

upgrade () {
    echo "update apt repo"
    apt-get update

    # upgrade warns about:
    # change the home folder of irc
    # from /var/run/ircd to /run/ircd
    usermod -d /run/ircd irc

    # upgrade postgresql manually
    upgrade_postgresql

    echo "update & upgrade all installed packages"
    apt-get -y --no-show-upgraded \
        --asume-yes \
        --allow-change-held-packages \
        --allow-remove-essential \
        full-upgrade

    echo "update searchsploit manually"
    searchsploit --update
}

upgrade_postgresql () {
    echo "manually upgrade postgress to 13"
    apt-get install -y postgresql-13 postgresql-client-13 postgresql-doc-13
    pg_dropcluster --stop 13 main
    pg_upgradecluster 12 main
    pg_dropcluster 12 main
    apt-get purge \
        --assume-yes \
        --allow-change-held-packages \
        --allow-remove-essential \
        postgresql-12 postgresql-client-12 postgresql-doc-12
    rm -rf /var/lib/postgresql/12/main
}

add_configs () {
    echo "cloning and installing dotfiles repo"

    rm "$homedir/.bashrc" "$homedir/.zshrc"
    git clone -b minimal --single-branch --bare https://github.com/Thewessen/dotfiles.git $homedir/dotfiles
    git --git-dir=$homedir/dotfiles --work-tree=$homedir checkout
    # TODO: remove traces of dotfiles
    git init --separate-git-dir=$homedir/dotfiles $homedir
    cd $homedir
    git config status.showUntrackedFiles no
    cd -
}

add_zsh_theme () {
    echo "installing powerlevel10k theme zsh"
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git $homedir/powerlevel10k
}

install_fzf () {
    echo "install fzf"
    git clone --depth 1 https://github.com/junegunn/fzf.git "$homedir/.fzf"
    "$homedir/.fzf/install" --all
    mv /root/.fzf.zsh $homedir
    mv /root/.fzf.bash $homedir
}

install_neovim () {
    echo "build neovim from source"
    apt-get install --fix-missing -y ninja-build gettext libtool libtool-bin autoconf automake cmake g++ pkg-config unzip python2 python3-pip nodejs npm
    git clone https://github.com/neovim/neovim.git neovim
    cd neovim
    make CMAKE_BUILD_TYPE=RelWithDebInfo #this also symlinks bin..
    sudo make install
    cd -
    rm -rf neovim

    # install neovim providers
    gem install neovim
    npm i -g neovim
    python2.7 -m pip install neovim
    python3 -m pip install neovim


    #install neovim plugins
    #XXX: needs dotfiles
    $homedir/install/vim-plugins.sh
}

install_rust () {
    echo "install rust"
    curl https://sh.rustup.rs -sSf | sh -s -- -y
    source ~/.cargo/env
}

install_bat () {
    echo "install bat"
    cargo install --locked bat
}

install_lsd () {
    echo "install lsd"
    cargo install lsd
}

install_python_modules () {
    echo "install apt dependencies"
    curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py
    python2 get-pip.py
    rm get-pip.py
    python2 -m pip install wheel
    python2 -m pip install virtualenv
}

install_seclists () {
    echo "install common wordlists"
    apt install -y seclists --fix-missing
}

install_openvpn () {
    echo "install openvpn"
    apt install -y openvpn --fix-missing
}

user_accessible () {
    echo "make installed packages accesible by vagrant"
    mv -r /root/.cargo $homedir/
    mv -r /root/.rustup $homedir/
    chown -R vagrant:vagrant $homedir
}

cleanup () {
    echo "cleanup..."
    apt-get autoremove -y
    apt-get clean -y
    #XXX: rm -rf $homedir/dotfiles
}

main "$@"
