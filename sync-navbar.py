#!/usr/bin/env python3
"""sync-navbar.py — Synchronize navbar HTML from navbar.el to all source files.

After editing src/navbar.el, run this script to update all inline navbars
in .org setupfiles and .el bindings files.

Usage: python3 sync-navbar.py          (apply changes)
       python3 sync-navbar.py --check   (show what would change)
"""

import glob
import sys

def main():
    dry_run = "--check" in sys.argv
    
    # The old and new navbar link segments (plain HTML)
    old_segment = 'Games</a> <a href="/pages/talks-index.html">'
    new_segment = 'Games</a> <a href="/pages/portfolio.html"><i class="fa-solid fa-briefcase" style="color:#59c5ee"></i> Portfolio</a> <a href="/pages/talks-index.html">'
    
    # Escaped versions for #+BIND: in .org files (quotes become \")
    old_segment_bind = old_segment.replace('"', '\\"')
    new_segment_bind = new_segment.replace('"', '\\"')
    
    files = glob.glob("src/**/*.org", recursive=True) + glob.glob("src/**/*.el", recursive=True)
    files = [f for f in files if "navbar.el" not in f and "_original" not in f and "index.org" not in f]
    
    updated = []
    for f in files:
        with open(f) as fh:
            content = fh.read()
        
        new_content = content.replace(old_segment, new_segment)
        new_content = new_content.replace(old_segment_bind, new_segment_bind)
        
        if new_content != content:
            updated.append(f)
            if not dry_run:
                with open(f, "w") as fh:
                    fh.write(new_content)
    
    if dry_run:
        if updated:
            print("Files that would be updated:")
            for f in updated:
                print(f"  {f}")
        else:
            print("All files already in sync.")
    else:
        if updated:
            for f in updated:
                print(f"  Updated: {f}")
            print(f"\nDone! Updated {len(updated)} file(s).")
        else:
            print("All files already in sync.")

if __name__ == "__main__":
    main()