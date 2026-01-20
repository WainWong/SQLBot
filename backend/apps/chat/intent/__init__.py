"""
意图识别模块类型定义

用于意图识别功能的类型和模型定义
"""
from enum import Enum
from typing import Optional, List
from pydantic import BaseModel, field_validator


class IntentType(str, Enum):
    """意图类型枚举"""
    QUERY = "query"   # 数据查询意图 → 可能需要澄清，最终进入 GENERATE_SQL
    OTHER = "other"   # 其他意图 → 直接返回数据集介绍

    @classmethod
    def _missing_(cls, value):
        """支持大小写不敏感的匹配"""
        if isinstance(value, str):
            lower_value = value.lower()
            for member in cls:
                if member.value == lower_value:
                    return member
        return None


class IntentResult(BaseModel):
    """意图识别 LLM 返回结果"""
    intent: IntentType
    is_clear: bool = True
    rewritten_query: Optional[str] = None    # QUERY + 清晰时
    guess_tables: Optional[List[str]] = None  # QUERY 时（无论清晰与否都会返回，用于获取表Schema）
    response: Optional[str] = None           # OTHER 时


class ClarificationResult(BaseModel):
    """澄清器 LLM 返回结果"""
    response: str  # 统一字段名，与 IntentResult.response 一致
