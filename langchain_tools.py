from langchain.tools.base import BaseTool
import nso_utils as nso

class HelloTool(BaseTool):
    """Tool that generates a personalized hello message."""

    name = "HelloTool"
    description = (
        "A tool that generates a personalized hello message. "
        "Input should be a name string."
    )

    def _run(self, name: str = None) -> str:
        return f"Hello {name}!"

    async def _arun(self, name: str = None) -> str:
        """Use the HelloTool asynchronously."""
        return self._run(name)
    
class getLoopback(BaseTool):
    """Tool that gets a Loopback address."""

    name = "getLoopback"
    description = (
        "A tool that gets a loopback address of a specific router. "
        "Input should be a hostname (string)."
    )

    def _run(self, hostname: str = None) -> str:
        loopback = nso.getLoopback(hostname)
        return f"{hostname}のループバックアドレスは{loopback}です!"

    async def _arun(self, hostname: str = None) -> str:
        """Use the HelloTool asynchronously."""
        return self._run(hostname)
    
class verifyBGPstatus(BaseTool):
    """Tool that gets a BGP status."""

    name = "verifyBGPstatus"
    description = (
        "A tool that gets a BGP status between two routers. "
        "Input should be two hostnames (string)."
    )

    def _run(self, hostname1, hostname2: str = None) -> str:
        return f"{hostname1}と{hostname2}のBGPはupしています!"

    async def _arun(self, hostname1, hostname2: str = None) -> str:
        """Use the HelloTool asynchronously."""
        return self._run(hostname1, hostname2)
    
class verifyIFstatus(BaseTool):
    """Tool that gets a Interface status."""

    name = "verifyIFstatus"
    description = (
        "A tool that gets a specific interface status of a router. "
        "Input should be a hostname (string) and an interface name (string)."
    )

    def _run(self, hostname, interfacename: str = None) -> str:
        return f"{hostname}の{interfacename}はupしています！"

    async def _arun(self, hostname, interfacename: str = None) -> str:
        """Use the HelloTool asynchronously."""
        return self._run(hostname, interfacename)
    
class dryrunBGPconfig(BaseTool):
    """Tool that dry-run BGP configuration."""

    name = "dryrunBGPconfig"
    description = (
        "A tool that dry-runs BGP configurations on two routers. "
        "Input should be a hostname1 (string), hostname2 (string), and asnumber (int)."
    )

    def _run(self, hostnam1, hostname2, asnumber: str = None) -> str:
        return f"{hostnam1}と{hostname2}のAS{asnumber}のdry-runが完了しました！"

    async def _arun(self, hostnam1, hostname2, asnumber: str = None) -> str:
        """Use the HelloTool asynchronously."""
        return self._run(hostnam1, hostname2, asnumber)

class setBGPconfig(BaseTool):
    """Tool that set BGP configuration."""

    name = "setBGPconfig"
    description = (
        "A tool that sets BGP configurations on two routers. "
        "Input should be a hostname1 (string), hostname2 (string), and asnumber (int)."
    )

    def _run(self, hostnam1, hostname2, asnumber: str = None) -> str:
        return f"{hostnam1}と{hostname2}のAS{asnumber}の設定が完了しました！"

    async def _arun(self, hostnam1, hostname2, asnumber: str = None) -> str:
        """Use the HelloTool asynchronously."""
        return self._run(hostnam1, hostname2, asnumber)