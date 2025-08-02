from contextvars import ContextVar

# Context var to store request UUID
request_id_ctx_var: ContextVar[str] = ContextVar("request_id", default="system")
