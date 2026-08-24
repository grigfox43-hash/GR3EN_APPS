import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://dev.tools.plbx.ai/validator')
        await page.wait_for_timeout(3000) # Wait for React to render
        await page.screenshot(path='validator_screenshot.png')
        content = await page.content()
        with open('validator_dom.html', 'w', encoding='utf-8') as f:
            f.write(content)
        await browser.close()

asyncio.run(main())
