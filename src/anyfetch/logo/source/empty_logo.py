from anyfetch.logo.source.base import LogoSourceStrategy


class EmptyLogo(LogoSourceStrategy):
    def render(self):
        return []
