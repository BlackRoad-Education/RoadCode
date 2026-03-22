"""Course engine — structured learning paths with AI tutoring."""
from dataclasses import dataclass, field

@dataclass
class Lesson:
    id: str
    title: str
    content: str
    exercises: list[dict] = field(default_factory=list)
    prerequisites: list[str] = field(default_factory=list)

@dataclass
class Course:
    id: str
    title: str
    description: str
    lessons: list[Lesson] = field(default_factory=list)
    difficulty: str = "beginner"

CATALOG = [
    Course("sovereign-101", "Sovereign Computing 101",
           "Learn to self-host everything on Raspberry Pis",
           difficulty="beginner"),
    Course("ai-fleet", "AI Fleet Management",
           "Deploy and manage AI models across a Pi cluster",
           difficulty="intermediate"),
    Course("mesh-networking", "Mesh Networking with WireGuard",
           "Build a private mesh network",
           difficulty="intermediate"),
    Course("amundson-math", "The Amundson Framework",
           "Mathematical foundations: G(n), A_G, and beyond",
           difficulty="advanced"),
]
