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
    user_accessible
    cleanup
}

upgrade () {
    # update & upgrade all installed packages
    apt-get update

    # upgrade warns about:
    # change the home folder of irc
    # from /var/run/ircd to /run/ircd
    usermod -d /run/ircd irc
    # upgrade postgresql manually
    upgrade_postgresql

    apt-get -y --no-show-upgraded upgrade 
}

upgrade_postgresql () {
    # obsolete postgress version 12
    # manually upgrade to 13
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
    # Clone dotfiles repo
    rm "$homedir/.bashrc" "$homedir/.zshrc"
    git clone -b minimal --single-branch --bare https://github.com/Thewessen/dotfiles $homedir/dotfiles
    git --git-dir=$homedir/dotfiles --work-tree=$homedir checkout
    git init --separate-git-dir=$homedir/dotfiles $homedir
    cd $homedir
    git config status.showUntrackedFiles no
    cd -
}

add_zsh_theme () {
    # powerlevel10k theme zsh
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git $homedir/powerlevel10k
}

install_fzf () {
    # install fzf
    git clone --depth 1 https://github.com/junegunn/fzf.git "$homedir/.fzf"
    "$homedir/.fzf/install" --all
    mv /root/.fzf.zsh $homedir
    mv /root/.fzf.bash $homedir
}

install_neovim () {
    # build neovim from source
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
    # install rust
    curl https://sh.rustup.rs -sSf | sh -s -- -y
    source ~/.cargo/env
}

install_bat () {
    # install bat
    cargo install --locked bat
}

install_lsd () {
    # install lsd
    cargo install lsd
}

install_python_modules () {
    # install apt dependencies
    curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py
    python2 get-pip.py
    rm get-pip.py
    python2 -m pip install wheel
    python2 -m pip install virtualenv
}

user_accessible () {
    # make installed packages accesible by vagrant
    mv /root/.cargo $homedir/
    mv /root/.rustup $homedir/
    chown -R vagrant:vagrant $homedir
}

cleanup () {
    apt-get autoremove -y
    apt-get clean -y
}

main "$@"
