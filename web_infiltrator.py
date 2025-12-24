import asyncio
from playwright.async_api import async_playwright

async def infiltrate(url, output_file="intelligence_dossier.txt"):
    print(f"🕵️ Starting infiltration of: {url}")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        try:
            # Set a realistic user agent
            await page.set_extra_http_headers({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
            
            await page.goto(url, wait_until="networkidle", timeout=60000)
            
            title = await page.title()
            content = await page.inner_text("body")
            
            report = f"--- 🛰️ INTELLIGENCE DOSSIER ---\n"
            report += f"URL: {url}\n"
            report += f"TITLE: {title}\n"
            report += f"TIMESTAMP: {datetime.now()}\n"
            report += f"--- CONTENT PREVIEW ---\n"
            report += content[:2000] # Capture first 2000 chars
            
            with open(output_file, "w") as f:
                f.write(report)
            
            print(f"✅ Infiltration successful. Dossier saved to {output_file}")
            return True
        except Exception as e:
            print(f"❌ Infiltration failed: {str(e)}")
            return False
        finally:
            await browser.close()

if __name__ == "__main__":
    import sys
    import datetime
    target = sys.argv[1] if len(sys.argv) > 1 else "https://news.ycombinator.com"
    asyncio.run(infiltrate(target))