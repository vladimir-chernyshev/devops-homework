Курсовая работа по итогам модуля "DevOps и системное администрирование"
===
1. Создайте виртуальную машину Linux.
 Добавим вторую вирутальную машину в Vagrantfile согласно [документации](https://www.vagrantup.com/docs/multi-machine):
Vagrantfile:

>Vagrant.configure("2") do |config|  
>  config.vm.define "ubuntu" do |ubt|  
>    ubt.vm.box = "bento/ubuntu-20.04"  
>  end  
>  config.vm.define "rocky" do |rck|  
>    rck.vm.box = "bento/rockylinux-8"  
>  end  
>end  

	$vagrant up rocky
	$vagrant ssh rocky

2. Установите ufw и разрешите к этой машине сессии на порты 22 и 443, при этом трафик на интерфейсе localhost (lo) должен ходить свободно на все порты.
---

В Телеграмм-чате курса был задан вопрос и эксперт уточнил, что использование конкретно *ufw* не принципиально, буду использовать *firewalld* - связано со спецификой основной работы.
