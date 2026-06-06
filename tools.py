"""
AI Infrastructure Tools - AI基础设施工具
支持IaC设计、Terraform、Ansible
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIInfrastructureTools:
    """
    AI基础设施工具
    支持：IaC、Terraform、Ansible
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_infrastructure(self, application: str, requirements: str) -> Dict:
        """设计基础设施"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{application}设计基础设施：

需求：{requirements}

请返回JSON格式：
{{
    "components": ["组件"],
    "networking": "网络方案",
    "compute": "计算方案",
    "storage": "存储方案"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"infrastructure": content}

    def generate_terraform(self, resource_type: str, requirements: str) -> str:
        """生成Terraform配置"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{resource_type}的Terraform配置：

需求：{requirements}

要求：
1. 模块化
2. 变量化
3. 输出"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_ansible_playbook(self, task: str, servers: List[str]) -> str:
        """生成Ansible Playbook"""
        if not self.client:
            return "LLM客户端未配置"

        servers_text = ", ".join(servers)

        prompt = f"""请生成Ansible Playbook：

任务：{task}
服务器：{servers_text}

要求：
1. 完整的Playbook
2. 错误处理
3. 幂等性"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_pulumi_code(self, cloud: str, resources: List[str]) -> str:
        """生成Pulumi代码"""
        if not self.client:
            return "LLM客户端未配置"

        resources_text = ", ".join(resources)

        prompt = f"""请生成{cloud}的Pulumi代码：

资源：{resources_text}

要求：
1. Python代码
2. 组件化
3. 配置管理"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def design_disaster_recovery(self, rto: str, rpo: str) -> Dict:
        """设计灾难恢复"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请设计灾难恢复方案：

RTO：{rto}
RPO：{rpo}

请返回JSON格式：
{{
    "strategy": "恢复策略",
    "backup": "备份方案",
    "replication": "复制方案"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"disaster_recovery": content}

    def estimate_costs(self, infrastructure: Dict, provider: str) -> Dict:
        """估算成本"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        infra_text = json.dumps(infrastructure, ensure_ascii=False)

        prompt = f"""请估算{provider}基础设施成本：

{infra_text}

请返回JSON格式：
{{
    "monthly_estimate": "月度预估",
    "breakdown": {{"组件": "成本"}},
    "optimizations": ["优化建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"costs": content}


def create_tools(**kwargs) -> AIInfrastructureTools:
    """创建基础设施工具"""
    return AIInfrastructureTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Infrastructure Tools")
    print()

    # 测试
    infra = tools.design_infrastructure("Web应用", "高可用，自动扩展")
    print(json.dumps(infra, ensure_ascii=False, indent=2))
