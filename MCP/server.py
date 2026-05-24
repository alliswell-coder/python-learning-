import csv
import os
from fastmcp import FastMCP

# ── Load CSV ─────────────────────────────────────────────────
CSV_PATH = os.path.join(os.path.dirname(__file__), "testcase.csv")

def _load() -> list[dict]:
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        return [{k.strip(): v.strip() for k, v in row.items()} for row in csv.DictReader(f)]

TEST_CASES: list[dict] = _load()

# ── MCP Server ───────────────────────────────────────────────
mcp = FastMCP(name="TestCase MCP")

@mcp.tool()
def get_all_testcases() -> list[dict]:
    """Return all test cases."""
    return TEST_CASES

@mcp.tool()
def get_testcase_by_id(tc_id: str) -> dict | str:
    """Fetch a single test case by ID e.g. TC001."""
    for tc in TEST_CASES:
        if tc["TC_ID"].upper() == tc_id.strip().upper():
            return tc
    return f"No test case found with ID '{tc_id}'."

@mcp.tool()
def search_testcases(keyword: str) -> list[dict]:
    """Search test cases by keyword across ID, Category, Description."""
    kw = keyword.lower()
    return [tc for tc in TEST_CASES if kw in tc.get("TC_ID","").lower()
            or kw in tc.get("Category","").lower()
            or kw in tc.get("Description","").lower()]

@mcp.tool()
def filter_by_category(category: str) -> list[dict]:
    """Filter test cases by category name (partial match)."""
    return [tc for tc in TEST_CASES if category.lower() in tc.get("Category","").lower()]

@mcp.tool()
def filter_by_status(status: str) -> list[dict]:
    """Filter by status: PASS, FAIL, SKIP, PENDING (not yet run)."""
    status = status.strip().upper()
    if status == "PENDING":
        return [tc for tc in TEST_CASES if not tc.get("Status","").strip()]
    return [tc for tc in TEST_CASES if tc.get("Status","").upper() == status]

@mcp.tool()
def get_categories() -> list[str]:
    """List all unique categories."""
    seen = []
    for tc in TEST_CASES:
        cat = tc.get("Category","").strip()
        if cat and cat not in seen:
            seen.append(cat)
    return seen

@mcp.tool()
def get_summary() -> dict:
    """Summary of total, by category and by status."""
    cats, stats = {}, {}
    for tc in TEST_CASES:
        c = tc.get("Category","Unknown").strip()
        s = tc.get("Status","").strip().upper() or "PENDING"
        cats[c] = cats.get(c, 0) + 1
        stats[s] = stats.get(s, 0) + 1
    return {"total": len(TEST_CASES), "by_category": cats, "by_status": stats}

# ── Run ──────────────────────────────────────────────────────
if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8000)
