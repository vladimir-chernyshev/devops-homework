 Домашнее задание к занятию "7.2. Облачные провайдеры и синтаксис Terraform."
===

Задача 1 (Вариант с Yandex.Cloud). Регистрация в ЯО и знакомство с основами (необязательно, но крайне желательно).
---


```bash
 yc config list
token: AQAAAAB**********************
cloud-id: b1gqo6r13ihd0vmgjq8p
folder-id: b1gf3qaa4c5nl8l72v3q
compute-default-zone: ru-central1-a
```


Задача 2. Создание aws ec2 или yandex_compute_instance через терраформ. 
---


```bash
$ terraform plan
$ terraform apply -auto-approve
```


```
Plan: 1 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address_node01_yandex_cloud = (known after apply)
yandex_compute_instance.node01: Creating...
yandex_compute_instance.node01: Still creating... [10s elapsed]
yandex_compute_instance.node01: Still creating... [20s elapsed]
yandex_compute_instance.node01: Creation complete after 28s [id=fhmoai7l470ri5ehcl7j]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

```

---

В качестве результата задания предоставьте:
1. Ответ на вопрос: при помощи какого инструмента (из разобранных на прошлом занятии) можно создать свой образ ami?

---

Свой образ для YC можно создать при помощи `packer`

---

2. Ссылку на репозиторий с исходной конфигурацией терраформа.  
 
---


*Ссылка на соответствующий [репозиторий](https://github.com/vladimir-chernyshev/devops-homework/tree/main/07-terraform-02-syntax/terraform/)*
