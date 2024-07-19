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
    

class pingCheck(BaseTool):
    """ping to a specific address from a router"""

    name = "pingCheck"
    description = (
        "A tool that execute ping from a router to a specific address. "
        "Input must have hostname (string) and ipv4 address(string)."
        "If addrss is unclear, please ask a user to input"
    )

    def _run(self, hostname, address: str = None) -> str:
        result = nso.pingCheck(hostname, address)
        return result

    async def _arun(self, hostname, address: str = None) -> str:
        return self._run(hostname, address)

   
class verifyBGPstatus(BaseTool):
    """Tool that gets a BGP status."""

    name = "verifyBGPstatus"
    description = (
        "A tool that gets a BGP status to a specific neighbor address"
        "Input should be a hostname (string), and a neighbor ipv4 address."
        "If addrss is unclear, please ask a user to input"
    )

    def _run(self, hostname, address: str = None) -> str:
        result = nso.checkBGPstatus(hostname, address)
        return result

    async def _arun(self, hostname, address: str = None) -> str:
        return self._run(hostname, address)
    

class configBGPcheck(BaseTool):
    """Tool that gets a BGP configuration."""

    name = "configBGPcheck"
    description = (
        "A tool that gets a BGP configuration of a specific neighbor"
        "Input must have a hostname (string), and a neighbor ipv4 address."
        "If addrss is unclear, please ask a user to input"
    )

    def _run(self, hostname, address: str = None) -> str:
        result = nso.configBGPcheck(hostname, address)
        return result

    async def _arun(self, hostname, address: str = None) -> str:
        return self._run(hostname, address)
    
    
class dryrunBGPconfig(BaseTool):
    """Tool that dry-run BGP configuration."""

    name = "dryrunBGPconfig"
    description = (
        "A tool that dry-runs BGP configurations on two routers. "
        "Input should be a router1-hostname, router2-hostname, router1-loopback-address, router2-loopback-address, and asnumber."
        "for example, router1-hostname is xr-1,  router2-hostname is xr-2, router1-loopback-address is 1.1.1.1, router2-loopback-address is 2.2.2.2, and asnumber is 100"
    )

    def _run(self, router1, router2, router1loopback, router2loopback, asnumber: str = None) -> str:
        result = nso.dryrunBGPconfig(router1, router2, router1loopback, router2loopback, asnumber)
        return result

    async def _arun(self, router1, router2, router1loopback, router2loopback, asnumber: str = None) -> str:
        return self._run(router1, router2, router1loopback, router2loopback, asnumber, asnumber)


class setBGPconfig(BaseTool):
    """Tool that dry-run BGP configuration."""

    name = "setBGPconfig"
    description = (
        "A tool that sets BGP configurations on two routers. "
        "Input should be a router1-hostname, router2-hostname, router1-loopback-address, router2-loopback-address, and asnumber."
        "for example, router1-hostname is xr-1,  router2-hostname is xr-2, router1-loopback-address is 1.1.1.1, router2-loopback-address is 2.2.2.2, and asnumber is 100"
    )

    def _run(self, router1, router2, router1loopback, router2loopback, asnumber: str = None) -> str:
        result = nso.setBGPconfig(router1, router2, router1loopback, router2loopback, asnumber)
        return result

    async def _arun(self, router1, router2, router1loopback, router2loopback, asnumber: str = None) -> str:
        return self._run(router1, router2, router1loopback, router2loopback, asnumber, asnumber)
    
