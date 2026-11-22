"""Check XACT paper screens with isolated headless Edge profiles."""

from __future__ import annotations

import base64
import argparse
import html
import json
from pathlib import Path
import re
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EDGE = Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
WIDTHS = (360, 375, 390, 430)


def make_visual_fixture(target: Path, screen: str) -> None:
    source = (ROOT / "MergedScreens2.html").read_text(encoding="utf-8")
    match = re.search(
        r'<script id="studentPayload" type="application/octet-stream">([A-Za-z0-9+/=]+)</script>',
        source,
    )
    if not match:
        raise RuntimeError("Student payload was not found")
    page = base64.b64decode(match.group(1)).decode("utf-8")
    page = page.replace("<head>", f'<head><base href="{ROOT.as_uri()}/">', 1)
    config = (
        f"<script>window.__UR_GURU_START_SCREEN__={json.dumps(screen)};"
        "window.__UR_GURU_MODE__='mobile';"
        "window.__UR_GURU_EMBEDDED__=true;</script>"
    )
    fixture_style = """<style>
html,body{width:100%;height:100%;overflow:hidden;background:#fff!important}
.workspace{display:block!important;width:100%!important;height:100%!important;min-height:0!important}
.rail,.rightpanel,.topbar,.device-tag{display:none!important}
.center{display:block!important;width:100%!important;height:100%!important;padding:0!important;background:none!important;overflow:hidden!important}
.mainlayout,.device-wrap{display:block!important;width:100%!important;height:100%!important}
.device{display:block!important;width:100%!important;min-width:0!important;height:100%!important;border:0!important;border-radius:0!important;transform:none!important;margin:0!important;box-shadow:none!important}
</style>"""
    page = page.replace("</head>", config + fixture_style + "</head>", 1)
    probe = """<script>
window.addEventListener('load',()=>setTimeout(()=>{
  const target=SCREEN_ID;
  if(target==='XA-03'){xactState.subject='Biology';render();}
  const q=s=>document.querySelector(s);
  const rect=s=>{const el=q(s);if(!el)return null;const r=el.getBoundingClientRect();return {top:r.top,bottom:r.bottom,left:r.left,right:r.right}};
  const content=q('.app-content'),paper=q('.xact-papers-page');
  const result={width:innerWidth,screen:q('#appScreen')?.dataset.screenId,
    gap:rect('.xact-papers-badge').top-rect('.app-header').bottom,
    overflow:content.scrollWidth-content.clientWidth,
    pageOverflow:document.documentElement.scrollWidth-innerWidth,
    brandingRow:!!paper.querySelector('.xact-topline'),
    brandingText:paper.innerText.includes('UR GURU | Xact'),
    selectedSubject:q(target==='XA-03'?'.xact-papers-subject-row strong':target==='XA-06'?'.xact-mock-subject .xact-mock-copy p':'.xact-detail-row strong')?.textContent,
    activeNav:q('.app-nav .navitem.active')?.textContent.trim(),
    home:rect('.xact-papers-home'),copy:rect('.xact-papers-copy'),
    notice:rect('.xact-disclosure'),nav:rect('.app-nav'),
    rowCount:document.querySelectorAll('.xact-detail-row').length,
    startDisabled:q('.xact-detail-actions .xbtn.primary,.xact-instructions-action .xbtn.primary')?.disabled,
    startRoute:q('.xact-instructions-action .xbtn.primary')?.getAttribute('onclick'),
    unavailablePanel:!!q('.xact-instructions-empty'),
    longRow:[...document.querySelectorAll('.xact-detail-row')].find(r=>r.textContent.includes('Awaiting paper settings'))?.getBoundingClientRect().right,
    longLabel:[...document.querySelectorAll('.xact-detail-row')].find(r=>r.textContent.includes('Awaiting paper settings'))?.querySelector('.xact-detail-label')?.getBoundingClientRect().right,
    longValue:[...document.querySelectorAll('.xact-detail-row')].find(r=>r.textContent.includes('Awaiting paper settings'))?.querySelector('strong')?.getBoundingClientRect().left,
    previewRoute:q('.xact-detail-actions .xbtn.outline')?.getAttribute('onclick'),
    buttons:[...document.querySelectorAll('.xact-detail-actions button')].map(b=>({left:b.getBoundingClientRect().left,right:b.getBoundingClientRect().right})),
    mockRoutes:[...document.querySelectorAll('.xact-mock-choose,.xact-mock-topics .xbtn,.xact-mock-settings .xbtn,.xact-mock-review .xbtn')].map(b=>b.getAttribute('onclick')),
    mockRows:[...document.querySelectorAll('.xact-mock-settings .xact-detail-row')].map(r=>r.textContent.trim()),
    mockCards:[...document.querySelectorAll('.xact-mock-card')].map(c=>({left:c.getBoundingClientRect().left,right:c.getBoundingClientRect().right}))};
  content.scrollTop=content.scrollHeight;
  result.scrollTop=content.scrollTop;
  result.scrolledNotice=rect('.xact-disclosure');
  if(target==='XA-04'){
    xactState.subject='Combined Mathematics';render();
    result.dynamicSubject=q('.xact-detail-row strong')?.textContent;
    result.longValue=rect('.xact-detail-row strong');
    result.subjectLabel=rect('.xact-detail-row .xact-detail-label');
  }
  if(target==='XA-06'){
    xactState.subject='Biology';xactState.difficulty='Hard';xactState.count=30;xactState.timed=true;render();
    result.dynamicSubject=q('.xact-mock-subject .xact-mock-copy p')?.textContent;
    result.dynamicRows=[...document.querySelectorAll('.xact-mock-settings .xact-detail-row')].map(r=>r.textContent.trim());
  }
  document.body.dataset.xactResult=JSON.stringify(result);
},350));
</script>""".replace('SCREEN_ID', json.dumps(screen))
    page = page.replace("</body>", probe + "</body>", 1)
    target.write_text(page, encoding="utf-8")


def make_wrapper(target: Path, width: int) -> None:
    target.write_text(
        '<!doctype html><html><head><meta charset="utf-8"></head><body style="margin:0">'
        f'<iframe id="test" src="visual.html" style="width:{width}px;height:844px;border:0"></iframe>'
        '<script>document.getElementById("test").addEventListener("load",()=>setTimeout(()=>{'
        'document.body.dataset.result=document.getElementById("test").contentDocument.body.dataset.xactResult||"missing";'
        '},1100));</script></body></html>',
        encoding="utf-8",
    )


def run_width(temp: Path, width: int) -> dict:
    wrapper = temp / f"width-{width}.html"
    make_wrapper(wrapper, width)
    profile = temp / f"edge-profile-{width}"
    profile.mkdir()  # Unique, absolute, writable directory for this invocation.
    command = [
        str(EDGE),
        "--headless=new",
        "--disable-gpu",
        "--no-first-run",
        "--allow-file-access-from-files",
        f"--user-data-dir={profile.resolve()}",
        "--window-size=800,900",
        "--virtual-time-budget=8000",
        "--dump-dom",
        wrapper.as_uri(),
    ]
    # Keep the process handle so a timeout can stop only this test's process tree.
    process = subprocess.Popen(command, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        output, errors = process.communicate(timeout=25)
    except subprocess.TimeoutExpired as exc:
        subprocess.run(
            ["taskkill", "/PID", str(process.pid), "/T", "/F"],
            capture_output=True,
            text=True,
            check=False,
        )
        process.communicate(timeout=5)
        raise RuntimeError(f"Edge timed out at {width}px; stopped test process {process.pid}") from exc
    match = re.search(r'data-result="([^"]+)"', output)
    if not match:
        raise RuntimeError(f"Edge returned no layout result at {width}px: {errors[-300:]}")
    metrics = json.loads(html.unescape(match.group(1)))
    if metrics == "missing":
        raise RuntimeError(f"The {width}px fixture did not finish loading")
    return metrics


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--screen', choices=('XA-03', 'XA-04', 'XA-05', 'XA-06'), default='XA-03')
    screen = parser.parse_args().screen
    if not EDGE.is_file():
        raise RuntimeError(f"Edge was not found at {EDGE}")
    with tempfile.TemporaryDirectory(prefix="xact-layout-", dir=ROOT) as folder:
        temp = Path(folder).resolve()
        if not temp.is_relative_to(ROOT.resolve()):
            raise RuntimeError("Temporary directory is outside the workspace")
        make_visual_fixture(temp / "visual.html", screen)
        for width in WIDTHS:
            metrics = run_width(temp, width)
            assert metrics["width"] == width, metrics
            assert metrics["screen"] == screen, metrics
            assert 20 <= metrics["gap"] <= 28, metrics
            assert metrics["overflow"] <= 0 and metrics["pageOverflow"] <= 0, metrics
            assert not metrics["brandingRow"] and not metrics["brandingText"], metrics
            assert metrics["activeNav"] == "Home", metrics
            assert metrics["home"]["left"] >= metrics["copy"]["right"], metrics
            assert metrics["scrolledNotice"]["bottom"] < metrics["nav"]["top"], metrics
            if screen == 'XA-03':
                assert metrics["selectedSubject"] == "Biology", metrics
            elif screen == 'XA-04':
                assert metrics["selectedSubject"] == "Not selected", metrics
                assert metrics["rowCount"] == 5 and metrics["startDisabled"], metrics
                assert metrics["previewRoute"] == 'xactGo(5)', metrics
                assert metrics["dynamicSubject"] == "Combined Mathematics", metrics
                assert metrics["longValue"]["left"] >= metrics["subjectLabel"]["right"], metrics
                assert all(0 <= button["left"] and button["right"] <= width for button in metrics["buttons"]), metrics
            elif screen == 'XA-05':
                assert metrics["rowCount"] == 5 and metrics["startDisabled"], metrics
                assert metrics["startRoute"] == 'xactGo(10)' and metrics["unavailablePanel"], metrics
                assert metrics["longValue"] >= metrics["longLabel"] and metrics["longRow"] <= width, metrics
            else:
                assert metrics["selectedSubject"] == "Choose a subject first.", metrics
                assert metrics["mockRoutes"] == ['xactGo(2)', 'xactGo(7)', 'xactGo(8)', 'xactGo(9)'], metrics
                assert all(term in ''.join(metrics["mockRows"]) for term in ('Medium', '20', 'Untimed preview')), metrics
                assert metrics["dynamicSubject"] == 'Biology', metrics
                assert all(term in ''.join(metrics["dynamicRows"]) for term in ('Hard', '30', 'Timed preview')), metrics
                assert all(0 <= card["left"] and card["right"] <= width for card in metrics["mockCards"]), metrics
            print(
                f'{width}px: gap {metrics["gap"]:.0f}px, no branding or horizontal overflow, '
                f'Home clear, scrolled notice clear of navigation'
            )


if __name__ == "__main__":
    main()
