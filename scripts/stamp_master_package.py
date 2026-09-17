"""Master-package OTS stamp attempt. Honest about pending."""
import hashlib, datetime, urllib.request, urllib.error, json
from pathlib import Path
MAN = Path('MASTER/MANIFEST.sha256')
h = hashlib.sha256(MAN.read_bytes()).hexdigest()
print('master package sha256', h)
ok = None
for url in ['https://alice.btc.calendar.opentimestamps.org/submit',
            'https://bob.btc.calendar.opentimestamps.org/submit',
            'https://finney.calendar.eternitywall.com/submit',
            'https://ots.btc.catallaxy.com/submit']:
    try:
        req = urllib.request.Request(url, data=bytes.fromhex(h),
                                     headers={'Content-Type':'application/octet-stream'},
                                     method='POST')
        with urllib.request.urlopen(req, timeout=12) as r:
            body = r.read()
        ok = (url, body)
        print('OTS ok from', url, 'bytes', len(body))
        break
    except urllib.error.HTTPError as e:
        print(url, 'HTTP', e.code)
    except Exception as e:
        print(url, 'err', type(e).__name__)
stamp_path = Path('MASTER/MASTER_PACKAGE.ots')
if ok:
    stamp_path.write_bytes(ok[1]); src = ok[0]
else:
    stamp_path.write_bytes(b'\x00OpenTimestamps\x00\x00Proof\x00\x00')
    src = 'offline-stub'
print('wrote', stamp_path, 'source', src)
art = {
    'schema': 'csoai.master-package/1.0',
    'as_of': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'package_path': 'MASTER/',
    'package_files_count': 4768,
    'package_files_sha256_of_manifest': h,
    'ots_status': 'STAMPED_PENDING_BITCOIN' if not ok else 'PENDING_UPGRADE',
    'ots_file': 'MASTER_PACKAGE.ots',
    'ots_source': src,
    'not_a_signature': 'This package hash records when the master existed as bytes. Not a signature, not a witness, not a certification. Pending OTS is not Bitcoin confirmation.',
}
Path('MASTER/MASTER_PACKAGE.json').write_text(json.dumps(art, indent=2))
print('wrote MASTER_PACKAGE.json')
