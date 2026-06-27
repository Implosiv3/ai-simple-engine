from abc import ABC



class Plugin(
    ABC
):
    
    def providers(
        self
    ) -> list:
        return []