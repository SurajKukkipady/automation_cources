from playwright.sync_api import Page

class NavigationPage:
    def __init__(self, page: Page):
        self.page = page
    
    async def form_layouts_page(self):
        await self.page.get_by_text('Forms').click()
        await self.page.get_by_text('Form Layouts').click()