# -*- mode: ruby -*-
# vi: set ft=ruby :

PACKAGE = "UnitTesting-example"

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box = "precise64"
    config.vm.box_url = "http://files.vagrantup.com/precise64.box"

    config.vm.define "st2" do |st2|
        st2.vm.provision "shell" do |s| 
            s.path = "vagrantup.sh"
            s.args = ["2", PACKAGE]
        end
    end

    config.vm.define "st3" do |st3|
        st3.vm.provision "shell" do |s| 
            s.path = "vagrantup.sh"
            s.args = ["3", PACKAGE]
        end
    end  
end