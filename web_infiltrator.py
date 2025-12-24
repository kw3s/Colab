import asyncio
from playwright.async_api import async_playwright
from datetime import datetime
import nest_asyncio

# Apply the patch to allow nested event loops in Colab
nest_asyncio.apply()

async def infiltrate(url, output_file="intelligence_dossier.txt"):
    print(f"🕵️ Starting infiltration of: {url}")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        page = await context.new_page()
        
        try:
            await page.goto(url, wait_until="networkidle", timeout=60000)
            title = await page.title()
            content = await page.inner_text("body")
            
            report = f"--- 🛰️ INTELLIGENCE DOSSIER ---\nURL: {url}\nTITLE: {title}\nTS: {datetime.now()}\n--- CONTENT ---\n{content[:2000]}"
            
            with open(output_file, "w") as f:
                f.write(report)
            
            print(f"✅ Infiltration successful. Dossier saved to {output_file}")
            return report
        except Exception as e:
            err = f"❌ Infiltration failed: {str(e)}"
            print(err)
            return err
        finally:
            await browser.close()

def run_infiltrator(url, output="intelligence_dossier.txt"):
    # This wrapper makes it easy to call from any context
    return asyncio.get_event_loop().run_until_complete(infiltrate(url, output))

if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "https://news.ycombinator.com"
    run_infiltrator(target)