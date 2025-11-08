class Context:
    def __init__(self, *args, **kwargs):
        self.info = "Placeholder Context for testing in Termux"


class Settings:
    """Mock settings container with .port, .server_mode, etc."""
    def __init__(self, port=0, server_mode="mock", debug=False):
        self.port = port
        self.server_mode = server_mode
        self.debug = debug


class FastMCP:
    def __init__(self, *args, **kwargs):
        self.status = "Mock FastMCP initialized"
        self.tools = {}
        self.prompts = {}
        # Now settings is an object with attributes
        self.settings = Settings(port=8888, server_mode="mock", debug=False)

    def tool(self, name=None):
        def decorator(func):
            self.tools[name or func.__name__] = func
            return func
        return decorator

    def prompt(self, name=None):
        def decorator(func):
            self.prompts[name or func.__name__] = func
            return func
        return decorator

    def run(self, *args, **kwargs):
        print("FastMCP mock run() called with:", args, kwargs)
        return {"status": "running"}

    def start(self):
        print("FastMCP mock server started")

    def stop(self):
        print("FastMCP mock server stopped")
