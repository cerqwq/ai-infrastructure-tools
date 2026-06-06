# 🏗️ AI Infrastructure Tools

AI基础设施工具，支持IaC设计、Terraform、Ansible。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🏗️ 基础设施设计
- 📋 Terraform配置生成
- 🔄 Ansible Playbook生成
- ☁️ Pulumi代码生成
- 🔄 灾难恢复设计
- 💰 成本估算

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_infrastructure_tools import create_tools

tools = create_tools()

# 基础设施设计
infra = tools.design_infrastructure("Web应用", "高可用")

# Terraform
terraform = tools.generate_terraform("ECS集群", requirements)

# Ansible
ansible = tools.generate_ansible_playbook("部署Web应用", ["server1", "server2"])

# Pulumi
pulumi = tools.generate_pulumi_code("AWS", ["EC2", "RDS", "S3"])

# 灾难恢复
dr = tools.design_disaster_recovery("4小时", "1小时")

# 成本估算
costs = tools.estimate_costs(infrastructure, "AWS")
```

## 📁 项目结构

```
ai-infrastructure-tools/
├── tools.py       # 基础设施工具核心
└── README.md
```

## 📄 许可证

MIT License
