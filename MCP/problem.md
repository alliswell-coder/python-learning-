# Problem Statement: Local MCP Server for Test Case Management

## Overview

Build a **local MCP (Model Context Protocol) server** using **FastMCP** that exposes 100 test cases as a data source. Any LLM (Claude, GPT, Gemini, etc.) can connect to this MCP server and interact with the test cases — searching by keyword, filtering by metadata, and fetching individual test case details.

---

## Problem

QA teams maintain large sets of test cases in files (CSV, JSON, Markdown). When working with AI assistants, there is no structured way for the LLM to:

- Browse available test cases
- Search test cases by keyword (e.g., "password", "two-factor")
- Filter test cases by metadata (e.g., category, status, priority)
- Fetch a specific test case by ID

Without an MCP server, the LLM has no live access to this data — you would have to paste test cases manually into every prompt.

---

## Goal

Create a **FastMCP server** that:

1. Loads 100 test cases from a local CSV/JSON file at startup
2. Exposes the following **MCP tools** that any connected LLM can call:

| Tool | Description |
|---|---|
| `get_all_testcases` | Returns all 100 test cases |
| `get_testcase_by_id` | Fetch a single test case by TC_ID (e.g., `TC001`) |
| `search_testcases` | Full-text keyword search across descriptions |
| `filter_by_category` | Filter test cases by category (e.g., "Login Form Validation") |
| `filter_by_status` | Filter by execution status (PASS / FAIL / SKIP / empty) |
| `get_categories` | List all unique categories available |

3. Runs locally on `http://localhost:8000` (SSE or stdio transport)
4. Can be connected to Claude, Cursor, or any MCP-compatible LLM client

---

## Data Source

Test cases are stored in `testcase.csv` with the following schema:

```
TC_ID, Category, Description, Status
TC001, Login Page Navigation, "Launch the VWO login page and verify the title",
TC002, Login Form Validation, "Enter a valid email and password...", PASS
...
```

---

## Tech Stack

| Layer | Tool |
|---|---|
| MCP Framework | FastMCP |
| Language | Python 3.10+ |
| Data Layer | CSV (via `csv` module or `pandas`) |
| Transport | `stdio` (for Claude Desktop) or `sse` (for HTTP clients) |
| LLM Clients | Claude Desktop, Cursor, or any MCP-compatible host |

---

## Expected Project Structure

```
MCP/
├── problem.md          <- This file
├── testcase.csv        <- 100 test cases data source
├── server.py           <- FastMCP server (tools defined here)
├── requirements.txt    <- fastmcp, pandas
└── README.md           <- How to run and connect
```

---

## How It Works (Flow)

```
LLM Client (Claude / GPT / Cursor)
        |
        |  MCP Protocol (stdio / SSE)
        v
  FastMCP Server (server.py)
        |
        |  Reads CSV at startup
        v
  testcase.csv (100 test cases)
```

1. LLM sends a tool call: `search_testcases(keyword="password")`
2. FastMCP routes the call to the matching Python function
3. The function searches the in-memory test case list
4. Result is returned to the LLM as structured JSON
5. LLM uses the result to answer the user's question

---

## Example Interactions

**User to LLM:**
> "Show me all test cases related to two-factor authentication"

**LLM MCP tool call:**
```json
{ "tool": "search_testcases", "keyword": "two-factor" }
```

**MCP response to LLM:**
```json
[
  { "TC_ID": "TC041", "Category": "Two-Factor Authentication", "Description": "...", "Status": "" },
  { "TC_ID": "TC042", "Category": "Two-Factor Authentication", "Description": "...", "Status": "" }
]
```

---

## Acceptance Criteria

- [ ] FastMCP server starts without errors
- [ ] All 6 tools are registered and callable
- [ ] `search_testcases` is case-insensitive and searches the description field
- [ ] `filter_by_category` returns exact category matches
- [ ] `filter_by_status` filters correctly on PASS / FAIL / SKIP
- [ ] Server connects successfully to at least one LLM client (Claude Desktop or Cursor)
- [ ] LLM can answer questions about test cases using only MCP tool calls (no manual pasting)
