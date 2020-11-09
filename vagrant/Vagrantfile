# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure('2') do |config|
  config.vm.define 'ctf'
  config.vm.hostname = 'kali'
  config.vm.box = 'kalilinux/rolling'

  # Default shared folder
  config.vm.synced_folder '.', '/vagrant', disabled: true

  # Custom shared folder
  config.vm.synced_folder '../data', '/data',
    SharedFoldersEnableSymlinksCreate: false,
    create: true,
    disabled: false

  config.vm.provider 'virtualbox' do |vb|
    # Display the VirtualBox GUI when booting the machine
    vb.gui = false
    # Customize the amount of memory on the VM:
    vb.memory = '4096'
    # set name of vm
    vb.name = 'kali'
  end

  config.vm.provision "shell", path: './provision.sh'
end
