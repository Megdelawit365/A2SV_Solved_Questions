class Node:
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Node(homepage)
        self.current = self.homepage

    def visit(self, url: str) -> None:
        curr = self.current
        newpage = Node(url)
        curr.next = newpage
        newpage.prev = curr
        self.current = newpage

    def back(self, steps: int) -> str:
        curr = self.current
        count = 0
        while curr.prev and count < steps:
            curr = curr.prev
            count += 1
        self.current = curr
        return curr.val

    def forward(self, steps: int) -> str:
        curr = self.current
        count = 0
        while curr.next and count < steps:
            curr = curr.next
            count += 1
        self.current = curr
        return curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)