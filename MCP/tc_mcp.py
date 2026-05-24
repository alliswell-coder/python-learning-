# ============================================================
# tc_mcp.py  —  Tool catalogue for the TestCase MCP Server
# Full implementation lives in server.py
# ============================================================

"""
MCP Server  : TestCase MCP
Data source : testcase.csv  (79 test cases across 8 categories)
Framework   : FastMCP 3.x
Transport   : stdio (default) | sse (HTTP)

──────────────────────────────────────────────────────────────
REGISTERED TOOLS
──────────────────────────────────────────────────────────────

1. get_all_testcases()
   ├─ Input  : (none)
   ├─ Output : list[dict]  — all test cases
   └─ Use    : Dump the full repository

2. get_testcase_by_id(tc_id: str)
   ├─ Input  : tc_id  e.g. "TC001"  (case-insensitive)
   ├─ Output : dict   — single test case  |  str error message
   └─ Use    : Look up a specific test case by its ID

3. search_testcases(keyword: str)
   ├─ Input  : keyword  e.g. "password", "two-factor", "tab"
   ├─ Output : list[dict]  — matching test cases
   ├─ Fields : searches TC_ID + Category + Description
   └─ Use    : Free-text search across the whole dataset

4. filter_by_category(category: str)
   ├─ Input  : category  e.g. "Browser Compatibility" (partial, case-insensitive)
   ├─ Output : list[dict]  — test cases in that category
   └─ Use    : Narrow down by test area / module

5. filter_by_status(status: str)
   ├─ Input  : status  →  "PASS" | "FAIL" | "SKIP" | "PENDING"
   │           PENDING = test cases with an empty Status field
   ├─ Output : list[dict]  — test cases matching the status
   └─ Use    : Check what has passed, failed, or not been run yet

6. get_categories()
   ├─ Input  : (none)
   ├─ Output : list[str]  — all unique category names
   └─ Use    : Discover what categories exist before filtering

7. get_summary()
   ├─ Input  : (none)
   ├─ Output : dict  →  { total, by_category, by_status }
   └─ Use    : High-level dashboard / stats at a glance

──────────────────────────────────────────────────────────────
CATEGORIES IN DATA
──────────────────────────────────────────────────────────────
  • Login Page Navigation        (TC001–TC010)
  • Login Form Validation        (TC011–TC020)
  • Error Messages               (TC021–TC030)
  • Password Requirements        (TC031–TC040)
  • Two-Factor Authentication    (TC041–TC050)
  • Browser Compatibility        (TC051–TC060)
  • Keyboard Navigation          (TC061–TC070)
  • Screen Reader Compatibility  (TC071–TC079)

──────────────────────────────────────────────────────────────
HOW TO RUN THE SERVER
──────────────────────────────────────────────────────────────

  # Install dependency
  pip install fastmcp

  # Run with MCP Inspector (browser UI on http://localhost:6274)
  fastmcp dev server.py

  # Run as stdio server (for Claude Desktop / Claude Code)
  python server.py

──────────────────────────────────────────────────────────────
CONNECT TO CLAUDE DESKTOP
──────────────────────────────────────────────────────────────

  Add to  %APPDATA%\\Claude\\claude_desktop_config.json :

  {
    "mcpServers": {
      "testcase-mcp": {
        "command": "python",
        "args": ["C:/Users/karth/OneDrive/Desktop/SDET/MCP/server.py"]
      }
    }
  }

──────────────────────────────────────────────────────────────
CONNECT VIA MCP INSPECTOR
──────────────────────────────────────────────────────────────

  Run:   fastmcp dev server.py
  Open:  http://localhost:6274
  → Select transport: stdio
  → Command: python server.py
  → Click Connect → test any tool interactively

──────────────────────────────────────────────────────────────
"""
