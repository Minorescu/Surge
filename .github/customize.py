from pathlib import Path
import sys
p=Path(sys.argv[1]); site_url=sys.argv[2].rstrip('/')+'/'
s=p.read_text()
for old,new in {
 'Surge Ruleset Server | Sukka (@SukkaW)':'Minorescu Ruleset Server',
 'Surge Ruleset | Sukka (@SukkaW)':'Minorescu Ruleset Server',
 'Sukka 自用的 Surge / Clash Premium 规则组':'Minorescu 的 Surge / Clash Premium 规则镜像',
 'https://ruleset.skk.moe/':site_url,
 '<h1>Sukka Ruleset Server</h1>':'<h1>Minorescu Ruleset Server</h1>',
 'Made by <a href="https://skk.moe">Sukka</a> | <a href="https://github.com/SukkaW/Surge/">Source @ GitHub</a> | Licensed under <a href="/LICENSE" target="_blank">AGPL-3.0</a>':'Made by <a href="https://github.com/Minorescu">Minorescu</a> | <a href="https://github.com/Minorescu/Surge">Source @ GitHub</a> | Fork <a href="https://github.com/SukkaLab/ruleset.skk.moe">Sukka</a> | Licensed under <a href="/LICENSE" target="_blank">AGPL-3.0</a>'
}.items(): s=s.replace(old,new)
p.write_text(s)
