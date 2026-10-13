"""Test LLM HTTP request/event relational constraint without user prompt storage."""
import sqlite3
from app.providers.provider_record_request_audit import provider_record_request_audit

def test_llm_audit_schema(tmp_path):
    db=str(tmp_path/"llm.sqlite3")
    rid=provider_record_request_audit("POST","/completion",200,24.5,db)
    with sqlite3.connect(db) as con:
        assert con.execute("SELECT COUNT(*) FROM llm_api_requests WHERE id=?",(rid,)).fetchone()[0]==1
        assert con.execute("SELECT COUNT(*) FROM llm_api_events WHERE request_id=?",(rid,)).fetchone()[0]==1
        assert con.execute("PRAGMA foreign_key_check").fetchall()==[]
