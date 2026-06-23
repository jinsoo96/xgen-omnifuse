"""Vault demo — fuse knowledge in, surface it out (salience-ranked). Zero infra.

    python examples/vault_example.py
"""
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from omnifuse import Vault  # noqa: E402

v = Vault()
v.fuse(facts=[("담보", "instanceOf", "규정"), ("감사규정", "instanceOf", "규정")])
v.fuse("담보 한도는 5억원이며 정규담보비율 60%가 적용된다.",
       facts=[("담보", "한도", "5억"), ("담보", "정규담보비율", "60%")])
v.fuse("담보 관련 추가 메모.")           # auto-links to 담보 -> salience↑

print("stats:", v.stats())
print("salience 담보:", v.salience("담보"), "/ 감사규정:", v.salience("감사규정"))
print("\n[surface: 담보 한도]\n", v.surface("담보 한도").answer[:180])
print("\n[surface: 규정 전부] evidence(salience순):", v.surface("규정 전부").evidence_nodes)
