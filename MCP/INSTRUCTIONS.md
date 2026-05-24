# MCP Server – Build Instructions & Prompt History

## What Was Built
A local MCP (Model Context Protocol) server using **FastMCP 3.x** that exposes
80 VWO login-page test cases to any MCP-compatible LLM (Claude, Cursor, LM Studio, etc.).

---

## Prompts Used (in order)

### 1. Convert test cases to CSV
> "Convert this file into a .csv file and put inside the MCP folder"

**Result:** `testcase.md` → `testcase.csv` with columns `TC_ID, Category, Description, Status`

---

### 2. Write the problem statement
> "Update this in problem.md — suppose you have 100 test cases and I need to develop
> a local MCP using FastMCP, where any LLM can be connected to this MCP and access
> the test cases which are present. They can search the test cases with keyword, metadata also."

**Result:** `problem.md` with full problem statement, goal, tech stack, flow diagram, acceptance criteria

---

### 3. Build the MCP server
> "So do work on creating the MCP server so that we can connect locally.
> Additionally let me know Inspector so that we can connect it locally."

**Result:** `server.py` with 7 tools registered via FastMCP, `requirements.txt`

---

### 4. Create tool catalogue
> "Can you update the tc_mcp.py with list of the functions that is been taken care"

**Result:** `tc_mcp.py` — reference doc listing all 7 tools with inputs, outputs, and connection instructions

---

### 5. Add a dummy test case
> "Can you add a new test case, any dummy test case also"

**Result:** `TC080` added — "Verify VWO login page loads within 3 seconds on slow 3G network" (Status: PASS)

---

### 6. Run locally & test tools
> "Can I check in local?"

**Commands used:**
```powershell
python -c "import server; print(server.get_summary())"
python -c "import server; print(server.get_categories())"
python -c "import server; print(server.get_testcase_by_id('TC005'))"
python -c "import server; print(server.filter_by_status('PENDING'))"
```

---

### 7. Deploy on HTTP transport
> "Can you deploy in different local?"
> "Let's refresh and start in other server — nothing is working"

**Fix:** Changed transport from `stdio` → `http` using `mcp.run(transport="http", host="127.0.0.1", port=8000)`

**Run server:**
```powershell
cd "C:\Users\karth\OneDrive\Desktop\SDET\MCP"
python server.py
```

Server runs at: `http://127.0.0.1:8000/mcp`

---

### 8. Push to GitHub
> "Create an instruction md and mention all the prompts that were used and then push all the code to GitHub"

**Result:** This file + all MCP files committed and pushed to `origin/main`

---

## Project Structure

```
MCP/
├── server.py           ← FastMCP server (7 tools)
├── testcase.csv        ← 80 test cases (data source)
├── tc_mcp.py           ← Tool catalogue & reference doc
├── problem.md          ← Problem statement
├── requirements.txt    ← fastmcp>=2.0.0
└── INSTRUCTIONS.md     ← This file
```

---

## 7 Tools in server.py

| Tool | Input | Description |
|---|---|---|
| `get_all_testcases` | none | Returns all 80 test cases |
| `get_testcase_by_id` | `tc_id` | Fetch one test case e.g. TC001 |
| `search_testcases` | `keyword` | Full-text search across ID, Category, Description |
| `filter_by_category` | `category` | Filter by category name (partial match) |
| `filter_by_status` | `status` | Filter by PASS / FAIL / SKIP / PENDING |
| `get_categories` | none | List all 8 unique categories |
| `get_summary` | none | Total count + breakdown by category and status |

---

## How to Run

```powershell
# Install dependency
pip install fastmcp

# Start the MCP server (HTTP mode)
cd "C:\Users\karth\OneDrive\Desktop\SDET\MCP"
python server.py
```

Server starts at: `http://127.0.0.1:8000/mcp`

---

## How to Test Locally (second terminal)

```powershell
# List all tools
fastmcp list http://127.0.0.1:8000/mcp

# Call tools
fastmcp call http://127.0.0.1:8000/mcp get_summary
fastmcp call http://127.0.0.1:8000/mcp search_testcases keyword=password
fastmcp call http://127.0.0.1:8000/mcp get_testcase_by_id tc_id=TC001
fastmcp call http://127.0.0.1:8000/mcp filter_by_category category=Browser
```

---

## Connect to Claude Desktop

Add to `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "testcase-mcp": {
      "command": "python",
      "args": ["C:/Users/karth/OneDrive/Desktop/SDET/MCP/server.py"]
    }
  }
}
```

---

## Tech Stack

| Layer | Tool |
|---|---|
| MCP Framework | FastMCP 3.3.1 |
| Language | Python 3.14 |
| Data | CSV (80 test cases) |
| Transport | HTTP (streamable-http) |
| LLM Clients | Claude Desktop, Cursor, LM Studio, Ollama |
